from dataclasses import dataclass, field
import logging
import shutil
from zensols.install import Installer

logger = logging.getLogger(__name__)


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
        logger.info('installing files')
        self.installer.install()

    def clean(self):
        """Remove downloaded files.

        """
        path = self.installer.base_directory
        logger.info(f'removing files in {path}')
        if path.is_dir():
            shutil.rmtree(path)
