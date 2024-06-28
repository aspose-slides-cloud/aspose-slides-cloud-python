from __future__ import absolute_import

from test.base_test import BaseTest
from asposeslidescloud import TableCell, TableRow, Table, TableCellMergeOptions, Portion, Paragraph

class TestTable(BaseTest):
    def setUp(self):
        self.slide_index = 9
        self.shape_index = 1
        self.row_index = 2
        self.cell_index = 1
        self.paragraph_index = 1
        self.portion_index = 1

    def tearDown(self):
        pass

    def test_update_table_cell(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = TableCell()
        dto.text = "Test text"
        response = BaseTest.slides_api.update_table_cell(
            self.file_name, self.slide_index, self.shape_index, self.row_index, self.cell_index, dto, self.password, self.folder_name)
        self.assertEqual(dto.text, response.text)

    def test_create_table_row(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
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
        response = BaseTest.slides_api.create_table_row(
            self.file_name, self.slide_index, self.shape_index, dto, None, self.password, self.folder_name)
        self.assertEqual(len(dto.cells), len(response.cells))
        self.assertEqual(dto.minimal_height, response.minimal_height)

    def test_delete_table_row(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        with_attached_table_rows = True
        response = BaseTest.slides_api.delete_table_row(
            self.file_name, self.slide_index, self.shape_index, self.row_index, with_attached_table_rows, self.password, self.folder_name)
        self.assertEqual(2, len(response.rows))

    def test_update_table_row(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = TableRow()
        dto.minimal_height = 30
        response = BaseTest.slides_api.update_table_row(
            self.file_name, self.slide_index, self.shape_index, self.row_index, dto, self.password, self.folder_name)
        self.assertEqual(dto.minimal_height, response.minimal_height)

    def test_merge_table_cells(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = TableCellMergeOptions()
        dto.first_row_index = 1
        dto.first_cell_index = 1
        dto.last_row_index = 2
        dto.last_cell_index = 2
        response = BaseTest.slides_api.merge_table_cells(
            self.file_name, self.slide_index, self.shape_index, dto, self.password, self.folder_name)
        self.assertEqual(2, response.rows[0].cells[0].col_span)
        self.assertEqual(2, response.rows[0].cells[0].row_span)

    def test_split_table_cell_by_width(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        row_index = 1
        cell_width = 10
        response = BaseTest.slides_api.split_table_cell(
            self.file_name,
            self.slide_index,
            self.shape_index,
            row_index,
            self.cell_index,
            'splitByWidth',
            cell_width,
            self.password,
            self.folder_name)
        self.assertEqual(5, len(response.rows[0].cells))

    def test_split_table_cell_by_height(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        cell_height = 10
        response = BaseTest.slides_api.split_table_cell(
            self.file_name,
            self.slide_index,
            self.shape_index,
            self.row_index,
            self.cell_index,
            'splitByHeight',
            cell_height,
            self.password,
            self.folder_name)
        self.assertEqual(5, len(response.rows))

    def test_split_table_cell_by_col_span(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        row_index = 3
        col_span = 1
        response = BaseTest.slides_api.split_table_cell(
            self.file_name,
            self.slide_index,
            self.shape_index,
            row_index,
            self.cell_index,
            'splitByColSpan',
            col_span,
            self.password,
            self.folder_name)
        self.assertEqual(None, response.rows[2].cells[0].col_span)

    def test_split_table_cell_by_row_span(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        cell_index = 3
        row_span = 1
        response = BaseTest.slides_api.split_table_cell(
            self.file_name,
            self.slide_index,
            self.shape_index,
            self.row_index,
            cell_index,
            'splitByRowSpan',
            row_span,
            self.password,
            self.folder_name)
        self.assertEqual(None, response.rows[1].cells[2].row_span)

    def test_get_table_cell_paragraphs(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_table_cell_paragraphs(
            self.file_name,
            self.slide_index,
            self.shape_index,
            self.row_index,
            self.cell_index,
            self.password,
            self.folder_name)
        self.assertEqual(1, len(response.paragraph_links))

    def test_get_table_cell_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        row_index = 1
        response = BaseTest.slides_api.get_table_cell_paragraph(
            self.file_name,
            self.slide_index,
            self.shape_index,
            row_index,
            self.cell_index,
            self.paragraph_index,
            self.password,
            self.folder_name)
        self.assertEqual(2, len(response.portion_list))

    def test_create_table_cell_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        portion_0 = Portion()
        portion_0.text = "Portion 1"
        portion_1 = Portion()
        portion_1.text = "Portion 2"
        dto = Paragraph()
        dto.portion_list = [portion_0, portion_1]

        response = BaseTest.slides_api.create_table_cell_paragraph(
            self.file_name, self.slide_index, self.shape_index, self.row_index, self.cell_index, dto, self.password, self.folder_name)
        self.assertEqual(2, len(response.portion_list))

    def test_update_table_cell_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        portion_0 = Portion()
        portion_0.text = "Portion 1"
        portion_1 = Portion()
        portion_1.text = "Portion 2"
        dto = Paragraph()
        dto.portion_list = [portion_0, portion_1]

        response = BaseTest.slides_api.update_table_cell_paragraph(
            self.file_name,
            self.slide_index,
            self.shape_index,
            self.row_index,
            self.cell_index,
            self.paragraph_index,
            dto,
            self.password,
            self.folder_name)
        self.assertEqual(2, len(response.portion_list))

    def test_delete_table_cell_paragraph(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        row_index = 1
        response = BaseTest.slides_api.delete_table_cell_paragraph(
            self.file_name,
            self.slide_index,
            self.shape_index,
            row_index,
            self.cell_index,
            self.paragraph_index,
            self.password,
            self.folder_name)
        self.assertEqual(0, len(response.paragraph_links))

    def test_get_table_cell_portions(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        row_index = 1
        response = BaseTest.slides_api.get_table_cell_portions(
            self.file_name,
            self.slide_index,
            self.shape_index,
            row_index,
            self.cell_index,
            self.paragraph_index,
            self.password,
            self.folder_name)
        self.assertEqual(2, len(response.items))

    def test_get_table_cell_portion(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        row_index = 1
        response = BaseTest.slides_api.get_table_cell_portion(
            self.file_name,
            self.slide_index,
            self.shape_index,
            row_index,
            self.cell_index,
            self.paragraph_index,
            self.portion_index,
            self.password,
            self.folder_name)
        self.assertEqual("Header", response.text)

    def test_create_table_cell_portion(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Portion()
        dto.text = "Portion 1"

        response = BaseTest.slides_api.create_table_cell_portion(
            self.file_name,
            self.slide_index,
            self.shape_index,
            self.row_index,
            self.cell_index,
            self.paragraph_index,
            dto,
            self.password,
            self.folder_name)
        self.assertEqual(dto.text, response.text)

    def test_update_table_cell_portion(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = Portion()
        dto.text = "Portion 1"

        response = BaseTest.slides_api.update_table_cell_portion(
            self.file_name,
            self.slide_index,
            self.shape_index,
            self.row_index,
            self.cell_index,
            self.paragraph_index,
            self.portion_index,
            dto,
            self.password,
            self.folder_name)
        self.assertEqual(dto.text, response.text)

    def test_delete_table_cell_portion(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        row_index = 1
        response = BaseTest.slides_api.delete_table_cell_portion(
            self.file_name,
            self.slide_index,
            self.shape_index,
            row_index,
            self.cell_index,
            self.paragraph_index,
            self.portion_index,
            self.password,
            self.folder_name)
        self.assertEqual(1, len(response.items))