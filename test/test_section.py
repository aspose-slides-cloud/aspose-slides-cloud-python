from __future__ import absolute_import

from asposeslidescloud import Sections, Section
from test.base_test import BaseTest

class TestSection(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_sections(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.get_sections(self.file_name, self.password, self.folder_name)
        self.assertEqual(3, len(result.section_list))

    def test_set_sections(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Sections()
        section1 = Section()
        section1.name = "Section1"
        section1.first_slide_index = 1
        section2 = Section()
        section2.name = "Section2"
        section2.first_slide_index = 3
        dto.section_list = [ section1, section2 ]
        result = BaseTest.slides_api.set_sections(self.file_name, dto, self.password, self.folder_name)
        self.assertEqual(len(dto.section_list), len(result.section_list))
        self.assertEqual(section2.first_slide_index - section1.first_slide_index, len(result.section_list[0].slide_list))

    def test_create_section(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.create_section(self.file_name, "NewSection", 5, self.password, self.folder_name)
        self.assertEqual(4, len(result.section_list))

    def test_update_section(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        section_index = 2
        section_name = "UpdatedSection"
        result = BaseTest.slides_api.update_section(self.file_name, section_index, section_name, self.password, self.folder_name)
        self.assertEqual(3, len(result.section_list))
        self.assertEqual(section_name, result.section_list[section_index - 1].name)

    def test_move_section(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.move_section(self.file_name, 1, 2, self.password, self.folder_name)
        self.assertEqual(3, len(result.section_list))

    def test_clear_sections(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_sections(self.file_name, None, None, self.password, self.folder_name)
        self.assertEqual(0, len(result.section_list))

    def test_delete_sections(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_sections(self.file_name, [ 2, 3 ], None, self.password, self.folder_name)
        self.assertEqual(1, len(result.section_list))

    def test_delete_section(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_section(self.file_name, 2, None, self.password, self.folder_name)
        self.assertEqual(2, len(result.section_list))