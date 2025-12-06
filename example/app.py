from dataclasses import dataclass, field
import logging
from pathlib import Path
from io import StringIO
import shutil
from zensols.cli import ApplicationFactory
from zensols.install import Installer, Resource

logger = logging.getLogger(__name__)


CONFIG = """
[cli]
class_name = zensols.cli.ActionCliManager
apps = list: pkg_cli, log_cli, app
default_action = install

[pkg_cli]
class_name = zensols.cli.PackageInfoImporter

[log_cli]
class_name = zensols.cli.LogConfigurator
log_name = ${package:name}
format = %%(asctime)s[%%(levelname)s]:%%(name)s %%(message)s
level = info

[import]
config_files = list: install.conf

[app]
class_name = app.Application
installer = instance: installer
"""


@dataclass
class Application(object):
    """Demonstrate the NLP parsing API.

    """
    CLI_META = {'option_includes': {}}

    installer: Installer = field()
    """Used to install sample files."""

    def install(self):
        """Install by downloading and extracting a zip file.

        """
        res: Resource
        for res in self.installer.resources:
            logger.info('resources:')
            res.write_to_log(logger, depth=1)
        path: Path
        for path in self.installer:
            logger.info(f'resource path: {path}')
        logger.info('installing files')
        self.installer.install()
        ufile: Path = self.installer.get_singleton_path()
        logger.info(f'uncompressed file: {ufile}, exists: {ufile.is_file()}')
        logger.info('remove any installed files (leaves an emtpy directory)')
        self.installer.clear()

    def clean(self):
        """Remove downloaded files.

        """
        path = self.installer.base_directory
        logger.info(f'removing files in {path}')
        if path.is_dir():
            shutil.rmtree(path)


if (__name__ == '__main__'):
    cli = ApplicationFactory('app', StringIO(CONFIG))
    cli.invoke()
