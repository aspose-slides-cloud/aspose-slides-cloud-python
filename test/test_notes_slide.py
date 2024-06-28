from __future__ import absolute_import

from asposeslidescloud import Portion, Paragraph, Shape, NotesSlide
from test.base_test import BaseTest

class TestNotesSlide(BaseTest):
    def setUp(self):
        self.slide_index = 1
        self.notes_slide_text = "Notes slide text"

    def tearDown(self):
        pass

    def test_notes_slide_get_storage(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.get_notes_slide(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertTrue(result.text)

    def test_notes_slide_exists_storage(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.notes_slide_exists(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertTrue(result.exists)

    def test_notes_slide_download_storage(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.download_notes_slide(self.file_name, self.slide_index, 'png', None, None, self.password, self.folder_name)

    def test_notes_slide_get_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.get_notes_slide_online(source, self.slide_index, self.password)
        self.assertTrue(result.text)

    def test_notes_slide_exists_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.notes_slide_exists_online(source, self.slide_index, self.password)
        self.assertTrue(result.exists)

    def test_notes_slide_download_request(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        BaseTest.slides_api.download_notes_slide_online(source, self.slide_index, 'png', None, None, self.password)

    def test_notes_slide_shapes(self):
        shape_count = 3
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        shapes = BaseTest.slides_api.get_special_slide_shapes(self.file_name, self.slide_index, 'notesSlide', self.password, self.folder_name)
        self.assertEqual(shape_count, len(shapes.shapes_links))

        dto = Shape()
        dto.x = 100
        dto.y = 100
        dto.width = 500
        dto.height = 200
        dto.shape_type = "Rectangle"
        dto.text = "New shape"
        shape = BaseTest.slides_api.create_special_slide_shape(self.file_name, self.slide_index, 'notesSlide', dto, None, None, self.password, self.folder_name)
        self.assertEqual(dto.text, shape.text)
        shapes = BaseTest.slides_api.get_special_slide_shapes(self.file_name, self.slide_index, 'notesSlide', self.password, self.folder_name)
        self.assertEqual(shape_count + 1, len(shapes.shapes_links))

        dto.Text = "updated shape"
        shape = BaseTest.slides_api.update_special_slide_shape(self.file_name, self.slide_index, 'notesSlide', shape_count + 1, dto, self.password, self.folder_name)
        self.assertEqual(dto.text, shape.text)
        shapes = BaseTest.slides_api.get_special_slide_shapes(self.file_name, self.slide_index, 'notesSlide', self.password, self.folder_name)
        self.assertEqual(shape_count + 1, len(shapes.shapes_links))

        BaseTest.slides_api.delete_special_slide_shape(self.file_name, self.slide_index, 'notesSlide', shape_count + 1, self.password, self.folder_name)
        shapes = BaseTest.slides_api.get_special_slide_shapes(self.file_name, self.slide_index, 'notesSlide', self.password, self.folder_name)
        self.assertEqual(shape_count, len(shapes.shapes_links))

    def test_notes_slide_paragraphs(self):
        shape_index = 2
        paragraph_count = 1
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(self.file_name, self.slide_index, 'notesSlide', shape_index, self.password, self.folder_name)
        self.assertEqual(paragraph_count, len(paragraphs.paragraph_links))

        portion = Portion()
        portion.text = "New Paragraph"
        dto = Paragraph()
        dto.alignment = "Right"
        dto.portion_list = [ portion ]
        paragraph = BaseTest.slides_api.create_special_slide_paragraph(self.file_name, self.slide_index, 'notesSlide', shape_index, dto, None, self.password, self.folder_name)
        self.assertEqual(dto.alignment, paragraph.alignment)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(self.file_name, self.slide_index, 'notesSlide', shape_index, self.password, self.folder_name)
        self.assertEqual(paragraph_count + 1, len(paragraphs.paragraph_links))

        dto = Paragraph()
        dto.alignment = "Center"
        paragraph = BaseTest.slides_api.update_special_slide_paragraph(self.file_name, self.slide_index, 'notesSlide', shape_index, paragraph_count + 1, dto, self.password, self.folder_name)
        self.assertEqual(dto.alignment, paragraph.alignment)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(self.file_name, self.slide_index, 'notesSlide', shape_index, self.password, self.folder_name)
        self.assertEqual(paragraph_count + 1, len(paragraphs.paragraph_links))

        BaseTest.slides_api.delete_special_slide_paragraph(self.file_name, self.slide_index, 'notesSlide', shape_index, paragraph_count + 1, self.password, self.folder_name)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(self.file_name, self.slide_index, 'notesSlide', shape_index, self.password, self.folder_name)
        self.assertEqual(paragraph_count, len(paragraphs.paragraph_links))

    def test_notes_slide_portions(self):
        shape_index = 2
        paragraph_index = 1
        portion_count = 1
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        portions = BaseTest.slides_api.get_special_slide_portions(self.file_name, self.slide_index, 'notesSlide', shape_index, paragraph_index, self.password, self.folder_name)
        self.assertEqual(portion_count, len(portions.items))

        dto = Portion()
        dto.text = "New portion"
        dto.font_bold = "True"
        portion = BaseTest.slides_api.create_special_slide_portion(self.file_name, self.slide_index, 'notesSlide', shape_index, paragraph_index, dto, None, self.password, self.folder_name)
        self.assertEqual(dto.font_bold, portion.font_bold)
        self.assertEqual(dto.text, portion.text)
        portions = BaseTest.slides_api.get_special_slide_portions(self.file_name, self.slide_index, 'notesSlide', shape_index, paragraph_index, self.password, self.folder_name)
        self.assertEqual(portion_count + 1, len(portions.items))

        dto2 = Portion()
        dto2.text = "Updated portion"
        dto2.font_height = 22
        portion = BaseTest.slides_api.update_special_slide_portion(self.file_name, self.slide_index, 'notesSlide', shape_index, paragraph_index, portion_count + 1, dto2, self.password, self.folder_name)
        self.assertEqual(dto.font_bold, portion.font_bold)
        self.assertEqual(dto2.font_height, portion.font_height)
        self.assertEqual(dto2.text, portion.text)
        portions = BaseTest.slides_api.get_special_slide_portions(self.file_name, self.slide_index, 'notesSlide', shape_index, paragraph_index, self.password, self.folder_name)
        self.assertEqual(portion_count + 1, len(portions.items))

        BaseTest.slides_api.delete_special_slide_portion(self.file_name, self.slide_index, 'notesSlide', shape_index, paragraph_index, portion_count + 1, self.password, self.folder_name)
        portions = BaseTest.slides_api.get_special_slide_portions(self.file_name, self.slide_index, 'notesSlide', shape_index, paragraph_index, self.password, self.folder_name)
        self.assertEqual(portion_count, len(portions.items))

    def test_create_notes_slide(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = NotesSlide()
        dto.text = self.notes_slide_text
        response = BaseTest.slides_api.create_notes_slide(self.file_name, self.slide_index, dto, self.password, self.folder_name)
        self.assertEqual(dto.text, response.text)

    def test_update_notes_slide(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = NotesSlide()
        dto.text = self.notes_slide_text
        response = BaseTest.slides_api.update_notes_slide(self.file_name, self.slide_index, dto, self.password, self.folder_name)
        self.assertEqual(dto.text, response.text)

    def test_delete_notes_slide(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_notes_slide(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertIsNone(response.notes_slide)