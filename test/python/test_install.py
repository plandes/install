from typing import List
import logging
import unittest
import shutil
from pathlib import Path
from zensols.config import ImportIniConfig, ImportConfigFactory
from zensols.install import Installer, Status

if 0:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)


class TestApplication(unittest.TestCase):
    def setUp(self):
        target = Path('target')
        conf = ImportIniConfig('test-resources/test.conf')
        self.fac = ImportConfigFactory(conf)
        self.no_name_file = Path(target / 'dump/no_name_pdf_resource')
        self.none_name_file = Path(target / 'dump/dummy.pdf')
        self.with_name_file = Path(target / 'dump/empty.pdf')
        self.zip_file = Path(target / 'dump/zenbuild-general_build.zip')
        self.zip_uncompressed_dir = Path(target / 'dump/zenbuild-general_build')
        self.zip_file_overridden = Path(target / 'dump/general_build.zip')
        self.zip_uncompressed_dir_overridden = Path(target / 'dump/general_build')
        if target.is_dir():
            shutil.rmtree(target)

    def test_no_name_file(self):
        self.assertFalse(self.no_name_file.exists())
        installer: Installer = self.fac('no_name_installer')
        statuses: List[Status] = installer.install()
        self.assertTrue(self.no_name_file.exists())
        self.assertEqual(1, len(statuses))
        st = statuses[0]
        self.assertEqual(st.resource.name, 'no_name_pdf_resource')
        self.assertEqual(st.target_path, self.no_name_file)
        self.assertEqual(st.downloaded_path, self.no_name_file)
        self.assertEqual(st.uncompressed, False)

        statuses = installer.install()
        st = statuses[0]
        self.assertEqual(1, len(statuses))
        self.assertEqual(st.target_path, self.no_name_file)
        self.assertEqual(st.downloaded_path, None)
        self.assertEqual(st.uncompressed, False)

    def test_none_name_file(self):
        self.assertFalse(self.none_name_file.exists())
        installer: Installer = self.fac('none_name_installer')
        statuses: List[Status] = installer.install()
        self.assertTrue(self.none_name_file.exists())
        self.assertEqual(1, len(statuses))
        st = statuses[0]
        self.assertEqual(st.resource.name, 'dummy.pdf')
        self.assertEqual(st.target_path, self.none_name_file)
        self.assertEqual(st.downloaded_path, self.none_name_file)
        self.assertEqual(st.uncompressed, False)

        statuses = installer.install()
        st = statuses[0]
        self.assertEqual(1, len(statuses))
        self.assertEqual(st.target_path, self.none_name_file)
        self.assertEqual(st.downloaded_path, None)
        self.assertEqual(st.uncompressed, False)

    def test_with_name_file(self):
        self.assertFalse(self.with_name_file.exists())
        installer: Installer = self.fac('with_name_installer')
        statuses: List[Status] = installer.install()
        self.assertTrue(self.with_name_file.exists())
        self.assertEqual(1, len(statuses))
        st = statuses[0]
        self.assertEqual(st.resource.name, 'empty.pdf')
        self.assertEqual(st.target_path, self.with_name_file)
        self.assertEqual(st.downloaded_path, self.with_name_file)
        self.assertEqual(st.uncompressed, False)

    def test_uncompress_zip(self):
        self.assertFalse(self.zip_file.exists())
        self.assertFalse(self.zip_uncompressed_dir.exists())
        installer: Installer = self.fac('zip_installer')
        statuses: List[Status] = installer.install()
        self.assertTrue(self.zip_file.is_file())
        self.assertTrue(self.zip_uncompressed_dir.is_dir())
        self.assertEqual(1, len(statuses))
        st = statuses[0]
        self.assertEqual(st.resource.name, self.zip_uncompressed_dir.name)
        self.assertEqual(st.target_path, self.zip_file)
        self.assertEqual(st.downloaded_path, self.zip_file)
        self.assertEqual(st.uncompressed, True)

        statuses: List[Status] = installer.install()
        st = statuses[0]
        self.assertEqual(st.resource.name, self.zip_uncompressed_dir.name)
        self.assertEqual(st.target_path, self.zip_file)
        self.assertEqual(st.downloaded_path, None)
        self.assertEqual(st.uncompressed, False)

    def test_uncompress_zip_overridden_dir(self):
        self.assertFalse(self.zip_file.exists())
        self.assertFalse(self.zip_uncompressed_dir.exists())
        installer: Installer = self.fac('zip_installer_overridden')
        statuses: List[Status] = installer.install()

        self.assertTrue(self.zip_file_overridden.is_file())
        self.assertTrue(self.zip_uncompressed_dir_overridden.is_dir())
        self.assertEqual(1, len(statuses))
        st = statuses[0]
        self.assertEqual(st.resource.name, self.zip_uncompressed_dir_overridden.name)
        self.assertEqual(st.target_path, self.zip_file_overridden)
        self.assertEqual(st.downloaded_path, self.zip_file_overridden)
        self.assertEqual(st.uncompressed, True)

        statuses: List[Status] = installer.install()
        st = statuses[0]
        self.assertEqual(st.resource.name, self.zip_uncompressed_dir_overridden.name)
        self.assertEqual(st.target_path, self.zip_file_overridden)
        self.assertEqual(st.downloaded_path, None)
        self.assertEqual(st.uncompressed, False)
