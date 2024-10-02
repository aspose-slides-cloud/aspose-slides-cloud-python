from __future__ import absolute_import

from test.base_test import BaseTest
from asposeslidescloud import Portion, PortionFormat

class TestText(BaseTest):
    def setUp(self):
        self.slide_index = 1

    def tearDown(self):
        pass

    def test_text_get(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.get_presentation_text_items(self.file_name, None, self.password, self.folder_name)
        result_with_empty = BaseTest.slides_api.get_presentation_text_items(self.file_name, True, self.password, self.folder_name)
        slide_result = BaseTest.slides_api.get_slide_text_items(self.file_name, self.slide_index, None, self.password, self.folder_name)
        slide_result_with_empty = BaseTest.slides_api.get_slide_text_items(self.file_name, self.slide_index, True, self.password, self.folder_name)
        self.assertLess(len(result.items), len(result_with_empty.items))
        self.assertLess(len(slide_result.items), len(result.items))
        self.assertLess(len(slide_result.items), len(slide_result_with_empty.items))

    def test_text_replace_storage(self):
        old_value = "text"
        new_value = "new_text"
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.replace_presentation_text(self.file_name, old_value, new_value, None, None, self.password, self.folder_name)
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result_regex = BaseTest.slides_api.replace_presentation_regex(self.file_name, old_value, new_value, None, self.password, self.folder_name)
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result_with_empty = BaseTest.slides_api.replace_presentation_text(self.file_name, old_value, new_value, True, None, self.password, self.folder_name)
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result_whole_words = BaseTest.slides_api.replace_presentation_text(self.file_name, old_value, new_value, True, True, self.password, self.folder_name)
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide_result = BaseTest.slides_api.replace_slide_text(self.file_name, self.slide_index, old_value, new_value, None, self.password, self.folder_name)
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide_result_with_empty = BaseTest.slides_api.replace_slide_text(self.file_name, self.slide_index, old_value, new_value, True, self.password, self.folder_name)
        self.assertEqual(result.matches, result_regex.matches)
        self.assertLess(result.matches, result_with_empty.matches)
        self.assertLess(result_whole_words.matches, result_with_empty.matches)
        self.assertLess(slide_result.matches, result.matches)
        self.assertLess(slide_result.matches, slide_result_with_empty.matches)

    def test_text_replace_request(self):
        old_value = "text"
        new_value = "new_text"
        with open(self.local_path, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.replace_presentation_text_online(source, old_value, new_value, None, None, self.password)
        BaseTest.slides_api.replace_presentation_regex_online(source, old_value, new_value, None, self.password)
        BaseTest.slides_api.replace_presentation_text_online(source, old_value, new_value, True, None, self.password)
        BaseTest.slides_api.replace_slide_text_online(source, self.slide_index, old_value, new_value, None, self.password)
        BaseTest.slides_api.replace_slide_text_online(source, self.slide_index, old_value, new_value, True, self.password)

    def test_replace_text_formatting(self):
        shape_index = 1
        paragraph_index = 1
        portion_index = 1
        old_text = "banana"
        new_text = "orange"
        color = "#FFFFA500"

        portion = Portion()
        portion.text = old_text

        portion_format = PortionFormat()
        portion_format.font_color = "#FFFFA500"

        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.create_portion(self.file_name, self.slide_index, shape_index, paragraph_index, portion, portion_index, self.password, self.folder_name)
        BaseTest.slides_api.replace_text_formatting(self.file_name, old_text, new_text, portion_format, None, self.password, self.folder_name)
        updated_portion = BaseTest.slides_api.get_portion(self.file_name, self.slide_index, shape_index, paragraph_index, portion_index, self.password, self.folder_name)
        self.assertEqual(new_text, updated_portion.text)
        self.assertEqual(color, updated_portion.font_color)

    def test_replace_text_formatting_online(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        portion_format = PortionFormat()
        portion_format.font_color = "#FFFFA500"
        BaseTest.slides_api.replace_text_formatting_online(source, "banana", "orange", portion_format, None, self.password)

    def test_highlight_shape_text(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        text_to_highlight = "highlight"
        color = "#FFF5FF8A"
        BaseTest.slides_api.highlight_shape_text(self.file_name, slide_index, shape_index, text_to_highlight, color, None, False, self.password, self.folder_name)
        para = BaseTest.slides_api.get_paragraph(self.file_name, slide_index, shape_index, paragraph_index, self.password, self.folder_name)
        self.assertNotEqual(para.portion_list[0].text, text_to_highlight)
        self.assertNotEqual(para.portion_list[0].highlight_color, color)
        self.assertEqual(para.portion_list[1].text, text_to_highlight)
        self.assertEqual(para.portion_list[1].highlight_color, color)

    def test_highlight_shape_regex(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        text_to_highlight = "highlight"
        regex = "h.ghl[abci]ght"
        color = "#FFF5FF8A"
        BaseTest.slides_api.highlight_shape_regex(self.file_name, slide_index, shape_index, regex, color, False, self.password, self.folder_name)
        para = BaseTest.slides_api.get_paragraph(self.file_name, slide_index, shape_index, paragraph_index, self.password, self.folder_name)
        self.assertNotEqual(para.portion_list[0].text, text_to_highlight)
        self.assertNotEqual(para.portion_list[0].highlight_color, color)
        self.assertEqual(para.portion_list[1].text, text_to_highlight)
        self.assertEqual(para.portion_list[1].highlight_color, color)

    def test_highlight_presentation_text(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        text_to_highlight = "highlight"
        color = "#FFF5FF8A"
        result = BaseTest.slides_api.highlight_presentation_text(self.file_name, text_to_highlight, color, None, False, self.password, self.folder_name)
        result_ignore_case = BaseTest.slides_api.highlight_presentation_text(self.file_name, text_to_highlight, color, None, True, self.password, self.folder_name)
        self.assertEqual(result.matches, result_ignore_case.matches)

        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        para = BaseTest.slides_api.get_paragraph(self.file_name, slide_index, shape_index, paragraph_index, self.password, self.folder_name)
        self.assertNotEqual(para.portion_list[0].text, text_to_highlight)
        self.assertNotEqual(para.portion_list[0].highlight_color, color)
        self.assertEqual(para.portion_list[1].text, text_to_highlight)
        self.assertEqual(para.portion_list[1].highlight_color, color)

    def test_highlight_presentation_regex(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        text_to_highlight = "highlight"
        regex = "h.ghl[abci]ght"
        color = "#FFF5FF8A"
        result = BaseTest.slides_api.highlight_presentation_regex(self.file_name, regex, color, False, self.password, self.folder_name)
        result_ignore_case = BaseTest.slides_api.highlight_presentation_regex(self.file_name, regex, color, True, self.password, self.folder_name)
        self.assertEqual(result.matches, result_ignore_case.matches)

        slide_index = 6
        shape_index = 1
        paragraph_index = 1
        para = BaseTest.slides_api.get_paragraph(self.file_name, slide_index, shape_index, paragraph_index, self.password, self.folder_name)
        self.assertNotEqual(para.portion_list[0].text, text_to_highlight)
        self.assertNotEqual(para.portion_list[0].highlight_color, color)
        self.assertEqual(para.portion_list[1].text, text_to_highlight)
        self.assertEqual(para.portion_list[1].highlight_color, color)