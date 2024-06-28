from __future__ import absolute_import

from asposeslidescloud import VbaModule, VbaReference
from test.base_test import BaseTest

class TestVba(BaseTest):
    def setUp(self):
        self.module_index = 1


    def tearDown(self):
        pass

    def test_create_vba_module(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = VbaModule()
        dto.name = "Module1"
        dto.source_code = "Sub Test() MsgBox ""Test"" End Sub"
        reference0 = VbaReference()
        reference0.name = "stdole"
        reference0.lib_id = "*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation"
        reference1 = VbaReference()
        reference1.name = "Office"
        reference1.lib_id = "*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library"
        dto.references = [reference0, reference1]
        response = BaseTest.slides_api.create_vba_module(self.file_name, dto, self.password, self.folder_name)
        self.assertEqual(dto.name, response.name)

    def test_delete_vba_module(self):
        file_name = "macros.pptm"
        BaseTest.slides_api.copy_file(self.temp_folder_name + "/" + file_name, self.folder_name + "/" + file_name)
        response = BaseTest.slides_api.delete_vba_module(file_name, self.module_index, None, self.folder_name)
        self.assertEqual(0, len(response.modules))

    def test_get_vba_module(self):
        file_name = "macros.pptm"
        BaseTest.slides_api.copy_file(self.temp_folder_name + "/" + file_name, self.folder_name + "/" + file_name)
        response = BaseTest.slides_api.get_vba_module(file_name, self.module_index, None, self.folder_name)
        self.assertEqual("Module1", response.name)

    def test_get_vba_project(self):
        file_name = "macros.pptm"
        BaseTest.slides_api.copy_file(self.temp_folder_name + "/" + file_name, self.folder_name + "/" + file_name)
        response = BaseTest.slides_api.get_vba_project(file_name, None, self.folder_name)
        self.assertEqual(1, len(response.modules))

    def test_update_vba_module(self):
        file_name = "macros.pptm"
        BaseTest.slides_api.copy_file(self.temp_folder_name + "/" + file_name, self.folder_name + "/" + file_name)
        dto = VbaModule()
        dto.source_code = "Sub Test() MsgBox ""Test"" End Sub"
        response = BaseTest.slides_api.update_vba_module(file_name, self.module_index, dto, self.password, self.folder_name)
        self.assertEqual(dto.source_code, response.source_code)
   