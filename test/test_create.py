from __future__ import absolute_import

from asposeslidescloud import PdfImportOptions
from test.base_test import BaseTest

class TestCreate(BaseTest):
    def setUp(self):
        self.pdf_path = self.test_data_path + "/test.pdf"
        self.html = "<html><body>New Content</body></html>"

    def tearDown(self):
        pass

    def test_create_empty(self):
        BaseTest.slides_api.delete_file(self.path)
        BaseTest.slides_api.create_presentation(self.file_name, None, None, None, self.folder_name)

    def test_create_from_request(self):
        BaseTest.slides_api.delete_file(self.path)
        with open(self.local_path, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.create_presentation(self.file_name, source, self.password, None, self.folder_name)

    def test_create_from_storage(self):
        new_file_name = "test2.pptx"
        BaseTest.slides_api.delete_file(self.folder_name + "/" + new_file_name)
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.create_presentation_from_source(new_file_name, self.path, self.password, None, None, self.folder_name)

    def test_create_from_template(self):
        template_file_name = "TemplateCV.pptx"
        BaseTest.slides_api.delete_file(self.path)
        template_path = self.folder_name + "/" + template_file_name
        BaseTest.slides_api.copy_file(self.temp_folder_name + "/" + template_file_name, template_path)
        data = "<staff><person><name>John Doe</name><address><line1>10 Downing Street</line1><line2>London</line2></address><phone>+457 123456</phone><bio>Hi, I'm John and this is my CV</bio><skills><skill><title>C#</title><level>Excellent</level></skill><skill><title>C++</title><level>Good</level></skill><skill><title>Java</title><level>Average</level></skill></skills></person></staff>"
        BaseTest.slides_api.create_presentation_from_template(
            self.file_name, template_path, data, None, None, None, None, self.folder_name)

    def test_create_from_html(self):
        BaseTest.slides_api.delete_file(self.path)
        BaseTest.slides_api.import_from_html(self.file_name, self.html, None, self.folder_name)

    def test_append_from_html(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slideCount = len(BaseTest.slides_api.get_slides(self.file_name, self.password, self.folder_name).slide_list)
        BaseTest.slides_api.import_from_html(self.file_name, self.html, self.password, self.folder_name)
        newSlideCount = len(BaseTest.slides_api.get_slides(self.file_name, self.password, self.folder_name).slide_list)
        self.assertEqual(slideCount + 1, newSlideCount)

    def test_create_from_pdf(self):
        BaseTest.slides_api.delete_file(self.path)
        with open(self.pdf_path, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.import_from_pdf(self.file_name, source, None, None, self.folder_name)

    def test_append_from_pdf(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slideCount = len(BaseTest.slides_api.get_slides(self.file_name, self.password, self.folder_name).slide_list)
        with open(self.pdf_path, 'rb') as f:
            source = f.read()
        options = PdfImportOptions()
        options.detect_tables = False
        BaseTest.slides_api.import_from_pdf(self.file_name, source, options, self.password, self.folder_name)
        newSlideCount = len(BaseTest.slides_api.get_slides(self.file_name, self.password, self.folder_name).slide_list)
        self.assertEqual(slideCount + 4, newSlideCount)