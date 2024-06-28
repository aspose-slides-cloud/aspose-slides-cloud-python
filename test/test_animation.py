from __future__ import absolute_import

from asposeslidescloud import SlideAnimation, Effect, InteractiveSequence
from test.base_test import BaseTest
import asposeslidescloud

class TestAnimation(BaseTest):
    def setUp(self):
        self.slide_index = 1

    def tearDown(self):
        pass

    def test__get_animation(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        animation = BaseTest.slides_api.get_animation(self.file_name, self.slide_index, None, None, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

        animation = BaseTest.slides_api.get_animation(self.file_name, self.slide_index, 3, None, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(0, len(animation.interactive_sequences))

        animation = BaseTest.slides_api.get_animation(self.file_name, self.slide_index, 3, 1, self.password, self.folder_name)
        self.assertEqual(0, len(animation.main_sequence))

    def test_set_animation(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        dto = SlideAnimation()

        effect1 = Effect()
        effect1.type = "Blink"
        effect1.shape_index = 2
        effect1.paragraph_index = 1

        effect2 = Effect()
        effect2.type = "Box"
        effect2.subtype = "In"
        effect2.preset_class_type = "Entrance"
        effect2.shape_index = 4
        dto.main_sequence = [ effect1, effect2 ]
        dto.interactive_sequences = []
        animation = BaseTest.slides_api.set_animation(self.file_name, self.slide_index, dto, self.password, self.folder_name)
        self.assertEqual(len(dto.main_sequence), len(animation.main_sequence))
        self.assertEqual(0, len(animation.interactive_sequences))

    def test_create_animation_effect(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Effect()
        dto.type = "Blast"
        dto.shape_index = 3
        animation = BaseTest.slides_api.create_animation_effect(self.file_name, self.slide_index, dto, self.password, self.folder_name)
        self.assertEqual(2, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_create_animation_interactive_sequence(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = InteractiveSequence()
        dto.trigger_shape_index = 2
        effect = Effect()
        effect.type = "Blast"
        effect.shape_index = 3
        dto.effects = [ effect ]
        animation = BaseTest.slides_api.create_animation_interactive_sequence(
            self.file_name, self.slide_index, dto, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(2, len(animation.interactive_sequences))

    def test_create_animation_interactive_sequence_effect(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Effect()
        dto.type = "Blast"
        dto.shape_index = 3
        animation = BaseTest.slides_api.create_animation_interactive_sequence_effect(
            self.file_name, self.slide_index, 1, dto, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_update_animation_effect(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Effect()
        dto.type = "Blast"
        dto.shape_index = 3
        animation = BaseTest.slides_api.update_animation_effect(
            self.file_name, self.slide_index, 1, dto, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_update_animation_interactive_sequence_effect(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Effect()
        dto.type = "Blast"
        dto.shape_index = 3
        animation = BaseTest.slides_api.update_animation_interactive_sequence_effect(
            self.file_name, self.slide_index, 1, 1, dto, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_delete_animation(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        animation = BaseTest.slides_api.delete_animation(self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(0, len(animation.main_sequence))
        self.assertEqual(0, len(animation.interactive_sequences))

    def test_delete_animation_main_sequence(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        animation = BaseTest.slides_api.delete_animation_main_sequence(
            self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(0, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_delete_animation_effect(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        animation = BaseTest.slides_api.delete_animation_effect(self.file_name, self.slide_index, 1, self.password, self.folder_name)
        self.assertEqual(0, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))

    def test_delete_animation_interactive_sequences(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        animation = BaseTest.slides_api.delete_animation_interactive_sequences(
            self.file_name, self.slide_index, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(0, len(animation.interactive_sequences))

    def test_delete_animation_interactive_sequence(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        animation = BaseTest.slides_api.delete_animation_interactive_sequence(
            self.file_name, self.slide_index, 1, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(0, len(animation.interactive_sequences))

    def test_delete_animation_interactive_sequence_effect(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        animation = BaseTest.slides_api.delete_animation_interactive_sequence_effect(
            self.file_name, self.slide_index, 1, 1, self.password, self.folder_name)
        self.assertEqual(1, len(animation.main_sequence))
        self.assertEqual(1, len(animation.interactive_sequences))