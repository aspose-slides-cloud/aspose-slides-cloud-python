from __future__ import absolute_import

import os

from asposeslidescloud import ProtectionProperties, SlideProperties, DocumentProperty, DocumentProperties, \
    ViewProperties, CommonSlideViewProperties, SlideShowProperties
from asposeslidescloud.rest import ApiException
from test.base_test import BaseTest

class TestProperty(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_document_properties_builtin(self):
        property_name = "Author"
        updated_property_value = "New Value"
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.get_document_property(self.file_name, property_name, self.password, self.folder_name)
        self.assertEqual(property_name, result.name)
        self.assertTrue(result.built_in)
        property = DocumentProperty()
        property.value = updated_property_value
        result = BaseTest.slides_api.set_document_property(self.file_name, property_name, property, self.password, self.folder_name)
        self.assertEqual(property_name, result.name)
        self.assertEqual(updated_property_value, result.value)
        self.assertTrue(result.built_in)
        BaseTest.slides_api.delete_document_property(self.file_name, property_name, self.password, self.folder_name)
        result = BaseTest.slides_api.get_document_property(self.file_name, property_name, self.password, self.folder_name)
        # built-in property is not actually deleted
        self.assertEqual(property_name, result.name)
        self.assertNotEqual(updated_property_value, result.value)
        self.assertTrue(result.built_in)

    def test_document_properties_custom(self):
        property_name = "CustomProperty2"
        updated_property_value = "New Value"
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        property = DocumentProperty()
        property.value = updated_property_value
        result = BaseTest.slides_api.set_document_property(self.file_name, property_name, property, self.password, self.folder_name)
        self.assertEqual(property_name, result.name)
        self.assertEqual(updated_property_value, result.value)
        self.assertFalse(result.built_in)
        BaseTest.slides_api.delete_document_property(self.file_name, property_name, self.password, self.folder_name)
        try:
            BaseTest.slides_api.get_document_property(self.file_name, property_name, self.password, self.folder_name)
            self.fail("The property must have been deleted")
        except ApiException as ex:
            self.assertEqual(404, ex.status)

    def test_document_properties_bulk_update(self):
        property_name = "Author"
        custom_property_name = "CustomProperty2"
        updated_property_value = "New Value"
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.get_document_properties(self.file_name, self.password, self.folder_name)
        count = len(result.list)
        property1 = DocumentProperty()
        property1.name = property_name
        property1.value = updated_property_value
        property2 = DocumentProperty()
        property2.name = custom_property_name
        property2.value = updated_property_value
        properties = DocumentProperties()
        properties.list = [property1, property2]
        result = BaseTest.slides_api.set_document_properties(self.file_name, properties, self.password, self.folder_name)
        self.assertEqual(count + 1, len(result.list))
        result = BaseTest.slides_api.delete_document_properties(self.file_name, self.password, self.folder_name)
        self.assertEqual(count - 1, len(result.list))

    def test_slide_properties(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        get_result = BaseTest.slides_api.get_slide_properties(self.file_name, self.password, self.folder_name)
        dto = SlideProperties()
        dto.first_slide_number = get_result.first_slide_number + 2
        put_result = BaseTest.slides_api.set_slide_properties(self.file_name, dto, self.password, self.folder_name)
        self.assertEqual(get_result.orientation, put_result.orientation)
        self.assertNotEqual(get_result.first_slide_number, put_result.first_slide_number)

    def test_slide_size_preset(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = SlideProperties()
        dto.size_type = 'B4IsoPaper'
        result = BaseTest.slides_api.set_slide_properties(self.file_name, dto, self.password, self.folder_name)
        self.assertEqual('B4IsoPaper', result.size_type)
        self.assertEqual(852, result.width)
        self.assertEqual(639, result.height)

    def test_slide_size_custom(self):
        width = 800
        height = 500
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = SlideProperties()
        dto.width = width
        dto.height = height
        result = BaseTest.slides_api.set_slide_properties(self.file_name, dto, self.password, self.folder_name)
        self.assertEqual('Custom', result.size_type)
        self.assertEqual(width, result.width)
        self.assertEqual(height, result.height)

    def test_protection(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        get_result = BaseTest.slides_api.get_protection_properties(self.file_name, self.password, self.folder_name)
        dto = ProtectionProperties()
        dto.read_only_recommended = not get_result.read_only_recommended
        put_result = BaseTest.slides_api.set_protection(self.file_name, dto, self.password, self.folder_name)
        self.assertEqual(get_result.encrypt_document_properties, put_result.encrypt_document_properties)
        self.assertNotEqual(get_result.read_only_recommended, put_result.read_only_recommended)

    def test_delete_protection(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        result = BaseTest.slides_api.delete_protection(self.file_name, self.password, self.folder_name)
        self.assertFalse(result.is_encrypted)
        self.assertFalse(result.read_only_recommended)
        self.assertFalse(result.read_password)

    def test_protect_online(self):
        dto = ProtectionProperties()
        dto.read_password = "newPassword"
        with open(self.local_path, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.set_protection_online(source, dto, self.password)
        self.assertTrue(os.path.getsize(result) > 0)

    def test_unprotect_online(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        result = BaseTest.slides_api.delete_protection_online(source, self.password)
        self.assertNotEqual(len(source), os.path.getsize(result))

    def test_get_view_properties(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_view_properties(self.file_name, self.password, self.folder_name)
        self.assertEqual("True", response.show_comments)

    def test_set_view_properties(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = ViewProperties()
        dto.show_comments = "False"
        dto.slide_view_properties = CommonSlideViewProperties()
        dto.slide_view_properties.scale = 50
        response = BaseTest.slides_api.set_view_properties(self.file_name, dto, self.password, self.folder_name)
        self.assertEqual("False", response.show_comments)
        self.assertEqual(50, response.slide_view_properties.scale)

    def test_protection_check(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        protection_properties = BaseTest.slides_api.get_protection_properties(self.file_name, None, self.folder_name)
        self.assertEqual(True, protection_properties.is_encrypted)
        self.assertEqual(None, protection_properties.read_password)

        protection_properties = BaseTest.slides_api.get_protection_properties(self.file_name, self.password, self.folder_name)
        self.assertEqual(True, protection_properties.is_encrypted)
        self.assertNotEqual(None, protection_properties.read_password)

    def test_get_slide_show_properties(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_slide_show_properties(self.file_name, self.password, self.folder_name)
        self.assertTrue(response.show_animation)
        self.assertTrue(response.show_narration)

    def test_set_slide_show_properties(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = SlideShowProperties()
        dto.loop = True
        dto.use_timings = True
        dto.slide_show_type = "PresentedBySpeaker"

        response = BaseTest.slides_api.set_slide_show_properties(self.file_name, dto, self.password, self.folder_name)
        self.assertEqual(dto.loop, response.loop)
        self.assertEqual(dto.use_timings, response.use_timings)
        self.assertEqual(dto.slide_show_type, response.slide_show_type)