from __future__ import absolute_import

from asposeslidescloud import SlideAnimation, Effect, Portion, Paragraph, Shape
from test.base_test import BaseTest

class TestMasterSlide(BaseTest):
    def setUp(self):
        self.slide_index = 1
        self.shape_index = 2

    def tearDown(self):
        pass

    def test_master_slides(self):
        source_file = "TemplateCV.pptx"
        source_path = self.folder_name + "/" + source_file
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.copy_file(self.temp_folder_name + "/" + source_file, source_path)

        master_slides = BaseTest.slides_api.get_master_slides(self.file_name, self.password, self.folder_name)
        self.assertEqual(1, len(master_slides.slide_list))

        master_slide = BaseTest.slides_api.get_master_slide(self.file_name, 1, self.password, self.folder_name)
        self.assertEqual("Office Theme", master_slide.name)

        master_slide = BaseTest.slides_api.copy_master_slide(self.file_name, source_path, 1, None, None, None, self.password, self.folder_name)
        self.assertEqual("Digital portfolio", master_slide.name)

        master_slides = BaseTest.slides_api.get_master_slides(self.file_name, self.password, self.folder_name)
        self.assertEqual(2, len(master_slides.slide_list))

    def test_master_slide_shapes(self):
        shape_count = 6
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        shapes = BaseTest.slides_api.get_special_slide_shapes(self.file_name, self.slide_index, 'masterSlide', self.password, self.folder_name)
        self.assertEqual(shape_count, len(shapes.shapes_links))

        dto = Shape()
        dto.x = 100
        dto.y = 100
        dto.width = 500
        dto.height = 200
        dto.shape_type = "Rectangle"
        dto.text = "New shape"
        shape = BaseTest.slides_api.create_special_slide_shape(self.file_name, self.slide_index, 'masterSlide', dto, None, None, self.password, self.folder_name)
        self.assertEqual(dto.text, shape.text)
        shapes = BaseTest.slides_api.get_special_slide_shapes(self.file_name, self.slide_index, 'masterSlide', self.password, self.folder_name)
        self.assertEqual(shape_count + 1, len(shapes.shapes_links))

        dto.Text = "updated shape"
        shape = BaseTest.slides_api.update_special_slide_shape(self.file_name, self.slide_index, 'masterSlide', shape_count + 1, dto, self.password, self.folder_name)
        self.assertEqual(dto.text, shape.text)
        shapes = BaseTest.slides_api.get_special_slide_shapes(self.file_name, self.slide_index, 'masterSlide', self.password, self.folder_name)
        self.assertEqual(shape_count + 1, len(shapes.shapes_links))

        BaseTest.slides_api.delete_special_slide_shape(self.file_name, self.slide_index, 'masterSlide', shape_count + 1, self.password, self.folder_name)
        shapes = BaseTest.slides_api.get_special_slide_shapes(self.file_name, self.slide_index, 'masterSlide', self.password, self.folder_name)
        self.assertEqual(shape_count, len(shapes.shapes_links))

    def test_master_slide_paragraphs(self):
        paragraph_count = 5
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(self.file_name, self.slide_index, 'masterSlide', self.shape_index, self.password, self.folder_name)
        self.assertEqual(paragraph_count, len(paragraphs.paragraph_links))

        portion = Portion()
        portion.text = "New Paragraph"
        dto = Paragraph()
        dto.alignment = "Right"
        dto.portion_list = [ portion ]
        paragraph = BaseTest.slides_api.create_special_slide_paragraph(self.file_name, self.slide_index, 'masterSlide', self.shape_index, dto, None, self.password, self.folder_name)
        self.assertEqual(dto.alignment, paragraph.alignment)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(self.file_name, self.slide_index, 'masterSlide', self.shape_index, self.password, self.folder_name)
        self.assertEqual(paragraph_count + 1, len(paragraphs.paragraph_links))

        dto = Paragraph()
        dto.alignment = "Center"
        paragraph = BaseTest.slides_api.update_special_slide_paragraph(self.file_name, self.slide_index, 'masterSlide', self.shape_index, paragraph_count + 1, dto, self.password, self.folder_name)
        self.assertEqual(dto.alignment, paragraph.alignment)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(self.file_name, self.slide_index, 'masterSlide', self.shape_index, self.password, self.folder_name)
        self.assertEqual(paragraph_count + 1, len(paragraphs.paragraph_links))

        BaseTest.slides_api.delete_special_slide_paragraph(self.file_name, self.slide_index, 'masterSlide', self.shape_index, paragraph_count + 1, self.password, self.folder_name)
        paragraphs = BaseTest.slides_api.get_special_slide_paragraphs(self.file_name, self.slide_index, 'masterSlide', self.shape_index, self.password, self.folder_name)
        self.assertEqual(paragraph_count, len(paragraphs.paragraph_links))

    def test_master_slide_portions(self):
        paragraph_index = 3
        portion_count = 1
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        portions = BaseTest.slides_api.get_special_slide_portions(self.file_name, self.slide_index, 'masterSlide', self.shape_index, paragraph_index, self.password, self.folder_name)
        self.assertEqual(portion_count, len(portions.items))

        dto = Portion()
        dto.text = "New portion"
        dto.font_bold = "True"
        portion = BaseTest.slides_api.create_special_slide_portion(self.file_name, self.slide_index, 'masterSlide', self.shape_index, paragraph_index, dto, None, self.password, self.folder_name)
        self.assertEqual(dto.font_bold, portion.font_bold)
        self.assertEqual(dto.text, portion.text)
        portions = BaseTest.slides_api.get_special_slide_portions(self.file_name, self.slide_index, 'masterSlide', self.shape_index, paragraph_index, self.password, self.folder_name)
        self.assertEqual(portion_count + 1, len(portions.items))

        dto2 = Portion()
        dto2.text = "Updated portion"
        dto2.font_height = 22
        portion = BaseTest.slides_api.update_special_slide_portion(self.file_name, self.slide_index, 'masterSlide', self.shape_index, paragraph_index, portion_count + 1, dto2, self.password, self.folder_name)
        self.assertEqual(dto.font_bold, portion.font_bold)
        self.assertEqual(dto2.font_height, portion.font_height)
        self.assertEqual(dto2.text, portion.text)
        portions = BaseTest.slides_api.get_special_slide_portions(self.file_name, self.slide_index, 'masterSlide', self.shape_index, paragraph_index, self.password, self.folder_name)
        self.assertEqual(portion_count + 1, len(portions.items))

        BaseTest.slides_api.delete_special_slide_portion(self.file_name, self.slide_index, 'masterSlide', self.shape_index, paragraph_index, portion_count + 1, self.password, self.folder_name)
        portions = BaseTest.slides_api.get_special_slide_portions(self.file_name, self.slide_index, 'masterSlide', self.shape_index, paragraph_index, self.password, self.folder_name)
        self.assertEqual(portion_count, len(portions.items))

    def test_master_slide_animation(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        animation = BaseTest.slides_api.get_special_slide_animation(self.file_name, self.slide_index, 'masterSlide', None, None, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))

        effect1 = Effect()
        effect1.type = "Blink"
        effect1.shape_index = 2

        effect2 = Effect()
        effect2.type = "Appear"
        effect2.shape_index = 3

        dto = SlideAnimation()
        dto.main_sequence = [ effect1, effect2 ]
        animation = BaseTest.slides_api.set_special_slide_animation(self.file_name, self.slide_index, 'masterSlide', dto, self.password, self.folder_name)
        self.assertEqual(len(dto.main_sequence), len(animation.main_sequence))

        animation = BaseTest.slides_api.get_special_slide_animation(self.file_name, self.slide_index, 'masterSlide', 3, None, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))

        BaseTest.slides_api.delete_special_slide_animation_effect(self.file_name, self.slide_index, 'masterSlide', 2, self.password, self.folder_name)
        self.assertEqual(len(dto.main_sequence) - 1, len(animation.main_sequence))

        animation = BaseTest.slides_api.get_special_slide_animation(self.file_name, self.slide_index, 'masterSlide', 3, None, self.password, self.folder_name)
        self.assertEqual(0, len(animation.main_sequence))

        BaseTest.slides_api.delete_special_slide_animation(self.file_name, self.slide_index, 'masterSlide', self.password, self.folder_name)
        self.assertEqual(0, len(animation.main_sequence))

    def test_delete_unused_master_slides(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_unused_master_slides(self.file_name, True, self.password, self.folder_name)
        self.assertEqual(1, len(result.slide_list))

    def test_delete_unused_master_slides_online(self):
        with open(self.local_path, 'rb') as f:
            file = f.read()

        result = BaseTest.slides_api.delete_unused_master_slides_online(file, True, self.password)
        self.assertIsNotNone(result)
