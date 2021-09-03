"""API to download, uncompress and cache files such as binary models.

"""
__author__ = 'Paul Landes'

from typing import Union, Tuple
from dataclasses import dataclass, field
import logging
import re
from pathlib import Path
import urllib
from urllib.parse import ParseResult
import patoolib
from zensols.util import APIError, PackageResource
from zensols.config import Dictable
from zensols.install import Downloader

logger = logging.getLogger(__name__)


class InstallError(APIError):
    """Raised for issues while downloading or installing files."""


@dataclass
class Installable(Dictable):
    """A resource that is downloaded from the Internet and then optionally
    uncompressed.  Once the file is downloaded, it is only uncompressed if it
    is an archive file.  This is determined by the file extension.

    """
    _DICTABLE_ATTRIBUTES = 'remote_name is_compressed compressed_name'.split()
    _FILE_REGEX = re.compile(r'^(.+)\.(tar\.gz|tgz|tar\.bz2|' +
                             '|'.join(patoolib.ArchiveFormats) + ')$')

    url: str = field()
    """The URL that locates the file to install."""

    name: str = field(default=None)
    """Used for local file naming."""

    clean_up: bool = field(default=True)
    """Whether or not to remove the downloaded compressed after finished."""

    def __post_init__(self):
        url: ParseResult = urllib.parse.urlparse(self.url)
        remote_path = Path(url.path)
        m = self._FILE_REGEX.match(remote_path.name)
        if m is None:
            self._extension = None
        else:
            self.remote_name, self._extension = m.groups()
            if self.name is None:
                self.name = self.remote_name

    def uncompress(self, path: Path = None, out_dir: Path = None):
        """Uncompress the file.

        :param path: the file to uncompress

        :param out_dir: where the uncompressed files are extracted

        """
        if path is None:
            src = Path(self.compressed_name)
            out_dir = Path('.')
        else:
            src = path
            if out_dir is None:
                out_dir = path.parent
        dst_dir = out_dir / self.name
        if logger.isEnabledFor(logging.INFO):
            logger.info(f'uncompressing {src} to {out_dir}')
        out_dir.mkdir(parents=True, exist_ok=True)
        patoolib.extract_archive(str(src), outdir=str(out_dir))
        if not dst_dir.is_dir():
            ext_dir = out_dir / self.remote_name
            if not ext_dir.is_dir():
                raise InstallError(f'Trying to create {dst_dir} but ' +
                                   f'expecting extracted dir: {ext_dir}')
            if logger.isEnabledFor(logging.INFO):
                logger.info(f'renaming {ext_dir} to {dst_dir}')
            ext_dir.rename(dst_dir)
        if self.clean_up:
            if logger.isEnabledFor(logging.INFO):
                logger.info(f'cleaning up downloaded file: {src}')
            src.unlink()

    @property
    def is_compressed(self) -> bool:
        """Whether or not the file is compressed.

        """
        return self._extension is not None

    @property
    def compressed_name(self) -> str:
        """The file name with the extension and used to uncompress.  If the resource
        isn't compressed, just the name is returned.

        """
        if self.is_compressed:
            name = f'{self.name}.{self._extension}'
        else:
            name = self.name
        return name


@dataclass
class Installer(object):
    """Downloads files from the internet and optionally extracts them.

    :see: :class:`.Installable`

    """

    package_resource: Union[str, PackageResource] = field()
    """Package resource (i.e. ``zensols.someappname``).  This field is converted to
    a package if given as a string during post initialization.

    """

    installs: Tuple[Installable] = field()
    """The list of resources to install."""

    downloader: Downloader = field(default_factory=Downloader)
    """Used to download the file from the Internet."""

    def __post_init__(self):
        if isinstance(self.package_resource, str):
            self.package_resource = PackageResource(self.package_resource)

    def _get_package_path(self, inst: Installable):
        home = Path('~/').expanduser()
        parts = self.package_resource.name.split('.')
        parts[0] = '.' + parts[0]
        return home / Path(*parts)

    def _get_local_path(self, inst: Installable, compressed: bool):
        pkg_path = self._get_package_path(inst)
        fname = inst.compressed_name if compressed else inst.name
        return pkg_path / fname

    def _install(self, inst: Installable, dst_path: Path):
        if logger.isEnabledFor(logging.INFO):
            logger.info(f'installing {inst.name} to {dst_path}')
        if inst.is_compressed:
            comp_path = self._get_local_path(inst, True)
            if not comp_path.is_file():
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug(f'missing compressed file {comp_path}')
                self.downloader.download(inst.url, comp_path)
            inst.uncompress(comp_path)
        else:
            self.downloader.download(inst.url, dst_path)

    def install(self):
        """Download and install all resources.

        """
        for inst in self.installs:
            local_path: Path = self._get_local_path(inst, False)
            if local_path.exists():
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug(f'found: {local_path}--skipping')
            else:
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug(f'missing {local_path}')
                self._install(inst, local_path)