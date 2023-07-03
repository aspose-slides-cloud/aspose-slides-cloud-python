from __future__ import absolute_import

from asposeslidescloud import VbaModule, VbaReference
from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestVba(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_create_vba_module(self):
        BaseTest.slides_api.copy_file("TempTests/" + constant.FILE_NAME,
                                      constant.FOLDER_NAME + "/" + constant.FILE_NAME)
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
        response = BaseTest.slides_api.create_vba_module(constant.FILE_NAME, dto, constant.PASSWORD,
                                                         constant.FOLDER_NAME)
        print("\"" + response.name + "\" has been created\n" + response.self_uri.href)

    def test_delete_vba_module(self):
        file_name = "macros.pptm"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, constant.FOLDER_NAME + "/" + file_name)
        module_index = 1
        response = BaseTest.slides_api.delete_vba_module(file_name, module_index, None, constant.FOLDER_NAME)
        print("VBA project contains: " + str(len(response.modules)) + " module(s), and " + str(
            len(response.references)) + " references")

    def test_get_vba_module(self):
        file_name = "macros.pptm"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, constant.FOLDER_NAME + "/" + file_name)
        module_index = 1
        response = BaseTest.slides_api.get_vba_module(file_name, module_index, None, constant.FOLDER_NAME)
        print("Module: " + response.name + "\n" + response.source_code)

    def test_get_vba_project(self):
        file_name = "macros.pptm"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, constant.FOLDER_NAME + "/" + file_name)

        response = BaseTest.slides_api.get_vba_project(file_name, None, constant.FOLDER_NAME)
        print("VBA project contains: " + str(len(response.modules)) + " module(s), and " + str(
            len(response.references)) + " references")

    def test_update_vba_module(self):
        file_name = "macros.pptm"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, constant.FOLDER_NAME + "/" + file_name)
        dto = VbaModule()
        dto.source_code = "Sub Test() MsgBox ""Test"" End Sub"
        module_index = 1

        response = BaseTest.slides_api.update_vba_module(file_name, module_index, dto, constant.PASSWORD,
                                                         constant.FOLDER_NAME)
        print("\"" + response.name + "\" has been updated\n" + response.self_uri.href)