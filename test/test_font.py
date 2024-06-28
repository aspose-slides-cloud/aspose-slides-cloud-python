from __future__ import absolute_import

import os
from asposeslidescloud import FontSubstRule, ImageExportOptions
from test.base_test import BaseTest

class TestFont(BaseTest):
    def setUp(self):
        self.font_name = "Calibri"
        self.font_name_times = "Times New Roman"
        self.font_file_name = "calibri.ttf"

    def tearDown(self):
        pass

    def test_get_available_fonts(self):
        response = BaseTest.slides_api.get_available_fonts()
        self.assertTrue(len(response.list) > 1)
        self.assertTrue(response.list[0].is_custom == None)

    def test_get_fonts(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_fonts(self.file_name, self.password, self.folder_name)
        self.assertEqual(3, len(response.list))

    def test_get_fonts_online(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.get_fonts_online(source, self.password)
        self.assertEqual(3, len(response.list))

    def test_set_embedded_font(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.set_embedded_font(self.file_name, self.font_name, False, self.password, self.folder_name)
        self.assertEqual(None, response.list[0].is_embedded)
        self.assertEqual(True, response.list[1].is_embedded)
        self.assertEqual(True, response.list[2].is_embedded)
        self.assertEqual(self.font_name, response.list[2].font_name)

    def test_set_embedded_font_online(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.set_embedded_font_online(source, self.font_name, False, self.password)

    def test_set_embedded_font_from_request(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        with open(self.test_data_path + "/" + self.font_file_name, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.set_embedded_font_from_request(source, self.file_name, False, self.password, self.folder_name)
        self.assertEqual(None, response.list[0].is_embedded)
        self.assertEqual(True, response.list[1].is_embedded)
        self.assertEqual(True, response.list[2].is_embedded)
        self.assertEqual(self.font_name, response.list[2].font_name)

    def test_set_embedded_font_from_request_online(self):
        with open(self.local_path, 'rb') as f:
            source_file = f.read()
        with open(self.test_data_path + "/" + self.font_file_name, 'rb') as f:
            source_font_file = f.read()
        response = BaseTest.slides_api.set_embedded_font_from_request_online(source_file, source_font_file, False, self.password)

    def test_compress_embedded_fonts(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.set_embedded_font(self.file_name, self.font_name, False, self.password, self.folder_name)
        self.assertEqual(True, response.list[2].is_embedded)
        #In a real world example, you would rather achieve the same result by calling SetEmbeddedFont with onlyUsed = true
        response = BaseTest.slides_api.compress_embedded_fonts(self.file_name, self.password, self.folder_name)

    def test_compress_embedded_fonts_online(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.set_embedded_font_online(source, self.font_name, False, self.password)
        with open(response, 'rb') as f:
            source_embedded = f.read()
        #In a real world example, you would rather achieve the same result by calling SetEmbeddedFont with onlyUsed = true
        responseCompressed = BaseTest.slides_api.compress_embedded_fonts_online(source_embedded, self.password)
        self.assertGreater(os.path.getsize(response), os.path.getsize(responseCompressed))

    def test_delete_embedded_font(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.set_embedded_font(self.file_name, self.font_name, False, self.password, self.folder_name)
        self.assertEqual(True, response.list[2].is_embedded)
        response = BaseTest.slides_api.delete_embedded_font(self.file_name, self.font_name, self.password, self.folder_name)
        self.assertEqual(None, response.list[2].is_embedded)

    def test_delete_embedded_font_online(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.set_embedded_font_online(source, self.font_name, False, self.password)
        with open(response, 'rb') as f:
            source_embedded = f.read()
        responseDeleted = BaseTest.slides_api.delete_embedded_font_online(source_embedded, self.font_name, self.password)
        self.assertGreater(os.path.getsize(response), os.path.getsize(responseDeleted))

    def test_replace_font(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.replace_font(
            self.file_name, self.font_name, self.font_name_times, True, self.password, self.folder_name)
        self.assertEqual(True, response.list[2].is_embedded)
        self.assertEqual(self.font_name_times, response.list[2].font_name)

    def test_replace_font_online(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.replace_font_online(source, self.font_name, self.font_name_times, True, self.password)

    def test_font_substitution(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        font_rule1 = FontSubstRule()
        font_rule1.source_font = self.font_name
        font_rule1.target_font = self.font_name_times
        font_rule1.not_found_only = False
        font_rule2 = FontSubstRule()
        font_rule2.source_font = self.font_name
        font_rule2.target_font = self.font_name_times

        exportOptions = ImageExportOptions()
        exportOptions.font_subst_rules = [font_rule1, font_rule2]
        response = BaseTest.slides_api.download_presentation(self.file_name, "PNG", exportOptions, self.password, self.folder_name)
