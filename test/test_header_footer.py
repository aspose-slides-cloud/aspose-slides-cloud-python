from __future__ import absolute_import

from asposeslidescloud import NotesSlideHeaderFooter, HeaderFooter
from test.base_test import BaseTest

class TestHeaderFooter(BaseTest):
    def setUp(self):
        self.slide_index = 1

    def tearDown(self):
        pass

    def test_slides_footer(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = HeaderFooter()
        dto.is_footer_visible = True
        dto.footer_text = "footer"
        dto.is_date_time_visible = False
        BaseTest.slides_api.set_presentation_header_footer(self.file_name, dto, self.password, self.folder_name)
        result = BaseTest.slides_api.get_slide_header_footer(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertTrue(result.is_footer_visible)
        self.assertFalse(result.is_date_time_visible)

    def test_slide_footer(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = HeaderFooter()
        dto.is_footer_visible = True
        dto.footer_text = "footer"
        dto.is_date_time_visible = False
        result = BaseTest.slides_api.set_slide_header_footer(self.file_name, self.slide_index, dto, self.password, self.folder_name)
        self.assertTrue(result.is_footer_visible)
        self.assertFalse(result.is_date_time_visible)
        result = BaseTest.slides_api.get_slide_header_footer(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertTrue(result.is_footer_visible)
        self.assertFalse(result.is_date_time_visible)

    def test_notes_slide_footer(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = NotesSlideHeaderFooter()
        dto.is_header_visible = True
        dto.footer_text = "footer"
        dto.is_date_time_visible = False
        result = BaseTest.slides_api.set_notes_slide_header_footer(self.file_name, self.slide_index, dto, self.password, self.folder_name)
        self.assertTrue(result.is_header_visible)
        self.assertFalse(result.is_date_time_visible)
        result = BaseTest.slides_api.get_notes_slide_header_footer(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertTrue(result.is_header_visible)
        self.assertFalse(result.is_date_time_visible)