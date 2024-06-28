from __future__ import absolute_import

from asposeslidescloud import OneValueSeries, Chart, OneValueChartDataPoint, ChartCategory, Axis, ChartLinesFormat, \
    LineFormat, NoFill, SolidFill, GradientFill, GradientFillStop, Axes, Legend, ChartWall, EffectFormat, BlurEffect, \
    Workbook, Literals
from asposeslidescloud.rest import ApiException
from test.base_test import BaseTest

class TestChart(BaseTest):
    def setUp(self):
        self.slide_index = 3
        self.shape_index = 1

    def tearDown(self):
        pass

    def test_get_chart(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = BaseTest.slides_api.get_shape(self.file_name, self.slide_index, self.shape_index, self.password, self.folder_name)
        self.assertEqual(3, len(chart.series))
        self.assertEqual(4, len(chart.categories))

    def test_create_chart_auto_data_source(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = Chart()
        chart.chart_type = 'ClusteredColumn'
        chart.width = 400
        chart.height = 300
        series1 = OneValueSeries()
        series1.name = "Series1"
        point11 = OneValueChartDataPoint()
        point11.value = 40
        point12 = OneValueChartDataPoint()
        point12.value = 50
        point13 = OneValueChartDataPoint()
        point13.value = 70
        series1.data_points = [point11, point12, point13]
        series2 = OneValueSeries()
        series2.name = "Series2"
        point21 = OneValueChartDataPoint()
        point21.value = 55
        point22 = OneValueChartDataPoint()
        point22.value = 35
        point23 = OneValueChartDataPoint()
        point23.value = 90
        series2.data_points = [point21, point22, point23]
        chart.series = [series1, series2]
        category1 = ChartCategory()
        category1.value = "Category1"
        category2 = ChartCategory()
        category2.value = "Category2"
        category3 = ChartCategory()
        category3.value = "Category3"
        chart.categories = [category1, category2, category3]
        result = BaseTest.slides_api.create_shape(self.file_name, self.slide_index, chart, None, None, self.password, self.folder_name)
        self.assertEqual(2, len(result.series))
        self.assertEqual(3, len(result.categories))

    def test_create_chart_workbook(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = Chart()
        chart.chart_type = 'ClusteredColumn'
        chart.width = 400
        chart.height = 300

        categories_data_source = Workbook()
        categories_data_source.worksheet_index = 1
        categories_data_source.row_index = 2
        categories_data_source.column_index = 1
        chart.data_source_for_categories = categories_data_source

        series1 = OneValueSeries()
        series1_name_data_source = Workbook()
        series1_name_data_source.worksheet_index = 1
        series1_name_data_source.column_index = 2
        series1_name_data_source.row_index = 1
        series1.data_source_for_series_name = series1_name_data_source
        series1.name = "Series1"

        series1_values_data_source = Workbook()
        series1_values_data_source.worksheet_index = 1
        series1_values_data_source.column_index = 2
        series1_values_data_source.row_index = 2
        series1.data_source_for_values = series1_values_data_source
        point11 = OneValueChartDataPoint()
        point11.value = 40
        point12 = OneValueChartDataPoint()
        point12.value = 50
        point13 = OneValueChartDataPoint()
        point13.value = 70
        series1.data_points = [point11, point12, point13]

        series2 = OneValueSeries()
        series2_name_data_source = Workbook()
        series2_name_data_source.worksheet_index = 1
        series2_name_data_source.column_index = 3
        series2_name_data_source.row_index = 1
        series2.data_source_for_series_name = series2_name_data_source
        series2.name = "Series2"

        series2_values_data_source = Workbook()
        series2_values_data_source.worksheet_index = 1
        series2_values_data_source.column_index = 3
        series2_values_data_source.row_index = 2
        series2.data_source_for_values = series2_values_data_source
        point21 = OneValueChartDataPoint()
        point21.value = 55
        point22 = OneValueChartDataPoint()
        point22.value = 35
        point23 = OneValueChartDataPoint()
        point23.value = 90
        series2.data_points = [point21, point22, point23]

        chart.series = [series1, series2]
        category1 = ChartCategory()
        category1.value = "Category1"
        category2 = ChartCategory()
        category2.value = "Category2"
        category3 = ChartCategory()
        category3.value = "Category3"
        chart.categories = [category1, category2, category3]
        result = BaseTest.slides_api.create_shape(self.file_name, self.slide_index, chart, None, None, self.password, self.folder_name)
        self.assertEqual(2, len(result.series))
        self.assertEqual(3, len(result.categories))

    def test_create_chart_literals(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = Chart()
        chart.chart_type = 'ClusteredColumn'
        chart.width = 400
        chart.height = 300

        chart.data_source_for_categories = Literals()

        series1 = OneValueSeries()
        series1.data_source_for_series_name = Literals()
        series1.name = "Series1"

        series1.data_source_for_values = Literals()
        point11 = OneValueChartDataPoint()
        point11.value = 40
        point12 = OneValueChartDataPoint()
        point12.value = 50
        point13 = OneValueChartDataPoint()
        point13.value = 70
        series1.data_points = [point11, point12, point13]

        series2 = OneValueSeries()
        series2.data_source_for_series_name = Literals()
        series2.name = "Series2"

        series2.data_source_for_values = Literals()
        point21 = OneValueChartDataPoint()
        point21.value = 55
        point22 = OneValueChartDataPoint()
        point22.value = 35
        point23 = OneValueChartDataPoint()
        point23.value = 90
        series2.data_points = [point21, point22, point23]

        chart.series = [series1, series2]
        category1 = ChartCategory()
        category1.value = "Category1"
        category2 = ChartCategory()
        category2.value = "Category2"
        category3 = ChartCategory()
        category3.value = "Category3"
        chart.categories = [category1, category2, category3]
        result = BaseTest.slides_api.create_shape(self.file_name, self.slide_index, chart, None, None, self.password, self.folder_name)
        self.assertEqual(2, len(result.series))
        self.assertEqual(3, len(result.categories))

    def test_update_chart(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = Chart()
        chart.chart_type = 'ClusteredColumn'
        chart.width = 400
        chart.height = 300
        series1 = OneValueSeries()
        series1.name = "Series1"
        point11 = OneValueChartDataPoint()
        point11.value = 40
        point12 = OneValueChartDataPoint()
        point12.value = 50
        point13 = OneValueChartDataPoint()
        point13.value = 70
        series1.data_points = [point11, point12, point13]
        series2 = OneValueSeries()
        series2.name = "Series2"
        point21 = OneValueChartDataPoint()
        point21.value = 55
        point22 = OneValueChartDataPoint()
        point22.value = 35
        point23 = OneValueChartDataPoint()
        point23.value = 90
        series2.data_points = [point21, point22, point23]
        chart.series = [series1, series2]
        category1 = ChartCategory()
        category1.value = "Category1"
        category2 = ChartCategory()
        category2.value = "Category2"
        category3 = ChartCategory()
        category3.value = "Category3"
        chart.categories = [category1, category2, category3]
        result = BaseTest.slides_api.update_shape(
            self.file_name, self.slide_index, self.shape_index, chart, self.password, self.folder_name)
        self.assertEqual(2, len(result.series))
        self.assertEqual(3, len(result.categories))

    def test_create_chart_series(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        series = OneValueSeries()
        series.name = "Series3"
        point1 = OneValueChartDataPoint()
        point1.value = 40
        point2 = OneValueChartDataPoint()
        point2.value = 50
        point3 = OneValueChartDataPoint()
        point3.value = 14
        point4 = OneValueChartDataPoint()
        point4.value = 70
        series.data_points = [point1, point2, point3, point4]
        result = BaseTest.slides_api.create_chart_series(
            self.file_name, self.slide_index, self.shape_index, series, self.password, self.folder_name)
        self.assertEqual(4, len(result.series))
        self.assertEqual(4, len(result.categories))

    def test_update_chart_series(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        series = OneValueSeries()
        series.name = "Series3"
        point1 = OneValueChartDataPoint()
        point1.value = 40
        point2 = OneValueChartDataPoint()
        point2.value = 50
        point3 = OneValueChartDataPoint()
        point3.value = 14
        point4 = OneValueChartDataPoint()
        point4.value = 70
        series.data_points = [point1, point2, point3, point4]
        result = BaseTest.slides_api.update_chart_series(
            self.file_name, self.slide_index, self.shape_index, 2, series, self.password, self.folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(4, len(result.categories))

    def test_delete_chart_series(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_chart_series(
            self.file_name, self.slide_index, self.shape_index, 2, self.password, self.folder_name)
        self.assertEqual(2, len(result.series))
        self.assertEqual(4, len(result.categories))

    def test_create_chart_category(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        category = ChartCategory()
        category.value = "NewCategory"
        point1 = OneValueChartDataPoint()
        point1.value = 40
        point2 = OneValueChartDataPoint()
        point2.value = 50
        point3 = OneValueChartDataPoint()
        point3.value = 14
        category.data_points = [point1, point2, point3]
        result = BaseTest.slides_api.create_chart_category(
            self.file_name, self.slide_index, self.shape_index, category, self.password, self.folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(5, len(result.categories))
        self.assertEqual(5, len(result.series[0].data_points))
        self.assertEqual(category.data_points[0].value, result.series[0].data_points[4].value)

    def test_update_chart_category(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        category = ChartCategory()
        category.value = "NewCategory"
        point1 = OneValueChartDataPoint()
        point1.value = 40
        point2 = OneValueChartDataPoint()
        point2.value = 50
        point3 = OneValueChartDataPoint()
        point3.value = 14
        category.data_points = [point1, point2, point3]
        result = BaseTest.slides_api.update_chart_category(
            self.file_name, self.slide_index, self.shape_index, 2, category, self.password, self.folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(4, len(result.categories))
        self.assertEqual(4, len(result.series[0].data_points))
        self.assertEqual(category.data_points[0].value, result.series[0].data_points[1].value)

    def test_delete_chart_category(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_chart_category(
            self.file_name, self.slide_index, self.shape_index, 2, self.password, self.folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(3, len(result.categories))
        self.assertEqual(3, len(result.series[0].data_points))

    def test_create_chart_data_point(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        point = OneValueChartDataPoint()
        point.value = 40
        try:
            BaseTest.slides_api.create_chart_data_point(
                self.file_name, self.slide_index, self.shape_index, 2, point, self.password, self.folder_name)
            self.fail("Must have failed because adding data points only works with Scatter & Bubble charts")
        except ApiException as ex:
            self.assertEqual(400, ex.status)

    def test_update_chart_data_point(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        point = OneValueChartDataPoint()
        point.value = 40
        result = BaseTest.slides_api.update_chart_data_point(
            self.file_name, self.slide_index, self.shape_index, 2, 2, point, self.password, self.folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(4, len(result.categories))
        self.assertEqual(4, len(result.series[1].data_points))
        self.assertEqual(point.value, result.series[1].data_points[1].value)

    def test_delete_chart_data_point(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_chart_data_point(
            self.file_name, self.slide_index, self.shape_index, 2, 2, self.password, self.folder_name)
        self.assertEqual(3, len(result.series))
        self.assertEqual(4, len(result.categories))
        self.assertIsNone(result.series[1].data_points[1])

    def test_sunburst_chart(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = Chart()
        chart.chart_type = 'Sunburst'
        chart.width = 400
        chart.height = 300
        series1 = OneValueSeries()
        series1.name = "Series1"
        point1 = OneValueChartDataPoint()
        point1.value = 40
        point2 = OneValueChartDataPoint()
        point2.value = 50
        point3 = OneValueChartDataPoint()
        point3.value = 70
        point4 = OneValueChartDataPoint()
        point4.value = 60
        series1.data_points = [point1, point2, point3, point4]
        chart.series = [series1]
        category1 = ChartCategory()
        category1.value = "Leaf1"
        category1.level = 3
        category1.parent_categories = ["Branch1", "Stem1"]
        category2 = ChartCategory()
        category2.value = "Leaf2"
        category2.level = 3
        category2.parent_categories = ["Branch1", "Stem1"]
        category3 = ChartCategory()
        category3.value = "Branch2"
        category3.level = 2
        category3.parent_categories = ["Stem1"]
        category4 = ChartCategory()
        category4.value = "Stem2"
        category4.level = 1
        chart.categories = [category1, category2, category3, category4]
        result = BaseTest.slides_api.create_shape(self.file_name, self.slide_index, chart, None, None, self.password, self.folder_name)
        self.assertEqual(1, len(result.series))
        self.assertEqual(4, len(result.categories))

    def test_multilevel_chart_category(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = Chart()
        chart.chart_type = "ClusteredColumn"
        chart.x = 100
        chart.y = 100
        chart.width = 500
        chart.height = 400

        series = OneValueSeries()
        series.type = "ClusteredColumn"
        point1 = OneValueChartDataPoint()
        point1.value = 1
        point2 = OneValueChartDataPoint()
        point2.value = 2
        point3 = OneValueChartDataPoint()
        point3.value = 3
        point4 = OneValueChartDataPoint()
        point4.value = 4
        point5 = OneValueChartDataPoint()
        point5.value = 5
        point6 = OneValueChartDataPoint()
        point6.value = 6
        point7 = OneValueChartDataPoint()
        point7.value = 7
        point8 = OneValueChartDataPoint()
        point8.value = 8
        series.data_points = [point1, point2, point3, point4, point5, point6, point7, point8]

        category1 = ChartCategory()
        category1.value = "Category 1"
        category1.parent_categories = ["Sub-category 1", "Root 1"]
        category2 = ChartCategory()
        category2.value = "Category 2"
        category3 = ChartCategory()
        category3.parent_categories = ["Sub-category 2"]
        category4 = ChartCategory()
        category4.value = "Category 4"
        category5 = ChartCategory()
        category5.value = "Category 5"
        category5.parent_categories = ["Sub-category 3", "Root 2"]
        category6 = ChartCategory()
        category6.value = "Category 6"
        category7 = ChartCategory()
        category7.value = "Category 7"
        category7.parent_categories = ["Sub-category 4"]
        category8 = ChartCategory()
        category8.value = "Category 8"

        chart.categories = [category1, category2, category3, category4, category5, category6, category7, category8]
        result = BaseTest.slides_api.create_shape(self.file_name, self.slide_index, chart, None, None, self.password, self.folder_name)
        self.assertEqual("ClusteredColumn", result.chart_type)

    def test_hide_chart_legend(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = BaseTest.slides_api.get_shape(self.file_name, self.slide_index, self.shape_index, self.password, self.folder_name)
        chart.legend.has_legend = False
        chart = BaseTest.slides_api.update_shape(
            self.file_name, self.slide_index, self.shape_index, chart, self.password, self.folder_name)
        self.assertEqual(False, chart.legend.has_legend)

    def test_chart_axis_grid_lines_format(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = BaseTest.slides_api.get_shape(self.file_name, self.slide_index, self.shape_index, self.password, self.folder_name)

        horizontal_axis = Axis()
        horizontal_axis.major_grid_lines_format = ChartLinesFormat()
        horizontal_axis.major_grid_lines_format.line_format = LineFormat()
        horizontal_axis.major_grid_lines_format.line_format.fill_format = NoFill()

        horizontal_axis.minor_grid_lines_format = ChartLinesFormat()
        horizontal_axis.minor_grid_lines_format.line_format = LineFormat()
        horizontal_axis.minor_grid_lines_format.line_format.fill_format = SolidFill()
        horizontal_axis.minor_grid_lines_format.line_format.fill_format.color = "Black"

        vertical_axis = Axis()
        vertical_axis.major_grid_lines_format = ChartLinesFormat()
        vertical_axis.major_grid_lines_format.line_format = LineFormat()
        gradient_fill = GradientFill()
        gradient_fill.direction = "FromCorner1"
        stop1 = GradientFillStop()
        stop1.color = "White"
        stop1.position = 0
        stop2 = GradientFillStop()
        stop2.color = "Black"
        stop2.position = 1
        gradient_fill.stops = [stop1, stop2]
        vertical_axis.major_grid_lines_format.line_format.fill_format = gradient_fill

        vertical_axis.minor_grid_lines_format = ChartLinesFormat()
        vertical_axis.minor_grid_lines_format.line_format = LineFormat()
        vertical_axis.minor_grid_lines_format.line_format.fill_format = NoFill()

        chart.axes = Axes()
        chart.axes.horizontal_axis = horizontal_axis
        chart.axes.vertical_axis = vertical_axis
        chart = BaseTest.slides_api.update_shape(
            self.file_name, self.slide_index, self.shape_index, chart, self.password, self.folder_name)

        self.assertEqual("NoFill", chart.axes.horizontal_axis.major_grid_lines_format.line_format.fill_format.type)
        self.assertEqual("Solid", chart.axes.horizontal_axis.minor_grid_lines_format.line_format.fill_format.type)
        self.assertEqual("Gradient", chart.axes.vertical_axis.major_grid_lines_format.line_format.fill_format.type)
        self.assertEqual("NoFill", chart.axes.vertical_axis.minor_grid_lines_format.line_format.fill_format.type)

    def test_chart_series_groups(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = BaseTest.slides_api.get_shape(self.file_name, self.slide_index, self.shape_index, self.password, self.folder_name)
        self.assertEqual(1, len(chart.series_groups))
        chart.series_groups[0].overlap = 10
        chart = BaseTest.slides_api.set_chart_series_group(
            self.file_name, self.slide_index, self.shape_index, 1, chart.series_groups[0], self.password, self.folder_name)
        self.assertEqual(10, chart.series_groups[0].overlap)

    def test_set_chart_legend(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        legend = Legend()
        legend.overlay = True
        fill_format = SolidFill()
        fill_format.color = "#FFF5FF8A"
        legend.fill_format = fill_format
        response = BaseTest.slides_api.set_chart_legend(
            self.file_name, self.slide_index, self.shape_index, legend, self.password, self.folder_name)
        self.assertTrue(response.overlay)
        self.assertEqual('Solid', response.fill_format.type)

    def test_set_chart_axis(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        axis = Axis()
        axis.has_title = True
        axis.is_automatic_max_value = False
        axis.max_value = 10
        response = BaseTest.slides_api.set_chart_axis(
            self.file_name, self.slide_index, self.shape_index, "VerticalAxis", axis, self.password, self.folder_name)
        self.assertTrue(axis.has_title)
        self.assertFalse(axis.is_automatic_max_value)
        self.assertEqual(axis.max_value, response.max_value)


    def test_set_chart_wall(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        wall = ChartWall()
        fill_format = SolidFill()
        fill_format.color = "#FFF5FF8A"
        wall.fill_format = fill_format

        response = BaseTest.slides_api.set_chart_wall(self.file_name, 8, 2, "Backwall", wall, self.password, self.folder_name)
        self.assertEqual('Solid', response.fill_format.type)

    def test_update_data_point_format(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide_index = 8
        shape_index = 2
        data_point_index = 2
        series_index = 2
        dto = OneValueChartDataPoint()
        dto.value = 40
        fill_format = SolidFill()
        fill_format.color = "#FFF5FF8A"
        line_format = LineFormat()
        line_fill_format = SolidFill()
        line_fill_format.color = "#FFF5FF8A"
        line_format.fill_format = line_fill_format
        effect_format = EffectFormat()
        effect_format.blur = BlurEffect()
        dto.fill_format = fill_format
        dto.line_format = line_format
        dto.effect_format = effect_format

        chart = BaseTest.slides_api.update_chart_data_point(
            self.file_name, slide_index, shape_index, series_index, data_point_index, dto, self.password, self.folder_name)
        data_point = chart.series[series_index - 1].data_points[data_point_index - 1]
        self.assertEqual(data_point.fill_format.type, "Solid")
        self.assertEqual(data_point.line_format.fill_format.type, "Solid")

    def test_chart_workbook_formulas(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        chart = Chart()
        chart.chart_type = 'ClusteredColumn'
        chart.width = 400
        chart.height = 300

        categories_data_source = Workbook()
        categories_data_source.worksheet_index = 1
        categories_data_source.row_index = 2
        categories_data_source.column_index = 1
        chart.data_source_for_categories = categories_data_source

        series1 = OneValueSeries()
        series1_name_data_source = Workbook()
        series1_name_data_source.worksheet_index = 1
        series1_name_data_source.column_index = 2
        series1_name_data_source.row_index = 1
        series1.data_source_for_series_name = series1_name_data_source
        series1.name = "Series1"

        series1_values_data_source = Workbook()
        series1_values_data_source.worksheet_index = 1
        series1_values_data_source.column_index = 2
        series1_values_data_source.row_index = 2
        series1.data_source_for_values = series1_values_data_source
        point11 = OneValueChartDataPoint()
        point11.value = 40
        point12 = OneValueChartDataPoint()
        point12.value = 50
        point13 = OneValueChartDataPoint()
        point13.value_formula = "SUM(B2:B3)"
        series1.data_points = [point11, point12, point13]

        chart.series = [series1]
        category1 = ChartCategory()
        category1.value = "Category1"
        category2 = ChartCategory()
        category2.value = "Category2"
        category3 = ChartCategory()
        category3.value = "Category3"
        chart.categories = [category1, category2, category3]
        result = BaseTest.slides_api.create_shape(self.file_name, self.slide_index, chart, None, None, self.password, self.folder_name)
        self.assertEqual(90, result.series[0].data_points[2].value)