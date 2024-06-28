from __future__ import absolute_import

from zipfile import ZipFile

from asposeslidescloud import PdfExportOptions
from test.base_test import BaseTest

class TestSplit(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_split(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result1 = BaseTest.slides_api.split(self.file_name, None, None, None, None, None, None, None, self.password, self.folder_name)
        result2 = BaseTest.slides_api.split(self.file_name, None, None, None, None, 2, 3, None, self.password, self.folder_name)
        self.assertEqual(2, len(result2.slides))
        self.assertGreater(len(result1.slides), len(result2.slides))
        url = result1.slides[0].href
        path = url[url.index("/storage/file/") + len("/storage/file/"):]
        self.assertTrue(BaseTest.slides_api.object_exists(path).exists)

    def test_split_online(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        result1 = BaseTest.slides_api.split_online(source, 'png', None, None, None, None, self.password)
        result2 = BaseTest.slides_api.split_online(source, 'png', None, None, 2, 3, self.password)
        with ZipFile(result1) as zip1:
            with ZipFile(result2) as zip2:
                self.assertEqual(2, len(zip2.namelist()))
                self.assertGreater(len(zip1.namelist()), len(zip2.namelist()))

    def test_split_and_save_online(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        result1 = BaseTest.slides_api.split_and_save_online(source, 'png', None, None, None, None, None, self.password)
        result2 = BaseTest.slides_api.split_and_save_online(source, 'png', None, None, None, 2, 3, self.password)
        self.assertEqual(2, len(result2.slides))
        self.assertGreater(len(result1.slides), len(result2.slides))
        url = result1.slides[0].href
        path = url[url.index("/storage/file/") + len("/storage/file/"):]
        self.assertTrue(BaseTest.slides_api.object_exists(path).exists)

    def test_split_with_options(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        options = PdfExportOptions()
        options.jpeg_quality = 50
        result = BaseTest.slides_api.split(self.file_name, options, None, None, None, None, None, None, self.password, self.folder_name)
        url = result.slides[0].href
        path = url[url.index("/storage/file/") + len("/storage/file/"):]
        self.assertTrue(BaseTest.slides_api.object_exists(path).exists)