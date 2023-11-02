from __future__ import absolute_import

from test.base_test import BaseTest
import asposeslidescloud
from test import constant
from asposeslidescloud import TableCell, TableRow, Table, TableCellMergeOptions, Portion, Paragraph

class TestTable(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.slides_api_configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_update_table_cell(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 2
        cell_index = 1
        dto = TableCell()
        dto.text = "Test text"
        response = BaseTest.slides_api.update_table_cell(constant.FILE_NAME, slide_index, shape_index, row_index,
                                                         cell_index, dto, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(dto.text, response.text)

    def test_create_table_row(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        cell_0 = TableCell()
        cell_0.text = "Cell 1"
        cell_1 = TableCell()
        cell_1.text = "Cell 2"
        cell_2 = TableCell()
        cell_2.text = "Cell 3"
        cell_3 = TableCell()
        cell_3.text = "Cell 4"
        dto = TableRow()
        dto.minimal_height = 30
        dto.cells = [cell_0, cell_1, cell_2, cell_3]
        response = BaseTest.slides_api.create_table_row(constant.FILE_NAME, slide_index, shape_index, dto, None,
                                                        constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(len(dto.cells), len(response.cells))
        self.assertEqual(dto.minimal_height, response.minimal_height)

    def test_delete_table_row(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 2
        with_attached_table_rows = True
        response = BaseTest.slides_api.delete_table_row(constant.FILE_NAME, slide_index, shape_index, row_index,
                                                        with_attached_table_rows, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(2, len(response.rows))

    def test_update_table_row(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        dto = TableRow()
        dto.minimal_height = 30
        response = BaseTest.slides_api.update_table_row(constant.FILE_NAME, slide_index, shape_index, row_index, dto,
                                                        constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(dto.minimal_height, response.minimal_height)

    def test_merge_table_cells(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        dto = TableCellMergeOptions()
        dto.first_row_index = 1
        dto.first_cell_index = 1
        dto.last_row_index = 2
        dto.last_cell_index = 2
        response = BaseTest.slides_api.merge_table_cells(constant.FILE_NAME, slide_index, shape_index, dto,
                                                        constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(2, response.rows[0].cells[0].col_span)
        self.assertEqual(2, response.rows[0].cells[0].row_span)

    def test_split_table_cell_by_width(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        cell_width = 10
        response = BaseTest.slides_api.split_table_cell(constant.FILE_NAME, slide_index,
                                                        shape_index, row_index, cell_index, 'splitByWidth', cell_width, constant.PASSWORD,
                                                        constant.FOLDER_NAME)
        self.assertEqual(5, len(response.rows[0].cells))

    def test_split_table_cell_by_height(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        cell_height = 10
        response = BaseTest.slides_api.split_table_cell(constant.FILE_NAME, slide_index,
                                                        shape_index, row_index, cell_index, 'splitByHeight', cell_height, constant.PASSWORD,
                                                        constant.FOLDER_NAME)
        self.assertEqual(5, len(response.rows))

    def test_split_table_cell_by_col_span(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 3
        cell_index = 1
        col_span = 1
        response = BaseTest.slides_api.split_table_cell(constant.FILE_NAME, slide_index,
                                                        shape_index, row_index, cell_index, 'splitByColSpan', col_span, constant.PASSWORD,
                                                        constant.FOLDER_NAME)
        self.assertEqual(None, response.rows[2].cells[0].col_span)

    def test_split_table_cell_by_row_span(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 2
        cell_index = 3
        row_span = 1
        response = BaseTest.slides_api.split_table_cell(constant.FILE_NAME, slide_index,
                                                        shape_index, row_index, cell_index, 'splitByRowSpan', row_span, constant.PASSWORD,
                                                        constant.FOLDER_NAME)
        self.assertEqual(None, response.rows[1].cells[2].row_span)

    def test_get_table_cell_paragraphs(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        response = BaseTest.slides_api.get_table_cell_paragraphs(constant.FILE_NAME, slide_index, shape_index,
                                                                 row_index, cell_index, constant.PASSWORD,
                                                                 constant.FOLDER_NAME)
        self.assertEqual(1, len(response.paragraph_links))

    def test_get_table_cell_paragraph(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        paragraph_index = 1
        response = BaseTest.slides_api.get_table_cell_paragraph(constant.FILE_NAME, slide_index, shape_index,
                                                                row_index, paragraph_index, cell_index,
                                                                constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(2, len(response.portion_list))

    def test_create_table_cell_paragraph(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        portion_0 = Portion()
        portion_0.text = "Portion 1"
        portion_1 = Portion()
        portion_1.text = "Portion 2"
        dto = Paragraph()
        dto.portion_list = [portion_0, portion_1]

        response = BaseTest.slides_api.create_table_cell_paragraph(constant.FILE_NAME, slide_index, shape_index,
                                                                   row_index, cell_index, dto,
                                                                   constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(2, len(response.portion_list))

    def test_update_table_cell_paragraph(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        paragraph_index = 1
        portion_0 = Portion()
        portion_0.text = "Portion 1"
        portion_1 = Portion()
        portion_1.text = "Portion 2"
        dto = Paragraph()
        dto.portion_list = [portion_0, portion_1]

        response = BaseTest.slides_api.update_table_cell_paragraph(constant.FILE_NAME, slide_index, shape_index,
                                                                   row_index, cell_index, paragraph_index, dto,
                                                                   constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(2, len(response.portion_list))

    def test_delete_table_cell_paragraph(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        paragraph_index = 1

        response = BaseTest.slides_api.delete_table_cell_paragraph(constant.FILE_NAME, slide_index, shape_index,
                                                                   row_index, cell_index, paragraph_index,
                                                                   constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(0, len(response.paragraph_links))

    def test_get_table_cell_portions(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        paragraph_index = 1

        response = BaseTest.slides_api.get_table_cell_portions(constant.FILE_NAME, slide_index, shape_index,
                                                               row_index, cell_index, paragraph_index,
                                                               constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(2, len(response.items))

    def test_get_table_cell_portion(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        paragraph_index = 1
        portion_index = 1

        response = BaseTest.slides_api.get_table_cell_portion(constant.FILE_NAME, slide_index, shape_index,
                                                              row_index, cell_index, paragraph_index, portion_index,
                                                              constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual("Header", response.text)

    def test_create_table_cell_portion(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        paragraph_index = 1
        dto = Portion()
        dto.text = "Portion 1"

        response = BaseTest.slides_api.create_table_cell_portion(constant.FILE_NAME, slide_index, shape_index,
                                                                 row_index, cell_index, paragraph_index, dto,
                                                                 constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(dto.text, response.text)

    def test_update_table_cell_portion(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        paragraph_index = 1
        portion_index = 1
        dto = Portion()
        dto.text = "Portion 1"

        response = BaseTest.slides_api.update_table_cell_portion(constant.FILE_NAME, slide_index, shape_index,
                                                                 row_index, cell_index, paragraph_index, portion_index,
                                                                 dto, constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(dto.text, response.text)

    def test_delete_table_cell_portion(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
        slide_index = 9
        shape_index = 1
        row_index = 1
        cell_index = 1
        paragraph_index = 1
        portion_index = 1

        response = BaseTest.slides_api.delete_table_cell_portion(constant.FILE_NAME, slide_index, shape_index,
                                                                 row_index, cell_index, paragraph_index, portion_index,
                                                                 constant.PASSWORD, constant.FOLDER_NAME)
        self.assertEqual(1, len(response.items))