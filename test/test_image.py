from __future__ import absolute_import

import os
from zipfile import ZipFile

from test.base_test import BaseTest
from asposeslidescloud.rest import ApiException

class TestImage(BaseTest):
    def setUp(self):
        self.slide_index = 1
        self.image_index = 1
        self.image_path = self.test_data_path + "/watermark.png"

    def tearDown(self):
        pass

    def test_images_get(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        presentation_result = BaseTest.slides_api.get_presentation_images(self.file_name, self.password, self.folder_name)
        slide_result = BaseTest.slides_api.get_slide_images(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertLess(len(slide_result.list), len(presentation_result.list))

    def test_images_download_storage(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        default_result = BaseTest.slides_api.download_images_default_format(self.file_name, self.password, self.folder_name)
        png_result = BaseTest.slides_api.download_images(self.file_name, 'png', self.password, self.folder_name)
        self.assertNotEqual(os.path.getsize(default_result), os.path.getsize(png_result))
        with ZipFile(default_result) as default_zip:
            with ZipFile(png_result) as png_zip:
                self.assertEqual(len(default_zip.namelist()), len(png_zip.namelist()))

    def test_images_download_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        default_result = BaseTest.slides_api.download_images_default_format_online(source, self.password)
        png_result = BaseTest.slides_api.download_images_online(source, 'png', self.password)
        self.assertNotEqual(os.path.getsize(default_result), os.path.getsize(png_result))
        with ZipFile(default_result) as default_zip:
            with ZipFile(png_result) as png_zip:
                self.assertEqual(len(default_zip.namelist()), len(png_zip.namelist()))

    def test_image_download_storage(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        default_result = BaseTest.slides_api.download_image_default_format(
            self.file_name, self.slide_index, self.password, self.folder_name)
        png_result = BaseTest.slides_api.download_image(self.file_name, self.slide_index, 'png', self.password, self.folder_name)
        self.assertNotEqual(os.path.getsize(default_result), os.path.getsize(png_result))

    def test_image_download_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        default_result = BaseTest.slides_api.download_image_default_format_online(source, self.slide_index, self.password)
        png_result = BaseTest.slides_api.download_image_online(source, self.slide_index, 'png', self.password)
        self.assertNotEqual(os.path.getsize(default_result), os.path.getsize(png_result))

    def test_image_download_quality(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        good_result = BaseTest.slides_api.download_image(self.file_name, self.slide_index, 'jpeg', self.password, self.folder_name, None, 100)
        bad_result = BaseTest.slides_api.download_image(self.file_name, self.slide_index, 'jpeg', self.password, self.folder_name, None, 50)
        self.assertGreater(os.path.getsize(good_result), os.path.getsize(bad_result))

    def test_image_download_quality_useless(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        good_result = BaseTest.slides_api.download_image(self.file_name, self.slide_index, 'png', self.password, self.folder_name, None, 100)
        bad_result = BaseTest.slides_api.download_image(self.file_name, self.slide_index, 'png', self.password, self.folder_name, None, 50)
        #Quality property only has effect on Jpeg images so these two must be identical
        self.assertEqual(os.path.getsize(good_result), os.path.getsize(bad_result))

    def test_replace_image(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        with open(self.image_path, 'rb') as f:
            image_source = f.read()
        BaseTest.slides_api.replace_image(self.file_name, self.image_index, image_source, self.password, self.folder_name)

    def test_replace_image_request(self):
        with open(self.local_path, 'rb') as f:
            file_source = f.read()
        with open(self.image_path, 'rb') as f:
            image_source = f.read()
        image_index = 1
        response = BaseTest.slides_api.replace_image_online(file_source, self.image_index, image_source, self.password)
        self.assertNotEqual(os.path.getsize(response), 0)

    def test_compress_image(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.compress_image(self.file_name, 2, 2, 150, False, self.password, self.folder_name)

    def test_delete_picture_cropped_areas(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.compress_image(self.file_name, 2, 2, None, True, self.password, self.folder_name)

    def test_delete_picture_cropped_areas_wrong_shape_type(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        try:
            BaseTest.slides_api.compress_image(self.file_name, 2, 3, None, True, self.password, self.folder_name)
            self.fail("Should throw an exception if shape is not PictureFrame")
        except ApiException as ex:
            self.assertEqual(400, ex.status)
