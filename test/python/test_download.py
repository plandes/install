from typing import Tuple
import unittest
import shutil
import hashlib
from pathlib import Path
from zensols.config import ImportIniConfig, ImportConfigFactory, Settings
from zensols.install import Downloader


class TestDownload(unittest.TestCase):
    def setUp(self):
        self.target = Path('target')
        conf = ImportIniConfig('test-resources/download.conf')
        self.fac = ImportConfigFactory(conf)
        if self.target.is_dir():
            shutil.rmtree(self.target)
        self.target.mkdir(parents=True)

    def _sha1(self, path: Path) -> str:
        self.assertTrue(path.is_file())
        with open(path, 'rb') as f:
            hfile = hashlib.sha1(f.read())
        return hfile.hexdigest()

    def _get_dl_out_path(self, name: str) -> Tuple[Downloader, Path]:
        sec: Settings = self.fac(name)
        dl: Downloader = sec.dl
        self.assertTrue(isinstance(dl, Downloader))
        return dl, (self.target / name), sec.url, sec.sha1

    def test_no_progress(self):
        dl, path, url, should_sha1 = self._get_dl_out_path('no_progress')
        dl.download(url, path)
        sha1 = self._sha1(path)
        self.assertEqual(should_sha1, sha1)

    def test_with_progress_medium_chunk(self):
        print()
        dl, path, url, should_sha1 = self._get_dl_out_path('with_progress_big_chunk')
        dl.download(url, path)
        sha1 = self._sha1(path)
        self.assertEqual(should_sha1, sha1)

    def test_with_progress_small_chunk(self):
        print()
        dl, path, url, should_sha1 = self._get_dl_out_path('with_progress_small_chunk')
        dl.download(url, path)
        sha1 = self._sha1(path)
        self.assertEqual(should_sha1, sha1)
