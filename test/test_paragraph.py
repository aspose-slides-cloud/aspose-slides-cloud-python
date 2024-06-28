from __future__ import absolute_import

from asposeslidescloud import Paragraph, Portion, PortionFormat
from test.base_test import BaseTest

class TestParagraph(BaseTest):
    def setUp(self):
        self.slide_index = 6
        self.shape_index = 2
        self.group_shape_index = 3
        self.sub_shape = "1"
        self.paragraph_index = 1

    def tearDown(self):
        pass

    def test_get_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_paragraph(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, self.password, self.folder_name)
        self.assertEqual(2, len(response.portion_list))

    def test_get_paragraphs(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_paragraphs(
            self.file_name, self.slide_index, self.shape_index, self.password, self.folder_name)
        self.assertEqual(2, len(response.paragraph_links))

    def test_get_sub_shape_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_paragraph(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(2, len(response.portion_list))

    def test_get_sub_shape_paragraphs(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_paragraphs(
            self.file_name, self.slide_index, self.group_shape_index, self.password, self.folder_name, None, self.sub_shape)
        self.assertEqual(2, len(response.paragraph_links))

    def test_create_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Paragraph()
        dto.margin_left = 2
        dto.margin_right = 2
        dto.alignment = "Center"
        response = BaseTest.slides_api.create_paragraph(
            self.file_name, self.slide_index, self.shape_index, dto, None, self.password, self.folder_name)
        self.assertEqual(dto.margin_left, response.margin_left)
        self.assertEqual(dto.margin_right, response.margin_right)
        self.assertEqual(dto.alignment, response.alignment)

    def test_create_paragraph_with_portions(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        portion1 = Portion()
        portion1.text = "Portion1"
        portion2 = Portion()
        portion2.text = "Portion2"
        dto = Paragraph()
        dto.portion_list = [portion1, portion2]
        response = BaseTest.slides_api.create_paragraph(
            self.file_name, self.slide_index, self.shape_index, dto, None, self.password, self.folder_name)
        self.assertEqual(2, len(response.portion_list))

    def test_create_sub_shape_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Paragraph()
        dto.margin_left = 2
        dto.margin_right = 2
        dto.alignment = "Center"
        response = BaseTest.slides_api.create_paragraph(
            self.file_name, self.slide_index, self.group_shape_index, dto, None, self.password, self.folder_name, None, self.sub_shape)
        self.assertEqual(dto.margin_left, response.margin_left)
        self.assertEqual(dto.margin_right, response.margin_right)
        self.assertEqual(dto.alignment, response.alignment)

    def test_update_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Paragraph()
        dto.margin_left = 2
        dto.margin_right = 2
        dto.alignment = "Center"
        response = BaseTest.slides_api.update_paragraph(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, dto, self.password, self.folder_name)
        self.assertEqual(dto.margin_left, response.margin_left)
        self.assertEqual(dto.margin_right, response.margin_right)
        self.assertEqual(dto.alignment, response.alignment)

    def test_update_sub_shape_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Paragraph()
        dto.margin_left = 2
        dto.margin_right = 2
        dto.alignment = "Center"
        response = BaseTest.slides_api.update_paragraph(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            dto,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(dto.margin_left, response.margin_left)
        self.assertEqual(dto.margin_right, response.margin_right)
        self.assertEqual(dto.alignment, response.alignment)

    def test_delete_paragraphs(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_paragraphs(
            self.file_name, self.slide_index, self.shape_index, None, self.password, self.folder_name)
        self.assertEqual(0, len(response.paragraph_links))

    def test_delete_paragraphs_indexes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_paragraphs(
            self.file_name, self.slide_index, self.shape_index, [2], self.password, self.folder_name)
        self.assertEqual(1, len(response.paragraph_links))

    def test_delete_sub_shape_paragraphs(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_paragraphs(
            self.file_name, self.slide_index, self.group_shape_index, None, self.password, self.folder_name, None, self.sub_shape)
        self.assertEqual(0, len(response.paragraph_links))

    def test_delete_sub_shape_paragraphs_indexes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_paragraphs(
            self.file_name, self.slide_index, self.group_shape_index, [1], self.password, self.folder_name, None, self.sub_shape)
        self.assertEqual(1, len(response.paragraph_links))

    def test_delete_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_paragraph(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, self.password, self.folder_name)
        self.assertEqual(1, len(response.paragraph_links))

    def test_delete_sub_shape_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_paragraph(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(1, len(response.paragraph_links))

    def test_get_paragraph_rect(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_paragraph_rectangle(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, self.password, self.folder_name)
        self.assertIsNotNone(response)
        self.assertGreater(response.x, 0)
        self.assertGreater(response.y, 0)
        self.assertGreater(response.width, 0)
        self.assertGreater(response.height, 0)

    def test_paragraph_default_portion_format(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Paragraph()
        portion_format = PortionFormat()
        portion_format.font_height = 20
        portion_format.latin_font = "Arial"
        portion1 = Portion()
        portion1.text = "Portion1"
        portion2 = Portion()
        portion2.text = "Portion2"
        dto.portion_list = [portion1, portion2]
        dto.default_portion_format = portion_format
        response = BaseTest.slides_api.create_paragraph(
            self.file_name, self.slide_index, self.shape_index, dto, None, self.password, self.folder_name)
        self.assertEqual(2, len(response.portion_list))
        self.assertIsNotNone(response.default_portion_format)
        self.assertEqual(response.default_portion_format.latin_font, dto.default_portion_format.latin_font)
        self.assertEqual(response.default_portion_format.font_height, dto.default_portion_format.font_height)

    def test_get_paragraph_effective(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_paragraph_effective(
            self.file_name, self.slide_index, self.shape_index, self.paragraph_index, self.password, self.folder_name)
        self.assertEqual(72, response.default_tab_size)


    def test_get_sub_shape_paragraph_effective(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_paragraph_effective(
            self.file_name,
            self.slide_index,
            self.group_shape_index,
            self.paragraph_index,
            self.password,
            self.folder_name,
            None,
            self.sub_shape)
        self.assertEqual(72, response.default_tab_size)
