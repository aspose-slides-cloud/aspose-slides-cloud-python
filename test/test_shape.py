from __future__ import absolute_import

import base64
import os

from asposeslidescloud import LineToPathSegment, MoveToPathSegment, GeometryPath, ClosePathSegment, GeometryPaths, \
    Connector, ResourceUri, GroupShape, Table, TableColumn, TableCell, TableRow, Chart, SmartArt, SmartArtNode, \
    OleObjectFrame, VideoFrame, AudioFrame, PictureFrame, GraphicalObject, Shape, ZoomFrame, \
    SectionZoomFrame, Portion, SolidFill, PictureFill, GradientFill, GradientFillStop
from asposeslidescloud.rest import ApiException
from test.base_test import BaseTest

class TestShape(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_shapes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        shapes = BaseTest.slides_api.get_shapes(self.file_name, 3, self.password, self.folder_name)
        self.assertEqual(2, len(shapes.shapes_links))

    def test_get_shapes_by_type(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        shapes = BaseTest.slides_api.get_shapes(self.file_name, 3, self.password, self.folder_name, None, "Chart")
        self.assertEqual(2, len(shapes.shapes_links))

    def test_get_sub_shapes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        shapes = BaseTest.slides_api.get_shapes(self.file_name, 1, self.password, self.folder_name, None, None, "4")
        self.assertEqual(2, len(shapes.shapes_links))

    def test_get_shape(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        shape = BaseTest.slides_api.get_shape(self.file_name, 3, 1, self.password, self.folder_name)
        self.assertEqual("Chart", shape.type)

    def test_get_sub_shape(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        shape = BaseTest.slides_api.get_shape(self.file_name, 1, 4, self.password, self.folder_name, None, "1")
        self.assertEqual("Shape", shape.type)

    def test_shape_load_save(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = BaseTest.slides_api.get_shape(self.file_name, 3, 1, self.password, self.folder_name)
        shape = BaseTest.slides_api.update_shape(self.file_name, 3, 1, dto, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, Chart))

    def test_shape_add(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Shape()
        dto.shape_type = 'Callout1'
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(result, Shape))

    def test_shape_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Shape()
        try:
            BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
            self.fail("Shape with undefinined type should not have been created")
        except ApiException as ex:
            self.assertEqual(400, ex.status)

    def test_graphical_object_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = GraphicalObject()
        try:
            BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
            self.fail("GraphicalObject should not have been created")
        except ApiException as ex:
            self.assertEqual(400, ex.status)

    def test_picture_frame_add(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = PictureFrame()
        fill = PictureFill()
        fill.base64_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXY5g+ffp/AAZTAsWGL27gAAAAAElFTkSuQmCC"
        dto.picture_fill_format = fill
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(result, PictureFrame))

    def test_picture_frame_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = PictureFrame()
        try:
            BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
            self.fail("PictureFrame with undefinined data should not have been created")
        except ApiException as ex:
            self.assertEqual(400, ex.status)

    def test_audio_frame_add(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = AudioFrame()
        dto.base64_data = "bXAzc2FtcGxl"
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(result, AudioFrame))

    def test_audio_frame_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = AudioFrame()
        try:
            BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
            self.fail("AudioFrame with undefinined data should not have been created")
        except ApiException as ex:
            self.assertEqual(400, ex.status)

    def test_video_frame_add(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = VideoFrame()
        dto.base64_data = "bXAzc2FtcGxl"
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(result, VideoFrame))

    def test_video_frame_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = VideoFrame()
        try:
            BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
            self.fail("VideoFrame with undefinined data should not have been created")
        except ApiException as ex:
            self.assertEqual(400, ex.status)

    def test_ole_object_frame_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = OleObjectFrame()
        try:
            BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
            self.fail("OleObjectFrame should not have been created")
        except ApiException as ex:
            self.assertEqual(400, ex.status)

    def test_smart_art_add(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = SmartArt()
        dto.x = 0
        dto.y = 0
        dto.width = 300
        dto.height = 200
        dto.layout = 'BasicProcess'
        dto.quick_style = 'SimpleFill'
        dto.color_style = 'ColoredFillAccent1'
        node1 = SmartArtNode()
        node1.text = "First"
        node1.org_chart_layout = 'Initial'
        sub_node1 = SmartArtNode()
        sub_node1.text = "SubFirst"
        sub_node1.org_chart_layout = 'Initial'
        node1.nodes = [ sub_node1 ]
        node2 = SmartArtNode()
        node2.text = "Second"
        node2.org_chart_layout = 'Initial'
        dto.nodes = [ node1, node2 ]
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(result, SmartArt))

    def test_smart_art_text_formatting(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        portion = Portion()
        portion.text = "New text"
        portion.font_height = 24
        portion.font_bold = "True"
        portion.spacing = 3
        fill_format = SolidFill()
        fill_format.color = "#FFFFFF00"
        portion.fill_format = fill_format

        response = BaseTest.slides_api.update_portion(self.file_name, 7, 1, 1, 1, portion, self.password, self.folder_name, None, "1/nodes/2")
        self.assertIsNotNone(response)
        self.assertEqual(response.text, portion.text)
        self.assertEqual(response.font_height, portion.font_height)
        self.assertEqual(response.font_bold, portion.font_bold)
        self.assertEqual(response.spacing, portion.spacing)
        self.assertEqual(response.fill_format.color, portion.fill_format.color)



    def test_smart_art_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = SmartArt()
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(result, SmartArt))

    def test_chart_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Chart()
        try:
            BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
            self.fail("Chart with undefined series should not have been created")
        except ApiException as ex:
            self.assertEqual(500, ex.status)

    def test_table_add(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Table()
        dto.x = 30
        dto.y = 20
        dto.style = 'MediumStyle2Accent1'
        row1 = TableRow()
        cell11 = TableCell()
        cell11.text = "0.1"
        cell12 = TableCell()
        cell12.text = "0.2"
        cell13 = TableCell()
        cell13.text = "0.3"
        cell14 = TableCell()
        cell14.text = "0.4"
        row1.cells = [ cell11, cell12, cell13, cell14 ]
        row2 = TableRow()
        cell21 = TableCell()
        cell21.text = "1"
        cell22 = TableCell()
        cell22.text = "2-3"
        cell22.col_span = 2
        cell22.row_span = 2
        cell24 = TableCell()
        cell24.text = "4"
        row2.cells = [ cell21, cell22, cell24 ]
        row3 = TableRow()
        cell31 = TableCell()
        cell31.text = "first"
        cell32 = TableCell()
        cell32.text = "last"
        row3.cells = [ cell31, cell32 ]
        row4 = TableRow()
        cell41 = TableCell()
        cell41.text = "3.1"
        cell42 = TableCell()
        cell42.text = "3.2"
        cell43 = TableCell()
        cell43.text = "3.3"
        cell44 = TableCell()
        cell44.text = "3.4"
        row4.cells = [ cell41, cell42, cell43, cell44 ]
        row5 = TableRow()
        cell51 = TableCell()
        cell51.text = "4.1"
        cell52 = TableCell()
        cell52.text = "4.2"
        cell53 = TableCell()
        cell53.text = "4.3"
        cell54 = TableCell()
        cell54.text = "4.4"
        row5.cells = [ cell51, cell52, cell53, cell54 ]
        dto.rows = [ row1, row2, row3, row4, row5 ]
        column1 = TableColumn()
        column1.width = 100
        column2 = TableColumn()
        column2.width = 100
        column3 = TableColumn()
        column3.width = 100
        column4 = TableColumn()
        column4.width = 100
        dto.columns = [ column1, column2, column3, column4 ]
        dto.first_row = True
        dto.horizontal_banding = True
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(result, Table))

    def test_table_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Table()
        try:
            BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
            self.fail("Table with undefinined cell data should not have been created")
        except ApiException as ex:
            self.assertEqual(400, ex.status)

    def test_group_shape_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = GroupShape()
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(result, GroupShape))

    def test_connector_add(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Connector()
        dto.shape_type = 'BentConnector3'
        start = ResourceUri()
        start.href = "https://api.aspose.cloud/v3.0/slides/myPresentation.pptx/slides/1/shapes/1"
        dto.start_shape_connected_to = start
        end = ResourceUri()
        end.href = "https://api.aspose.cloud/v3.0/slides/myPresentation.pptx/slides/1/shapes/2"
        dto.end_shape_connected_to = end
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(result, Connector))

    def test_connector_empty(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Connector()
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(result, Connector))

    def test_create_sub_shape(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Shape()
        dto.shape_type = 'Rectangle'
        dto.x = 200
        dto.y = 200
        dto.width = 50
        dto.height = 50
        result = BaseTest.slides_api.create_shape(self.file_name, 1, dto, None, None, self.password, self.folder_name, None, "4")
        self.assertTrue(isinstance(result, Shape))

    def test_update_shape(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Shape()
        dto.width = 200
        dto.height = 200
        fill_format = SolidFill()
        fill_format.color = "#FFF5FF8A"
        dto.fill_format = fill_format
        result = BaseTest.slides_api.update_shape(self.file_name, 1, 3, dto, self.password, self.folder_name)
        self.assertTrue(isinstance(result, Shape))
        self.assertEqual(dto.width, result.width)
        self.assertEqual(dto.height, result.height)
        self.assertTrue(isinstance(result.fill_format, SolidFill))

    def test_update_sub_shape(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Shape()
        dto.width = 200
        dto.height = 200
        fill_format = GradientFill()
        fill_format.shape = 'Linear'
        fill_format.direction = 'FromCorner1'
        stop1 = GradientFillStop()
        stop1.color = "#FFF5FF8A"
        stop1.position = 0
        stop2 = GradientFillStop()
        stop2.color = "#FFF5FF8A"
        stop2.position = 1
        fill_format.stops = [ stop1, stop2 ]
        dto.fill_format = fill_format
        result = BaseTest.slides_api.update_shape(self.file_name, 1, 4, dto, self.password, self.folder_name, None, "1")
        self.assertTrue(isinstance(result, Shape))
        self.assertEqual(dto.width, result.width)
        self.assertEqual(dto.height, result.height)
        self.assertTrue(isinstance(result.fill_format, GradientFill))

    def test_delete_shapes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_shapes(self.file_name, 1, None, self.password, self.folder_name)
        self.assertEqual(0, len(result.shapes_links))

    def test_delete_shapes_indexes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_shapes(self.file_name, 1, [2], self.password, self.folder_name)
        self.assertEqual(3, len(result.shapes_links))

    def test_delete_sub_shapes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_shapes(self.file_name, 1, None, self.password, self.folder_name, None, "4")
        self.assertEqual(0, len(result.shapes_links))

    def test_delete_sub_shapes_indexes(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_shapes(self.file_name, 1, [2], self.password, self.folder_name, None, "4")
        self.assertEqual(1, len(result.shapes_links))

    def test_delete_shape(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_shape(self.file_name, 1, 4, self.password, self.folder_name)
        self.assertEqual(3, len(result.shapes_links))

    def test_delete_sub_shape(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_shape(self.file_name, 1, 4, self.password, self.folder_name, None, "1")
        self.assertEqual(1, len(result.shapes_links))

    def test_shapes_align(self):
        slide_index = 3
        shape1_index = 1
        shape2_index = 2
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        shape11 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape1_index, self.password, self.folder_name)
        shape12 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape2_index, self.password, self.folder_name)
        self.assertNotEqual(shape11.x, shape12.x)
        self.assertNotEqual(shape11.y, shape12.y)
        BaseTest.slides_api.align_shapes(self.file_name, slide_index, "AlignTop", None, None, self.password, self.folder_name)
        shape21 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape1_index, self.password, self.folder_name)
        shape22 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape2_index, self.password, self.folder_name)
        self.assertNotEqual(shape21.x, shape22.x)
        self.assertLess(abs(shape21.y - shape22.y), 1)
        BaseTest.slides_api.align_shapes(self.file_name, slide_index, "AlignLeft", True, [1, 2], self.password, self.folder_name)
        shape31 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape1_index, self.password, self.folder_name)
        shape32 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape2_index, self.password, self.folder_name)
        self.assertLess(abs(shape31.x - shape32.x), 1)
        self.assertLess(abs(shape31.x), 1)
        self.assertLess(abs(shape31.y - shape32.y), 1)

    def test_shapes_align_group(self):
        slide_index = 1
        shape_index = 4
        sub_shape1 = 1
        sub_shape2 = 2
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        shape11 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape_index, self.password, self.folder_name, None, sub_shape1)
        shape12 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape_index, self.password, self.folder_name, None, sub_shape2)
        self.assertNotEqual(shape11.x, shape12.x)
        self.assertNotEqual(shape11.y, shape12.y)
        BaseTest.slides_api.align_shapes(self.file_name, slide_index, "AlignTop", None, None, self.password, self.folder_name, None, "4")
        shape21 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape_index, self.password, self.folder_name, None, sub_shape1)
        shape22 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape_index, self.password, self.folder_name, None, sub_shape2)
        self.assertNotEqual(shape21.x, shape22.x)
        self.assertLess(abs(shape21.y - shape22.y), 1)
        BaseTest.slides_api.align_shapes(self.file_name, slide_index, "AlignLeft", True, [1, 2], self.password, self.folder_name, None, "4")
        shape31 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape_index, self.password, self.folder_name, None, sub_shape1)
        shape32 = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape_index, self.password, self.folder_name, None, sub_shape2)
        self.assertLess(abs(shape31.x - shape32.x), 1)
        self.assertLess(abs(shape31.x), 1)
        self.assertLess(abs(shape31.y - shape32.y), 1)

    def test_shape_geometry_get(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        paths = BaseTest.slides_api.get_shape_geometry_path(self.file_name, 4, 2, self.password, self.folder_name)
        self.assertIsNotNone(paths.paths)
        self.assertEqual(1, len(paths.paths))

    def test_shape_geometry_set(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = GeometryPaths()
        path = GeometryPath()
        start = MoveToPathSegment()
        start.x = 0
        start.y = 0
        line1 = LineToPathSegment()
        line1.x = 0
        line1.y = 200
        line2 = LineToPathSegment()
        line2.x = 200
        line2.y = 300
        line3 = LineToPathSegment()
        line3.x = 400
        line3.y = 200
        line4 = LineToPathSegment()
        line4.x = 400
        line4.y = 0
        end = ClosePathSegment()
        path.path_data = [ start, line1, line2, line3, line4, end ]
        dto.paths = [ path ]
        shape = BaseTest.slides_api.set_shape_geometry_path(self.file_name, 4, 1, dto, self.password, self.folder_name)
        self.assertIsNotNone(shape)

    def test_zoom_frame_add(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = ZoomFrame()
        dto.x = 20
        dto.y = 20
        dto.width = 200
        dto.height = 100
        dto.target_slide_index = 2
        shape = BaseTest.slides_api.create_shape(self.file_name, 3, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, ZoomFrame))
        self.assertEqual(dto.target_slide_index, shape.target_slide_index)

    def test_section_zoom_frame_add(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = SectionZoomFrame()
        dto.x = 20
        dto.y = 20
        dto.width = 200
        dto.height = 100
        dto.target_section_index = 2
        shape = BaseTest.slides_api.create_shape(self.file_name, 3, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(shape,SectionZoomFrame))
        self.assertEqual(dto.target_section_index, shape.target_section_index)

    def test_ole_object_frame_add_by_link(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = OleObjectFrame()
        dto.x = 100
        dto.y = 100
        dto.width = 200
        dto.height = 200
        dto.link_path = "oleObject.xlsx"
        dto.object_prog_id = "Excel.Sheet.8"
        shape = BaseTest.slides_api.create_shape(self.file_name, 3, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, OleObjectFrame))
        self.assertEqual(shape.link_path, dto.link_path)

    def test_ole_object_frame_add_embedded(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        with open(self.test_data_path + "/oleObject.xlsx", 'rb') as f:
            document = f.read()
        dto = OleObjectFrame()
        dto.x = 100
        dto.y = 100
        dto.width = 200
        dto.height = 200
        dto.embedded_file_base64_data = base64.b64encode(document).decode('utf-8')
        dto.embedded_file_extension = "xlsx"
        shape = BaseTest.slides_api.create_shape(self.file_name, 3, dto, None, None, self.password, self.folder_name)
        self.assertTrue(isinstance(shape, OleObjectFrame))
        self.assertIsNotNone(shape.embedded_file_base64_data)

    def test_group_shape_add(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide_index = 5
        shapes = BaseTest.slides_api.get_shapes(self.file_name, slide_index, self.password, self.folder_name)
        self.assertEqual(0, len(shapes.shapes_links))

        dto = GroupShape()
        BaseTest.slides_api.create_shape(self.file_name, slide_index, dto, None, None, self.password, self.folder_name)
        shape1 = Shape()
        shape1.shape_type = "Rectangle"
        shape1.x = 50
        shape1.y = 400
        shape1.width = 50
        shape1.height = 50

        shape2 = Shape()
        shape2.shape_type = "Ellipse"
        shape2.x = 150
        shape2.y = 400
        shape2.width = 50
        shape2.height = 50

        shape3 = Shape()
        shape3.shape_type = "Triangle"
        shape3.x = 250
        shape3.y = 400
        shape3.width = 50
        shape3.height = 50

        BaseTest.slides_api.create_shape(self.file_name, slide_index, shape1, None, None, self.password, self.folder_name, None, "1")
        BaseTest.slides_api.create_shape(self.file_name, slide_index, shape2, None, None, self.password, self.folder_name, None, "1")
        BaseTest.slides_api.create_shape(self.file_name, slide_index, shape3, None, None, self.password, self.folder_name, None, "1")

        shapes = BaseTest.slides_api.get_shapes(self.file_name, slide_index, self.password, self.folder_name)
        self.assertEqual(1, len(shapes.shapes_links))
        shapes = BaseTest.slides_api.get_shapes(self.file_name, slide_index, self.password, self.folder_name, None, None, "1")
        self.assertEqual(3, len(shapes.shapes_links))

    def test_import_shapes_from_svg(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        with open(self.test_data_path + "/" + "shapes.svg", 'rb') as f:
            source = f.read()
        response = BaseTest.slides_api.import_shapes_from_svg(self.file_name, 5, source, 50, 50, 300, 300, [1, 3, 5], False, self.password, self.folder_name)
        self.assertEqual(3, len(response.shapes_links))

    def test_create_smart_art_node(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        new_node_text = "New root node"
        response = BaseTest.slides_api.create_smart_art_node(self.file_name, 7, 1, "", new_node_text, "", self.password, self.folder_name)
        self.assertEqual(2, len(response.nodes))
        self.assertEqual(new_node_text, response.nodes[1].text)

    def test_create_smart_art_sub_node(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        new_sub_node_text = "New sub-node"
        response = BaseTest.slides_api.create_smart_art_node(self.file_name, 7, 1, "1", new_sub_node_text, 1, self.password, self.folder_name)
        self.assertEqual(5, len(response.nodes[0].nodes))
        self.assertEqual(new_sub_node_text, response.nodes[0].nodes[0].text)

    def test_create_smart_art_sub_sub_node(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        new_sub_node_text = "New sub-sub-node"
        response = BaseTest.slides_api.create_smart_art_node(self.file_name, 7, 1, "1/nodes/1", new_sub_node_text, "", self.password, self.folder_name)
        self.assertEqual(1, len(response.nodes[0].nodes[0].nodes))
        self.assertEqual(new_sub_node_text, response.nodes[0].nodes[0].nodes[0].text)

    def test_delete_smart_art_node(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_smart_art_node(self.file_name, 7, 2, 1, "", self.password, self.folder_name)
        self.assertEqual(2, len(response.nodes))

    def test_delete_smart_art_sub_node(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.delete_smart_art_node(self.file_name, 7, 1, 1, "2", self.password, self.folder_name)
        self.assertEqual(3, len(response.nodes[0].nodes))

    def test_download_shape_from_dto(self):
        dto = Shape()
        dto.width = 400
        dto.height = 200
        dto.shape_type = "Rectangle"
        dto.text = "Shape text"

        result = BaseTest.slides_api.download_shape_from_dto("png", dto)