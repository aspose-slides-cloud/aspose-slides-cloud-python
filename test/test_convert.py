from __future__ import absolute_import

import os

from asposeslidescloud import PdfExportOptions, Html5ExportOptions, ImageExportOptions, HandoutLayoutingOptions, FontFallbackRule
from test.base_test import BaseTest

class TestConvert(BaseTest):
    def setUp(self):
        self.pdf_file = "test.pdf"
        self.out_path = "out/" + self.pdf_file

    def tearDown(self):
        pass

    def test_convert_request_to_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.convert(source, 'pdf', self.password)
        result_slides = BaseTest.slides_api.convert(source, 'pdf', self.password, None, None, [ 2, 4 ])
        self.assertGreater(os.path.getsize(result), os.path.getsize(result_slides))

    def test_convert_request_to_storage(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.convert_and_save(source, 'pdf', self.out_path, self.password)
        self.assertTrue(BaseTest.slides_api.object_exists(self.out_path).exists)

    def test_convert_storage_to_request(self):
        file_name = self.pdf_file
        BaseTest.slides_api.copy_file(self.temp_folder_name + "/" + file_name, self.folder_name + "/" + file_name)
        BaseTest.slides_api.download_presentation(file_name, 'html5', None, self.password, self.folder_name)

    def test_convert_storage_to_storage(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.save_presentation(self.file_name, 'pdf', self.out_path, None, self.password, self.folder_name)
        self.assertTrue(BaseTest.slides_api.object_exists(self.out_path).exists)

    def test_convert_request_with_options(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.convert(source, 'pdf', self.password)
        options = PdfExportOptions()
        options.draw_slides_frame = True
        result_with_options = BaseTest.slides_api.convert(source, 'pdf', self.password, None, None, None, options)
        self.assertNotEqual(os.path.getsize(result), os.path.getsize(result_with_options))

    def test_convert_storage_with_options(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.download_presentation(self.file_name, 'png', None, self.password, self.folder_name)
        options = ImageExportOptions()
        options.width = 480
        options.height = 360
        result_with_options = BaseTest.slides_api.download_presentation(self.file_name, 'png', options, self.password, self.folder_name)
        self.assertGreater(os.path.getsize(result), os.path.getsize(result_with_options))

    def test_convert_slide_request_to_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.download_slide_online(source, 1, 'pdf', None, None, self.password)

    def test_convert_slide_request_to_storage(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.save_slide_online(source, 1, 'pdf', self.out_path, None, None, self.password)
        self.assertTrue(BaseTest.slides_api.object_exists(self.out_path).exists)

    def test_convert_slide_storage_to_request(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.download_slide(self.file_name, 1, 'pdf', None, None, None, self.password, self.folder_name)

    def test_convert_slide_storage_to_storage(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.save_slide(self.file_name, 1, 'pdf', self.out_path, None, None, None, self.password, self.folder_name)
        self.assertTrue(BaseTest.slides_api.object_exists(self.out_path).exists)

    def test_convert_slide_request_with_options(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.download_slide_online(source, 1, 'pdf', None, None, self.password)
        options = PdfExportOptions()
        options.draw_slides_frame = True
        result_with_options = BaseTest.slides_api.download_slide_online(
            source, 1, 'pdf', None, None, self.password, None, None, options)
        self.assertNotEqual(os.path.getsize(result), os.path.getsize(result_with_options))

    def test_convert_slide_storage_with_options(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.download_slide(self.file_name, 1, 'pdf', None, None, None, self.password, self.folder_name)
        options = PdfExportOptions()
        options.draw_slides_frame = True
        result_with_options = BaseTest.slides_api.download_slide(
            self.file_name, 1, 'pdf', options, None, None, self.password, self.folder_name)
        self.assertNotEqual(os.path.getsize(result), os.path.getsize(result_with_options))

    def test_convert_shape_request_to_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.download_shape_online(source, 1, 3, 'png', None, None, None, self.password)

    def test_convert_shape_request_to_storage(self):
        out_path = "out/test.png"
        with open(self.local_path, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.save_shape_online(source, 1, 1, 'png', out_path, None, None, None, self.password)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_convert_shape_storage_to_request(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.download_shape(self.file_name, 1, 1, 'png', None, None, None, None, self.password, self.folder_name)

    def test_convert_sub_shape_storage_to_request(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        converted = BaseTest.slides_api.download_shape(
            self.file_name, 1, 4, 'png', None, None, None, None, self.password, self.folder_name, None, "1")
        self.assertIsNotNone(converted)

    def test_convert_shape_storage_to_storage(self):
        out_path = "out/test.png"
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.save_shape(self.file_name, 1, 1, 'png', out_path, None, None, None, None, self.password, self.folder_name)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_convert_subshape_storage_to_storage(self):
        out_path = "out/test.png"
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.save_shape(
            self.file_name, 1, 4, 'png', out_path, None, None, None, None, self.password, self.folder_name, None, "1")
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_convert_with_font_fallback_rules(self):
        c_startUnicodeIndex = 0x0B80
        c_endUnicodeIndex = 0x0BFF

        font_rule1 = FontFallbackRule()
        font_rule1.range_start_index = c_startUnicodeIndex
        font_rule1.range_end_index = c_endUnicodeIndex
        font_rule1.fallback_font_list = ["Vijaya" ]

        font_rule2 = FontFallbackRule()
        font_rule2.range_start_index = c_startUnicodeIndex
        font_rule2.range_end_index = c_endUnicodeIndex
        font_rule2.fallback_font_list = ["Segoe UI Emoji", "Segoe UI Symbol", "Arial"]

        export_options = ImageExportOptions()
        export_options.font_fallback_rules = [font_rule1, font_rule2]

        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.download_presentation(self.file_name, "png", export_options, self.password, self.folder_name)
        self.assertIsNotNone(response)

    def test_convert_with_slide_layout_options(self):
        slides_layout_options = HandoutLayoutingOptions()
        slides_layout_options.handout = "Handouts2"
        slides_layout_options.print_slide_numbers = True

        export_options = PdfExportOptions()
        export_options.slides_layout_options = slides_layout_options

        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.download_presentation(self.file_name, "pdf", export_options, self.password, self.folder_name)
        self.assertIsNotNone(response)

    def test_convert_with_custom_html5_templates(self):
        templates_path = "Html5Templates"
        template_file_name = "pictureFrame.html"

        BaseTest.slides_api.create_folder(templates_path)
        BaseTest.slides_api.copy_file(self.temp_folder_name + "/" + template_file_name, templates_path + "/" + template_file_name)
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        html5_options = Html5ExportOptions()
        html5_options.templates_path = templates_path
        html5_options.animate_transitions = True
        response = BaseTest.slides_api.download_presentation(self.file_name, "html5", html5_options, self.password, self.folder_name)
        self.assertIsNotNone(response)

    def test_get_html5_templates(self):
        response = BaseTest.slides_api.get_html5_templates()
        self.assertIsNotNone(response)
