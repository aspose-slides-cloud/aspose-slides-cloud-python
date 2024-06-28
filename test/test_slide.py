from __future__ import absolute_import

from asposeslidescloud import SlideComment, SlideModernComment, SlideShowTransition, Slide, ResourceUri, SlideBackground, SolidFill, NoFill
from test.base_test import BaseTest

class TestSlide(BaseTest):
    def setUp(self):
        self.slide_index = 1

    def tearDown(self):
        pass

    def test_get_slides(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slides = BaseTest.slides_api.get_slides(self.file_name, self.password, self.folder_name)
        self.assertEqual(9, len(slides.slide_list))

    def test_get_slide(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide = BaseTest.slides_api.get_slide(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertIsNotNone(slide)

    def test_create_slide(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        layout_slide_path = "layoutSlides/3"
        slides = BaseTest.slides_api.create_slide(self.file_name, layout_slide_path, 1, self.password, self.folder_name)
        self.assertEqual(10, len(slides.slide_list))
        slides = BaseTest.slides_api.create_slide(self.file_name, None, None, self.password, self.folder_name)
        self.assertEqual(11, len(slides.slide_list))

    def test_copy_slide(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide_to_copy_index = 3
        slides = BaseTest.slides_api.copy_slide(
            self.file_name, slide_to_copy_index, None, None, None, None, self.password, self.folder_name)
        self.assertEqual(10, len(slides.slide_list))

    def test_copy_slide_from_source(self):
        source_file_name = "TemplateCV.pptx"
        source_path = self.folder_name + "/" + source_file_name
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.copy_file(self.temp_folder_name + "/" + source_file_name, source_path)
        slides = BaseTest.slides_api.copy_slide(
            self.file_name, self.slide_index, 1, source_path, None, None, self.password, self.folder_name)
        self.assertEqual(10, len(slides.slide_list))

    def test_move_slide(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slides = BaseTest.slides_api.move_slide(self.file_name, self.slide_index, 2, self.password, self.folder_name)
        self.assertEqual(9, len(slides.slide_list))

    def test_reorder_slides(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        old_positions = [1, 2, 3, 4, 5, 6]
        new_positions = [6, 5, 4, 3, 2, 1]
        slides = BaseTest.slides_api.reorder_slides(self.file_name, old_positions, new_positions, self.password, self.folder_name)
        self.assertEqual(9, len(slides.slide_list))

    def test_update_slide(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        layout_slide_path = "layoutSlides/3"
        dto = Slide()
        dto.layout_slide = ResourceUri()
        dto.layout_slide.href = layout_slide_path
        slide = BaseTest.slides_api.update_slide(self.file_name, self.slide_index, dto, self.password, self.folder_name)
        self.assertTrue(layout_slide_path in slide.layout_slide.href)

    def test_set_slide_transition(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Slide()
        dto.slide_show_transition = SlideShowTransition()
        dto.slide_show_transition.type = 'Circle'
        dto.slide_show_transition.speed = 'Medium'
        slide = BaseTest.slides_api.update_slide(self.file_name, self.slide_index, dto, self.password, self.folder_name)
        self.assertEqual(dto.slide_show_transition.type, slide.slide_show_transition.type)

    def test_delete_slides(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slides = BaseTest.slides_api.delete_slides(self.file_name, None, self.password, self.folder_name)
        self.assertEqual(1, len(slides.slide_list))

    def test_delete_slide_indexes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slides = BaseTest.slides_api.delete_slides(self.file_name, [1, 3, 5], self.password, self.folder_name)
        self.assertEqual(6, len(slides.slide_list))

    def test_delete_slide(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slides = BaseTest.slides_api.delete_slide(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(8, len(slides.slide_list))

    def test_get_background(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide_index = 5
        response = BaseTest.slides_api.get_background(self.file_name, slide_index, self.password, self.folder_name)
        self.assertTrue(isinstance(response.fill_format, SolidFill))

    def test_set_background(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = SlideBackground()
        fill_format = SolidFill()
        fill_format.color = "#FFF5FF8A"
        dto.fill_format = fill_format
        response = BaseTest.slides_api.set_background(self.file_name, self.slide_index, dto, self.password, self.folder_name)
        self.assertTrue(isinstance(response.fill_format, SolidFill))
        self.assertEqual(fill_format.color, response.fill_format.color)

    def test_set_background_color(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        color = "#FFF5FF8A"
        response = BaseTest.slides_api.set_background_color(self.file_name, self.slide_index, color, self.password, self.folder_name)
        self.assertTrue(isinstance(response.fill_format, SolidFill))
        self.assertEqual(color, response.fill_format.color)

    def test_delete_background(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide_index = 5
        response = BaseTest.slides_api.delete_background(self.file_name, slide_index, self.password, self.folder_name)
        self.assertTrue(isinstance(response.fill_format, NoFill))