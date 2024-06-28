from __future__ import absolute_import

from asposeslidescloud import Chart
from test.base_test import BaseTest

class TestAbstractClass(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_shape_type(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.get_shape(self.file_name, 1, 1, self.password, self.folder_name)
        self.assertEqual("1", result.text)

    def test_chart_type(self):
        chart = Chart()
        self.assertEqual("Chart", chart.type)