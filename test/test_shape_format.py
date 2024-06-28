from __future__ import absolute_import

from asposeslidescloud import LightRig, Camera, Shape, ThreeDFormat, ShapeBevel, InnerShadowEffect, EffectFormat, \
    SolidFill, LineFormat
from test.base_test import BaseTest

class TestShapeFormat(BaseTest):
    def setUp(self):
        self.slideIndex = 1
        self.shapeIndex = 1

    def tearDown(self):
        pass

    def test_shape_format_line(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Shape()
        line_format = LineFormat()
        line_format.style = "ThickThin"
        line_format.width = 7
        line_format.dash_style = "Dash"
        dto.line_format = line_format
        shape = BaseTest.slides_api.update_shape(self.file_name, self.slideIndex, self.shapeIndex, dto, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, Shape))
        shape = BaseTest.slides_api.get_shape(self.file_name, self.slideIndex, self.shapeIndex, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, Shape))
        self.assertEqual(dto.line_format.width, shape.line_format.width)

    def test_shape_format_fill(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Shape()
        fill_format = SolidFill()
        fill_format.color = "#FFFFFF00"
        dto.fill_format = fill_format
        shape = BaseTest.slides_api.update_shape(self.file_name, self.slideIndex, self.shapeIndex, dto, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, Shape))
        shape = BaseTest.slides_api.get_shape(self.file_name, self.slideIndex, self.shapeIndex, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, Shape))
        self.assertTrue(isinstance(shape.fill_format, SolidFill))
        self.assertEqual(dto.fill_format.color, shape.fill_format.color)

    def test_shape_format_effect(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Shape()
        effect_format = EffectFormat()
        inner_shadow = InnerShadowEffect()
        inner_shadow.direction = 35
        inner_shadow.blur_radius = 30
        inner_shadow.distance = 40
        inner_shadow.shadow_color = "#FFFFFF00"
        effect_format.inner_shadow = inner_shadow
        dto.effect_format = effect_format
        shape = BaseTest.slides_api.update_shape(self.file_name, self.slideIndex, self.shapeIndex, dto, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, Shape))
        shape = BaseTest.slides_api.get_shape(self.file_name, self.slideIndex, self.shapeIndex, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, Shape))
        self.assertEqual(dto.effect_format.inner_shadow.direction, shape.effect_format.inner_shadow.direction)

    def test_shape_format_3d(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        dto = Shape()
        three_d_format = ThreeDFormat()
        three_d_format.depth = 4

        bevel_top = ShapeBevel()
        bevel_top.bevel_type = "Circle"
        bevel_top.height = 6
        bevel_top.width = 6
        three_d_format.bevel_top = bevel_top

        camera = Camera()
        camera.camera_type = "OrthographicFront"
        three_d_format.camera = camera

        light_rig = LightRig()
        light_rig.light_type = "ThreePt"
        light_rig.direction = "Top"
        three_d_format.light_rig = light_rig
        dto.three_d_format = three_d_format
        shape = BaseTest.slides_api.update_shape(self.file_name, self.slideIndex, self.shapeIndex, dto, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, Shape))
        shape = BaseTest.slides_api.get_shape(self.file_name, self.slideIndex, self.shapeIndex, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, Shape))
        self.assertEqual(dto.three_d_format.depth, shape.three_d_format.depth)