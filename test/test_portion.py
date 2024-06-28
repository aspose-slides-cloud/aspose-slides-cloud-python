from __future__ import absolute_import

from asposeslidescloud import Portion, SolidFill
from test.base_test import BaseTest

class TestPortion(BaseTest):
    def setUp(self):
        self.slide_index = 6
        self.shape_index = 2
        self.group_shape_index = 3
        self.sub_shape = "1"
        self.paragraph_index = 1
        self.portion_index = 1

    def tearDown(self):
        pass

    def test_get_portions(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_portions(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, self.password, self.folder_name)
        self.assertEqual(2, len(response.items))

    def test_get_sub_shape_portions(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_portions(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(2, len(response.items))

    def test_get_portion(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_portion(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, self.portion_index, self.password, self.folder_name)
        self.assertTrue("portion 1" in response.text)

    def test_get_sub_shape_portion(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_portion(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            self.portion_index,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertTrue("portion 1" in response.text)

    def test_create_portion(self):
        dto = Portion()
        dto.text = "portion 1"
        dto.font_bold = "True"
        dto.font_height = 20
        dto.latin_font = "Arial"
        fill_format = SolidFill()
        fill_format.color = "#FFF5FF8A"
        dto.fill_format = fill_format

        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.create_portion(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, dto, None, self.password, self.folder_name)
        self.assertEqual(dto.text, response.text)
        self.assertEqual(dto.font_bold, response.font_bold)
        self.assertEqual(dto.font_height, response.font_height)
        self.assertEqual(dto.latin_font, response.latin_font)
        self.assertEqual("Solid", response.fill_format.type)

    def test_create_sub_shape_portion(self):
        dto = Portion()
        dto.text = "portion 1"
        dto.font_bold = "True"
        dto.font_height = 20
        dto.latin_font = "Arial"
        fill_format = SolidFill()
        fill_format.color = "#FFF5FF8A"
        dto.fill_format = fill_format

        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.create_portion(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            dto,
            None,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(dto.text, response.text)
        self.assertEqual(dto.font_bold, response.font_bold)
        self.assertEqual(dto.font_height, response.font_height)
        self.assertEqual(dto.latin_font, response.latin_font)
        self.assertEqual("Solid", response.fill_format.type)

    def test_update_portion(self):
        dto = Portion()
        dto.text = "portion 1"
        dto.font_bold = "True"
        dto.font_height = 20
        dto.latin_font = "Arial"
        fill_format = SolidFill()
        fill_format.color = "#FFF5FF8A"
        dto.fill_format = fill_format

        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.update_portion(
            self.file_name,
            self.slide_index,
            self.shape_index,
            self.paragraph_index,
            self.portion_index,
            dto,
            self.password,
            self.folder_name)
        self.assertEqual(dto.text, response.text)
        self.assertEqual(dto.font_bold, response.font_bold)
        self.assertEqual(dto.font_height, response.font_height)
        self.assertEqual(dto.latin_font, response.latin_font)
        self.assertEqual("Solid", response.fill_format.type)

    def test_update_sub_shape_portion(self):
        dto = Portion()
        dto.text = "portion 1"
        dto.font_bold = "True"
        dto.font_height = 20
        dto.latin_font = "Arial"
        fill_format = SolidFill()
        fill_format.color = "#FFF5FF8A"
        dto.fill_format = fill_format

        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.update_portion(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            self.portion_index,
            dto,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(dto.text, response.text)
        self.assertEqual(dto.font_bold, response.font_bold)
        self.assertEqual(dto.font_height, response.font_height)
        self.assertEqual(dto.latin_font, response.latin_font)
        self.assertEqual("Solid", response.fill_format.type)

    def test_delete_portions(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_portions(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, None, self.password, self.folder_name)
        self.assertEqual(0, len(response.items))

    def test_delete_portions_indexes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_portions(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, [1], self.password, self.folder_name)
        self.assertEqual(1, len(response.items))

    def test_delete_sub_shape_portions(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_portions(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            None,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(0, len(response.items))

    def test_delete_sub_shape_portions_indexes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_portions(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            [1],
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(1, len(response.items))

    def test_delete_portion(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_portion(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, self.portion_index, self.password, self.folder_name)
        self.assertEqual(1, len(response.items))

    def test_delete_sub_shape_portion(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_portion(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            self.portion_index,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(1, len(response.items))

    def test_get_portion_rect(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_portion_rectangle(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, self.portion_index, self.password, self.folder_name)
        self.assertIsNotNone(response)
        self.assertGreater(response.x, 0)
        self.assertGreater(response.y, 0)
        self.assertGreater(response.width, 0)
        self.assertGreater(response.height, 0)

    def test_get_portion_effective(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_portion_effective(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, self.portion_index, self.password, self.folder_name)
        self.assertEqual(18, response.font_height)

    def test_get_sub_shape_portion_effective(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_portion_effective(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            self.portion_index,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(18, response.font_height)