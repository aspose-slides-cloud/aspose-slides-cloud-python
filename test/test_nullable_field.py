from __future__ import absolute_import

from asposeslidescloud import Axis, Chart, Axes, OneValueChartDataPoint, OneValueSeries, ChartTitle, ChartCategory
from test.base_test import BaseTest

class TestNullableField(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nullable_properties(self):
        slide_index = 1
        shape_index = 5
        min1  = 44.3;
        min2 = 12;
        max1 = 104.3;
        max2 = 87;
        BaseTest.slides_api.copy_file(self.temp_path, self.path)

        test_dto = Chart()
        test_dto.chart_type = "Line"
        test_dto.width = 400
        test_dto.height = 300
        test_dto.has_title = True

        test_title = ChartTitle()
        test_title.text = "MyTitle"
        test_dto.title = test_title

        test_series = OneValueSeries()
        test_series.type = "ClusteredColumn"
        test_series.data_point_type = "OneValue"
        test_series.name = "Series1"
        test_point1 = OneValueChartDataPoint()
        test_point1.value = 40
        test_point2 = OneValueChartDataPoint()
        test_point2.value = 50
        test_series.data_points = [ test_point1, test_point2 ]
        test_dto.series = ([test_series])
        test_axes = Axes()
        test_axis = Axis()
        test_axis.is_automatic_min_value = False
        test_axis.min_value = min1
        test_axis.is_automatic_max_value = False
        test_axis.max_value = max1
        test_axes.horizontal_axis = test_axis
        test_dto.axes = test_axes
        result = BaseTest.slides_api.create_shape(self.file_name, slide_index, test_dto, None, None, self.password, self.folder_name)

        result = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape_index, self.password, self.folder_name)
        self.assertEqual(min1, result.axes.horizontal_axis.min_value)
        self.assertEqual(max1, result.axes.horizontal_axis.max_value)

        test_dto = Chart()
        test_axes = Axes()
        test_axis = Axis()
        test_axis.min_value = min2
        test_axes.horizontal_axis = test_axis
        test_dto.axes = test_axes
        result = BaseTest.slides_api.update_shape(self.file_name, slide_index, shape_index, test_dto, self.password, self.folder_name)

        result = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape_index, self.password, self.folder_name)
        self.assertEqual(min2, result.axes.horizontal_axis.min_value)
        self.assertEqual(max1, result.axes.horizontal_axis.max_value)

        test_axis = Axis()
        test_axis.max_value = max2
        test_axes.horizontal_axis = test_axis
        test_dto.axes = test_axes
        result = BaseTest.slides_api.update_shape(self.file_name, slide_index, shape_index, test_dto, self.password, self.folder_name)

        result = BaseTest.slides_api.get_shape(self.file_name, slide_index, shape_index, self.password, self.folder_name)
        self.assertEqual(min2, result.axes.horizontal_axis.min_value)
        self.assertEqual(max2, result.axes.horizontal_axis.max_value)