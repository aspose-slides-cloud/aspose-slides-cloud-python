from __future__ import absolute_import

from asposeslidescloud import PictureFrame, Hyperlink, Portion, Shape
from test.base_test import BaseTest

class TestHyperlink(BaseTest):
    def setUp(self):
        self.slide_index = 2
        self.shape_index = 2

    def tearDown(self):
        pass

    def test_hyperlink_get_shape(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        shape = BaseTest.slides_api.get_shape(self.file_name, self.slide_index, self.shape_index, self.password, self.folder_name)
        self.assertIsNotNone(shape.hyperlink_click)
        self.assertEqual("Hyperlink", shape.hyperlink_click.action_type)
        self.assertIsNone(shape.hyperlink_mouse_over)

    def test_hyperlink_get_portion(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        portion = BaseTest.slides_api.get_portion(self.file_name, self.slide_index, 1, 1, 2, self.password, self.folder_name)
        self.assertIsNone(portion.hyperlink_click)
        self.assertIsNotNone(portion.hyperlink_mouse_over)
        self.assertEqual("JumpLastSlide", portion.hyperlink_mouse_over.action_type)

    def test_hyperlink_create_shape(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        shape = Shape()
        hyperlink = Hyperlink()
        hyperlink.action_type = "Hyperlink"
        hyperlink.external_url = "https://docs.aspose.cloud/slides"
        shape.hyperlink_click = hyperlink
        updated_shape = BaseTest.slides_api.update_shape(
            self.file_name, self.slide_index, self.shape_index, shape, self.password, self.folder_name)
        self.assertIsNotNone(updated_shape.hyperlink_click)
        self.assertEqual(shape.hyperlink_click.external_url, updated_shape.hyperlink_click.external_url)

    def test_hyperlink_create_portion(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Portion()
        dto.text = "Link text"
        hyperlink = Hyperlink()
        hyperlink.action_type = "JumpLastSlide"
        dto.hyperlink_mouse_over = hyperlink
        updated_portion = BaseTest.slides_api.create_portion(self.file_name, 1, 1, 1, dto, None, self.password, self.folder_name)
        self.assertIsNotNone(updated_portion.hyperlink_mouse_over)
        self.assertEqual(dto.hyperlink_mouse_over.action_type, updated_portion.hyperlink_mouse_over.action_type)

    def test_hyperlink_delete(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        shape = PictureFrame()
        hyperlink = Hyperlink()
        hyperlink.is_disabled = True
        shape.hyperlink_click = hyperlink
        updated_shape = BaseTest.slides_api.update_shape(
            self.file_name, self.slide_index, self.shape_index, shape, self.password, self.folder_name)
        self.assertIsNone(updated_shape.hyperlink_click)