import tempfile
import unittest
import os
import shutil
from droidtools import ext4fs_utils

FS_SIZE     = 32 * 1024 * 1024
SPARSE_SIZE = 4771976
GZIP_SIZE   = 32917

class Ext4utilsTest(unittest.TestCase):
    def test_make(self):
        path = tempfile.mkdtemp()
        directory = os.path.join(path, "target")
        filepath = os.path.join(path, "target.img")
        os.makedirs(directory)
        ext4fs_utils.make_ext4fs(filepath, directory, FS_SIZE)
        self.assertEqual(os.path.getsize(filepath), FS_SIZE)
        shutil.rmtree(path)

    def test_sparsed(self):
        path = tempfile.mkdtemp()
        directory = os.path.join(path, "target")
        filepath = os.path.join(path, "target.img")
        os.makedirs(directory)
        ext4fs_utils.make_ext4fs(filepath, directory, FS_SIZE, mode = ext4fs_utils.MODE_SPARSED)
        self.assertEqual(os.path.getsize(filepath), SPARSE_SIZE)
        shutil.rmtree(path)

    def test_android(self):
        path = tempfile.mkdtemp()
        directory = os.path.join(path, "target")
        filepath = os.path.join(path, "target.img")
        os.makedirs(directory)
        ext4fs_utils.make_ext4fs(filepath, directory, FS_SIZE, mountPoint="cache")
        self.assertEqual(os.path.getsize(filepath), FS_SIZE)
        shutil.rmtree(path)

    def test_android_sparsed(self):
        path = tempfile.mkdtemp()
        directory = os.path.join(path, "target")
        filepath = os.path.join(path, "target.img")
        os.makedirs(directory)
        ext4fs_utils.make_ext4fs(filepath, directory, FS_SIZE, mountPoint="cache", mode=ext4fs_utils.MODE_SPARSED)
        self.assertEqual(os.path.getsize(filepath), SPARSE_SIZE)
        shutil.rmtree(path)

    def test_gzip(self):
        path = tempfile.mkdtemp()
        directory = os.path.join(path, "target")
        filepath = os.path.join(path, "target.img")
        os.makedirs(directory)
        ext4fs_utils.make_ext4fs(filepath, directory, FS_SIZE, mode=ext4fs_utils.MODE_GZIP)
        self.assertEqual(os.path.getsize(filepath), GZIP_SIZE)
        shutil.rmtree(path)