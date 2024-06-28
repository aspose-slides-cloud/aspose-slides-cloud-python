from __future__ import absolute_import

import base64
import os

from asposeslidescloud import PictureFrame, PictureFill, Shape
from test.base_test import BaseTest

class TestWatermark(BaseTest):
    def setUp(self):
        self.slide_index = 1
        self.watermark_text = "watermarkText"

    def tearDown(self):
        pass

    def test_watermark_text_storage(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        get1_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        shape_count = len(get1_result.shapes_links) + 1
        BaseTest.slides_api.create_watermark(self.file_name, None, None, self.watermark_text, None, None, self.password, self.folder_name)
        get2_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(shape_count, len(get2_result.shapes_links))
        shape = BaseTest.slides_api.get_shape(self.file_name, self.slide_index, shape_count, self.password, self.folder_name)
        self.assertEqual("watermark", shape.name)
        self.assertEqual(self.watermark_text, shape.text)
        BaseTest.slides_api.delete_watermark(self.file_name, None, self.password, self.folder_name)
        get3_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(shape_count - 1, len(get3_result.shapes_links))

    def test_watermark_dto_storage(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        get1_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        shape_count = len(get1_result.shapes_links) + 1
        watermark = Shape()
        watermark.text = self.watermark_text
        BaseTest.slides_api.create_watermark(self.file_name, watermark, None, None, None, None, self.password, self.folder_name)
        get2_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(shape_count, len(get2_result.shapes_links))
        shape = BaseTest.slides_api.get_shape(self.file_name, self.slide_index, shape_count, self.password, self.folder_name)
        self.assertEqual("watermark", shape.name)
        self.assertEqual(self.watermark_text, shape.text)
        BaseTest.slides_api.delete_watermark(self.file_name, None, self.password, self.folder_name)
        get3_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(shape_count - 1, len(get3_result.shapes_links))

    def test_watermark_image_storage(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        get1_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        shape_count = len(get1_result.shapes_links) + 1
        with open(self.test_data_path + "/watermark.png", 'rb') as f:
            source = f.read()
        BaseTest.slides_api.create_image_watermark(self.file_name, source, None, self.password, self.folder_name)
        get2_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(shape_count, len(get2_result.shapes_links))
        shape = BaseTest.slides_api.get_shape(self.file_name, self.slide_index, shape_count, self.password, self.folder_name)
        self.assertEqual("watermark", shape.name)
        BaseTest.slides_api.delete_watermark(self.file_name, None, self.password, self.folder_name)
        get3_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(shape_count - 1, len(get3_result.shapes_links))

    def test_watermark_image_dto_storage(self):
        watermark_name = "myWatermark"
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        get1_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        shape_count = len(get1_result.shapes_links) + 1
        with open(self.test_data_path + "/watermark.png", 'rb') as f:
            source = f.read()
        watermark = PictureFrame()
        fill_format = PictureFill()
        fill_format.base64_data = base64.b64encode(source).decode('utf-8')
        watermark.fill_format = fill_format
        watermark.name = watermark_name
        BaseTest.slides_api.create_image_watermark(self.file_name, None, watermark, self.password, self.folder_name)
        get2_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(shape_count, len(get2_result.shapes_links))
        shape = BaseTest.slides_api.get_shape(self.file_name, self.slide_index, shape_count, self.password, self.folder_name)
        self.assertEqual(watermark_name, shape.name)
        BaseTest.slides_api.delete_watermark(self.file_name, watermark_name, self.password, self.folder_name)
        get3_result = BaseTest.slides_api.get_shapes(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(shape_count - 1, len(get3_result.shapes_links))

    def test_watermark_text_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        post_result = BaseTest.slides_api.create_watermark_online(source, None, None, self.watermark_text, None, None, self.password)
        self.assertNotEqual(len(source), os.path.getsize(post_result))
        delete_result = BaseTest.slides_api.delete_watermark_online(source, None, self.password)
        self.assertLess(os.path.getsize(delete_result), os.path.getsize(post_result))

    def test_watermark_dto_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        watermark = Shape()
        watermark.text = self.watermark_text
        post_result = BaseTest.slides_api.create_watermark_online(source, watermark, None, None, None, None, self.password)
        self.assertNotEqual(len(source), os.path.getsize(post_result))
        delete_result = BaseTest.slides_api.delete_watermark_online(source, None, self.password)
        self.assertLess(os.path.getsize(delete_result), os.path.getsize(post_result))

    def test_watermark_image_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        with open(self.test_data_path + "/watermark.png", 'rb') as f:
            watermark = f.read()
        post_result = BaseTest.slides_api.create_image_watermark_online(source, watermark, None, self.password)
        self.assertNotEqual(len(source), os.path.getsize(post_result))
        delete_result = BaseTest.slides_api.delete_watermark_online(source, None, self.password)
        self.assertLess(os.path.getsize(delete_result), os.path.getsize(post_result))

    def test_watermark_image_dto_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        with open(self.test_data_path + "/watermark.png", 'rb') as f:
            watermark_source = f.read()
        watermark = PictureFrame()
        fill_format = PictureFill()
        fill_format.base64_data = base64.b64encode(watermark_source).decode('utf-8')
        watermark.fill_format = fill_format
        post_result = BaseTest.slides_api.create_image_watermark_online(source, None, watermark, self.password)
        self.assertNotEqual(len(source), os.path.getsize(post_result))
        delete_result = BaseTest.slides_api.delete_watermark_online(source, None, self.password)
        self.assertLess(os.path.getsize(delete_result), os.path.getsize(post_result))
