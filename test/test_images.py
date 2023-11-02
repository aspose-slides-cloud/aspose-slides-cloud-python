from __future__ import absolute_import

import os
from zipfile import ZipFile

from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestImages(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.slides_api_configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_image_get(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        presentation_result = BaseTest.slides_api.get_presentation_images(file_name, password, folder_name)
        slide_result = BaseTest.slides_api.get_slide_images(file_name, 1, password, folder_name)
        self.assertLess(len(slide_result.list), len(presentation_result.list))

    def test_image_download_all_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        default_result = BaseTest.slides_api.download_images_default_format(file_name, password, folder_name)
        png_result = BaseTest.slides_api.download_images(file_name, 'png', password, folder_name)
        self.assertNotEqual(os.path.getsize(default_result), os.path.getsize(png_result))
        with ZipFile(default_result) as default_zip:
            with ZipFile(png_result) as png_zip:
                self.assertEqual(len(default_zip.namelist()), len(png_zip.namelist()))

    def test_image_download_all_request(self):
        password = "password"
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        default_result = BaseTest.slides_api.download_images_default_format_online(source, password)
        png_result = BaseTest.slides_api.download_images_online(source, 'png', password)
        self.assertNotEqual(os.path.getsize(default_result), os.path.getsize(png_result))
        with ZipFile(default_result) as default_zip:
            with ZipFile(png_result) as png_zip:
                self.assertEqual(len(default_zip.namelist()), len(png_zip.namelist()))

    def test_image_download_storage(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        slide_index = 1
        password = "password"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        default_result = BaseTest.slides_api.download_image_default_format(file_name, slide_index, password, folder_name)
        png_result = BaseTest.slides_api.download_image(file_name, slide_index, 'png', password, folder_name)
        self.assertNotEqual(os.path.getsize(default_result), os.path.getsize(png_result))

    def test_image_download_request(self):
        slide_index = 1
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        default_result = BaseTest.slides_api.download_image_default_format_online(source, slide_index, constant.PASSWORD)
        png_result = BaseTest.slides_api.download_image_online(source, slide_index, 'png', constant.PASSWORD)
        self.assertNotEqual(os.path.getsize(default_result), os.path.getsize(png_result))

    def test_replace_image(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME, constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/watermark.png", 'rb') as f:
            image_source = f.read()
        image_index = 1
        BaseTest.slides_api.replace_image(constant.FILE_NAME, image_index, image_source, constant.PASSWORD, constant.FOLDER_NAME)

    def test_replace_image_request(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            file_source = f.read()
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/watermark.png", 'rb') as f:
            image_source = f.read()
        image_index = 1
        response = BaseTest.slides_api.replace_image_online(file_source, image_index, image_source, constant.PASSWORD)
        self.assertNotEqual(os.path.getsize(response), 0)