# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose">
#   Copyright (c) 2018 Aspose.Slides for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

from __future__ import absolute_import

import unittest

from test.base_test import BaseTest

import asposeslidescloud
from asposeslidescloud.apis.slides_api import SlidesApi  # noqa: E501
from asposeslidescloud.rest import ApiException

class TestSlidesApi(BaseTest):

    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_copy_file(self):
        """Test case for copy_file
        """
        request = self.__prepare_copy_file_request()
        self.initialize('copy_file', None, None)
        response = self.api.copy_file(request)
        self.assertIsNone(response)

    def test_copy_file_invalid_src_path(self):
        """Test case for copy_file with invalid src_path
        """
        request = self.__prepare_copy_file_request()
        request.src_path = self.get_invalid_test_value('copy_file', 'src_path', request.src_path, 'str')
        self.initialize('copy_file', 'src_path', request.src_path)
        ok = False
        try:
            self.api.copy_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'copy_file', 'src_path', request.src_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('copy_file', 'src_path')

    def test_copy_file_invalid_dest_path(self):
        """Test case for copy_file with invalid dest_path
        """
        request = self.__prepare_copy_file_request()
        request.dest_path = self.get_invalid_test_value('copy_file', 'dest_path', request.dest_path, 'str')
        self.initialize('copy_file', 'dest_path', request.dest_path)
        ok = False
        try:
            self.api.copy_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'copy_file', 'dest_path', request.dest_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('copy_file', 'dest_path')

    def test_copy_file_invalid_src_storage_name(self):
        """Test case for copy_file with invalid src_storage_name
        """
        request = self.__prepare_copy_file_request()
        request.src_storage_name = self.get_invalid_test_value('copy_file', 'src_storage_name', request.src_storage_name, 'str')
        self.initialize('copy_file', 'src_storage_name', request.src_storage_name)
        ok = False
        try:
            self.api.copy_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'copy_file', 'src_storage_name', request.src_storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('copy_file', 'src_storage_name')

    def test_copy_file_invalid_dest_storage_name(self):
        """Test case for copy_file with invalid dest_storage_name
        """
        request = self.__prepare_copy_file_request()
        request.dest_storage_name = self.get_invalid_test_value('copy_file', 'dest_storage_name', request.dest_storage_name, 'str')
        self.initialize('copy_file', 'dest_storage_name', request.dest_storage_name)
        ok = False
        try:
            self.api.copy_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'copy_file', 'dest_storage_name', request.dest_storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('copy_file', 'dest_storage_name')

    def test_copy_file_invalid_version_id(self):
        """Test case for copy_file with invalid version_id
        """
        request = self.__prepare_copy_file_request()
        request.version_id = self.get_invalid_test_value('copy_file', 'version_id', request.version_id, 'str')
        self.initialize('copy_file', 'version_id', request.version_id)
        ok = False
        try:
            self.api.copy_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'copy_file', 'version_id', request.version_id)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('copy_file', 'version_id')

    def __prepare_copy_file_request(self):
        src_path = self.get_test_value('copy_file', 'src_path', 'str')
        dest_path = self.get_test_value('copy_file', 'dest_path', 'str')
        src_storage_name = self.get_test_value('copy_file', 'src_storage_name', 'str')
        dest_storage_name = self.get_test_value('copy_file', 'dest_storage_name', 'str')
        version_id = self.get_test_value('copy_file', 'version_id', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.CopyFileRequest(src_path, dest_path, src_storage_name, dest_storage_name, version_id)

    def test_copy_folder(self):
        """Test case for copy_folder
        """
        request = self.__prepare_copy_folder_request()
        self.initialize('copy_folder', None, None)
        response = self.api.copy_folder(request)
        self.assertIsNone(response)

    def test_copy_folder_invalid_src_path(self):
        """Test case for copy_folder with invalid src_path
        """
        request = self.__prepare_copy_folder_request()
        request.src_path = self.get_invalid_test_value('copy_folder', 'src_path', request.src_path, 'str')
        self.initialize('copy_folder', 'src_path', request.src_path)
        ok = False
        try:
            self.api.copy_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'copy_folder', 'src_path', request.src_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('copy_folder', 'src_path')

    def test_copy_folder_invalid_dest_path(self):
        """Test case for copy_folder with invalid dest_path
        """
        request = self.__prepare_copy_folder_request()
        request.dest_path = self.get_invalid_test_value('copy_folder', 'dest_path', request.dest_path, 'str')
        self.initialize('copy_folder', 'dest_path', request.dest_path)
        ok = False
        try:
            self.api.copy_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'copy_folder', 'dest_path', request.dest_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('copy_folder', 'dest_path')

    def test_copy_folder_invalid_src_storage_name(self):
        """Test case for copy_folder with invalid src_storage_name
        """
        request = self.__prepare_copy_folder_request()
        request.src_storage_name = self.get_invalid_test_value('copy_folder', 'src_storage_name', request.src_storage_name, 'str')
        self.initialize('copy_folder', 'src_storage_name', request.src_storage_name)
        ok = False
        try:
            self.api.copy_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'copy_folder', 'src_storage_name', request.src_storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('copy_folder', 'src_storage_name')

    def test_copy_folder_invalid_dest_storage_name(self):
        """Test case for copy_folder with invalid dest_storage_name
        """
        request = self.__prepare_copy_folder_request()
        request.dest_storage_name = self.get_invalid_test_value('copy_folder', 'dest_storage_name', request.dest_storage_name, 'str')
        self.initialize('copy_folder', 'dest_storage_name', request.dest_storage_name)
        ok = False
        try:
            self.api.copy_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'copy_folder', 'dest_storage_name', request.dest_storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('copy_folder', 'dest_storage_name')

    def __prepare_copy_folder_request(self):
        src_path = self.get_test_value('copy_folder', 'src_path', 'str')
        dest_path = self.get_test_value('copy_folder', 'dest_path', 'str')
        src_storage_name = self.get_test_value('copy_folder', 'src_storage_name', 'str')
        dest_storage_name = self.get_test_value('copy_folder', 'dest_storage_name', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.CopyFolderRequest(src_path, dest_path, src_storage_name, dest_storage_name)

    def test_create_folder(self):
        """Test case for create_folder
        """
        request = self.__prepare_create_folder_request()
        self.initialize('create_folder', None, None)
        response = self.api.create_folder(request)
        self.assertIsNone(response)

    def test_create_folder_invalid_path(self):
        """Test case for create_folder with invalid path
        """
        request = self.__prepare_create_folder_request()
        request.path = self.get_invalid_test_value('create_folder', 'path', request.path, 'str')
        self.initialize('create_folder', 'path', request.path)
        ok = False
        try:
            self.api.create_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'create_folder', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('create_folder', 'path')

    def test_create_folder_invalid_storage_name(self):
        """Test case for create_folder with invalid storage_name
        """
        request = self.__prepare_create_folder_request()
        request.storage_name = self.get_invalid_test_value('create_folder', 'storage_name', request.storage_name, 'str')
        self.initialize('create_folder', 'storage_name', request.storage_name)
        ok = False
        try:
            self.api.create_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'create_folder', 'storage_name', request.storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('create_folder', 'storage_name')

    def __prepare_create_folder_request(self):
        path = self.get_test_value('create_folder', 'path', 'str')
        storage_name = self.get_test_value('create_folder', 'storage_name', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.CreateFolderRequest(path, storage_name)

    def test_delete_file(self):
        """Test case for delete_file
        """
        request = self.__prepare_delete_file_request()
        self.initialize('delete_file', None, None)
        response = self.api.delete_file(request)
        self.assertIsNone(response)

    def test_delete_file_invalid_path(self):
        """Test case for delete_file with invalid path
        """
        request = self.__prepare_delete_file_request()
        request.path = self.get_invalid_test_value('delete_file', 'path', request.path, 'str')
        self.initialize('delete_file', 'path', request.path)
        ok = False
        try:
            self.api.delete_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_file', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_file', 'path')

    def test_delete_file_invalid_storage_name(self):
        """Test case for delete_file with invalid storage_name
        """
        request = self.__prepare_delete_file_request()
        request.storage_name = self.get_invalid_test_value('delete_file', 'storage_name', request.storage_name, 'str')
        self.initialize('delete_file', 'storage_name', request.storage_name)
        ok = False
        try:
            self.api.delete_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_file', 'storage_name', request.storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_file', 'storage_name')

    def test_delete_file_invalid_version_id(self):
        """Test case for delete_file with invalid version_id
        """
        request = self.__prepare_delete_file_request()
        request.version_id = self.get_invalid_test_value('delete_file', 'version_id', request.version_id, 'str')
        self.initialize('delete_file', 'version_id', request.version_id)
        ok = False
        try:
            self.api.delete_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_file', 'version_id', request.version_id)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_file', 'version_id')

    def __prepare_delete_file_request(self):
        path = self.get_test_value('delete_file', 'path', 'str')
        storage_name = self.get_test_value('delete_file', 'storage_name', 'str')
        version_id = self.get_test_value('delete_file', 'version_id', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteFileRequest(path, storage_name, version_id)

    def test_delete_folder(self):
        """Test case for delete_folder
        """
        request = self.__prepare_delete_folder_request()
        self.initialize('delete_folder', None, None)
        response = self.api.delete_folder(request)
        self.assertIsNone(response)

    def test_delete_folder_invalid_path(self):
        """Test case for delete_folder with invalid path
        """
        request = self.__prepare_delete_folder_request()
        request.path = self.get_invalid_test_value('delete_folder', 'path', request.path, 'str')
        self.initialize('delete_folder', 'path', request.path)
        ok = False
        try:
            self.api.delete_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_folder', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_folder', 'path')

    def test_delete_folder_invalid_storage_name(self):
        """Test case for delete_folder with invalid storage_name
        """
        request = self.__prepare_delete_folder_request()
        request.storage_name = self.get_invalid_test_value('delete_folder', 'storage_name', request.storage_name, 'str')
        self.initialize('delete_folder', 'storage_name', request.storage_name)
        ok = False
        try:
            self.api.delete_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_folder', 'storage_name', request.storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_folder', 'storage_name')

    def test_delete_folder_invalid_recursive(self):
        """Test case for delete_folder with invalid recursive
        """
        request = self.__prepare_delete_folder_request()
        request.recursive = self.get_invalid_test_value('delete_folder', 'recursive', request.recursive, 'bool')
        self.initialize('delete_folder', 'recursive', request.recursive)
        ok = False
        try:
            self.api.delete_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_folder', 'recursive', request.recursive)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_folder', 'recursive')

    def __prepare_delete_folder_request(self):
        path = self.get_test_value('delete_folder', 'path', 'str')
        storage_name = self.get_test_value('delete_folder', 'storage_name', 'str')
        recursive = self.get_test_value('delete_folder', 'recursive', 'bool')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteFolderRequest(path, storage_name, recursive)

    def test_delete_notes_slide(self):
        """Test case for delete_notes_slide
        """
        request = self.__prepare_delete_notes_slide_request()
        self.initialize('delete_notes_slide', None, None)
        response = self.api.delete_notes_slide(request)
        self.assertIsNotNone(response)

    def test_delete_notes_slide_invalid_name(self):
        """Test case for delete_notes_slide with invalid name
        """
        request = self.__prepare_delete_notes_slide_request()
        request.name = self.get_invalid_test_value('delete_notes_slide', 'name', request.name, 'str')
        self.initialize('delete_notes_slide', 'name', request.name)
        ok = False
        try:
            self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide', 'name')

    def test_delete_notes_slide_invalid_slide_index(self):
        """Test case for delete_notes_slide with invalid slide_index
        """
        request = self.__prepare_delete_notes_slide_request()
        request.slide_index = self.get_invalid_test_value('delete_notes_slide', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_notes_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide', 'slide_index')

    def test_delete_notes_slide_invalid_password(self):
        """Test case for delete_notes_slide with invalid password
        """
        request = self.__prepare_delete_notes_slide_request()
        request.password = self.get_invalid_test_value('delete_notes_slide', 'password', request.password, 'str')
        self.initialize('delete_notes_slide', 'password', request.password)
        ok = False
        try:
            self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide', 'password')

    def test_delete_notes_slide_invalid_folder(self):
        """Test case for delete_notes_slide with invalid folder
        """
        request = self.__prepare_delete_notes_slide_request()
        request.folder = self.get_invalid_test_value('delete_notes_slide', 'folder', request.folder, 'str')
        self.initialize('delete_notes_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide', 'folder')

    def test_delete_notes_slide_invalid_storage(self):
        """Test case for delete_notes_slide with invalid storage
        """
        request = self.__prepare_delete_notes_slide_request()
        request.storage = self.get_invalid_test_value('delete_notes_slide', 'storage', request.storage, 'str')
        self.initialize('delete_notes_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide', 'storage')

    def __prepare_delete_notes_slide_request(self):
        name = self.get_test_value('delete_notes_slide', 'name', 'str')
        slide_index = self.get_test_value('delete_notes_slide', 'slide_index', 'int')
        password = self.get_test_value('delete_notes_slide', 'password', 'str')
        folder = self.get_test_value('delete_notes_slide', 'folder', 'str')
        storage = self.get_test_value('delete_notes_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteNotesSlideRequest(name, slide_index, password, folder, storage)

    def test_delete_notes_slide_paragraph(self):
        """Test case for delete_notes_slide_paragraph
        """
        request = self.__prepare_delete_notes_slide_paragraph_request()
        self.initialize('delete_notes_slide_paragraph', None, None)
        response = self.api.delete_notes_slide_paragraph(request)
        self.assertIsNotNone(response)

    def test_delete_notes_slide_paragraph_invalid_name(self):
        """Test case for delete_notes_slide_paragraph with invalid name
        """
        request = self.__prepare_delete_notes_slide_paragraph_request()
        request.name = self.get_invalid_test_value('delete_notes_slide_paragraph', 'name', request.name, 'str')
        self.initialize('delete_notes_slide_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.delete_notes_slide_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraph', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraph', 'name')

    def test_delete_notes_slide_paragraph_invalid_slide_index(self):
        """Test case for delete_notes_slide_paragraph with invalid slide_index
        """
        request = self.__prepare_delete_notes_slide_paragraph_request()
        request.slide_index = self.get_invalid_test_value('delete_notes_slide_paragraph', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_notes_slide_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_notes_slide_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraph', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraph', 'slide_index')

    def test_delete_notes_slide_paragraph_invalid_shape_index(self):
        """Test case for delete_notes_slide_paragraph with invalid shape_index
        """
        request = self.__prepare_delete_notes_slide_paragraph_request()
        request.shape_index = self.get_invalid_test_value('delete_notes_slide_paragraph', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_notes_slide_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_notes_slide_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraph', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraph', 'shape_index')

    def test_delete_notes_slide_paragraph_invalid_paragraph_index(self):
        """Test case for delete_notes_slide_paragraph with invalid paragraph_index
        """
        request = self.__prepare_delete_notes_slide_paragraph_request()
        request.paragraph_index = self.get_invalid_test_value('delete_notes_slide_paragraph', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_notes_slide_paragraph', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_notes_slide_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraph', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraph', 'paragraph_index')

    def test_delete_notes_slide_paragraph_invalid_password(self):
        """Test case for delete_notes_slide_paragraph with invalid password
        """
        request = self.__prepare_delete_notes_slide_paragraph_request()
        request.password = self.get_invalid_test_value('delete_notes_slide_paragraph', 'password', request.password, 'str')
        self.initialize('delete_notes_slide_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.delete_notes_slide_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraph', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraph', 'password')

    def test_delete_notes_slide_paragraph_invalid_folder(self):
        """Test case for delete_notes_slide_paragraph with invalid folder
        """
        request = self.__prepare_delete_notes_slide_paragraph_request()
        request.folder = self.get_invalid_test_value('delete_notes_slide_paragraph', 'folder', request.folder, 'str')
        self.initialize('delete_notes_slide_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_notes_slide_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraph', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraph', 'folder')

    def test_delete_notes_slide_paragraph_invalid_storage(self):
        """Test case for delete_notes_slide_paragraph with invalid storage
        """
        request = self.__prepare_delete_notes_slide_paragraph_request()
        request.storage = self.get_invalid_test_value('delete_notes_slide_paragraph', 'storage', request.storage, 'str')
        self.initialize('delete_notes_slide_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_notes_slide_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraph', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraph', 'storage')

    def __prepare_delete_notes_slide_paragraph_request(self):
        name = self.get_test_value('delete_notes_slide_paragraph', 'name', 'str')
        slide_index = self.get_test_value('delete_notes_slide_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_notes_slide_paragraph', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_notes_slide_paragraph', 'paragraph_index', 'int')
        password = self.get_test_value('delete_notes_slide_paragraph', 'password', 'str')
        folder = self.get_test_value('delete_notes_slide_paragraph', 'folder', 'str')
        storage = self.get_test_value('delete_notes_slide_paragraph', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteNotesSlideParagraphRequest(name, slide_index, shape_index, paragraph_index, password, folder, storage)

    def test_delete_notes_slide_paragraphs(self):
        """Test case for delete_notes_slide_paragraphs
        """
        request = self.__prepare_delete_notes_slide_paragraphs_request()
        self.initialize('delete_notes_slide_paragraphs', None, None)
        response = self.api.delete_notes_slide_paragraphs(request)
        self.assertIsNotNone(response)

    def test_delete_notes_slide_paragraphs_invalid_name(self):
        """Test case for delete_notes_slide_paragraphs with invalid name
        """
        request = self.__prepare_delete_notes_slide_paragraphs_request()
        request.name = self.get_invalid_test_value('delete_notes_slide_paragraphs', 'name', request.name, 'str')
        self.initialize('delete_notes_slide_paragraphs', 'name', request.name)
        ok = False
        try:
            self.api.delete_notes_slide_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraphs', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraphs', 'name')

    def test_delete_notes_slide_paragraphs_invalid_slide_index(self):
        """Test case for delete_notes_slide_paragraphs with invalid slide_index
        """
        request = self.__prepare_delete_notes_slide_paragraphs_request()
        request.slide_index = self.get_invalid_test_value('delete_notes_slide_paragraphs', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_notes_slide_paragraphs', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_notes_slide_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraphs', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraphs', 'slide_index')

    def test_delete_notes_slide_paragraphs_invalid_shape_index(self):
        """Test case for delete_notes_slide_paragraphs with invalid shape_index
        """
        request = self.__prepare_delete_notes_slide_paragraphs_request()
        request.shape_index = self.get_invalid_test_value('delete_notes_slide_paragraphs', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_notes_slide_paragraphs', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_notes_slide_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraphs', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraphs', 'shape_index')

    def test_delete_notes_slide_paragraphs_invalid_paragraphs(self):
        """Test case for delete_notes_slide_paragraphs with invalid paragraphs
        """
        request = self.__prepare_delete_notes_slide_paragraphs_request()
        request.paragraphs = self.get_invalid_test_value('delete_notes_slide_paragraphs', 'paragraphs', request.paragraphs, 'list[int]')
        self.initialize('delete_notes_slide_paragraphs', 'paragraphs', request.paragraphs)
        ok = False
        try:
            self.api.delete_notes_slide_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraphs', 'paragraphs', request.paragraphs)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraphs', 'paragraphs')

    def test_delete_notes_slide_paragraphs_invalid_password(self):
        """Test case for delete_notes_slide_paragraphs with invalid password
        """
        request = self.__prepare_delete_notes_slide_paragraphs_request()
        request.password = self.get_invalid_test_value('delete_notes_slide_paragraphs', 'password', request.password, 'str')
        self.initialize('delete_notes_slide_paragraphs', 'password', request.password)
        ok = False
        try:
            self.api.delete_notes_slide_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraphs', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraphs', 'password')

    def test_delete_notes_slide_paragraphs_invalid_folder(self):
        """Test case for delete_notes_slide_paragraphs with invalid folder
        """
        request = self.__prepare_delete_notes_slide_paragraphs_request()
        request.folder = self.get_invalid_test_value('delete_notes_slide_paragraphs', 'folder', request.folder, 'str')
        self.initialize('delete_notes_slide_paragraphs', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_notes_slide_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraphs', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraphs', 'folder')

    def test_delete_notes_slide_paragraphs_invalid_storage(self):
        """Test case for delete_notes_slide_paragraphs with invalid storage
        """
        request = self.__prepare_delete_notes_slide_paragraphs_request()
        request.storage = self.get_invalid_test_value('delete_notes_slide_paragraphs', 'storage', request.storage, 'str')
        self.initialize('delete_notes_slide_paragraphs', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_notes_slide_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_paragraphs', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_paragraphs', 'storage')

    def __prepare_delete_notes_slide_paragraphs_request(self):
        name = self.get_test_value('delete_notes_slide_paragraphs', 'name', 'str')
        slide_index = self.get_test_value('delete_notes_slide_paragraphs', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_notes_slide_paragraphs', 'shape_index', 'int')
        paragraphs = self.get_test_value('delete_notes_slide_paragraphs', 'paragraphs', 'list[int]')
        password = self.get_test_value('delete_notes_slide_paragraphs', 'password', 'str')
        folder = self.get_test_value('delete_notes_slide_paragraphs', 'folder', 'str')
        storage = self.get_test_value('delete_notes_slide_paragraphs', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteNotesSlideParagraphsRequest(name, slide_index, shape_index, paragraphs, password, folder, storage)

    def test_delete_notes_slide_portion(self):
        """Test case for delete_notes_slide_portion
        """
        request = self.__prepare_delete_notes_slide_portion_request()
        self.initialize('delete_notes_slide_portion', None, None)
        response = self.api.delete_notes_slide_portion(request)
        self.assertIsNotNone(response)

    def test_delete_notes_slide_portion_invalid_name(self):
        """Test case for delete_notes_slide_portion with invalid name
        """
        request = self.__prepare_delete_notes_slide_portion_request()
        request.name = self.get_invalid_test_value('delete_notes_slide_portion', 'name', request.name, 'str')
        self.initialize('delete_notes_slide_portion', 'name', request.name)
        ok = False
        try:
            self.api.delete_notes_slide_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portion', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portion', 'name')

    def test_delete_notes_slide_portion_invalid_slide_index(self):
        """Test case for delete_notes_slide_portion with invalid slide_index
        """
        request = self.__prepare_delete_notes_slide_portion_request()
        request.slide_index = self.get_invalid_test_value('delete_notes_slide_portion', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_notes_slide_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_notes_slide_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portion', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portion', 'slide_index')

    def test_delete_notes_slide_portion_invalid_shape_index(self):
        """Test case for delete_notes_slide_portion with invalid shape_index
        """
        request = self.__prepare_delete_notes_slide_portion_request()
        request.shape_index = self.get_invalid_test_value('delete_notes_slide_portion', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_notes_slide_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_notes_slide_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portion', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portion', 'shape_index')

    def test_delete_notes_slide_portion_invalid_paragraph_index(self):
        """Test case for delete_notes_slide_portion with invalid paragraph_index
        """
        request = self.__prepare_delete_notes_slide_portion_request()
        request.paragraph_index = self.get_invalid_test_value('delete_notes_slide_portion', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_notes_slide_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_notes_slide_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portion', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portion', 'paragraph_index')

    def test_delete_notes_slide_portion_invalid_portion_index(self):
        """Test case for delete_notes_slide_portion with invalid portion_index
        """
        request = self.__prepare_delete_notes_slide_portion_request()
        request.portion_index = self.get_invalid_test_value('delete_notes_slide_portion', 'portion_index', request.portion_index, 'int')
        self.initialize('delete_notes_slide_portion', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.delete_notes_slide_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portion', 'portion_index', request.portion_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portion', 'portion_index')

    def test_delete_notes_slide_portion_invalid_password(self):
        """Test case for delete_notes_slide_portion with invalid password
        """
        request = self.__prepare_delete_notes_slide_portion_request()
        request.password = self.get_invalid_test_value('delete_notes_slide_portion', 'password', request.password, 'str')
        self.initialize('delete_notes_slide_portion', 'password', request.password)
        ok = False
        try:
            self.api.delete_notes_slide_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portion', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portion', 'password')

    def test_delete_notes_slide_portion_invalid_folder(self):
        """Test case for delete_notes_slide_portion with invalid folder
        """
        request = self.__prepare_delete_notes_slide_portion_request()
        request.folder = self.get_invalid_test_value('delete_notes_slide_portion', 'folder', request.folder, 'str')
        self.initialize('delete_notes_slide_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_notes_slide_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portion', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portion', 'folder')

    def test_delete_notes_slide_portion_invalid_storage(self):
        """Test case for delete_notes_slide_portion with invalid storage
        """
        request = self.__prepare_delete_notes_slide_portion_request()
        request.storage = self.get_invalid_test_value('delete_notes_slide_portion', 'storage', request.storage, 'str')
        self.initialize('delete_notes_slide_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_notes_slide_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portion', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portion', 'storage')

    def __prepare_delete_notes_slide_portion_request(self):
        name = self.get_test_value('delete_notes_slide_portion', 'name', 'str')
        slide_index = self.get_test_value('delete_notes_slide_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_notes_slide_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_notes_slide_portion', 'paragraph_index', 'int')
        portion_index = self.get_test_value('delete_notes_slide_portion', 'portion_index', 'int')
        password = self.get_test_value('delete_notes_slide_portion', 'password', 'str')
        folder = self.get_test_value('delete_notes_slide_portion', 'folder', 'str')
        storage = self.get_test_value('delete_notes_slide_portion', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteNotesSlidePortionRequest(name, slide_index, shape_index, paragraph_index, portion_index, password, folder, storage)

    def test_delete_notes_slide_portions(self):
        """Test case for delete_notes_slide_portions
        """
        request = self.__prepare_delete_notes_slide_portions_request()
        self.initialize('delete_notes_slide_portions', None, None)
        response = self.api.delete_notes_slide_portions(request)
        self.assertIsNotNone(response)

    def test_delete_notes_slide_portions_invalid_name(self):
        """Test case for delete_notes_slide_portions with invalid name
        """
        request = self.__prepare_delete_notes_slide_portions_request()
        request.name = self.get_invalid_test_value('delete_notes_slide_portions', 'name', request.name, 'str')
        self.initialize('delete_notes_slide_portions', 'name', request.name)
        ok = False
        try:
            self.api.delete_notes_slide_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portions', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portions', 'name')

    def test_delete_notes_slide_portions_invalid_slide_index(self):
        """Test case for delete_notes_slide_portions with invalid slide_index
        """
        request = self.__prepare_delete_notes_slide_portions_request()
        request.slide_index = self.get_invalid_test_value('delete_notes_slide_portions', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_notes_slide_portions', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_notes_slide_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portions', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portions', 'slide_index')

    def test_delete_notes_slide_portions_invalid_shape_index(self):
        """Test case for delete_notes_slide_portions with invalid shape_index
        """
        request = self.__prepare_delete_notes_slide_portions_request()
        request.shape_index = self.get_invalid_test_value('delete_notes_slide_portions', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_notes_slide_portions', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_notes_slide_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portions', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portions', 'shape_index')

    def test_delete_notes_slide_portions_invalid_paragraph_index(self):
        """Test case for delete_notes_slide_portions with invalid paragraph_index
        """
        request = self.__prepare_delete_notes_slide_portions_request()
        request.paragraph_index = self.get_invalid_test_value('delete_notes_slide_portions', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_notes_slide_portions', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_notes_slide_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portions', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portions', 'paragraph_index')

    def test_delete_notes_slide_portions_invalid_portions(self):
        """Test case for delete_notes_slide_portions with invalid portions
        """
        request = self.__prepare_delete_notes_slide_portions_request()
        request.portions = self.get_invalid_test_value('delete_notes_slide_portions', 'portions', request.portions, 'list[int]')
        self.initialize('delete_notes_slide_portions', 'portions', request.portions)
        ok = False
        try:
            self.api.delete_notes_slide_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portions', 'portions', request.portions)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portions', 'portions')

    def test_delete_notes_slide_portions_invalid_password(self):
        """Test case for delete_notes_slide_portions with invalid password
        """
        request = self.__prepare_delete_notes_slide_portions_request()
        request.password = self.get_invalid_test_value('delete_notes_slide_portions', 'password', request.password, 'str')
        self.initialize('delete_notes_slide_portions', 'password', request.password)
        ok = False
        try:
            self.api.delete_notes_slide_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portions', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portions', 'password')

    def test_delete_notes_slide_portions_invalid_folder(self):
        """Test case for delete_notes_slide_portions with invalid folder
        """
        request = self.__prepare_delete_notes_slide_portions_request()
        request.folder = self.get_invalid_test_value('delete_notes_slide_portions', 'folder', request.folder, 'str')
        self.initialize('delete_notes_slide_portions', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_notes_slide_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portions', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portions', 'folder')

    def test_delete_notes_slide_portions_invalid_storage(self):
        """Test case for delete_notes_slide_portions with invalid storage
        """
        request = self.__prepare_delete_notes_slide_portions_request()
        request.storage = self.get_invalid_test_value('delete_notes_slide_portions', 'storage', request.storage, 'str')
        self.initialize('delete_notes_slide_portions', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_notes_slide_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_portions', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_portions', 'storage')

    def __prepare_delete_notes_slide_portions_request(self):
        name = self.get_test_value('delete_notes_slide_portions', 'name', 'str')
        slide_index = self.get_test_value('delete_notes_slide_portions', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_notes_slide_portions', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_notes_slide_portions', 'paragraph_index', 'int')
        portions = self.get_test_value('delete_notes_slide_portions', 'portions', 'list[int]')
        password = self.get_test_value('delete_notes_slide_portions', 'password', 'str')
        folder = self.get_test_value('delete_notes_slide_portions', 'folder', 'str')
        storage = self.get_test_value('delete_notes_slide_portions', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteNotesSlidePortionsRequest(name, slide_index, shape_index, paragraph_index, portions, password, folder, storage)

    def test_delete_notes_slide_shape(self):
        """Test case for delete_notes_slide_shape
        """
        request = self.__prepare_delete_notes_slide_shape_request()
        self.initialize('delete_notes_slide_shape', None, None)
        response = self.api.delete_notes_slide_shape(request)
        self.assertIsNotNone(response)

    def test_delete_notes_slide_shape_invalid_name(self):
        """Test case for delete_notes_slide_shape with invalid name
        """
        request = self.__prepare_delete_notes_slide_shape_request()
        request.name = self.get_invalid_test_value('delete_notes_slide_shape', 'name', request.name, 'str')
        self.initialize('delete_notes_slide_shape', 'name', request.name)
        ok = False
        try:
            self.api.delete_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shape', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shape', 'name')

    def test_delete_notes_slide_shape_invalid_slide_index(self):
        """Test case for delete_notes_slide_shape with invalid slide_index
        """
        request = self.__prepare_delete_notes_slide_shape_request()
        request.slide_index = self.get_invalid_test_value('delete_notes_slide_shape', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_notes_slide_shape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shape', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shape', 'slide_index')

    def test_delete_notes_slide_shape_invalid_shape_index(self):
        """Test case for delete_notes_slide_shape with invalid shape_index
        """
        request = self.__prepare_delete_notes_slide_shape_request()
        request.shape_index = self.get_invalid_test_value('delete_notes_slide_shape', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_notes_slide_shape', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shape', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shape', 'shape_index')

    def test_delete_notes_slide_shape_invalid_password(self):
        """Test case for delete_notes_slide_shape with invalid password
        """
        request = self.__prepare_delete_notes_slide_shape_request()
        request.password = self.get_invalid_test_value('delete_notes_slide_shape', 'password', request.password, 'str')
        self.initialize('delete_notes_slide_shape', 'password', request.password)
        ok = False
        try:
            self.api.delete_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shape', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shape', 'password')

    def test_delete_notes_slide_shape_invalid_folder(self):
        """Test case for delete_notes_slide_shape with invalid folder
        """
        request = self.__prepare_delete_notes_slide_shape_request()
        request.folder = self.get_invalid_test_value('delete_notes_slide_shape', 'folder', request.folder, 'str')
        self.initialize('delete_notes_slide_shape', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shape', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shape', 'folder')

    def test_delete_notes_slide_shape_invalid_storage(self):
        """Test case for delete_notes_slide_shape with invalid storage
        """
        request = self.__prepare_delete_notes_slide_shape_request()
        request.storage = self.get_invalid_test_value('delete_notes_slide_shape', 'storage', request.storage, 'str')
        self.initialize('delete_notes_slide_shape', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shape', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shape', 'storage')

    def __prepare_delete_notes_slide_shape_request(self):
        name = self.get_test_value('delete_notes_slide_shape', 'name', 'str')
        slide_index = self.get_test_value('delete_notes_slide_shape', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_notes_slide_shape', 'shape_index', 'int')
        password = self.get_test_value('delete_notes_slide_shape', 'password', 'str')
        folder = self.get_test_value('delete_notes_slide_shape', 'folder', 'str')
        storage = self.get_test_value('delete_notes_slide_shape', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteNotesSlideShapeRequest(name, slide_index, shape_index, password, folder, storage)

    def test_delete_notes_slide_shapes(self):
        """Test case for delete_notes_slide_shapes
        """
        request = self.__prepare_delete_notes_slide_shapes_request()
        self.initialize('delete_notes_slide_shapes', None, None)
        response = self.api.delete_notes_slide_shapes(request)
        self.assertIsNotNone(response)

    def test_delete_notes_slide_shapes_invalid_name(self):
        """Test case for delete_notes_slide_shapes with invalid name
        """
        request = self.__prepare_delete_notes_slide_shapes_request()
        request.name = self.get_invalid_test_value('delete_notes_slide_shapes', 'name', request.name, 'str')
        self.initialize('delete_notes_slide_shapes', 'name', request.name)
        ok = False
        try:
            self.api.delete_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shapes', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shapes', 'name')

    def test_delete_notes_slide_shapes_invalid_slide_index(self):
        """Test case for delete_notes_slide_shapes with invalid slide_index
        """
        request = self.__prepare_delete_notes_slide_shapes_request()
        request.slide_index = self.get_invalid_test_value('delete_notes_slide_shapes', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_notes_slide_shapes', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shapes', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shapes', 'slide_index')

    def test_delete_notes_slide_shapes_invalid_shapes(self):
        """Test case for delete_notes_slide_shapes with invalid shapes
        """
        request = self.__prepare_delete_notes_slide_shapes_request()
        request.shapes = self.get_invalid_test_value('delete_notes_slide_shapes', 'shapes', request.shapes, 'list[int]')
        self.initialize('delete_notes_slide_shapes', 'shapes', request.shapes)
        ok = False
        try:
            self.api.delete_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shapes', 'shapes', request.shapes)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shapes', 'shapes')

    def test_delete_notes_slide_shapes_invalid_password(self):
        """Test case for delete_notes_slide_shapes with invalid password
        """
        request = self.__prepare_delete_notes_slide_shapes_request()
        request.password = self.get_invalid_test_value('delete_notes_slide_shapes', 'password', request.password, 'str')
        self.initialize('delete_notes_slide_shapes', 'password', request.password)
        ok = False
        try:
            self.api.delete_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shapes', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shapes', 'password')

    def test_delete_notes_slide_shapes_invalid_folder(self):
        """Test case for delete_notes_slide_shapes with invalid folder
        """
        request = self.__prepare_delete_notes_slide_shapes_request()
        request.folder = self.get_invalid_test_value('delete_notes_slide_shapes', 'folder', request.folder, 'str')
        self.initialize('delete_notes_slide_shapes', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shapes', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shapes', 'folder')

    def test_delete_notes_slide_shapes_invalid_storage(self):
        """Test case for delete_notes_slide_shapes with invalid storage
        """
        request = self.__prepare_delete_notes_slide_shapes_request()
        request.storage = self.get_invalid_test_value('delete_notes_slide_shapes', 'storage', request.storage, 'str')
        self.initialize('delete_notes_slide_shapes', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_notes_slide_shapes', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_notes_slide_shapes', 'storage')

    def __prepare_delete_notes_slide_shapes_request(self):
        name = self.get_test_value('delete_notes_slide_shapes', 'name', 'str')
        slide_index = self.get_test_value('delete_notes_slide_shapes', 'slide_index', 'int')
        shapes = self.get_test_value('delete_notes_slide_shapes', 'shapes', 'list[int]')
        password = self.get_test_value('delete_notes_slide_shapes', 'password', 'str')
        folder = self.get_test_value('delete_notes_slide_shapes', 'folder', 'str')
        storage = self.get_test_value('delete_notes_slide_shapes', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteNotesSlideShapesRequest(name, slide_index, shapes, password, folder, storage)

    def test_delete_paragraph(self):
        """Test case for delete_paragraph
        """
        request = self.__prepare_delete_paragraph_request()
        self.initialize('delete_paragraph', None, None)
        response = self.api.delete_paragraph(request)
        self.assertIsNotNone(response)

    def test_delete_paragraph_invalid_name(self):
        """Test case for delete_paragraph with invalid name
        """
        request = self.__prepare_delete_paragraph_request()
        request.name = self.get_invalid_test_value('delete_paragraph', 'name', request.name, 'str')
        self.initialize('delete_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraph', 'name')

    def test_delete_paragraph_invalid_slide_index(self):
        """Test case for delete_paragraph with invalid slide_index
        """
        request = self.__prepare_delete_paragraph_request()
        request.slide_index = self.get_invalid_test_value('delete_paragraph', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraph', 'slide_index')

    def test_delete_paragraph_invalid_shape_index(self):
        """Test case for delete_paragraph with invalid shape_index
        """
        request = self.__prepare_delete_paragraph_request()
        request.shape_index = self.get_invalid_test_value('delete_paragraph', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraph', 'shape_index')

    def test_delete_paragraph_invalid_paragraph_index(self):
        """Test case for delete_paragraph with invalid paragraph_index
        """
        request = self.__prepare_delete_paragraph_request()
        request.paragraph_index = self.get_invalid_test_value('delete_paragraph', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_paragraph', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraph', 'paragraph_index')

    def test_delete_paragraph_invalid_password(self):
        """Test case for delete_paragraph with invalid password
        """
        request = self.__prepare_delete_paragraph_request()
        request.password = self.get_invalid_test_value('delete_paragraph', 'password', request.password, 'str')
        self.initialize('delete_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraph', 'password')

    def test_delete_paragraph_invalid_folder(self):
        """Test case for delete_paragraph with invalid folder
        """
        request = self.__prepare_delete_paragraph_request()
        request.folder = self.get_invalid_test_value('delete_paragraph', 'folder', request.folder, 'str')
        self.initialize('delete_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraph', 'folder')

    def test_delete_paragraph_invalid_storage(self):
        """Test case for delete_paragraph with invalid storage
        """
        request = self.__prepare_delete_paragraph_request()
        request.storage = self.get_invalid_test_value('delete_paragraph', 'storage', request.storage, 'str')
        self.initialize('delete_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraph', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraph', 'storage')

    def __prepare_delete_paragraph_request(self):
        name = self.get_test_value('delete_paragraph', 'name', 'str')
        slide_index = self.get_test_value('delete_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_paragraph', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_paragraph', 'paragraph_index', 'int')
        password = self.get_test_value('delete_paragraph', 'password', 'str')
        folder = self.get_test_value('delete_paragraph', 'folder', 'str')
        storage = self.get_test_value('delete_paragraph', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteParagraphRequest(name, slide_index, shape_index, paragraph_index, password, folder, storage)

    def test_delete_paragraphs(self):
        """Test case for delete_paragraphs
        """
        request = self.__prepare_delete_paragraphs_request()
        self.initialize('delete_paragraphs', None, None)
        response = self.api.delete_paragraphs(request)
        self.assertIsNotNone(response)

    def test_delete_paragraphs_invalid_name(self):
        """Test case for delete_paragraphs with invalid name
        """
        request = self.__prepare_delete_paragraphs_request()
        request.name = self.get_invalid_test_value('delete_paragraphs', 'name', request.name, 'str')
        self.initialize('delete_paragraphs', 'name', request.name)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraphs', 'name')

    def test_delete_paragraphs_invalid_slide_index(self):
        """Test case for delete_paragraphs with invalid slide_index
        """
        request = self.__prepare_delete_paragraphs_request()
        request.slide_index = self.get_invalid_test_value('delete_paragraphs', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_paragraphs', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraphs', 'slide_index')

    def test_delete_paragraphs_invalid_shape_index(self):
        """Test case for delete_paragraphs with invalid shape_index
        """
        request = self.__prepare_delete_paragraphs_request()
        request.shape_index = self.get_invalid_test_value('delete_paragraphs', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_paragraphs', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraphs', 'shape_index')

    def test_delete_paragraphs_invalid_paragraphs(self):
        """Test case for delete_paragraphs with invalid paragraphs
        """
        request = self.__prepare_delete_paragraphs_request()
        request.paragraphs = self.get_invalid_test_value('delete_paragraphs', 'paragraphs', request.paragraphs, 'list[int]')
        self.initialize('delete_paragraphs', 'paragraphs', request.paragraphs)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'paragraphs', request.paragraphs)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraphs', 'paragraphs')

    def test_delete_paragraphs_invalid_password(self):
        """Test case for delete_paragraphs with invalid password
        """
        request = self.__prepare_delete_paragraphs_request()
        request.password = self.get_invalid_test_value('delete_paragraphs', 'password', request.password, 'str')
        self.initialize('delete_paragraphs', 'password', request.password)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraphs', 'password')

    def test_delete_paragraphs_invalid_folder(self):
        """Test case for delete_paragraphs with invalid folder
        """
        request = self.__prepare_delete_paragraphs_request()
        request.folder = self.get_invalid_test_value('delete_paragraphs', 'folder', request.folder, 'str')
        self.initialize('delete_paragraphs', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraphs', 'folder')

    def test_delete_paragraphs_invalid_storage(self):
        """Test case for delete_paragraphs with invalid storage
        """
        request = self.__prepare_delete_paragraphs_request()
        request.storage = self.get_invalid_test_value('delete_paragraphs', 'storage', request.storage, 'str')
        self.initialize('delete_paragraphs', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_paragraphs', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_paragraphs', 'storage')

    def __prepare_delete_paragraphs_request(self):
        name = self.get_test_value('delete_paragraphs', 'name', 'str')
        slide_index = self.get_test_value('delete_paragraphs', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_paragraphs', 'shape_index', 'int')
        paragraphs = self.get_test_value('delete_paragraphs', 'paragraphs', 'list[int]')
        password = self.get_test_value('delete_paragraphs', 'password', 'str')
        folder = self.get_test_value('delete_paragraphs', 'folder', 'str')
        storage = self.get_test_value('delete_paragraphs', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteParagraphsRequest(name, slide_index, shape_index, paragraphs, password, folder, storage)

    def test_delete_portion(self):
        """Test case for delete_portion
        """
        request = self.__prepare_delete_portion_request()
        self.initialize('delete_portion', None, None)
        response = self.api.delete_portion(request)
        self.assertIsNotNone(response)

    def test_delete_portion_invalid_name(self):
        """Test case for delete_portion with invalid name
        """
        request = self.__prepare_delete_portion_request()
        request.name = self.get_invalid_test_value('delete_portion', 'name', request.name, 'str')
        self.initialize('delete_portion', 'name', request.name)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portion', 'name')

    def test_delete_portion_invalid_slide_index(self):
        """Test case for delete_portion with invalid slide_index
        """
        request = self.__prepare_delete_portion_request()
        request.slide_index = self.get_invalid_test_value('delete_portion', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portion', 'slide_index')

    def test_delete_portion_invalid_shape_index(self):
        """Test case for delete_portion with invalid shape_index
        """
        request = self.__prepare_delete_portion_request()
        request.shape_index = self.get_invalid_test_value('delete_portion', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portion', 'shape_index')

    def test_delete_portion_invalid_paragraph_index(self):
        """Test case for delete_portion with invalid paragraph_index
        """
        request = self.__prepare_delete_portion_request()
        request.paragraph_index = self.get_invalid_test_value('delete_portion', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portion', 'paragraph_index')

    def test_delete_portion_invalid_portion_index(self):
        """Test case for delete_portion with invalid portion_index
        """
        request = self.__prepare_delete_portion_request()
        request.portion_index = self.get_invalid_test_value('delete_portion', 'portion_index', request.portion_index, 'int')
        self.initialize('delete_portion', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'portion_index', request.portion_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portion', 'portion_index')

    def test_delete_portion_invalid_password(self):
        """Test case for delete_portion with invalid password
        """
        request = self.__prepare_delete_portion_request()
        request.password = self.get_invalid_test_value('delete_portion', 'password', request.password, 'str')
        self.initialize('delete_portion', 'password', request.password)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portion', 'password')

    def test_delete_portion_invalid_folder(self):
        """Test case for delete_portion with invalid folder
        """
        request = self.__prepare_delete_portion_request()
        request.folder = self.get_invalid_test_value('delete_portion', 'folder', request.folder, 'str')
        self.initialize('delete_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portion', 'folder')

    def test_delete_portion_invalid_storage(self):
        """Test case for delete_portion with invalid storage
        """
        request = self.__prepare_delete_portion_request()
        request.storage = self.get_invalid_test_value('delete_portion', 'storage', request.storage, 'str')
        self.initialize('delete_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portion', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portion', 'storage')

    def __prepare_delete_portion_request(self):
        name = self.get_test_value('delete_portion', 'name', 'str')
        slide_index = self.get_test_value('delete_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_portion', 'paragraph_index', 'int')
        portion_index = self.get_test_value('delete_portion', 'portion_index', 'int')
        password = self.get_test_value('delete_portion', 'password', 'str')
        folder = self.get_test_value('delete_portion', 'folder', 'str')
        storage = self.get_test_value('delete_portion', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeletePortionRequest(name, slide_index, shape_index, paragraph_index, portion_index, password, folder, storage)

    def test_delete_portions(self):
        """Test case for delete_portions
        """
        request = self.__prepare_delete_portions_request()
        self.initialize('delete_portions', None, None)
        response = self.api.delete_portions(request)
        self.assertIsNotNone(response)

    def test_delete_portions_invalid_name(self):
        """Test case for delete_portions with invalid name
        """
        request = self.__prepare_delete_portions_request()
        request.name = self.get_invalid_test_value('delete_portions', 'name', request.name, 'str')
        self.initialize('delete_portions', 'name', request.name)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portions', 'name')

    def test_delete_portions_invalid_slide_index(self):
        """Test case for delete_portions with invalid slide_index
        """
        request = self.__prepare_delete_portions_request()
        request.slide_index = self.get_invalid_test_value('delete_portions', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_portions', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portions', 'slide_index')

    def test_delete_portions_invalid_shape_index(self):
        """Test case for delete_portions with invalid shape_index
        """
        request = self.__prepare_delete_portions_request()
        request.shape_index = self.get_invalid_test_value('delete_portions', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_portions', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portions', 'shape_index')

    def test_delete_portions_invalid_paragraph_index(self):
        """Test case for delete_portions with invalid paragraph_index
        """
        request = self.__prepare_delete_portions_request()
        request.paragraph_index = self.get_invalid_test_value('delete_portions', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_portions', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portions', 'paragraph_index')

    def test_delete_portions_invalid_portions(self):
        """Test case for delete_portions with invalid portions
        """
        request = self.__prepare_delete_portions_request()
        request.portions = self.get_invalid_test_value('delete_portions', 'portions', request.portions, 'list[int]')
        self.initialize('delete_portions', 'portions', request.portions)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'portions', request.portions)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portions', 'portions')

    def test_delete_portions_invalid_password(self):
        """Test case for delete_portions with invalid password
        """
        request = self.__prepare_delete_portions_request()
        request.password = self.get_invalid_test_value('delete_portions', 'password', request.password, 'str')
        self.initialize('delete_portions', 'password', request.password)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portions', 'password')

    def test_delete_portions_invalid_folder(self):
        """Test case for delete_portions with invalid folder
        """
        request = self.__prepare_delete_portions_request()
        request.folder = self.get_invalid_test_value('delete_portions', 'folder', request.folder, 'str')
        self.initialize('delete_portions', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portions', 'folder')

    def test_delete_portions_invalid_storage(self):
        """Test case for delete_portions with invalid storage
        """
        request = self.__prepare_delete_portions_request()
        request.storage = self.get_invalid_test_value('delete_portions', 'storage', request.storage, 'str')
        self.initialize('delete_portions', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_portions', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_portions', 'storage')

    def __prepare_delete_portions_request(self):
        name = self.get_test_value('delete_portions', 'name', 'str')
        slide_index = self.get_test_value('delete_portions', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_portions', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_portions', 'paragraph_index', 'int')
        portions = self.get_test_value('delete_portions', 'portions', 'list[int]')
        password = self.get_test_value('delete_portions', 'password', 'str')
        folder = self.get_test_value('delete_portions', 'folder', 'str')
        storage = self.get_test_value('delete_portions', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeletePortionsRequest(name, slide_index, shape_index, paragraph_index, portions, password, folder, storage)

    def test_delete_slide_animation(self):
        """Test case for delete_slide_animation
        """
        request = self.__prepare_delete_slide_animation_request()
        self.initialize('delete_slide_animation', None, None)
        response = self.api.delete_slide_animation(request)
        self.assertIsNotNone(response)

    def test_delete_slide_animation_invalid_name(self):
        """Test case for delete_slide_animation with invalid name
        """
        request = self.__prepare_delete_slide_animation_request()
        request.name = self.get_invalid_test_value('delete_slide_animation', 'name', request.name, 'str')
        self.initialize('delete_slide_animation', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation', 'name')

    def test_delete_slide_animation_invalid_slide_index(self):
        """Test case for delete_slide_animation with invalid slide_index
        """
        request = self.__prepare_delete_slide_animation_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_animation', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_animation', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation', 'slide_index')

    def test_delete_slide_animation_invalid_password(self):
        """Test case for delete_slide_animation with invalid password
        """
        request = self.__prepare_delete_slide_animation_request()
        request.password = self.get_invalid_test_value('delete_slide_animation', 'password', request.password, 'str')
        self.initialize('delete_slide_animation', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation', 'password')

    def test_delete_slide_animation_invalid_folder(self):
        """Test case for delete_slide_animation with invalid folder
        """
        request = self.__prepare_delete_slide_animation_request()
        request.folder = self.get_invalid_test_value('delete_slide_animation', 'folder', request.folder, 'str')
        self.initialize('delete_slide_animation', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation', 'folder')

    def test_delete_slide_animation_invalid_storage(self):
        """Test case for delete_slide_animation with invalid storage
        """
        request = self.__prepare_delete_slide_animation_request()
        request.storage = self.get_invalid_test_value('delete_slide_animation', 'storage', request.storage, 'str')
        self.initialize('delete_slide_animation', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation', 'storage')

    def __prepare_delete_slide_animation_request(self):
        name = self.get_test_value('delete_slide_animation', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_animation', 'slide_index', 'int')
        password = self.get_test_value('delete_slide_animation', 'password', 'str')
        folder = self.get_test_value('delete_slide_animation', 'folder', 'str')
        storage = self.get_test_value('delete_slide_animation', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideAnimationRequest(name, slide_index, password, folder, storage)

    def test_delete_slide_animation_effect(self):
        """Test case for delete_slide_animation_effect
        """
        request = self.__prepare_delete_slide_animation_effect_request()
        self.initialize('delete_slide_animation_effect', None, None)
        response = self.api.delete_slide_animation_effect(request)
        self.assertIsNotNone(response)

    def test_delete_slide_animation_effect_invalid_name(self):
        """Test case for delete_slide_animation_effect with invalid name
        """
        request = self.__prepare_delete_slide_animation_effect_request()
        request.name = self.get_invalid_test_value('delete_slide_animation_effect', 'name', request.name, 'str')
        self.initialize('delete_slide_animation_effect', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_effect', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_effect', 'name')

    def test_delete_slide_animation_effect_invalid_slide_index(self):
        """Test case for delete_slide_animation_effect with invalid slide_index
        """
        request = self.__prepare_delete_slide_animation_effect_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_animation_effect', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_animation_effect', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_effect', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_effect', 'slide_index')

    def test_delete_slide_animation_effect_invalid_effect_index(self):
        """Test case for delete_slide_animation_effect with invalid effect_index
        """
        request = self.__prepare_delete_slide_animation_effect_request()
        request.effect_index = self.get_invalid_test_value('delete_slide_animation_effect', 'effect_index', request.effect_index, 'int')
        self.initialize('delete_slide_animation_effect', 'effect_index', request.effect_index)
        ok = False
        try:
            self.api.delete_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_effect', 'effect_index', request.effect_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_effect', 'effect_index')

    def test_delete_slide_animation_effect_invalid_password(self):
        """Test case for delete_slide_animation_effect with invalid password
        """
        request = self.__prepare_delete_slide_animation_effect_request()
        request.password = self.get_invalid_test_value('delete_slide_animation_effect', 'password', request.password, 'str')
        self.initialize('delete_slide_animation_effect', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_effect', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_effect', 'password')

    def test_delete_slide_animation_effect_invalid_folder(self):
        """Test case for delete_slide_animation_effect with invalid folder
        """
        request = self.__prepare_delete_slide_animation_effect_request()
        request.folder = self.get_invalid_test_value('delete_slide_animation_effect', 'folder', request.folder, 'str')
        self.initialize('delete_slide_animation_effect', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_effect', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_effect', 'folder')

    def test_delete_slide_animation_effect_invalid_storage(self):
        """Test case for delete_slide_animation_effect with invalid storage
        """
        request = self.__prepare_delete_slide_animation_effect_request()
        request.storage = self.get_invalid_test_value('delete_slide_animation_effect', 'storage', request.storage, 'str')
        self.initialize('delete_slide_animation_effect', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_effect', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_effect', 'storage')

    def __prepare_delete_slide_animation_effect_request(self):
        name = self.get_test_value('delete_slide_animation_effect', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_animation_effect', 'slide_index', 'int')
        effect_index = self.get_test_value('delete_slide_animation_effect', 'effect_index', 'int')
        password = self.get_test_value('delete_slide_animation_effect', 'password', 'str')
        folder = self.get_test_value('delete_slide_animation_effect', 'folder', 'str')
        storage = self.get_test_value('delete_slide_animation_effect', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideAnimationEffectRequest(name, slide_index, effect_index, password, folder, storage)

    def test_delete_slide_animation_interactive_sequence(self):
        """Test case for delete_slide_animation_interactive_sequence
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_request()
        self.initialize('delete_slide_animation_interactive_sequence', None, None)
        response = self.api.delete_slide_animation_interactive_sequence(request)
        self.assertIsNotNone(response)

    def test_delete_slide_animation_interactive_sequence_invalid_name(self):
        """Test case for delete_slide_animation_interactive_sequence with invalid name
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_request()
        request.name = self.get_invalid_test_value('delete_slide_animation_interactive_sequence', 'name', request.name, 'str')
        self.initialize('delete_slide_animation_interactive_sequence', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence', 'name')

    def test_delete_slide_animation_interactive_sequence_invalid_slide_index(self):
        """Test case for delete_slide_animation_interactive_sequence with invalid slide_index
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_animation_interactive_sequence', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_animation_interactive_sequence', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence', 'slide_index')

    def test_delete_slide_animation_interactive_sequence_invalid_sequence_index(self):
        """Test case for delete_slide_animation_interactive_sequence with invalid sequence_index
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_request()
        request.sequence_index = self.get_invalid_test_value('delete_slide_animation_interactive_sequence', 'sequence_index', request.sequence_index, 'int')
        self.initialize('delete_slide_animation_interactive_sequence', 'sequence_index', request.sequence_index)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence', 'sequence_index', request.sequence_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence', 'sequence_index')

    def test_delete_slide_animation_interactive_sequence_invalid_password(self):
        """Test case for delete_slide_animation_interactive_sequence with invalid password
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_request()
        request.password = self.get_invalid_test_value('delete_slide_animation_interactive_sequence', 'password', request.password, 'str')
        self.initialize('delete_slide_animation_interactive_sequence', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence', 'password')

    def test_delete_slide_animation_interactive_sequence_invalid_folder(self):
        """Test case for delete_slide_animation_interactive_sequence with invalid folder
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_request()
        request.folder = self.get_invalid_test_value('delete_slide_animation_interactive_sequence', 'folder', request.folder, 'str')
        self.initialize('delete_slide_animation_interactive_sequence', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence', 'folder')

    def test_delete_slide_animation_interactive_sequence_invalid_storage(self):
        """Test case for delete_slide_animation_interactive_sequence with invalid storage
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_request()
        request.storage = self.get_invalid_test_value('delete_slide_animation_interactive_sequence', 'storage', request.storage, 'str')
        self.initialize('delete_slide_animation_interactive_sequence', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence', 'storage')

    def __prepare_delete_slide_animation_interactive_sequence_request(self):
        name = self.get_test_value('delete_slide_animation_interactive_sequence', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_animation_interactive_sequence', 'slide_index', 'int')
        sequence_index = self.get_test_value('delete_slide_animation_interactive_sequence', 'sequence_index', 'int')
        password = self.get_test_value('delete_slide_animation_interactive_sequence', 'password', 'str')
        folder = self.get_test_value('delete_slide_animation_interactive_sequence', 'folder', 'str')
        storage = self.get_test_value('delete_slide_animation_interactive_sequence', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideAnimationInteractiveSequenceRequest(name, slide_index, sequence_index, password, folder, storage)

    def test_delete_slide_animation_interactive_sequence_effect(self):
        """Test case for delete_slide_animation_interactive_sequence_effect
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_effect_request()
        self.initialize('delete_slide_animation_interactive_sequence_effect', None, None)
        response = self.api.delete_slide_animation_interactive_sequence_effect(request)
        self.assertIsNotNone(response)

    def test_delete_slide_animation_interactive_sequence_effect_invalid_name(self):
        """Test case for delete_slide_animation_interactive_sequence_effect with invalid name
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_effect_request()
        request.name = self.get_invalid_test_value('delete_slide_animation_interactive_sequence_effect', 'name', request.name, 'str')
        self.initialize('delete_slide_animation_interactive_sequence_effect', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence_effect', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence_effect', 'name')

    def test_delete_slide_animation_interactive_sequence_effect_invalid_slide_index(self):
        """Test case for delete_slide_animation_interactive_sequence_effect with invalid slide_index
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_effect_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_animation_interactive_sequence_effect', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_animation_interactive_sequence_effect', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence_effect', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence_effect', 'slide_index')

    def test_delete_slide_animation_interactive_sequence_effect_invalid_sequence_index(self):
        """Test case for delete_slide_animation_interactive_sequence_effect with invalid sequence_index
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_effect_request()
        request.sequence_index = self.get_invalid_test_value('delete_slide_animation_interactive_sequence_effect', 'sequence_index', request.sequence_index, 'int')
        self.initialize('delete_slide_animation_interactive_sequence_effect', 'sequence_index', request.sequence_index)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence_effect', 'sequence_index', request.sequence_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence_effect', 'sequence_index')

    def test_delete_slide_animation_interactive_sequence_effect_invalid_effect_index(self):
        """Test case for delete_slide_animation_interactive_sequence_effect with invalid effect_index
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_effect_request()
        request.effect_index = self.get_invalid_test_value('delete_slide_animation_interactive_sequence_effect', 'effect_index', request.effect_index, 'int')
        self.initialize('delete_slide_animation_interactive_sequence_effect', 'effect_index', request.effect_index)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence_effect', 'effect_index', request.effect_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence_effect', 'effect_index')

    def test_delete_slide_animation_interactive_sequence_effect_invalid_password(self):
        """Test case for delete_slide_animation_interactive_sequence_effect with invalid password
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_effect_request()
        request.password = self.get_invalid_test_value('delete_slide_animation_interactive_sequence_effect', 'password', request.password, 'str')
        self.initialize('delete_slide_animation_interactive_sequence_effect', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence_effect', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence_effect', 'password')

    def test_delete_slide_animation_interactive_sequence_effect_invalid_folder(self):
        """Test case for delete_slide_animation_interactive_sequence_effect with invalid folder
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_effect_request()
        request.folder = self.get_invalid_test_value('delete_slide_animation_interactive_sequence_effect', 'folder', request.folder, 'str')
        self.initialize('delete_slide_animation_interactive_sequence_effect', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence_effect', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence_effect', 'folder')

    def test_delete_slide_animation_interactive_sequence_effect_invalid_storage(self):
        """Test case for delete_slide_animation_interactive_sequence_effect with invalid storage
        """
        request = self.__prepare_delete_slide_animation_interactive_sequence_effect_request()
        request.storage = self.get_invalid_test_value('delete_slide_animation_interactive_sequence_effect', 'storage', request.storage, 'str')
        self.initialize('delete_slide_animation_interactive_sequence_effect', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequence_effect', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequence_effect', 'storage')

    def __prepare_delete_slide_animation_interactive_sequence_effect_request(self):
        name = self.get_test_value('delete_slide_animation_interactive_sequence_effect', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_animation_interactive_sequence_effect', 'slide_index', 'int')
        sequence_index = self.get_test_value('delete_slide_animation_interactive_sequence_effect', 'sequence_index', 'int')
        effect_index = self.get_test_value('delete_slide_animation_interactive_sequence_effect', 'effect_index', 'int')
        password = self.get_test_value('delete_slide_animation_interactive_sequence_effect', 'password', 'str')
        folder = self.get_test_value('delete_slide_animation_interactive_sequence_effect', 'folder', 'str')
        storage = self.get_test_value('delete_slide_animation_interactive_sequence_effect', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideAnimationInteractiveSequenceEffectRequest(name, slide_index, sequence_index, effect_index, password, folder, storage)

    def test_delete_slide_animation_interactive_sequences(self):
        """Test case for delete_slide_animation_interactive_sequences
        """
        request = self.__prepare_delete_slide_animation_interactive_sequences_request()
        self.initialize('delete_slide_animation_interactive_sequences', None, None)
        response = self.api.delete_slide_animation_interactive_sequences(request)
        self.assertIsNotNone(response)

    def test_delete_slide_animation_interactive_sequences_invalid_name(self):
        """Test case for delete_slide_animation_interactive_sequences with invalid name
        """
        request = self.__prepare_delete_slide_animation_interactive_sequences_request()
        request.name = self.get_invalid_test_value('delete_slide_animation_interactive_sequences', 'name', request.name, 'str')
        self.initialize('delete_slide_animation_interactive_sequences', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequences(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequences', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequences', 'name')

    def test_delete_slide_animation_interactive_sequences_invalid_slide_index(self):
        """Test case for delete_slide_animation_interactive_sequences with invalid slide_index
        """
        request = self.__prepare_delete_slide_animation_interactive_sequences_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_animation_interactive_sequences', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_animation_interactive_sequences', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequences(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequences', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequences', 'slide_index')

    def test_delete_slide_animation_interactive_sequences_invalid_password(self):
        """Test case for delete_slide_animation_interactive_sequences with invalid password
        """
        request = self.__prepare_delete_slide_animation_interactive_sequences_request()
        request.password = self.get_invalid_test_value('delete_slide_animation_interactive_sequences', 'password', request.password, 'str')
        self.initialize('delete_slide_animation_interactive_sequences', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequences(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequences', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequences', 'password')

    def test_delete_slide_animation_interactive_sequences_invalid_folder(self):
        """Test case for delete_slide_animation_interactive_sequences with invalid folder
        """
        request = self.__prepare_delete_slide_animation_interactive_sequences_request()
        request.folder = self.get_invalid_test_value('delete_slide_animation_interactive_sequences', 'folder', request.folder, 'str')
        self.initialize('delete_slide_animation_interactive_sequences', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequences(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequences', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequences', 'folder')

    def test_delete_slide_animation_interactive_sequences_invalid_storage(self):
        """Test case for delete_slide_animation_interactive_sequences with invalid storage
        """
        request = self.__prepare_delete_slide_animation_interactive_sequences_request()
        request.storage = self.get_invalid_test_value('delete_slide_animation_interactive_sequences', 'storage', request.storage, 'str')
        self.initialize('delete_slide_animation_interactive_sequences', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_animation_interactive_sequences(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_interactive_sequences', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_interactive_sequences', 'storage')

    def __prepare_delete_slide_animation_interactive_sequences_request(self):
        name = self.get_test_value('delete_slide_animation_interactive_sequences', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_animation_interactive_sequences', 'slide_index', 'int')
        password = self.get_test_value('delete_slide_animation_interactive_sequences', 'password', 'str')
        folder = self.get_test_value('delete_slide_animation_interactive_sequences', 'folder', 'str')
        storage = self.get_test_value('delete_slide_animation_interactive_sequences', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideAnimationInteractiveSequencesRequest(name, slide_index, password, folder, storage)

    def test_delete_slide_animation_main_sequence(self):
        """Test case for delete_slide_animation_main_sequence
        """
        request = self.__prepare_delete_slide_animation_main_sequence_request()
        self.initialize('delete_slide_animation_main_sequence', None, None)
        response = self.api.delete_slide_animation_main_sequence(request)
        self.assertIsNotNone(response)

    def test_delete_slide_animation_main_sequence_invalid_name(self):
        """Test case for delete_slide_animation_main_sequence with invalid name
        """
        request = self.__prepare_delete_slide_animation_main_sequence_request()
        request.name = self.get_invalid_test_value('delete_slide_animation_main_sequence', 'name', request.name, 'str')
        self.initialize('delete_slide_animation_main_sequence', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_animation_main_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_main_sequence', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_main_sequence', 'name')

    def test_delete_slide_animation_main_sequence_invalid_slide_index(self):
        """Test case for delete_slide_animation_main_sequence with invalid slide_index
        """
        request = self.__prepare_delete_slide_animation_main_sequence_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_animation_main_sequence', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_animation_main_sequence', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_animation_main_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_main_sequence', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_main_sequence', 'slide_index')

    def test_delete_slide_animation_main_sequence_invalid_password(self):
        """Test case for delete_slide_animation_main_sequence with invalid password
        """
        request = self.__prepare_delete_slide_animation_main_sequence_request()
        request.password = self.get_invalid_test_value('delete_slide_animation_main_sequence', 'password', request.password, 'str')
        self.initialize('delete_slide_animation_main_sequence', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_animation_main_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_main_sequence', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_main_sequence', 'password')

    def test_delete_slide_animation_main_sequence_invalid_folder(self):
        """Test case for delete_slide_animation_main_sequence with invalid folder
        """
        request = self.__prepare_delete_slide_animation_main_sequence_request()
        request.folder = self.get_invalid_test_value('delete_slide_animation_main_sequence', 'folder', request.folder, 'str')
        self.initialize('delete_slide_animation_main_sequence', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_animation_main_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_main_sequence', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_main_sequence', 'folder')

    def test_delete_slide_animation_main_sequence_invalid_storage(self):
        """Test case for delete_slide_animation_main_sequence with invalid storage
        """
        request = self.__prepare_delete_slide_animation_main_sequence_request()
        request.storage = self.get_invalid_test_value('delete_slide_animation_main_sequence', 'storage', request.storage, 'str')
        self.initialize('delete_slide_animation_main_sequence', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_animation_main_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_animation_main_sequence', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_animation_main_sequence', 'storage')

    def __prepare_delete_slide_animation_main_sequence_request(self):
        name = self.get_test_value('delete_slide_animation_main_sequence', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_animation_main_sequence', 'slide_index', 'int')
        password = self.get_test_value('delete_slide_animation_main_sequence', 'password', 'str')
        folder = self.get_test_value('delete_slide_animation_main_sequence', 'folder', 'str')
        storage = self.get_test_value('delete_slide_animation_main_sequence', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideAnimationMainSequenceRequest(name, slide_index, password, folder, storage)

    def test_delete_slide_by_index(self):
        """Test case for delete_slide_by_index
        """
        request = self.__prepare_delete_slide_by_index_request()
        self.initialize('delete_slide_by_index', None, None)
        response = self.api.delete_slide_by_index(request)
        self.assertIsNotNone(response)

    def test_delete_slide_by_index_invalid_name(self):
        """Test case for delete_slide_by_index with invalid name
        """
        request = self.__prepare_delete_slide_by_index_request()
        request.name = self.get_invalid_test_value('delete_slide_by_index', 'name', request.name, 'str')
        self.initialize('delete_slide_by_index', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_by_index', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_by_index', 'name')

    def test_delete_slide_by_index_invalid_slide_index(self):
        """Test case for delete_slide_by_index with invalid slide_index
        """
        request = self.__prepare_delete_slide_by_index_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_by_index', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_by_index', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_by_index', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_by_index', 'slide_index')

    def test_delete_slide_by_index_invalid_password(self):
        """Test case for delete_slide_by_index with invalid password
        """
        request = self.__prepare_delete_slide_by_index_request()
        request.password = self.get_invalid_test_value('delete_slide_by_index', 'password', request.password, 'str')
        self.initialize('delete_slide_by_index', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_by_index', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_by_index', 'password')

    def test_delete_slide_by_index_invalid_folder(self):
        """Test case for delete_slide_by_index with invalid folder
        """
        request = self.__prepare_delete_slide_by_index_request()
        request.folder = self.get_invalid_test_value('delete_slide_by_index', 'folder', request.folder, 'str')
        self.initialize('delete_slide_by_index', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_by_index', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_by_index', 'folder')

    def test_delete_slide_by_index_invalid_storage(self):
        """Test case for delete_slide_by_index with invalid storage
        """
        request = self.__prepare_delete_slide_by_index_request()
        request.storage = self.get_invalid_test_value('delete_slide_by_index', 'storage', request.storage, 'str')
        self.initialize('delete_slide_by_index', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_by_index(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_by_index', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_by_index', 'storage')

    def __prepare_delete_slide_by_index_request(self):
        name = self.get_test_value('delete_slide_by_index', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_by_index', 'slide_index', 'int')
        password = self.get_test_value('delete_slide_by_index', 'password', 'str')
        folder = self.get_test_value('delete_slide_by_index', 'folder', 'str')
        storage = self.get_test_value('delete_slide_by_index', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideByIndexRequest(name, slide_index, password, folder, storage)

    def test_delete_slide_shape(self):
        """Test case for delete_slide_shape
        """
        request = self.__prepare_delete_slide_shape_request()
        self.initialize('delete_slide_shape', None, None)
        response = self.api.delete_slide_shape(request)
        self.assertIsNotNone(response)

    def test_delete_slide_shape_invalid_name(self):
        """Test case for delete_slide_shape with invalid name
        """
        request = self.__prepare_delete_slide_shape_request()
        request.name = self.get_invalid_test_value('delete_slide_shape', 'name', request.name, 'str')
        self.initialize('delete_slide_shape', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shape', 'name')

    def test_delete_slide_shape_invalid_slide_index(self):
        """Test case for delete_slide_shape with invalid slide_index
        """
        request = self.__prepare_delete_slide_shape_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_shape', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_shape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shape', 'slide_index')

    def test_delete_slide_shape_invalid_shape_index(self):
        """Test case for delete_slide_shape with invalid shape_index
        """
        request = self.__prepare_delete_slide_shape_request()
        request.shape_index = self.get_invalid_test_value('delete_slide_shape', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_slide_shape', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shape', 'shape_index')

    def test_delete_slide_shape_invalid_password(self):
        """Test case for delete_slide_shape with invalid password
        """
        request = self.__prepare_delete_slide_shape_request()
        request.password = self.get_invalid_test_value('delete_slide_shape', 'password', request.password, 'str')
        self.initialize('delete_slide_shape', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shape', 'password')

    def test_delete_slide_shape_invalid_folder(self):
        """Test case for delete_slide_shape with invalid folder
        """
        request = self.__prepare_delete_slide_shape_request()
        request.folder = self.get_invalid_test_value('delete_slide_shape', 'folder', request.folder, 'str')
        self.initialize('delete_slide_shape', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shape', 'folder')

    def test_delete_slide_shape_invalid_storage(self):
        """Test case for delete_slide_shape with invalid storage
        """
        request = self.__prepare_delete_slide_shape_request()
        request.storage = self.get_invalid_test_value('delete_slide_shape', 'storage', request.storage, 'str')
        self.initialize('delete_slide_shape', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shape', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shape', 'storage')

    def __prepare_delete_slide_shape_request(self):
        name = self.get_test_value('delete_slide_shape', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_shape', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_slide_shape', 'shape_index', 'int')
        password = self.get_test_value('delete_slide_shape', 'password', 'str')
        folder = self.get_test_value('delete_slide_shape', 'folder', 'str')
        storage = self.get_test_value('delete_slide_shape', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideShapeRequest(name, slide_index, shape_index, password, folder, storage)

    def test_delete_slide_shapes(self):
        """Test case for delete_slide_shapes
        """
        request = self.__prepare_delete_slide_shapes_request()
        self.initialize('delete_slide_shapes', None, None)
        response = self.api.delete_slide_shapes(request)
        self.assertIsNotNone(response)

    def test_delete_slide_shapes_invalid_name(self):
        """Test case for delete_slide_shapes with invalid name
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.name = self.get_invalid_test_value('delete_slide_shapes', 'name', request.name, 'str')
        self.initialize('delete_slide_shapes', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'name')

    def test_delete_slide_shapes_invalid_slide_index(self):
        """Test case for delete_slide_shapes with invalid slide_index
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_shapes', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_shapes', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'slide_index')

    def test_delete_slide_shapes_invalid_shapes(self):
        """Test case for delete_slide_shapes with invalid shapes
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.shapes = self.get_invalid_test_value('delete_slide_shapes', 'shapes', request.shapes, 'list[int]')
        self.initialize('delete_slide_shapes', 'shapes', request.shapes)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'shapes', request.shapes)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'shapes')

    def test_delete_slide_shapes_invalid_password(self):
        """Test case for delete_slide_shapes with invalid password
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.password = self.get_invalid_test_value('delete_slide_shapes', 'password', request.password, 'str')
        self.initialize('delete_slide_shapes', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'password')

    def test_delete_slide_shapes_invalid_folder(self):
        """Test case for delete_slide_shapes with invalid folder
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.folder = self.get_invalid_test_value('delete_slide_shapes', 'folder', request.folder, 'str')
        self.initialize('delete_slide_shapes', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'folder')

    def test_delete_slide_shapes_invalid_storage(self):
        """Test case for delete_slide_shapes with invalid storage
        """
        request = self.__prepare_delete_slide_shapes_request()
        request.storage = self.get_invalid_test_value('delete_slide_shapes', 'storage', request.storage, 'str')
        self.initialize('delete_slide_shapes', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_shapes', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_shapes', 'storage')

    def __prepare_delete_slide_shapes_request(self):
        name = self.get_test_value('delete_slide_shapes', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_shapes', 'slide_index', 'int')
        shapes = self.get_test_value('delete_slide_shapes', 'shapes', 'list[int]')
        password = self.get_test_value('delete_slide_shapes', 'password', 'str')
        folder = self.get_test_value('delete_slide_shapes', 'folder', 'str')
        storage = self.get_test_value('delete_slide_shapes', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideShapesRequest(name, slide_index, shapes, password, folder, storage)

    def test_delete_slide_subshape(self):
        """Test case for delete_slide_subshape
        """
        request = self.__prepare_delete_slide_subshape_request()
        self.initialize('delete_slide_subshape', None, None)
        response = self.api.delete_slide_subshape(request)
        self.assertIsNotNone(response)

    def test_delete_slide_subshape_invalid_name(self):
        """Test case for delete_slide_subshape with invalid name
        """
        request = self.__prepare_delete_slide_subshape_request()
        request.name = self.get_invalid_test_value('delete_slide_subshape', 'name', request.name, 'str')
        self.initialize('delete_slide_subshape', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshape', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshape', 'name')

    def test_delete_slide_subshape_invalid_slide_index(self):
        """Test case for delete_slide_subshape with invalid slide_index
        """
        request = self.__prepare_delete_slide_subshape_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_subshape', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_subshape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshape', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshape', 'slide_index')

    def test_delete_slide_subshape_invalid_shape_index(self):
        """Test case for delete_slide_subshape with invalid shape_index
        """
        request = self.__prepare_delete_slide_subshape_request()
        request.shape_index = self.get_invalid_test_value('delete_slide_subshape', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_slide_subshape', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshape', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshape', 'shape_index')

    def test_delete_slide_subshape_invalid_path(self):
        """Test case for delete_slide_subshape with invalid path
        """
        request = self.__prepare_delete_slide_subshape_request()
        request.path = self.get_invalid_test_value('delete_slide_subshape', 'path', request.path, 'str')
        self.initialize('delete_slide_subshape', 'path', request.path)
        ok = False
        try:
            self.api.delete_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshape', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshape', 'path')

    def test_delete_slide_subshape_invalid_password(self):
        """Test case for delete_slide_subshape with invalid password
        """
        request = self.__prepare_delete_slide_subshape_request()
        request.password = self.get_invalid_test_value('delete_slide_subshape', 'password', request.password, 'str')
        self.initialize('delete_slide_subshape', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshape', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshape', 'password')

    def test_delete_slide_subshape_invalid_folder(self):
        """Test case for delete_slide_subshape with invalid folder
        """
        request = self.__prepare_delete_slide_subshape_request()
        request.folder = self.get_invalid_test_value('delete_slide_subshape', 'folder', request.folder, 'str')
        self.initialize('delete_slide_subshape', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshape', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshape', 'folder')

    def test_delete_slide_subshape_invalid_storage(self):
        """Test case for delete_slide_subshape with invalid storage
        """
        request = self.__prepare_delete_slide_subshape_request()
        request.storage = self.get_invalid_test_value('delete_slide_subshape', 'storage', request.storage, 'str')
        self.initialize('delete_slide_subshape', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshape', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshape', 'storage')

    def __prepare_delete_slide_subshape_request(self):
        name = self.get_test_value('delete_slide_subshape', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_subshape', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_slide_subshape', 'shape_index', 'int')
        path = self.get_test_value('delete_slide_subshape', 'path', 'str')
        password = self.get_test_value('delete_slide_subshape', 'password', 'str')
        folder = self.get_test_value('delete_slide_subshape', 'folder', 'str')
        storage = self.get_test_value('delete_slide_subshape', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideSubshapeRequest(name, slide_index, shape_index, path, password, folder, storage)

    def test_delete_slide_subshapes(self):
        """Test case for delete_slide_subshapes
        """
        request = self.__prepare_delete_slide_subshapes_request()
        self.initialize('delete_slide_subshapes', None, None)
        response = self.api.delete_slide_subshapes(request)
        self.assertIsNotNone(response)

    def test_delete_slide_subshapes_invalid_name(self):
        """Test case for delete_slide_subshapes with invalid name
        """
        request = self.__prepare_delete_slide_subshapes_request()
        request.name = self.get_invalid_test_value('delete_slide_subshapes', 'name', request.name, 'str')
        self.initialize('delete_slide_subshapes', 'name', request.name)
        ok = False
        try:
            self.api.delete_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshapes', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshapes', 'name')

    def test_delete_slide_subshapes_invalid_slide_index(self):
        """Test case for delete_slide_subshapes with invalid slide_index
        """
        request = self.__prepare_delete_slide_subshapes_request()
        request.slide_index = self.get_invalid_test_value('delete_slide_subshapes', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slide_subshapes', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshapes', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshapes', 'slide_index')

    def test_delete_slide_subshapes_invalid_path(self):
        """Test case for delete_slide_subshapes with invalid path
        """
        request = self.__prepare_delete_slide_subshapes_request()
        request.path = self.get_invalid_test_value('delete_slide_subshapes', 'path', request.path, 'str')
        self.initialize('delete_slide_subshapes', 'path', request.path)
        ok = False
        try:
            self.api.delete_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshapes', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshapes', 'path')

    def test_delete_slide_subshapes_invalid_shapes(self):
        """Test case for delete_slide_subshapes with invalid shapes
        """
        request = self.__prepare_delete_slide_subshapes_request()
        request.shapes = self.get_invalid_test_value('delete_slide_subshapes', 'shapes', request.shapes, 'list[int]')
        self.initialize('delete_slide_subshapes', 'shapes', request.shapes)
        ok = False
        try:
            self.api.delete_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshapes', 'shapes', request.shapes)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshapes', 'shapes')

    def test_delete_slide_subshapes_invalid_password(self):
        """Test case for delete_slide_subshapes with invalid password
        """
        request = self.__prepare_delete_slide_subshapes_request()
        request.password = self.get_invalid_test_value('delete_slide_subshapes', 'password', request.password, 'str')
        self.initialize('delete_slide_subshapes', 'password', request.password)
        ok = False
        try:
            self.api.delete_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshapes', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshapes', 'password')

    def test_delete_slide_subshapes_invalid_folder(self):
        """Test case for delete_slide_subshapes with invalid folder
        """
        request = self.__prepare_delete_slide_subshapes_request()
        request.folder = self.get_invalid_test_value('delete_slide_subshapes', 'folder', request.folder, 'str')
        self.initialize('delete_slide_subshapes', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshapes', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshapes', 'folder')

    def test_delete_slide_subshapes_invalid_storage(self):
        """Test case for delete_slide_subshapes with invalid storage
        """
        request = self.__prepare_delete_slide_subshapes_request()
        request.storage = self.get_invalid_test_value('delete_slide_subshapes', 'storage', request.storage, 'str')
        self.initialize('delete_slide_subshapes', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slide_subshapes', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slide_subshapes', 'storage')

    def __prepare_delete_slide_subshapes_request(self):
        name = self.get_test_value('delete_slide_subshapes', 'name', 'str')
        slide_index = self.get_test_value('delete_slide_subshapes', 'slide_index', 'int')
        path = self.get_test_value('delete_slide_subshapes', 'path', 'str')
        shapes = self.get_test_value('delete_slide_subshapes', 'shapes', 'list[int]')
        password = self.get_test_value('delete_slide_subshapes', 'password', 'str')
        folder = self.get_test_value('delete_slide_subshapes', 'folder', 'str')
        storage = self.get_test_value('delete_slide_subshapes', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlideSubshapesRequest(name, slide_index, path, shapes, password, folder, storage)

    def test_delete_slides_clean_slides_list(self):
        """Test case for delete_slides_clean_slides_list
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        self.initialize('delete_slides_clean_slides_list', None, None)
        response = self.api.delete_slides_clean_slides_list(request)
        self.assertIsNotNone(response)

    def test_delete_slides_clean_slides_list_invalid_name(self):
        """Test case for delete_slides_clean_slides_list with invalid name
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        request.name = self.get_invalid_test_value('delete_slides_clean_slides_list', 'name', request.name, 'str')
        self.initialize('delete_slides_clean_slides_list', 'name', request.name)
        ok = False
        try:
            self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_clean_slides_list', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_clean_slides_list', 'name')

    def test_delete_slides_clean_slides_list_invalid_slides(self):
        """Test case for delete_slides_clean_slides_list with invalid slides
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        request.slides = self.get_invalid_test_value('delete_slides_clean_slides_list', 'slides', request.slides, 'list[int]')
        self.initialize('delete_slides_clean_slides_list', 'slides', request.slides)
        ok = False
        try:
            self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_clean_slides_list', 'slides', request.slides)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_clean_slides_list', 'slides')

    def test_delete_slides_clean_slides_list_invalid_password(self):
        """Test case for delete_slides_clean_slides_list with invalid password
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        request.password = self.get_invalid_test_value('delete_slides_clean_slides_list', 'password', request.password, 'str')
        self.initialize('delete_slides_clean_slides_list', 'password', request.password)
        ok = False
        try:
            self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_clean_slides_list', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_clean_slides_list', 'password')

    def test_delete_slides_clean_slides_list_invalid_folder(self):
        """Test case for delete_slides_clean_slides_list with invalid folder
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        request.folder = self.get_invalid_test_value('delete_slides_clean_slides_list', 'folder', request.folder, 'str')
        self.initialize('delete_slides_clean_slides_list', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_clean_slides_list', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_clean_slides_list', 'folder')

    def test_delete_slides_clean_slides_list_invalid_storage(self):
        """Test case for delete_slides_clean_slides_list with invalid storage
        """
        request = self.__prepare_delete_slides_clean_slides_list_request()
        request.storage = self.get_invalid_test_value('delete_slides_clean_slides_list', 'storage', request.storage, 'str')
        self.initialize('delete_slides_clean_slides_list', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slides_clean_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_clean_slides_list', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_clean_slides_list', 'storage')

    def __prepare_delete_slides_clean_slides_list_request(self):
        name = self.get_test_value('delete_slides_clean_slides_list', 'name', 'str')
        slides = self.get_test_value('delete_slides_clean_slides_list', 'slides', 'list[int]')
        password = self.get_test_value('delete_slides_clean_slides_list', 'password', 'str')
        folder = self.get_test_value('delete_slides_clean_slides_list', 'folder', 'str')
        storage = self.get_test_value('delete_slides_clean_slides_list', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlidesCleanSlidesListRequest(name, slides, password, folder, storage)

    def test_delete_slides_document_properties(self):
        """Test case for delete_slides_document_properties
        """
        request = self.__prepare_delete_slides_document_properties_request()
        self.initialize('delete_slides_document_properties', None, None)
        response = self.api.delete_slides_document_properties(request)
        self.assertIsNotNone(response)

    def test_delete_slides_document_properties_invalid_name(self):
        """Test case for delete_slides_document_properties with invalid name
        """
        request = self.__prepare_delete_slides_document_properties_request()
        request.name = self.get_invalid_test_value('delete_slides_document_properties', 'name', request.name, 'str')
        self.initialize('delete_slides_document_properties', 'name', request.name)
        ok = False
        try:
            self.api.delete_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_properties', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_document_properties', 'name')

    def test_delete_slides_document_properties_invalid_password(self):
        """Test case for delete_slides_document_properties with invalid password
        """
        request = self.__prepare_delete_slides_document_properties_request()
        request.password = self.get_invalid_test_value('delete_slides_document_properties', 'password', request.password, 'str')
        self.initialize('delete_slides_document_properties', 'password', request.password)
        ok = False
        try:
            self.api.delete_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_properties', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_document_properties', 'password')

    def test_delete_slides_document_properties_invalid_folder(self):
        """Test case for delete_slides_document_properties with invalid folder
        """
        request = self.__prepare_delete_slides_document_properties_request()
        request.folder = self.get_invalid_test_value('delete_slides_document_properties', 'folder', request.folder, 'str')
        self.initialize('delete_slides_document_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_properties', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_document_properties', 'folder')

    def test_delete_slides_document_properties_invalid_storage(self):
        """Test case for delete_slides_document_properties with invalid storage
        """
        request = self.__prepare_delete_slides_document_properties_request()
        request.storage = self.get_invalid_test_value('delete_slides_document_properties', 'storage', request.storage, 'str')
        self.initialize('delete_slides_document_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_properties', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_document_properties', 'storage')

    def __prepare_delete_slides_document_properties_request(self):
        name = self.get_test_value('delete_slides_document_properties', 'name', 'str')
        password = self.get_test_value('delete_slides_document_properties', 'password', 'str')
        folder = self.get_test_value('delete_slides_document_properties', 'folder', 'str')
        storage = self.get_test_value('delete_slides_document_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlidesDocumentPropertiesRequest(name, password, folder, storage)

    def test_delete_slides_document_property(self):
        """Test case for delete_slides_document_property
        """
        request = self.__prepare_delete_slides_document_property_request()
        self.initialize('delete_slides_document_property', None, None)
        response = self.api.delete_slides_document_property(request)
        self.assertIsNotNone(response)

    def test_delete_slides_document_property_invalid_name(self):
        """Test case for delete_slides_document_property with invalid name
        """
        request = self.__prepare_delete_slides_document_property_request()
        request.name = self.get_invalid_test_value('delete_slides_document_property', 'name', request.name, 'str')
        self.initialize('delete_slides_document_property', 'name', request.name)
        ok = False
        try:
            self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_property', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_document_property', 'name')

    def test_delete_slides_document_property_invalid_property_name(self):
        """Test case for delete_slides_document_property with invalid property_name
        """
        request = self.__prepare_delete_slides_document_property_request()
        request.property_name = self.get_invalid_test_value('delete_slides_document_property', 'property_name', request.property_name, 'str')
        self.initialize('delete_slides_document_property', 'property_name', request.property_name)
        ok = False
        try:
            self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_property', 'property_name', request.property_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_document_property', 'property_name')

    def test_delete_slides_document_property_invalid_password(self):
        """Test case for delete_slides_document_property with invalid password
        """
        request = self.__prepare_delete_slides_document_property_request()
        request.password = self.get_invalid_test_value('delete_slides_document_property', 'password', request.password, 'str')
        self.initialize('delete_slides_document_property', 'password', request.password)
        ok = False
        try:
            self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_property', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_document_property', 'password')

    def test_delete_slides_document_property_invalid_folder(self):
        """Test case for delete_slides_document_property with invalid folder
        """
        request = self.__prepare_delete_slides_document_property_request()
        request.folder = self.get_invalid_test_value('delete_slides_document_property', 'folder', request.folder, 'str')
        self.initialize('delete_slides_document_property', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_property', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_document_property', 'folder')

    def test_delete_slides_document_property_invalid_storage(self):
        """Test case for delete_slides_document_property with invalid storage
        """
        request = self.__prepare_delete_slides_document_property_request()
        request.storage = self.get_invalid_test_value('delete_slides_document_property', 'storage', request.storage, 'str')
        self.initialize('delete_slides_document_property', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_document_property', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_document_property', 'storage')

    def __prepare_delete_slides_document_property_request(self):
        name = self.get_test_value('delete_slides_document_property', 'name', 'str')
        property_name = self.get_test_value('delete_slides_document_property', 'property_name', 'str')
        password = self.get_test_value('delete_slides_document_property', 'password', 'str')
        folder = self.get_test_value('delete_slides_document_property', 'folder', 'str')
        storage = self.get_test_value('delete_slides_document_property', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlidesDocumentPropertyRequest(name, property_name, password, folder, storage)

    def test_delete_slides_slide_background(self):
        """Test case for delete_slides_slide_background
        """
        request = self.__prepare_delete_slides_slide_background_request()
        self.initialize('delete_slides_slide_background', None, None)
        response = self.api.delete_slides_slide_background(request)
        self.assertIsNotNone(response)

    def test_delete_slides_slide_background_invalid_name(self):
        """Test case for delete_slides_slide_background with invalid name
        """
        request = self.__prepare_delete_slides_slide_background_request()
        request.name = self.get_invalid_test_value('delete_slides_slide_background', 'name', request.name, 'str')
        self.initialize('delete_slides_slide_background', 'name', request.name)
        ok = False
        try:
            self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_slide_background', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_slide_background', 'name')

    def test_delete_slides_slide_background_invalid_slide_index(self):
        """Test case for delete_slides_slide_background with invalid slide_index
        """
        request = self.__prepare_delete_slides_slide_background_request()
        request.slide_index = self.get_invalid_test_value('delete_slides_slide_background', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_slides_slide_background', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_slide_background', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_slide_background', 'slide_index')

    def test_delete_slides_slide_background_invalid_password(self):
        """Test case for delete_slides_slide_background with invalid password
        """
        request = self.__prepare_delete_slides_slide_background_request()
        request.password = self.get_invalid_test_value('delete_slides_slide_background', 'password', request.password, 'str')
        self.initialize('delete_slides_slide_background', 'password', request.password)
        ok = False
        try:
            self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_slide_background', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_slide_background', 'password')

    def test_delete_slides_slide_background_invalid_folder(self):
        """Test case for delete_slides_slide_background with invalid folder
        """
        request = self.__prepare_delete_slides_slide_background_request()
        request.folder = self.get_invalid_test_value('delete_slides_slide_background', 'folder', request.folder, 'str')
        self.initialize('delete_slides_slide_background', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_slide_background', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_slide_background', 'folder')

    def test_delete_slides_slide_background_invalid_storage(self):
        """Test case for delete_slides_slide_background with invalid storage
        """
        request = self.__prepare_delete_slides_slide_background_request()
        request.storage = self.get_invalid_test_value('delete_slides_slide_background', 'storage', request.storage, 'str')
        self.initialize('delete_slides_slide_background', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_slides_slide_background', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_slides_slide_background', 'storage')

    def __prepare_delete_slides_slide_background_request(self):
        name = self.get_test_value('delete_slides_slide_background', 'name', 'str')
        slide_index = self.get_test_value('delete_slides_slide_background', 'slide_index', 'int')
        password = self.get_test_value('delete_slides_slide_background', 'password', 'str')
        folder = self.get_test_value('delete_slides_slide_background', 'folder', 'str')
        storage = self.get_test_value('delete_slides_slide_background', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSlidesSlideBackgroundRequest(name, slide_index, password, folder, storage)

    def test_delete_subshape_paragraph(self):
        """Test case for delete_subshape_paragraph
        """
        request = self.__prepare_delete_subshape_paragraph_request()
        self.initialize('delete_subshape_paragraph', None, None)
        response = self.api.delete_subshape_paragraph(request)
        self.assertIsNotNone(response)

    def test_delete_subshape_paragraph_invalid_name(self):
        """Test case for delete_subshape_paragraph with invalid name
        """
        request = self.__prepare_delete_subshape_paragraph_request()
        request.name = self.get_invalid_test_value('delete_subshape_paragraph', 'name', request.name, 'str')
        self.initialize('delete_subshape_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.delete_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraph', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraph', 'name')

    def test_delete_subshape_paragraph_invalid_slide_index(self):
        """Test case for delete_subshape_paragraph with invalid slide_index
        """
        request = self.__prepare_delete_subshape_paragraph_request()
        request.slide_index = self.get_invalid_test_value('delete_subshape_paragraph', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_subshape_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraph', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraph', 'slide_index')

    def test_delete_subshape_paragraph_invalid_shape_index(self):
        """Test case for delete_subshape_paragraph with invalid shape_index
        """
        request = self.__prepare_delete_subshape_paragraph_request()
        request.shape_index = self.get_invalid_test_value('delete_subshape_paragraph', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_subshape_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraph', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraph', 'shape_index')

    def test_delete_subshape_paragraph_invalid_paragraph_index(self):
        """Test case for delete_subshape_paragraph with invalid paragraph_index
        """
        request = self.__prepare_delete_subshape_paragraph_request()
        request.paragraph_index = self.get_invalid_test_value('delete_subshape_paragraph', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_subshape_paragraph', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraph', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraph', 'paragraph_index')

    def test_delete_subshape_paragraph_invalid_path(self):
        """Test case for delete_subshape_paragraph with invalid path
        """
        request = self.__prepare_delete_subshape_paragraph_request()
        request.path = self.get_invalid_test_value('delete_subshape_paragraph', 'path', request.path, 'str')
        self.initialize('delete_subshape_paragraph', 'path', request.path)
        ok = False
        try:
            self.api.delete_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraph', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraph', 'path')

    def test_delete_subshape_paragraph_invalid_password(self):
        """Test case for delete_subshape_paragraph with invalid password
        """
        request = self.__prepare_delete_subshape_paragraph_request()
        request.password = self.get_invalid_test_value('delete_subshape_paragraph', 'password', request.password, 'str')
        self.initialize('delete_subshape_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.delete_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraph', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraph', 'password')

    def test_delete_subshape_paragraph_invalid_folder(self):
        """Test case for delete_subshape_paragraph with invalid folder
        """
        request = self.__prepare_delete_subshape_paragraph_request()
        request.folder = self.get_invalid_test_value('delete_subshape_paragraph', 'folder', request.folder, 'str')
        self.initialize('delete_subshape_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraph', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraph', 'folder')

    def test_delete_subshape_paragraph_invalid_storage(self):
        """Test case for delete_subshape_paragraph with invalid storage
        """
        request = self.__prepare_delete_subshape_paragraph_request()
        request.storage = self.get_invalid_test_value('delete_subshape_paragraph', 'storage', request.storage, 'str')
        self.initialize('delete_subshape_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraph', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraph', 'storage')

    def __prepare_delete_subshape_paragraph_request(self):
        name = self.get_test_value('delete_subshape_paragraph', 'name', 'str')
        slide_index = self.get_test_value('delete_subshape_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_subshape_paragraph', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_subshape_paragraph', 'paragraph_index', 'int')
        path = self.get_test_value('delete_subshape_paragraph', 'path', 'str')
        password = self.get_test_value('delete_subshape_paragraph', 'password', 'str')
        folder = self.get_test_value('delete_subshape_paragraph', 'folder', 'str')
        storage = self.get_test_value('delete_subshape_paragraph', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSubshapeParagraphRequest(name, slide_index, shape_index, paragraph_index, path, password, folder, storage)

    def test_delete_subshape_paragraphs(self):
        """Test case for delete_subshape_paragraphs
        """
        request = self.__prepare_delete_subshape_paragraphs_request()
        self.initialize('delete_subshape_paragraphs', None, None)
        response = self.api.delete_subshape_paragraphs(request)
        self.assertIsNotNone(response)

    def test_delete_subshape_paragraphs_invalid_name(self):
        """Test case for delete_subshape_paragraphs with invalid name
        """
        request = self.__prepare_delete_subshape_paragraphs_request()
        request.name = self.get_invalid_test_value('delete_subshape_paragraphs', 'name', request.name, 'str')
        self.initialize('delete_subshape_paragraphs', 'name', request.name)
        ok = False
        try:
            self.api.delete_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraphs', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraphs', 'name')

    def test_delete_subshape_paragraphs_invalid_slide_index(self):
        """Test case for delete_subshape_paragraphs with invalid slide_index
        """
        request = self.__prepare_delete_subshape_paragraphs_request()
        request.slide_index = self.get_invalid_test_value('delete_subshape_paragraphs', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_subshape_paragraphs', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraphs', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraphs', 'slide_index')

    def test_delete_subshape_paragraphs_invalid_shape_index(self):
        """Test case for delete_subshape_paragraphs with invalid shape_index
        """
        request = self.__prepare_delete_subshape_paragraphs_request()
        request.shape_index = self.get_invalid_test_value('delete_subshape_paragraphs', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_subshape_paragraphs', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraphs', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraphs', 'shape_index')

    def test_delete_subshape_paragraphs_invalid_path(self):
        """Test case for delete_subshape_paragraphs with invalid path
        """
        request = self.__prepare_delete_subshape_paragraphs_request()
        request.path = self.get_invalid_test_value('delete_subshape_paragraphs', 'path', request.path, 'str')
        self.initialize('delete_subshape_paragraphs', 'path', request.path)
        ok = False
        try:
            self.api.delete_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraphs', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraphs', 'path')

    def test_delete_subshape_paragraphs_invalid_paragraphs(self):
        """Test case for delete_subshape_paragraphs with invalid paragraphs
        """
        request = self.__prepare_delete_subshape_paragraphs_request()
        request.paragraphs = self.get_invalid_test_value('delete_subshape_paragraphs', 'paragraphs', request.paragraphs, 'list[int]')
        self.initialize('delete_subshape_paragraphs', 'paragraphs', request.paragraphs)
        ok = False
        try:
            self.api.delete_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraphs', 'paragraphs', request.paragraphs)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraphs', 'paragraphs')

    def test_delete_subshape_paragraphs_invalid_password(self):
        """Test case for delete_subshape_paragraphs with invalid password
        """
        request = self.__prepare_delete_subshape_paragraphs_request()
        request.password = self.get_invalid_test_value('delete_subshape_paragraphs', 'password', request.password, 'str')
        self.initialize('delete_subshape_paragraphs', 'password', request.password)
        ok = False
        try:
            self.api.delete_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraphs', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraphs', 'password')

    def test_delete_subshape_paragraphs_invalid_folder(self):
        """Test case for delete_subshape_paragraphs with invalid folder
        """
        request = self.__prepare_delete_subshape_paragraphs_request()
        request.folder = self.get_invalid_test_value('delete_subshape_paragraphs', 'folder', request.folder, 'str')
        self.initialize('delete_subshape_paragraphs', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraphs', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraphs', 'folder')

    def test_delete_subshape_paragraphs_invalid_storage(self):
        """Test case for delete_subshape_paragraphs with invalid storage
        """
        request = self.__prepare_delete_subshape_paragraphs_request()
        request.storage = self.get_invalid_test_value('delete_subshape_paragraphs', 'storage', request.storage, 'str')
        self.initialize('delete_subshape_paragraphs', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_paragraphs', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_paragraphs', 'storage')

    def __prepare_delete_subshape_paragraphs_request(self):
        name = self.get_test_value('delete_subshape_paragraphs', 'name', 'str')
        slide_index = self.get_test_value('delete_subshape_paragraphs', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_subshape_paragraphs', 'shape_index', 'int')
        path = self.get_test_value('delete_subshape_paragraphs', 'path', 'str')
        paragraphs = self.get_test_value('delete_subshape_paragraphs', 'paragraphs', 'list[int]')
        password = self.get_test_value('delete_subshape_paragraphs', 'password', 'str')
        folder = self.get_test_value('delete_subshape_paragraphs', 'folder', 'str')
        storage = self.get_test_value('delete_subshape_paragraphs', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSubshapeParagraphsRequest(name, slide_index, shape_index, path, paragraphs, password, folder, storage)

    def test_delete_subshape_portion(self):
        """Test case for delete_subshape_portion
        """
        request = self.__prepare_delete_subshape_portion_request()
        self.initialize('delete_subshape_portion', None, None)
        response = self.api.delete_subshape_portion(request)
        self.assertIsNotNone(response)

    def test_delete_subshape_portion_invalid_name(self):
        """Test case for delete_subshape_portion with invalid name
        """
        request = self.__prepare_delete_subshape_portion_request()
        request.name = self.get_invalid_test_value('delete_subshape_portion', 'name', request.name, 'str')
        self.initialize('delete_subshape_portion', 'name', request.name)
        ok = False
        try:
            self.api.delete_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portion', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portion', 'name')

    def test_delete_subshape_portion_invalid_slide_index(self):
        """Test case for delete_subshape_portion with invalid slide_index
        """
        request = self.__prepare_delete_subshape_portion_request()
        request.slide_index = self.get_invalid_test_value('delete_subshape_portion', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_subshape_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portion', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portion', 'slide_index')

    def test_delete_subshape_portion_invalid_shape_index(self):
        """Test case for delete_subshape_portion with invalid shape_index
        """
        request = self.__prepare_delete_subshape_portion_request()
        request.shape_index = self.get_invalid_test_value('delete_subshape_portion', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_subshape_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portion', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portion', 'shape_index')

    def test_delete_subshape_portion_invalid_paragraph_index(self):
        """Test case for delete_subshape_portion with invalid paragraph_index
        """
        request = self.__prepare_delete_subshape_portion_request()
        request.paragraph_index = self.get_invalid_test_value('delete_subshape_portion', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_subshape_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portion', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portion', 'paragraph_index')

    def test_delete_subshape_portion_invalid_portion_index(self):
        """Test case for delete_subshape_portion with invalid portion_index
        """
        request = self.__prepare_delete_subshape_portion_request()
        request.portion_index = self.get_invalid_test_value('delete_subshape_portion', 'portion_index', request.portion_index, 'int')
        self.initialize('delete_subshape_portion', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.delete_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portion', 'portion_index', request.portion_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portion', 'portion_index')

    def test_delete_subshape_portion_invalid_path(self):
        """Test case for delete_subshape_portion with invalid path
        """
        request = self.__prepare_delete_subshape_portion_request()
        request.path = self.get_invalid_test_value('delete_subshape_portion', 'path', request.path, 'str')
        self.initialize('delete_subshape_portion', 'path', request.path)
        ok = False
        try:
            self.api.delete_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portion', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portion', 'path')

    def test_delete_subshape_portion_invalid_password(self):
        """Test case for delete_subshape_portion with invalid password
        """
        request = self.__prepare_delete_subshape_portion_request()
        request.password = self.get_invalid_test_value('delete_subshape_portion', 'password', request.password, 'str')
        self.initialize('delete_subshape_portion', 'password', request.password)
        ok = False
        try:
            self.api.delete_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portion', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portion', 'password')

    def test_delete_subshape_portion_invalid_folder(self):
        """Test case for delete_subshape_portion with invalid folder
        """
        request = self.__prepare_delete_subshape_portion_request()
        request.folder = self.get_invalid_test_value('delete_subshape_portion', 'folder', request.folder, 'str')
        self.initialize('delete_subshape_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portion', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portion', 'folder')

    def test_delete_subshape_portion_invalid_storage(self):
        """Test case for delete_subshape_portion with invalid storage
        """
        request = self.__prepare_delete_subshape_portion_request()
        request.storage = self.get_invalid_test_value('delete_subshape_portion', 'storage', request.storage, 'str')
        self.initialize('delete_subshape_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portion', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portion', 'storage')

    def __prepare_delete_subshape_portion_request(self):
        name = self.get_test_value('delete_subshape_portion', 'name', 'str')
        slide_index = self.get_test_value('delete_subshape_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_subshape_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_subshape_portion', 'paragraph_index', 'int')
        portion_index = self.get_test_value('delete_subshape_portion', 'portion_index', 'int')
        path = self.get_test_value('delete_subshape_portion', 'path', 'str')
        password = self.get_test_value('delete_subshape_portion', 'password', 'str')
        folder = self.get_test_value('delete_subshape_portion', 'folder', 'str')
        storage = self.get_test_value('delete_subshape_portion', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSubshapePortionRequest(name, slide_index, shape_index, paragraph_index, portion_index, path, password, folder, storage)

    def test_delete_subshape_portions(self):
        """Test case for delete_subshape_portions
        """
        request = self.__prepare_delete_subshape_portions_request()
        self.initialize('delete_subshape_portions', None, None)
        response = self.api.delete_subshape_portions(request)
        self.assertIsNotNone(response)

    def test_delete_subshape_portions_invalid_name(self):
        """Test case for delete_subshape_portions with invalid name
        """
        request = self.__prepare_delete_subshape_portions_request()
        request.name = self.get_invalid_test_value('delete_subshape_portions', 'name', request.name, 'str')
        self.initialize('delete_subshape_portions', 'name', request.name)
        ok = False
        try:
            self.api.delete_subshape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portions', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portions', 'name')

    def test_delete_subshape_portions_invalid_slide_index(self):
        """Test case for delete_subshape_portions with invalid slide_index
        """
        request = self.__prepare_delete_subshape_portions_request()
        request.slide_index = self.get_invalid_test_value('delete_subshape_portions', 'slide_index', request.slide_index, 'int')
        self.initialize('delete_subshape_portions', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.delete_subshape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portions', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portions', 'slide_index')

    def test_delete_subshape_portions_invalid_shape_index(self):
        """Test case for delete_subshape_portions with invalid shape_index
        """
        request = self.__prepare_delete_subshape_portions_request()
        request.shape_index = self.get_invalid_test_value('delete_subshape_portions', 'shape_index', request.shape_index, 'int')
        self.initialize('delete_subshape_portions', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.delete_subshape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portions', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portions', 'shape_index')

    def test_delete_subshape_portions_invalid_paragraph_index(self):
        """Test case for delete_subshape_portions with invalid paragraph_index
        """
        request = self.__prepare_delete_subshape_portions_request()
        request.paragraph_index = self.get_invalid_test_value('delete_subshape_portions', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('delete_subshape_portions', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.delete_subshape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portions', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portions', 'paragraph_index')

    def test_delete_subshape_portions_invalid_path(self):
        """Test case for delete_subshape_portions with invalid path
        """
        request = self.__prepare_delete_subshape_portions_request()
        request.path = self.get_invalid_test_value('delete_subshape_portions', 'path', request.path, 'str')
        self.initialize('delete_subshape_portions', 'path', request.path)
        ok = False
        try:
            self.api.delete_subshape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portions', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portions', 'path')

    def test_delete_subshape_portions_invalid_portions(self):
        """Test case for delete_subshape_portions with invalid portions
        """
        request = self.__prepare_delete_subshape_portions_request()
        request.portions = self.get_invalid_test_value('delete_subshape_portions', 'portions', request.portions, 'list[int]')
        self.initialize('delete_subshape_portions', 'portions', request.portions)
        ok = False
        try:
            self.api.delete_subshape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portions', 'portions', request.portions)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portions', 'portions')

    def test_delete_subshape_portions_invalid_password(self):
        """Test case for delete_subshape_portions with invalid password
        """
        request = self.__prepare_delete_subshape_portions_request()
        request.password = self.get_invalid_test_value('delete_subshape_portions', 'password', request.password, 'str')
        self.initialize('delete_subshape_portions', 'password', request.password)
        ok = False
        try:
            self.api.delete_subshape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portions', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portions', 'password')

    def test_delete_subshape_portions_invalid_folder(self):
        """Test case for delete_subshape_portions with invalid folder
        """
        request = self.__prepare_delete_subshape_portions_request()
        request.folder = self.get_invalid_test_value('delete_subshape_portions', 'folder', request.folder, 'str')
        self.initialize('delete_subshape_portions', 'folder', request.folder)
        ok = False
        try:
            self.api.delete_subshape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portions', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portions', 'folder')

    def test_delete_subshape_portions_invalid_storage(self):
        """Test case for delete_subshape_portions with invalid storage
        """
        request = self.__prepare_delete_subshape_portions_request()
        request.storage = self.get_invalid_test_value('delete_subshape_portions', 'storage', request.storage, 'str')
        self.initialize('delete_subshape_portions', 'storage', request.storage)
        ok = False
        try:
            self.api.delete_subshape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'delete_subshape_portions', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('delete_subshape_portions', 'storage')

    def __prepare_delete_subshape_portions_request(self):
        name = self.get_test_value('delete_subshape_portions', 'name', 'str')
        slide_index = self.get_test_value('delete_subshape_portions', 'slide_index', 'int')
        shape_index = self.get_test_value('delete_subshape_portions', 'shape_index', 'int')
        paragraph_index = self.get_test_value('delete_subshape_portions', 'paragraph_index', 'int')
        path = self.get_test_value('delete_subshape_portions', 'path', 'str')
        portions = self.get_test_value('delete_subshape_portions', 'portions', 'list[int]')
        password = self.get_test_value('delete_subshape_portions', 'password', 'str')
        folder = self.get_test_value('delete_subshape_portions', 'folder', 'str')
        storage = self.get_test_value('delete_subshape_portions', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DeleteSubshapePortionsRequest(name, slide_index, shape_index, paragraph_index, path, portions, password, folder, storage)

    def test_download_file(self):
        """Test case for download_file
        """
        request = self.__prepare_download_file_request()
        self.initialize('download_file', None, None)
        response = self.api.download_file(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_download_file_invalid_path(self):
        """Test case for download_file with invalid path
        """
        request = self.__prepare_download_file_request()
        request.path = self.get_invalid_test_value('download_file', 'path', request.path, 'str')
        self.initialize('download_file', 'path', request.path)
        ok = False
        try:
            self.api.download_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'download_file', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('download_file', 'path')

    def test_download_file_invalid_storage_name(self):
        """Test case for download_file with invalid storage_name
        """
        request = self.__prepare_download_file_request()
        request.storage_name = self.get_invalid_test_value('download_file', 'storage_name', request.storage_name, 'str')
        self.initialize('download_file', 'storage_name', request.storage_name)
        ok = False
        try:
            self.api.download_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'download_file', 'storage_name', request.storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('download_file', 'storage_name')

    def test_download_file_invalid_version_id(self):
        """Test case for download_file with invalid version_id
        """
        request = self.__prepare_download_file_request()
        request.version_id = self.get_invalid_test_value('download_file', 'version_id', request.version_id, 'str')
        self.initialize('download_file', 'version_id', request.version_id)
        ok = False
        try:
            self.api.download_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'download_file', 'version_id', request.version_id)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('download_file', 'version_id')

    def __prepare_download_file_request(self):
        path = self.get_test_value('download_file', 'path', 'str')
        storage_name = self.get_test_value('download_file', 'storage_name', 'str')
        version_id = self.get_test_value('download_file', 'version_id', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.DownloadFileRequest(path, storage_name, version_id)

    def test_get_disc_usage(self):
        """Test case for get_disc_usage
        """
        request = self.__prepare_get_disc_usage_request()
        self.initialize('get_disc_usage', None, None)
        response = self.api.get_disc_usage(request)
        self.assertIsNotNone(response)

    def test_get_disc_usage_invalid_storage_name(self):
        """Test case for get_disc_usage with invalid storage_name
        """
        request = self.__prepare_get_disc_usage_request()
        request.storage_name = self.get_invalid_test_value('get_disc_usage', 'storage_name', request.storage_name, 'str')
        self.initialize('get_disc_usage', 'storage_name', request.storage_name)
        ok = False
        try:
            self.api.get_disc_usage(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_disc_usage', 'storage_name', request.storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_disc_usage', 'storage_name')

    def __prepare_get_disc_usage_request(self):
        storage_name = self.get_test_value('get_disc_usage', 'storage_name', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetDiscUsageRequest(storage_name)

    def test_get_file_versions(self):
        """Test case for get_file_versions
        """
        request = self.__prepare_get_file_versions_request()
        self.initialize('get_file_versions', None, None)
        response = self.api.get_file_versions(request)
        self.assertIsNotNone(response)

    def test_get_file_versions_invalid_path(self):
        """Test case for get_file_versions with invalid path
        """
        request = self.__prepare_get_file_versions_request()
        request.path = self.get_invalid_test_value('get_file_versions', 'path', request.path, 'str')
        self.initialize('get_file_versions', 'path', request.path)
        ok = False
        try:
            self.api.get_file_versions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_file_versions', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_file_versions', 'path')

    def test_get_file_versions_invalid_storage_name(self):
        """Test case for get_file_versions with invalid storage_name
        """
        request = self.__prepare_get_file_versions_request()
        request.storage_name = self.get_invalid_test_value('get_file_versions', 'storage_name', request.storage_name, 'str')
        self.initialize('get_file_versions', 'storage_name', request.storage_name)
        ok = False
        try:
            self.api.get_file_versions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_file_versions', 'storage_name', request.storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_file_versions', 'storage_name')

    def __prepare_get_file_versions_request(self):
        path = self.get_test_value('get_file_versions', 'path', 'str')
        storage_name = self.get_test_value('get_file_versions', 'storage_name', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetFileVersionsRequest(path, storage_name)

    def test_get_files_list(self):
        """Test case for get_files_list
        """
        request = self.__prepare_get_files_list_request()
        self.initialize('get_files_list', None, None)
        response = self.api.get_files_list(request)
        self.assertIsNotNone(response)

    def test_get_files_list_invalid_path(self):
        """Test case for get_files_list with invalid path
        """
        request = self.__prepare_get_files_list_request()
        request.path = self.get_invalid_test_value('get_files_list', 'path', request.path, 'str')
        self.initialize('get_files_list', 'path', request.path)
        ok = False
        try:
            self.api.get_files_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_files_list', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_files_list', 'path')

    def test_get_files_list_invalid_storage_name(self):
        """Test case for get_files_list with invalid storage_name
        """
        request = self.__prepare_get_files_list_request()
        request.storage_name = self.get_invalid_test_value('get_files_list', 'storage_name', request.storage_name, 'str')
        self.initialize('get_files_list', 'storage_name', request.storage_name)
        ok = False
        try:
            self.api.get_files_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_files_list', 'storage_name', request.storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_files_list', 'storage_name')

    def __prepare_get_files_list_request(self):
        path = self.get_test_value('get_files_list', 'path', 'str')
        storage_name = self.get_test_value('get_files_list', 'storage_name', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetFilesListRequest(path, storage_name)

    def test_get_layout_slide(self):
        """Test case for get_layout_slide
        """
        request = self.__prepare_get_layout_slide_request()
        self.initialize('get_layout_slide', None, None)
        response = self.api.get_layout_slide(request)
        self.assertIsNotNone(response)

    def test_get_layout_slide_invalid_name(self):
        """Test case for get_layout_slide with invalid name
        """
        request = self.__prepare_get_layout_slide_request()
        request.name = self.get_invalid_test_value('get_layout_slide', 'name', request.name, 'str')
        self.initialize('get_layout_slide', 'name', request.name)
        ok = False
        try:
            self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slide', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_layout_slide', 'name')

    def test_get_layout_slide_invalid_slide_index(self):
        """Test case for get_layout_slide with invalid slide_index
        """
        request = self.__prepare_get_layout_slide_request()
        request.slide_index = self.get_invalid_test_value('get_layout_slide', 'slide_index', request.slide_index, 'int')
        self.initialize('get_layout_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slide', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_layout_slide', 'slide_index')

    def test_get_layout_slide_invalid_password(self):
        """Test case for get_layout_slide with invalid password
        """
        request = self.__prepare_get_layout_slide_request()
        request.password = self.get_invalid_test_value('get_layout_slide', 'password', request.password, 'str')
        self.initialize('get_layout_slide', 'password', request.password)
        ok = False
        try:
            self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slide', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_layout_slide', 'password')

    def test_get_layout_slide_invalid_folder(self):
        """Test case for get_layout_slide with invalid folder
        """
        request = self.__prepare_get_layout_slide_request()
        request.folder = self.get_invalid_test_value('get_layout_slide', 'folder', request.folder, 'str')
        self.initialize('get_layout_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slide', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_layout_slide', 'folder')

    def test_get_layout_slide_invalid_storage(self):
        """Test case for get_layout_slide with invalid storage
        """
        request = self.__prepare_get_layout_slide_request()
        request.storage = self.get_invalid_test_value('get_layout_slide', 'storage', request.storage, 'str')
        self.initialize('get_layout_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.get_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slide', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_layout_slide', 'storage')

    def __prepare_get_layout_slide_request(self):
        name = self.get_test_value('get_layout_slide', 'name', 'str')
        slide_index = self.get_test_value('get_layout_slide', 'slide_index', 'int')
        password = self.get_test_value('get_layout_slide', 'password', 'str')
        folder = self.get_test_value('get_layout_slide', 'folder', 'str')
        storage = self.get_test_value('get_layout_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetLayoutSlideRequest(name, slide_index, password, folder, storage)

    def test_get_layout_slides_list(self):
        """Test case for get_layout_slides_list
        """
        request = self.__prepare_get_layout_slides_list_request()
        self.initialize('get_layout_slides_list', None, None)
        response = self.api.get_layout_slides_list(request)
        self.assertIsNotNone(response)

    def test_get_layout_slides_list_invalid_name(self):
        """Test case for get_layout_slides_list with invalid name
        """
        request = self.__prepare_get_layout_slides_list_request()
        request.name = self.get_invalid_test_value('get_layout_slides_list', 'name', request.name, 'str')
        self.initialize('get_layout_slides_list', 'name', request.name)
        ok = False
        try:
            self.api.get_layout_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slides_list', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_layout_slides_list', 'name')

    def test_get_layout_slides_list_invalid_password(self):
        """Test case for get_layout_slides_list with invalid password
        """
        request = self.__prepare_get_layout_slides_list_request()
        request.password = self.get_invalid_test_value('get_layout_slides_list', 'password', request.password, 'str')
        self.initialize('get_layout_slides_list', 'password', request.password)
        ok = False
        try:
            self.api.get_layout_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slides_list', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_layout_slides_list', 'password')

    def test_get_layout_slides_list_invalid_folder(self):
        """Test case for get_layout_slides_list with invalid folder
        """
        request = self.__prepare_get_layout_slides_list_request()
        request.folder = self.get_invalid_test_value('get_layout_slides_list', 'folder', request.folder, 'str')
        self.initialize('get_layout_slides_list', 'folder', request.folder)
        ok = False
        try:
            self.api.get_layout_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slides_list', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_layout_slides_list', 'folder')

    def test_get_layout_slides_list_invalid_storage(self):
        """Test case for get_layout_slides_list with invalid storage
        """
        request = self.__prepare_get_layout_slides_list_request()
        request.storage = self.get_invalid_test_value('get_layout_slides_list', 'storage', request.storage, 'str')
        self.initialize('get_layout_slides_list', 'storage', request.storage)
        ok = False
        try:
            self.api.get_layout_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_layout_slides_list', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_layout_slides_list', 'storage')

    def __prepare_get_layout_slides_list_request(self):
        name = self.get_test_value('get_layout_slides_list', 'name', 'str')
        password = self.get_test_value('get_layout_slides_list', 'password', 'str')
        folder = self.get_test_value('get_layout_slides_list', 'folder', 'str')
        storage = self.get_test_value('get_layout_slides_list', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetLayoutSlidesListRequest(name, password, folder, storage)

    def test_get_master_slide(self):
        """Test case for get_master_slide
        """
        request = self.__prepare_get_master_slide_request()
        self.initialize('get_master_slide', None, None)
        response = self.api.get_master_slide(request)
        self.assertIsNotNone(response)

    def test_get_master_slide_invalid_name(self):
        """Test case for get_master_slide with invalid name
        """
        request = self.__prepare_get_master_slide_request()
        request.name = self.get_invalid_test_value('get_master_slide', 'name', request.name, 'str')
        self.initialize('get_master_slide', 'name', request.name)
        ok = False
        try:
            self.api.get_master_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_master_slide', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_master_slide', 'name')

    def test_get_master_slide_invalid_slide_index(self):
        """Test case for get_master_slide with invalid slide_index
        """
        request = self.__prepare_get_master_slide_request()
        request.slide_index = self.get_invalid_test_value('get_master_slide', 'slide_index', request.slide_index, 'int')
        self.initialize('get_master_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_master_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_master_slide', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_master_slide', 'slide_index')

    def test_get_master_slide_invalid_password(self):
        """Test case for get_master_slide with invalid password
        """
        request = self.__prepare_get_master_slide_request()
        request.password = self.get_invalid_test_value('get_master_slide', 'password', request.password, 'str')
        self.initialize('get_master_slide', 'password', request.password)
        ok = False
        try:
            self.api.get_master_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_master_slide', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_master_slide', 'password')

    def test_get_master_slide_invalid_folder(self):
        """Test case for get_master_slide with invalid folder
        """
        request = self.__prepare_get_master_slide_request()
        request.folder = self.get_invalid_test_value('get_master_slide', 'folder', request.folder, 'str')
        self.initialize('get_master_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.get_master_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_master_slide', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_master_slide', 'folder')

    def test_get_master_slide_invalid_storage(self):
        """Test case for get_master_slide with invalid storage
        """
        request = self.__prepare_get_master_slide_request()
        request.storage = self.get_invalid_test_value('get_master_slide', 'storage', request.storage, 'str')
        self.initialize('get_master_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.get_master_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_master_slide', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_master_slide', 'storage')

    def __prepare_get_master_slide_request(self):
        name = self.get_test_value('get_master_slide', 'name', 'str')
        slide_index = self.get_test_value('get_master_slide', 'slide_index', 'int')
        password = self.get_test_value('get_master_slide', 'password', 'str')
        folder = self.get_test_value('get_master_slide', 'folder', 'str')
        storage = self.get_test_value('get_master_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetMasterSlideRequest(name, slide_index, password, folder, storage)

    def test_get_master_slides_list(self):
        """Test case for get_master_slides_list
        """
        request = self.__prepare_get_master_slides_list_request()
        self.initialize('get_master_slides_list', None, None)
        response = self.api.get_master_slides_list(request)
        self.assertIsNotNone(response)

    def test_get_master_slides_list_invalid_name(self):
        """Test case for get_master_slides_list with invalid name
        """
        request = self.__prepare_get_master_slides_list_request()
        request.name = self.get_invalid_test_value('get_master_slides_list', 'name', request.name, 'str')
        self.initialize('get_master_slides_list', 'name', request.name)
        ok = False
        try:
            self.api.get_master_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_master_slides_list', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_master_slides_list', 'name')

    def test_get_master_slides_list_invalid_password(self):
        """Test case for get_master_slides_list with invalid password
        """
        request = self.__prepare_get_master_slides_list_request()
        request.password = self.get_invalid_test_value('get_master_slides_list', 'password', request.password, 'str')
        self.initialize('get_master_slides_list', 'password', request.password)
        ok = False
        try:
            self.api.get_master_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_master_slides_list', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_master_slides_list', 'password')

    def test_get_master_slides_list_invalid_folder(self):
        """Test case for get_master_slides_list with invalid folder
        """
        request = self.__prepare_get_master_slides_list_request()
        request.folder = self.get_invalid_test_value('get_master_slides_list', 'folder', request.folder, 'str')
        self.initialize('get_master_slides_list', 'folder', request.folder)
        ok = False
        try:
            self.api.get_master_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_master_slides_list', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_master_slides_list', 'folder')

    def test_get_master_slides_list_invalid_storage(self):
        """Test case for get_master_slides_list with invalid storage
        """
        request = self.__prepare_get_master_slides_list_request()
        request.storage = self.get_invalid_test_value('get_master_slides_list', 'storage', request.storage, 'str')
        self.initialize('get_master_slides_list', 'storage', request.storage)
        ok = False
        try:
            self.api.get_master_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_master_slides_list', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_master_slides_list', 'storage')

    def __prepare_get_master_slides_list_request(self):
        name = self.get_test_value('get_master_slides_list', 'name', 'str')
        password = self.get_test_value('get_master_slides_list', 'password', 'str')
        folder = self.get_test_value('get_master_slides_list', 'folder', 'str')
        storage = self.get_test_value('get_master_slides_list', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetMasterSlidesListRequest(name, password, folder, storage)

    def test_get_notes_slide(self):
        """Test case for get_notes_slide
        """
        request = self.__prepare_get_notes_slide_request()
        self.initialize('get_notes_slide', None, None)
        response = self.api.get_notes_slide(request)
        self.assertIsNotNone(response)

    def test_get_notes_slide_invalid_name(self):
        """Test case for get_notes_slide with invalid name
        """
        request = self.__prepare_get_notes_slide_request()
        request.name = self.get_invalid_test_value('get_notes_slide', 'name', request.name, 'str')
        self.initialize('get_notes_slide', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide', 'name')

    def test_get_notes_slide_invalid_slide_index(self):
        """Test case for get_notes_slide with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_request()
        request.slide_index = self.get_invalid_test_value('get_notes_slide', 'slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide', 'slide_index')

    def test_get_notes_slide_invalid_password(self):
        """Test case for get_notes_slide with invalid password
        """
        request = self.__prepare_get_notes_slide_request()
        request.password = self.get_invalid_test_value('get_notes_slide', 'password', request.password, 'str')
        self.initialize('get_notes_slide', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide', 'password')

    def test_get_notes_slide_invalid_folder(self):
        """Test case for get_notes_slide with invalid folder
        """
        request = self.__prepare_get_notes_slide_request()
        request.folder = self.get_invalid_test_value('get_notes_slide', 'folder', request.folder, 'str')
        self.initialize('get_notes_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide', 'folder')

    def test_get_notes_slide_invalid_storage(self):
        """Test case for get_notes_slide with invalid storage
        """
        request = self.__prepare_get_notes_slide_request()
        request.storage = self.get_invalid_test_value('get_notes_slide', 'storage', request.storage, 'str')
        self.initialize('get_notes_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide', 'storage')

    def __prepare_get_notes_slide_request(self):
        name = self.get_test_value('get_notes_slide', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide', 'slide_index', 'int')
        password = self.get_test_value('get_notes_slide', 'password', 'str')
        folder = self.get_test_value('get_notes_slide', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetNotesSlideRequest(name, slide_index, password, folder, storage)

    def test_get_notes_slide_exists(self):
        """Test case for get_notes_slide_exists
        """
        request = self.__prepare_get_notes_slide_exists_request()
        self.initialize('get_notes_slide_exists', None, None)
        response = self.api.get_notes_slide_exists(request)
        self.assertIsNotNone(response)

    def test_get_notes_slide_exists_invalid_name(self):
        """Test case for get_notes_slide_exists with invalid name
        """
        request = self.__prepare_get_notes_slide_exists_request()
        request.name = self.get_invalid_test_value('get_notes_slide_exists', 'name', request.name, 'str')
        self.initialize('get_notes_slide_exists', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_exists', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_exists', 'name')

    def test_get_notes_slide_exists_invalid_slide_index(self):
        """Test case for get_notes_slide_exists with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_exists_request()
        request.slide_index = self.get_invalid_test_value('get_notes_slide_exists', 'slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide_exists', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_exists', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_exists', 'slide_index')

    def test_get_notes_slide_exists_invalid_password(self):
        """Test case for get_notes_slide_exists with invalid password
        """
        request = self.__prepare_get_notes_slide_exists_request()
        request.password = self.get_invalid_test_value('get_notes_slide_exists', 'password', request.password, 'str')
        self.initialize('get_notes_slide_exists', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_exists', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_exists', 'password')

    def test_get_notes_slide_exists_invalid_folder(self):
        """Test case for get_notes_slide_exists with invalid folder
        """
        request = self.__prepare_get_notes_slide_exists_request()
        request.folder = self.get_invalid_test_value('get_notes_slide_exists', 'folder', request.folder, 'str')
        self.initialize('get_notes_slide_exists', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_exists', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_exists', 'folder')

    def test_get_notes_slide_exists_invalid_storage(self):
        """Test case for get_notes_slide_exists with invalid storage
        """
        request = self.__prepare_get_notes_slide_exists_request()
        request.storage = self.get_invalid_test_value('get_notes_slide_exists', 'storage', request.storage, 'str')
        self.initialize('get_notes_slide_exists', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_exists', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_exists', 'storage')

    def __prepare_get_notes_slide_exists_request(self):
        name = self.get_test_value('get_notes_slide_exists', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide_exists', 'slide_index', 'int')
        password = self.get_test_value('get_notes_slide_exists', 'password', 'str')
        folder = self.get_test_value('get_notes_slide_exists', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide_exists', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetNotesSlideExistsRequest(name, slide_index, password, folder, storage)

    def test_get_notes_slide_shape(self):
        """Test case for get_notes_slide_shape
        """
        request = self.__prepare_get_notes_slide_shape_request()
        self.initialize('get_notes_slide_shape', None, None)
        response = self.api.get_notes_slide_shape(request)
        self.assertIsNotNone(response)

    def test_get_notes_slide_shape_invalid_name(self):
        """Test case for get_notes_slide_shape with invalid name
        """
        request = self.__prepare_get_notes_slide_shape_request()
        request.name = self.get_invalid_test_value('get_notes_slide_shape', 'name', request.name, 'str')
        self.initialize('get_notes_slide_shape', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape', 'name')

    def test_get_notes_slide_shape_invalid_slide_index(self):
        """Test case for get_notes_slide_shape with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_shape_request()
        request.slide_index = self.get_invalid_test_value('get_notes_slide_shape', 'slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide_shape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape', 'slide_index')

    def test_get_notes_slide_shape_invalid_shape_index(self):
        """Test case for get_notes_slide_shape with invalid shape_index
        """
        request = self.__prepare_get_notes_slide_shape_request()
        request.shape_index = self.get_invalid_test_value('get_notes_slide_shape', 'shape_index', request.shape_index, 'int')
        self.initialize('get_notes_slide_shape', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape', 'shape_index')

    def test_get_notes_slide_shape_invalid_password(self):
        """Test case for get_notes_slide_shape with invalid password
        """
        request = self.__prepare_get_notes_slide_shape_request()
        request.password = self.get_invalid_test_value('get_notes_slide_shape', 'password', request.password, 'str')
        self.initialize('get_notes_slide_shape', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape', 'password')

    def test_get_notes_slide_shape_invalid_folder(self):
        """Test case for get_notes_slide_shape with invalid folder
        """
        request = self.__prepare_get_notes_slide_shape_request()
        request.folder = self.get_invalid_test_value('get_notes_slide_shape', 'folder', request.folder, 'str')
        self.initialize('get_notes_slide_shape', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape', 'folder')

    def test_get_notes_slide_shape_invalid_storage(self):
        """Test case for get_notes_slide_shape with invalid storage
        """
        request = self.__prepare_get_notes_slide_shape_request()
        request.storage = self.get_invalid_test_value('get_notes_slide_shape', 'storage', request.storage, 'str')
        self.initialize('get_notes_slide_shape', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape', 'storage')

    def __prepare_get_notes_slide_shape_request(self):
        name = self.get_test_value('get_notes_slide_shape', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide_shape', 'slide_index', 'int')
        shape_index = self.get_test_value('get_notes_slide_shape', 'shape_index', 'int')
        password = self.get_test_value('get_notes_slide_shape', 'password', 'str')
        folder = self.get_test_value('get_notes_slide_shape', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide_shape', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetNotesSlideShapeRequest(name, slide_index, shape_index, password, folder, storage)

    def test_get_notes_slide_shape_paragraph(self):
        """Test case for get_notes_slide_shape_paragraph
        """
        request = self.__prepare_get_notes_slide_shape_paragraph_request()
        self.initialize('get_notes_slide_shape_paragraph', None, None)
        response = self.api.get_notes_slide_shape_paragraph(request)
        self.assertIsNotNone(response)

    def test_get_notes_slide_shape_paragraph_invalid_name(self):
        """Test case for get_notes_slide_shape_paragraph with invalid name
        """
        request = self.__prepare_get_notes_slide_shape_paragraph_request()
        request.name = self.get_invalid_test_value('get_notes_slide_shape_paragraph', 'name', request.name, 'str')
        self.initialize('get_notes_slide_shape_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraph', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraph', 'name')

    def test_get_notes_slide_shape_paragraph_invalid_slide_index(self):
        """Test case for get_notes_slide_shape_paragraph with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_shape_paragraph_request()
        request.slide_index = self.get_invalid_test_value('get_notes_slide_shape_paragraph', 'slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide_shape_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraph', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraph', 'slide_index')

    def test_get_notes_slide_shape_paragraph_invalid_shape_index(self):
        """Test case for get_notes_slide_shape_paragraph with invalid shape_index
        """
        request = self.__prepare_get_notes_slide_shape_paragraph_request()
        request.shape_index = self.get_invalid_test_value('get_notes_slide_shape_paragraph', 'shape_index', request.shape_index, 'int')
        self.initialize('get_notes_slide_shape_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraph', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraph', 'shape_index')

    def test_get_notes_slide_shape_paragraph_invalid_paragraph_index(self):
        """Test case for get_notes_slide_shape_paragraph with invalid paragraph_index
        """
        request = self.__prepare_get_notes_slide_shape_paragraph_request()
        request.paragraph_index = self.get_invalid_test_value('get_notes_slide_shape_paragraph', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_notes_slide_shape_paragraph', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraph', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraph', 'paragraph_index')

    def test_get_notes_slide_shape_paragraph_invalid_password(self):
        """Test case for get_notes_slide_shape_paragraph with invalid password
        """
        request = self.__prepare_get_notes_slide_shape_paragraph_request()
        request.password = self.get_invalid_test_value('get_notes_slide_shape_paragraph', 'password', request.password, 'str')
        self.initialize('get_notes_slide_shape_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraph', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraph', 'password')

    def test_get_notes_slide_shape_paragraph_invalid_folder(self):
        """Test case for get_notes_slide_shape_paragraph with invalid folder
        """
        request = self.__prepare_get_notes_slide_shape_paragraph_request()
        request.folder = self.get_invalid_test_value('get_notes_slide_shape_paragraph', 'folder', request.folder, 'str')
        self.initialize('get_notes_slide_shape_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraph', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraph', 'folder')

    def test_get_notes_slide_shape_paragraph_invalid_storage(self):
        """Test case for get_notes_slide_shape_paragraph with invalid storage
        """
        request = self.__prepare_get_notes_slide_shape_paragraph_request()
        request.storage = self.get_invalid_test_value('get_notes_slide_shape_paragraph', 'storage', request.storage, 'str')
        self.initialize('get_notes_slide_shape_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraph', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraph', 'storage')

    def __prepare_get_notes_slide_shape_paragraph_request(self):
        name = self.get_test_value('get_notes_slide_shape_paragraph', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide_shape_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('get_notes_slide_shape_paragraph', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_notes_slide_shape_paragraph', 'paragraph_index', 'int')
        password = self.get_test_value('get_notes_slide_shape_paragraph', 'password', 'str')
        folder = self.get_test_value('get_notes_slide_shape_paragraph', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide_shape_paragraph', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetNotesSlideShapeParagraphRequest(name, slide_index, shape_index, paragraph_index, password, folder, storage)

    def test_get_notes_slide_shape_paragraphs(self):
        """Test case for get_notes_slide_shape_paragraphs
        """
        request = self.__prepare_get_notes_slide_shape_paragraphs_request()
        self.initialize('get_notes_slide_shape_paragraphs', None, None)
        response = self.api.get_notes_slide_shape_paragraphs(request)
        self.assertIsNotNone(response)

    def test_get_notes_slide_shape_paragraphs_invalid_name(self):
        """Test case for get_notes_slide_shape_paragraphs with invalid name
        """
        request = self.__prepare_get_notes_slide_shape_paragraphs_request()
        request.name = self.get_invalid_test_value('get_notes_slide_shape_paragraphs', 'name', request.name, 'str')
        self.initialize('get_notes_slide_shape_paragraphs', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraphs', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraphs', 'name')

    def test_get_notes_slide_shape_paragraphs_invalid_slide_index(self):
        """Test case for get_notes_slide_shape_paragraphs with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_shape_paragraphs_request()
        request.slide_index = self.get_invalid_test_value('get_notes_slide_shape_paragraphs', 'slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide_shape_paragraphs', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraphs', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraphs', 'slide_index')

    def test_get_notes_slide_shape_paragraphs_invalid_shape_index(self):
        """Test case for get_notes_slide_shape_paragraphs with invalid shape_index
        """
        request = self.__prepare_get_notes_slide_shape_paragraphs_request()
        request.shape_index = self.get_invalid_test_value('get_notes_slide_shape_paragraphs', 'shape_index', request.shape_index, 'int')
        self.initialize('get_notes_slide_shape_paragraphs', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraphs', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraphs', 'shape_index')

    def test_get_notes_slide_shape_paragraphs_invalid_password(self):
        """Test case for get_notes_slide_shape_paragraphs with invalid password
        """
        request = self.__prepare_get_notes_slide_shape_paragraphs_request()
        request.password = self.get_invalid_test_value('get_notes_slide_shape_paragraphs', 'password', request.password, 'str')
        self.initialize('get_notes_slide_shape_paragraphs', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraphs', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraphs', 'password')

    def test_get_notes_slide_shape_paragraphs_invalid_folder(self):
        """Test case for get_notes_slide_shape_paragraphs with invalid folder
        """
        request = self.__prepare_get_notes_slide_shape_paragraphs_request()
        request.folder = self.get_invalid_test_value('get_notes_slide_shape_paragraphs', 'folder', request.folder, 'str')
        self.initialize('get_notes_slide_shape_paragraphs', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraphs', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraphs', 'folder')

    def test_get_notes_slide_shape_paragraphs_invalid_storage(self):
        """Test case for get_notes_slide_shape_paragraphs with invalid storage
        """
        request = self.__prepare_get_notes_slide_shape_paragraphs_request()
        request.storage = self.get_invalid_test_value('get_notes_slide_shape_paragraphs', 'storage', request.storage, 'str')
        self.initialize('get_notes_slide_shape_paragraphs', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_paragraphs', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_paragraphs', 'storage')

    def __prepare_get_notes_slide_shape_paragraphs_request(self):
        name = self.get_test_value('get_notes_slide_shape_paragraphs', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide_shape_paragraphs', 'slide_index', 'int')
        shape_index = self.get_test_value('get_notes_slide_shape_paragraphs', 'shape_index', 'int')
        password = self.get_test_value('get_notes_slide_shape_paragraphs', 'password', 'str')
        folder = self.get_test_value('get_notes_slide_shape_paragraphs', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide_shape_paragraphs', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetNotesSlideShapeParagraphsRequest(name, slide_index, shape_index, password, folder, storage)

    def test_get_notes_slide_shape_portion(self):
        """Test case for get_notes_slide_shape_portion
        """
        request = self.__prepare_get_notes_slide_shape_portion_request()
        self.initialize('get_notes_slide_shape_portion', None, None)
        response = self.api.get_notes_slide_shape_portion(request)
        self.assertIsNotNone(response)

    def test_get_notes_slide_shape_portion_invalid_name(self):
        """Test case for get_notes_slide_shape_portion with invalid name
        """
        request = self.__prepare_get_notes_slide_shape_portion_request()
        request.name = self.get_invalid_test_value('get_notes_slide_shape_portion', 'name', request.name, 'str')
        self.initialize('get_notes_slide_shape_portion', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portion', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portion', 'name')

    def test_get_notes_slide_shape_portion_invalid_slide_index(self):
        """Test case for get_notes_slide_shape_portion with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_shape_portion_request()
        request.slide_index = self.get_invalid_test_value('get_notes_slide_shape_portion', 'slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide_shape_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portion', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portion', 'slide_index')

    def test_get_notes_slide_shape_portion_invalid_shape_index(self):
        """Test case for get_notes_slide_shape_portion with invalid shape_index
        """
        request = self.__prepare_get_notes_slide_shape_portion_request()
        request.shape_index = self.get_invalid_test_value('get_notes_slide_shape_portion', 'shape_index', request.shape_index, 'int')
        self.initialize('get_notes_slide_shape_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portion', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portion', 'shape_index')

    def test_get_notes_slide_shape_portion_invalid_paragraph_index(self):
        """Test case for get_notes_slide_shape_portion with invalid paragraph_index
        """
        request = self.__prepare_get_notes_slide_shape_portion_request()
        request.paragraph_index = self.get_invalid_test_value('get_notes_slide_shape_portion', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_notes_slide_shape_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portion', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portion', 'paragraph_index')

    def test_get_notes_slide_shape_portion_invalid_portion_index(self):
        """Test case for get_notes_slide_shape_portion with invalid portion_index
        """
        request = self.__prepare_get_notes_slide_shape_portion_request()
        request.portion_index = self.get_invalid_test_value('get_notes_slide_shape_portion', 'portion_index', request.portion_index, 'int')
        self.initialize('get_notes_slide_shape_portion', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portion', 'portion_index', request.portion_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portion', 'portion_index')

    def test_get_notes_slide_shape_portion_invalid_password(self):
        """Test case for get_notes_slide_shape_portion with invalid password
        """
        request = self.__prepare_get_notes_slide_shape_portion_request()
        request.password = self.get_invalid_test_value('get_notes_slide_shape_portion', 'password', request.password, 'str')
        self.initialize('get_notes_slide_shape_portion', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portion', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portion', 'password')

    def test_get_notes_slide_shape_portion_invalid_folder(self):
        """Test case for get_notes_slide_shape_portion with invalid folder
        """
        request = self.__prepare_get_notes_slide_shape_portion_request()
        request.folder = self.get_invalid_test_value('get_notes_slide_shape_portion', 'folder', request.folder, 'str')
        self.initialize('get_notes_slide_shape_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portion', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portion', 'folder')

    def test_get_notes_slide_shape_portion_invalid_storage(self):
        """Test case for get_notes_slide_shape_portion with invalid storage
        """
        request = self.__prepare_get_notes_slide_shape_portion_request()
        request.storage = self.get_invalid_test_value('get_notes_slide_shape_portion', 'storage', request.storage, 'str')
        self.initialize('get_notes_slide_shape_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portion', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portion', 'storage')

    def __prepare_get_notes_slide_shape_portion_request(self):
        name = self.get_test_value('get_notes_slide_shape_portion', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide_shape_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('get_notes_slide_shape_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_notes_slide_shape_portion', 'paragraph_index', 'int')
        portion_index = self.get_test_value('get_notes_slide_shape_portion', 'portion_index', 'int')
        password = self.get_test_value('get_notes_slide_shape_portion', 'password', 'str')
        folder = self.get_test_value('get_notes_slide_shape_portion', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide_shape_portion', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetNotesSlideShapePortionRequest(name, slide_index, shape_index, paragraph_index, portion_index, password, folder, storage)

    def test_get_notes_slide_shape_portions(self):
        """Test case for get_notes_slide_shape_portions
        """
        request = self.__prepare_get_notes_slide_shape_portions_request()
        self.initialize('get_notes_slide_shape_portions', None, None)
        response = self.api.get_notes_slide_shape_portions(request)
        self.assertIsNotNone(response)

    def test_get_notes_slide_shape_portions_invalid_name(self):
        """Test case for get_notes_slide_shape_portions with invalid name
        """
        request = self.__prepare_get_notes_slide_shape_portions_request()
        request.name = self.get_invalid_test_value('get_notes_slide_shape_portions', 'name', request.name, 'str')
        self.initialize('get_notes_slide_shape_portions', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide_shape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portions', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portions', 'name')

    def test_get_notes_slide_shape_portions_invalid_slide_index(self):
        """Test case for get_notes_slide_shape_portions with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_shape_portions_request()
        request.slide_index = self.get_invalid_test_value('get_notes_slide_shape_portions', 'slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide_shape_portions', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portions', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portions', 'slide_index')

    def test_get_notes_slide_shape_portions_invalid_shape_index(self):
        """Test case for get_notes_slide_shape_portions with invalid shape_index
        """
        request = self.__prepare_get_notes_slide_shape_portions_request()
        request.shape_index = self.get_invalid_test_value('get_notes_slide_shape_portions', 'shape_index', request.shape_index, 'int')
        self.initialize('get_notes_slide_shape_portions', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portions', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portions', 'shape_index')

    def test_get_notes_slide_shape_portions_invalid_paragraph_index(self):
        """Test case for get_notes_slide_shape_portions with invalid paragraph_index
        """
        request = self.__prepare_get_notes_slide_shape_portions_request()
        request.paragraph_index = self.get_invalid_test_value('get_notes_slide_shape_portions', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_notes_slide_shape_portions', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_notes_slide_shape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portions', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portions', 'paragraph_index')

    def test_get_notes_slide_shape_portions_invalid_password(self):
        """Test case for get_notes_slide_shape_portions with invalid password
        """
        request = self.__prepare_get_notes_slide_shape_portions_request()
        request.password = self.get_invalid_test_value('get_notes_slide_shape_portions', 'password', request.password, 'str')
        self.initialize('get_notes_slide_shape_portions', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide_shape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portions', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portions', 'password')

    def test_get_notes_slide_shape_portions_invalid_folder(self):
        """Test case for get_notes_slide_shape_portions with invalid folder
        """
        request = self.__prepare_get_notes_slide_shape_portions_request()
        request.folder = self.get_invalid_test_value('get_notes_slide_shape_portions', 'folder', request.folder, 'str')
        self.initialize('get_notes_slide_shape_portions', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide_shape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portions', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portions', 'folder')

    def test_get_notes_slide_shape_portions_invalid_storage(self):
        """Test case for get_notes_slide_shape_portions with invalid storage
        """
        request = self.__prepare_get_notes_slide_shape_portions_request()
        request.storage = self.get_invalid_test_value('get_notes_slide_shape_portions', 'storage', request.storage, 'str')
        self.initialize('get_notes_slide_shape_portions', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide_shape_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shape_portions', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shape_portions', 'storage')

    def __prepare_get_notes_slide_shape_portions_request(self):
        name = self.get_test_value('get_notes_slide_shape_portions', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide_shape_portions', 'slide_index', 'int')
        shape_index = self.get_test_value('get_notes_slide_shape_portions', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_notes_slide_shape_portions', 'paragraph_index', 'int')
        password = self.get_test_value('get_notes_slide_shape_portions', 'password', 'str')
        folder = self.get_test_value('get_notes_slide_shape_portions', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide_shape_portions', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetNotesSlideShapePortionsRequest(name, slide_index, shape_index, paragraph_index, password, folder, storage)

    def test_get_notes_slide_shapes(self):
        """Test case for get_notes_slide_shapes
        """
        request = self.__prepare_get_notes_slide_shapes_request()
        self.initialize('get_notes_slide_shapes', None, None)
        response = self.api.get_notes_slide_shapes(request)
        self.assertIsNotNone(response)

    def test_get_notes_slide_shapes_invalid_name(self):
        """Test case for get_notes_slide_shapes with invalid name
        """
        request = self.__prepare_get_notes_slide_shapes_request()
        request.name = self.get_invalid_test_value('get_notes_slide_shapes', 'name', request.name, 'str')
        self.initialize('get_notes_slide_shapes', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shapes', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shapes', 'name')

    def test_get_notes_slide_shapes_invalid_slide_index(self):
        """Test case for get_notes_slide_shapes with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_shapes_request()
        request.slide_index = self.get_invalid_test_value('get_notes_slide_shapes', 'slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide_shapes', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shapes', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shapes', 'slide_index')

    def test_get_notes_slide_shapes_invalid_password(self):
        """Test case for get_notes_slide_shapes with invalid password
        """
        request = self.__prepare_get_notes_slide_shapes_request()
        request.password = self.get_invalid_test_value('get_notes_slide_shapes', 'password', request.password, 'str')
        self.initialize('get_notes_slide_shapes', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shapes', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shapes', 'password')

    def test_get_notes_slide_shapes_invalid_folder(self):
        """Test case for get_notes_slide_shapes with invalid folder
        """
        request = self.__prepare_get_notes_slide_shapes_request()
        request.folder = self.get_invalid_test_value('get_notes_slide_shapes', 'folder', request.folder, 'str')
        self.initialize('get_notes_slide_shapes', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shapes', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shapes', 'folder')

    def test_get_notes_slide_shapes_invalid_storage(self):
        """Test case for get_notes_slide_shapes with invalid storage
        """
        request = self.__prepare_get_notes_slide_shapes_request()
        request.storage = self.get_invalid_test_value('get_notes_slide_shapes', 'storage', request.storage, 'str')
        self.initialize('get_notes_slide_shapes', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_shapes', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_shapes', 'storage')

    def __prepare_get_notes_slide_shapes_request(self):
        name = self.get_test_value('get_notes_slide_shapes', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide_shapes', 'slide_index', 'int')
        password = self.get_test_value('get_notes_slide_shapes', 'password', 'str')
        folder = self.get_test_value('get_notes_slide_shapes', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide_shapes', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetNotesSlideShapesRequest(name, slide_index, password, folder, storage)

    def test_get_notes_slide_with_format(self):
        """Test case for get_notes_slide_with_format
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        self.initialize('get_notes_slide_with_format', None, None)
        response = self.api.get_notes_slide_with_format(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_get_notes_slide_with_format_invalid_name(self):
        """Test case for get_notes_slide_with_format with invalid name
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.name = self.get_invalid_test_value('get_notes_slide_with_format', 'name', request.name, 'str')
        self.initialize('get_notes_slide_with_format', 'name', request.name)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'name')

    def test_get_notes_slide_with_format_invalid_slide_index(self):
        """Test case for get_notes_slide_with_format with invalid slide_index
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.slide_index = self.get_invalid_test_value('get_notes_slide_with_format', 'slide_index', request.slide_index, 'int')
        self.initialize('get_notes_slide_with_format', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'slide_index')

    def test_get_notes_slide_with_format_invalid_format(self):
        """Test case for get_notes_slide_with_format with invalid format
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.format = self.get_invalid_test_value('get_notes_slide_with_format', 'format', request.format, 'str')
        self.initialize('get_notes_slide_with_format', 'format', request.format)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'format')

    def test_get_notes_slide_with_format_invalid_width(self):
        """Test case for get_notes_slide_with_format with invalid width
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.width = self.get_invalid_test_value('get_notes_slide_with_format', 'width', request.width, 'int')
        self.initialize('get_notes_slide_with_format', 'width', request.width)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'width', request.width)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'width')

    def test_get_notes_slide_with_format_invalid_height(self):
        """Test case for get_notes_slide_with_format with invalid height
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.height = self.get_invalid_test_value('get_notes_slide_with_format', 'height', request.height, 'int')
        self.initialize('get_notes_slide_with_format', 'height', request.height)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'height', request.height)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'height')

    def test_get_notes_slide_with_format_invalid_password(self):
        """Test case for get_notes_slide_with_format with invalid password
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.password = self.get_invalid_test_value('get_notes_slide_with_format', 'password', request.password, 'str')
        self.initialize('get_notes_slide_with_format', 'password', request.password)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'password')

    def test_get_notes_slide_with_format_invalid_folder(self):
        """Test case for get_notes_slide_with_format with invalid folder
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.folder = self.get_invalid_test_value('get_notes_slide_with_format', 'folder', request.folder, 'str')
        self.initialize('get_notes_slide_with_format', 'folder', request.folder)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'folder')

    def test_get_notes_slide_with_format_invalid_storage(self):
        """Test case for get_notes_slide_with_format with invalid storage
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.storage = self.get_invalid_test_value('get_notes_slide_with_format', 'storage', request.storage, 'str')
        self.initialize('get_notes_slide_with_format', 'storage', request.storage)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'storage')

    def test_get_notes_slide_with_format_invalid_fonts_folder(self):
        """Test case for get_notes_slide_with_format with invalid fonts_folder
        """
        request = self.__prepare_get_notes_slide_with_format_request()
        request.fonts_folder = self.get_invalid_test_value('get_notes_slide_with_format', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('get_notes_slide_with_format', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_notes_slide_with_format', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_notes_slide_with_format', 'fonts_folder')

    def __prepare_get_notes_slide_with_format_request(self):
        name = self.get_test_value('get_notes_slide_with_format', 'name', 'str')
        slide_index = self.get_test_value('get_notes_slide_with_format', 'slide_index', 'int')
        format = self.get_test_value('get_notes_slide_with_format', 'format', 'str')
        width = self.get_test_value('get_notes_slide_with_format', 'width', 'int')
        height = self.get_test_value('get_notes_slide_with_format', 'height', 'int')
        password = self.get_test_value('get_notes_slide_with_format', 'password', 'str')
        folder = self.get_test_value('get_notes_slide_with_format', 'folder', 'str')
        storage = self.get_test_value('get_notes_slide_with_format', 'storage', 'str')
        fonts_folder = self.get_test_value('get_notes_slide_with_format', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetNotesSlideWithFormatRequest(name, slide_index, format, width, height, password, folder, storage, fonts_folder)

    def test_get_paragraph_portion(self):
        """Test case for get_paragraph_portion
        """
        request = self.__prepare_get_paragraph_portion_request()
        self.initialize('get_paragraph_portion', None, None)
        response = self.api.get_paragraph_portion(request)
        self.assertIsNotNone(response)

    def test_get_paragraph_portion_invalid_name(self):
        """Test case for get_paragraph_portion with invalid name
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.name = self.get_invalid_test_value('get_paragraph_portion', 'name', request.name, 'str')
        self.initialize('get_paragraph_portion', 'name', request.name)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'name')

    def test_get_paragraph_portion_invalid_slide_index(self):
        """Test case for get_paragraph_portion with invalid slide_index
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.slide_index = self.get_invalid_test_value('get_paragraph_portion', 'slide_index', request.slide_index, 'int')
        self.initialize('get_paragraph_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'slide_index')

    def test_get_paragraph_portion_invalid_shape_index(self):
        """Test case for get_paragraph_portion with invalid shape_index
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.shape_index = self.get_invalid_test_value('get_paragraph_portion', 'shape_index', request.shape_index, 'int')
        self.initialize('get_paragraph_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'shape_index')

    def test_get_paragraph_portion_invalid_paragraph_index(self):
        """Test case for get_paragraph_portion with invalid paragraph_index
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.paragraph_index = self.get_invalid_test_value('get_paragraph_portion', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_paragraph_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'paragraph_index')

    def test_get_paragraph_portion_invalid_portion_index(self):
        """Test case for get_paragraph_portion with invalid portion_index
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.portion_index = self.get_invalid_test_value('get_paragraph_portion', 'portion_index', request.portion_index, 'int')
        self.initialize('get_paragraph_portion', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'portion_index', request.portion_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'portion_index')

    def test_get_paragraph_portion_invalid_password(self):
        """Test case for get_paragraph_portion with invalid password
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.password = self.get_invalid_test_value('get_paragraph_portion', 'password', request.password, 'str')
        self.initialize('get_paragraph_portion', 'password', request.password)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'password')

    def test_get_paragraph_portion_invalid_folder(self):
        """Test case for get_paragraph_portion with invalid folder
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.folder = self.get_invalid_test_value('get_paragraph_portion', 'folder', request.folder, 'str')
        self.initialize('get_paragraph_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'folder')

    def test_get_paragraph_portion_invalid_storage(self):
        """Test case for get_paragraph_portion with invalid storage
        """
        request = self.__prepare_get_paragraph_portion_request()
        request.storage = self.get_invalid_test_value('get_paragraph_portion', 'storage', request.storage, 'str')
        self.initialize('get_paragraph_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.get_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portion', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portion', 'storage')

    def __prepare_get_paragraph_portion_request(self):
        name = self.get_test_value('get_paragraph_portion', 'name', 'str')
        slide_index = self.get_test_value('get_paragraph_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('get_paragraph_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_paragraph_portion', 'paragraph_index', 'int')
        portion_index = self.get_test_value('get_paragraph_portion', 'portion_index', 'int')
        password = self.get_test_value('get_paragraph_portion', 'password', 'str')
        folder = self.get_test_value('get_paragraph_portion', 'folder', 'str')
        storage = self.get_test_value('get_paragraph_portion', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetParagraphPortionRequest(name, slide_index, shape_index, paragraph_index, portion_index, password, folder, storage)

    def test_get_paragraph_portions(self):
        """Test case for get_paragraph_portions
        """
        request = self.__prepare_get_paragraph_portions_request()
        self.initialize('get_paragraph_portions', None, None)
        response = self.api.get_paragraph_portions(request)
        self.assertIsNotNone(response)

    def test_get_paragraph_portions_invalid_name(self):
        """Test case for get_paragraph_portions with invalid name
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.name = self.get_invalid_test_value('get_paragraph_portions', 'name', request.name, 'str')
        self.initialize('get_paragraph_portions', 'name', request.name)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'name')

    def test_get_paragraph_portions_invalid_slide_index(self):
        """Test case for get_paragraph_portions with invalid slide_index
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.slide_index = self.get_invalid_test_value('get_paragraph_portions', 'slide_index', request.slide_index, 'int')
        self.initialize('get_paragraph_portions', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'slide_index')

    def test_get_paragraph_portions_invalid_shape_index(self):
        """Test case for get_paragraph_portions with invalid shape_index
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.shape_index = self.get_invalid_test_value('get_paragraph_portions', 'shape_index', request.shape_index, 'int')
        self.initialize('get_paragraph_portions', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'shape_index')

    def test_get_paragraph_portions_invalid_paragraph_index(self):
        """Test case for get_paragraph_portions with invalid paragraph_index
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.paragraph_index = self.get_invalid_test_value('get_paragraph_portions', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_paragraph_portions', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'paragraph_index')

    def test_get_paragraph_portions_invalid_password(self):
        """Test case for get_paragraph_portions with invalid password
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.password = self.get_invalid_test_value('get_paragraph_portions', 'password', request.password, 'str')
        self.initialize('get_paragraph_portions', 'password', request.password)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'password')

    def test_get_paragraph_portions_invalid_folder(self):
        """Test case for get_paragraph_portions with invalid folder
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.folder = self.get_invalid_test_value('get_paragraph_portions', 'folder', request.folder, 'str')
        self.initialize('get_paragraph_portions', 'folder', request.folder)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'folder')

    def test_get_paragraph_portions_invalid_storage(self):
        """Test case for get_paragraph_portions with invalid storage
        """
        request = self.__prepare_get_paragraph_portions_request()
        request.storage = self.get_invalid_test_value('get_paragraph_portions', 'storage', request.storage, 'str')
        self.initialize('get_paragraph_portions', 'storage', request.storage)
        ok = False
        try:
            self.api.get_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_paragraph_portions', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_paragraph_portions', 'storage')

    def __prepare_get_paragraph_portions_request(self):
        name = self.get_test_value('get_paragraph_portions', 'name', 'str')
        slide_index = self.get_test_value('get_paragraph_portions', 'slide_index', 'int')
        shape_index = self.get_test_value('get_paragraph_portions', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_paragraph_portions', 'paragraph_index', 'int')
        password = self.get_test_value('get_paragraph_portions', 'password', 'str')
        folder = self.get_test_value('get_paragraph_portions', 'folder', 'str')
        storage = self.get_test_value('get_paragraph_portions', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetParagraphPortionsRequest(name, slide_index, shape_index, paragraph_index, password, folder, storage)

    def test_get_slide_animation(self):
        """Test case for get_slide_animation
        """
        request = self.__prepare_get_slide_animation_request()
        self.initialize('get_slide_animation', None, None)
        response = self.api.get_slide_animation(request)
        self.assertIsNotNone(response)

    def test_get_slide_animation_invalid_name(self):
        """Test case for get_slide_animation with invalid name
        """
        request = self.__prepare_get_slide_animation_request()
        request.name = self.get_invalid_test_value('get_slide_animation', 'name', request.name, 'str')
        self.initialize('get_slide_animation', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_animation', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_animation', 'name')

    def test_get_slide_animation_invalid_slide_index(self):
        """Test case for get_slide_animation with invalid slide_index
        """
        request = self.__prepare_get_slide_animation_request()
        request.slide_index = self.get_invalid_test_value('get_slide_animation', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slide_animation', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_animation', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_animation', 'slide_index')

    def test_get_slide_animation_invalid_shape_index(self):
        """Test case for get_slide_animation with invalid shape_index
        """
        request = self.__prepare_get_slide_animation_request()
        request.shape_index = self.get_invalid_test_value('get_slide_animation', 'shape_index', request.shape_index, 'int')
        self.initialize('get_slide_animation', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_animation', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_animation', 'shape_index')

    def test_get_slide_animation_invalid_password(self):
        """Test case for get_slide_animation with invalid password
        """
        request = self.__prepare_get_slide_animation_request()
        request.password = self.get_invalid_test_value('get_slide_animation', 'password', request.password, 'str')
        self.initialize('get_slide_animation', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_animation', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_animation', 'password')

    def test_get_slide_animation_invalid_folder(self):
        """Test case for get_slide_animation with invalid folder
        """
        request = self.__prepare_get_slide_animation_request()
        request.folder = self.get_invalid_test_value('get_slide_animation', 'folder', request.folder, 'str')
        self.initialize('get_slide_animation', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_animation', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_animation', 'folder')

    def test_get_slide_animation_invalid_storage(self):
        """Test case for get_slide_animation with invalid storage
        """
        request = self.__prepare_get_slide_animation_request()
        request.storage = self.get_invalid_test_value('get_slide_animation', 'storage', request.storage, 'str')
        self.initialize('get_slide_animation', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_animation', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_animation', 'storage')

    def __prepare_get_slide_animation_request(self):
        name = self.get_test_value('get_slide_animation', 'name', 'str')
        slide_index = self.get_test_value('get_slide_animation', 'slide_index', 'int')
        shape_index = self.get_test_value('get_slide_animation', 'shape_index', 'int')
        password = self.get_test_value('get_slide_animation', 'password', 'str')
        folder = self.get_test_value('get_slide_animation', 'folder', 'str')
        storage = self.get_test_value('get_slide_animation', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlideAnimationRequest(name, slide_index, shape_index, password, folder, storage)

    def test_get_slide_shape(self):
        """Test case for get_slide_shape
        """
        request = self.__prepare_get_slide_shape_request()
        self.initialize('get_slide_shape', None, None)
        response = self.api.get_slide_shape(request)
        self.assertIsNotNone(response)

    def test_get_slide_shape_invalid_name(self):
        """Test case for get_slide_shape with invalid name
        """
        request = self.__prepare_get_slide_shape_request()
        request.name = self.get_invalid_test_value('get_slide_shape', 'name', request.name, 'str')
        self.initialize('get_slide_shape', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape', 'name')

    def test_get_slide_shape_invalid_slide_index(self):
        """Test case for get_slide_shape with invalid slide_index
        """
        request = self.__prepare_get_slide_shape_request()
        request.slide_index = self.get_invalid_test_value('get_slide_shape', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slide_shape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape', 'slide_index')

    def test_get_slide_shape_invalid_shape_index(self):
        """Test case for get_slide_shape with invalid shape_index
        """
        request = self.__prepare_get_slide_shape_request()
        request.shape_index = self.get_invalid_test_value('get_slide_shape', 'shape_index', request.shape_index, 'int')
        self.initialize('get_slide_shape', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape', 'shape_index')

    def test_get_slide_shape_invalid_password(self):
        """Test case for get_slide_shape with invalid password
        """
        request = self.__prepare_get_slide_shape_request()
        request.password = self.get_invalid_test_value('get_slide_shape', 'password', request.password, 'str')
        self.initialize('get_slide_shape', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape', 'password')

    def test_get_slide_shape_invalid_folder(self):
        """Test case for get_slide_shape with invalid folder
        """
        request = self.__prepare_get_slide_shape_request()
        request.folder = self.get_invalid_test_value('get_slide_shape', 'folder', request.folder, 'str')
        self.initialize('get_slide_shape', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape', 'folder')

    def test_get_slide_shape_invalid_storage(self):
        """Test case for get_slide_shape with invalid storage
        """
        request = self.__prepare_get_slide_shape_request()
        request.storage = self.get_invalid_test_value('get_slide_shape', 'storage', request.storage, 'str')
        self.initialize('get_slide_shape', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape', 'storage')

    def __prepare_get_slide_shape_request(self):
        name = self.get_test_value('get_slide_shape', 'name', 'str')
        slide_index = self.get_test_value('get_slide_shape', 'slide_index', 'int')
        shape_index = self.get_test_value('get_slide_shape', 'shape_index', 'int')
        password = self.get_test_value('get_slide_shape', 'password', 'str')
        folder = self.get_test_value('get_slide_shape', 'folder', 'str')
        storage = self.get_test_value('get_slide_shape', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlideShapeRequest(name, slide_index, shape_index, password, folder, storage)

    def test_get_slide_shape_paragraph(self):
        """Test case for get_slide_shape_paragraph
        """
        request = self.__prepare_get_slide_shape_paragraph_request()
        self.initialize('get_slide_shape_paragraph', None, None)
        response = self.api.get_slide_shape_paragraph(request)
        self.assertIsNotNone(response)

    def test_get_slide_shape_paragraph_invalid_name(self):
        """Test case for get_slide_shape_paragraph with invalid name
        """
        request = self.__prepare_get_slide_shape_paragraph_request()
        request.name = self.get_invalid_test_value('get_slide_shape_paragraph', 'name', request.name, 'str')
        self.initialize('get_slide_shape_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraph', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraph', 'name')

    def test_get_slide_shape_paragraph_invalid_slide_index(self):
        """Test case for get_slide_shape_paragraph with invalid slide_index
        """
        request = self.__prepare_get_slide_shape_paragraph_request()
        request.slide_index = self.get_invalid_test_value('get_slide_shape_paragraph', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slide_shape_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraph', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraph', 'slide_index')

    def test_get_slide_shape_paragraph_invalid_shape_index(self):
        """Test case for get_slide_shape_paragraph with invalid shape_index
        """
        request = self.__prepare_get_slide_shape_paragraph_request()
        request.shape_index = self.get_invalid_test_value('get_slide_shape_paragraph', 'shape_index', request.shape_index, 'int')
        self.initialize('get_slide_shape_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraph', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraph', 'shape_index')

    def test_get_slide_shape_paragraph_invalid_paragraph_index(self):
        """Test case for get_slide_shape_paragraph with invalid paragraph_index
        """
        request = self.__prepare_get_slide_shape_paragraph_request()
        request.paragraph_index = self.get_invalid_test_value('get_slide_shape_paragraph', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_slide_shape_paragraph', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraph', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraph', 'paragraph_index')

    def test_get_slide_shape_paragraph_invalid_password(self):
        """Test case for get_slide_shape_paragraph with invalid password
        """
        request = self.__prepare_get_slide_shape_paragraph_request()
        request.password = self.get_invalid_test_value('get_slide_shape_paragraph', 'password', request.password, 'str')
        self.initialize('get_slide_shape_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraph', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraph', 'password')

    def test_get_slide_shape_paragraph_invalid_folder(self):
        """Test case for get_slide_shape_paragraph with invalid folder
        """
        request = self.__prepare_get_slide_shape_paragraph_request()
        request.folder = self.get_invalid_test_value('get_slide_shape_paragraph', 'folder', request.folder, 'str')
        self.initialize('get_slide_shape_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraph', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraph', 'folder')

    def test_get_slide_shape_paragraph_invalid_storage(self):
        """Test case for get_slide_shape_paragraph with invalid storage
        """
        request = self.__prepare_get_slide_shape_paragraph_request()
        request.storage = self.get_invalid_test_value('get_slide_shape_paragraph', 'storage', request.storage, 'str')
        self.initialize('get_slide_shape_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraph', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraph', 'storage')

    def __prepare_get_slide_shape_paragraph_request(self):
        name = self.get_test_value('get_slide_shape_paragraph', 'name', 'str')
        slide_index = self.get_test_value('get_slide_shape_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('get_slide_shape_paragraph', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_slide_shape_paragraph', 'paragraph_index', 'int')
        password = self.get_test_value('get_slide_shape_paragraph', 'password', 'str')
        folder = self.get_test_value('get_slide_shape_paragraph', 'folder', 'str')
        storage = self.get_test_value('get_slide_shape_paragraph', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlideShapeParagraphRequest(name, slide_index, shape_index, paragraph_index, password, folder, storage)

    def test_get_slide_shape_paragraphs(self):
        """Test case for get_slide_shape_paragraphs
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        self.initialize('get_slide_shape_paragraphs', None, None)
        response = self.api.get_slide_shape_paragraphs(request)
        self.assertIsNotNone(response)

    def test_get_slide_shape_paragraphs_invalid_name(self):
        """Test case for get_slide_shape_paragraphs with invalid name
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.name = self.get_invalid_test_value('get_slide_shape_paragraphs', 'name', request.name, 'str')
        self.initialize('get_slide_shape_paragraphs', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'name')

    def test_get_slide_shape_paragraphs_invalid_slide_index(self):
        """Test case for get_slide_shape_paragraphs with invalid slide_index
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.slide_index = self.get_invalid_test_value('get_slide_shape_paragraphs', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slide_shape_paragraphs', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'slide_index')

    def test_get_slide_shape_paragraphs_invalid_shape_index(self):
        """Test case for get_slide_shape_paragraphs with invalid shape_index
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.shape_index = self.get_invalid_test_value('get_slide_shape_paragraphs', 'shape_index', request.shape_index, 'int')
        self.initialize('get_slide_shape_paragraphs', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'shape_index')

    def test_get_slide_shape_paragraphs_invalid_password(self):
        """Test case for get_slide_shape_paragraphs with invalid password
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.password = self.get_invalid_test_value('get_slide_shape_paragraphs', 'password', request.password, 'str')
        self.initialize('get_slide_shape_paragraphs', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'password')

    def test_get_slide_shape_paragraphs_invalid_folder(self):
        """Test case for get_slide_shape_paragraphs with invalid folder
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.folder = self.get_invalid_test_value('get_slide_shape_paragraphs', 'folder', request.folder, 'str')
        self.initialize('get_slide_shape_paragraphs', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'folder')

    def test_get_slide_shape_paragraphs_invalid_storage(self):
        """Test case for get_slide_shape_paragraphs with invalid storage
        """
        request = self.__prepare_get_slide_shape_paragraphs_request()
        request.storage = self.get_invalid_test_value('get_slide_shape_paragraphs', 'storage', request.storage, 'str')
        self.initialize('get_slide_shape_paragraphs', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_shape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shape_paragraphs', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shape_paragraphs', 'storage')

    def __prepare_get_slide_shape_paragraphs_request(self):
        name = self.get_test_value('get_slide_shape_paragraphs', 'name', 'str')
        slide_index = self.get_test_value('get_slide_shape_paragraphs', 'slide_index', 'int')
        shape_index = self.get_test_value('get_slide_shape_paragraphs', 'shape_index', 'int')
        password = self.get_test_value('get_slide_shape_paragraphs', 'password', 'str')
        folder = self.get_test_value('get_slide_shape_paragraphs', 'folder', 'str')
        storage = self.get_test_value('get_slide_shape_paragraphs', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlideShapeParagraphsRequest(name, slide_index, shape_index, password, folder, storage)

    def test_get_slide_shapes(self):
        """Test case for get_slide_shapes
        """
        request = self.__prepare_get_slide_shapes_request()
        self.initialize('get_slide_shapes', None, None)
        response = self.api.get_slide_shapes(request)
        self.assertIsNotNone(response)

    def test_get_slide_shapes_invalid_name(self):
        """Test case for get_slide_shapes with invalid name
        """
        request = self.__prepare_get_slide_shapes_request()
        request.name = self.get_invalid_test_value('get_slide_shapes', 'name', request.name, 'str')
        self.initialize('get_slide_shapes', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shapes', 'name')

    def test_get_slide_shapes_invalid_slide_index(self):
        """Test case for get_slide_shapes with invalid slide_index
        """
        request = self.__prepare_get_slide_shapes_request()
        request.slide_index = self.get_invalid_test_value('get_slide_shapes', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slide_shapes', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shapes', 'slide_index')

    def test_get_slide_shapes_invalid_password(self):
        """Test case for get_slide_shapes with invalid password
        """
        request = self.__prepare_get_slide_shapes_request()
        request.password = self.get_invalid_test_value('get_slide_shapes', 'password', request.password, 'str')
        self.initialize('get_slide_shapes', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shapes', 'password')

    def test_get_slide_shapes_invalid_folder(self):
        """Test case for get_slide_shapes with invalid folder
        """
        request = self.__prepare_get_slide_shapes_request()
        request.folder = self.get_invalid_test_value('get_slide_shapes', 'folder', request.folder, 'str')
        self.initialize('get_slide_shapes', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shapes', 'folder')

    def test_get_slide_shapes_invalid_storage(self):
        """Test case for get_slide_shapes with invalid storage
        """
        request = self.__prepare_get_slide_shapes_request()
        request.storage = self.get_invalid_test_value('get_slide_shapes', 'storage', request.storage, 'str')
        self.initialize('get_slide_shapes', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_shapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_shapes', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_shapes', 'storage')

    def __prepare_get_slide_shapes_request(self):
        name = self.get_test_value('get_slide_shapes', 'name', 'str')
        slide_index = self.get_test_value('get_slide_shapes', 'slide_index', 'int')
        password = self.get_test_value('get_slide_shapes', 'password', 'str')
        folder = self.get_test_value('get_slide_shapes', 'folder', 'str')
        storage = self.get_test_value('get_slide_shapes', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlideShapesRequest(name, slide_index, password, folder, storage)

    def test_get_slide_subshape(self):
        """Test case for get_slide_subshape
        """
        request = self.__prepare_get_slide_subshape_request()
        self.initialize('get_slide_subshape', None, None)
        response = self.api.get_slide_subshape(request)
        self.assertIsNotNone(response)

    def test_get_slide_subshape_invalid_name(self):
        """Test case for get_slide_subshape with invalid name
        """
        request = self.__prepare_get_slide_subshape_request()
        request.name = self.get_invalid_test_value('get_slide_subshape', 'name', request.name, 'str')
        self.initialize('get_slide_subshape', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape', 'name')

    def test_get_slide_subshape_invalid_slide_index(self):
        """Test case for get_slide_subshape with invalid slide_index
        """
        request = self.__prepare_get_slide_subshape_request()
        request.slide_index = self.get_invalid_test_value('get_slide_subshape', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slide_subshape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape', 'slide_index')

    def test_get_slide_subshape_invalid_shape_index(self):
        """Test case for get_slide_subshape with invalid shape_index
        """
        request = self.__prepare_get_slide_subshape_request()
        request.shape_index = self.get_invalid_test_value('get_slide_subshape', 'shape_index', request.shape_index, 'int')
        self.initialize('get_slide_subshape', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape', 'shape_index')

    def test_get_slide_subshape_invalid_path(self):
        """Test case for get_slide_subshape with invalid path
        """
        request = self.__prepare_get_slide_subshape_request()
        request.path = self.get_invalid_test_value('get_slide_subshape', 'path', request.path, 'str')
        self.initialize('get_slide_subshape', 'path', request.path)
        ok = False
        try:
            self.api.get_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape', 'path')

    def test_get_slide_subshape_invalid_password(self):
        """Test case for get_slide_subshape with invalid password
        """
        request = self.__prepare_get_slide_subshape_request()
        request.password = self.get_invalid_test_value('get_slide_subshape', 'password', request.password, 'str')
        self.initialize('get_slide_subshape', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape', 'password')

    def test_get_slide_subshape_invalid_folder(self):
        """Test case for get_slide_subshape with invalid folder
        """
        request = self.__prepare_get_slide_subshape_request()
        request.folder = self.get_invalid_test_value('get_slide_subshape', 'folder', request.folder, 'str')
        self.initialize('get_slide_subshape', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape', 'folder')

    def test_get_slide_subshape_invalid_storage(self):
        """Test case for get_slide_subshape with invalid storage
        """
        request = self.__prepare_get_slide_subshape_request()
        request.storage = self.get_invalid_test_value('get_slide_subshape', 'storage', request.storage, 'str')
        self.initialize('get_slide_subshape', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape', 'storage')

    def __prepare_get_slide_subshape_request(self):
        name = self.get_test_value('get_slide_subshape', 'name', 'str')
        slide_index = self.get_test_value('get_slide_subshape', 'slide_index', 'int')
        shape_index = self.get_test_value('get_slide_subshape', 'shape_index', 'int')
        path = self.get_test_value('get_slide_subshape', 'path', 'str')
        password = self.get_test_value('get_slide_subshape', 'password', 'str')
        folder = self.get_test_value('get_slide_subshape', 'folder', 'str')
        storage = self.get_test_value('get_slide_subshape', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlideSubshapeRequest(name, slide_index, shape_index, path, password, folder, storage)

    def test_get_slide_subshape_paragraph(self):
        """Test case for get_slide_subshape_paragraph
        """
        request = self.__prepare_get_slide_subshape_paragraph_request()
        self.initialize('get_slide_subshape_paragraph', None, None)
        response = self.api.get_slide_subshape_paragraph(request)
        self.assertIsNotNone(response)

    def test_get_slide_subshape_paragraph_invalid_name(self):
        """Test case for get_slide_subshape_paragraph with invalid name
        """
        request = self.__prepare_get_slide_subshape_paragraph_request()
        request.name = self.get_invalid_test_value('get_slide_subshape_paragraph', 'name', request.name, 'str')
        self.initialize('get_slide_subshape_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraph', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraph', 'name')

    def test_get_slide_subshape_paragraph_invalid_slide_index(self):
        """Test case for get_slide_subshape_paragraph with invalid slide_index
        """
        request = self.__prepare_get_slide_subshape_paragraph_request()
        request.slide_index = self.get_invalid_test_value('get_slide_subshape_paragraph', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slide_subshape_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraph', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraph', 'slide_index')

    def test_get_slide_subshape_paragraph_invalid_shape_index(self):
        """Test case for get_slide_subshape_paragraph with invalid shape_index
        """
        request = self.__prepare_get_slide_subshape_paragraph_request()
        request.shape_index = self.get_invalid_test_value('get_slide_subshape_paragraph', 'shape_index', request.shape_index, 'int')
        self.initialize('get_slide_subshape_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_slide_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraph', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraph', 'shape_index')

    def test_get_slide_subshape_paragraph_invalid_paragraph_index(self):
        """Test case for get_slide_subshape_paragraph with invalid paragraph_index
        """
        request = self.__prepare_get_slide_subshape_paragraph_request()
        request.paragraph_index = self.get_invalid_test_value('get_slide_subshape_paragraph', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_slide_subshape_paragraph', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_slide_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraph', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraph', 'paragraph_index')

    def test_get_slide_subshape_paragraph_invalid_path(self):
        """Test case for get_slide_subshape_paragraph with invalid path
        """
        request = self.__prepare_get_slide_subshape_paragraph_request()
        request.path = self.get_invalid_test_value('get_slide_subshape_paragraph', 'path', request.path, 'str')
        self.initialize('get_slide_subshape_paragraph', 'path', request.path)
        ok = False
        try:
            self.api.get_slide_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraph', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraph', 'path')

    def test_get_slide_subshape_paragraph_invalid_password(self):
        """Test case for get_slide_subshape_paragraph with invalid password
        """
        request = self.__prepare_get_slide_subshape_paragraph_request()
        request.password = self.get_invalid_test_value('get_slide_subshape_paragraph', 'password', request.password, 'str')
        self.initialize('get_slide_subshape_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraph', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraph', 'password')

    def test_get_slide_subshape_paragraph_invalid_folder(self):
        """Test case for get_slide_subshape_paragraph with invalid folder
        """
        request = self.__prepare_get_slide_subshape_paragraph_request()
        request.folder = self.get_invalid_test_value('get_slide_subshape_paragraph', 'folder', request.folder, 'str')
        self.initialize('get_slide_subshape_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraph', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraph', 'folder')

    def test_get_slide_subshape_paragraph_invalid_storage(self):
        """Test case for get_slide_subshape_paragraph with invalid storage
        """
        request = self.__prepare_get_slide_subshape_paragraph_request()
        request.storage = self.get_invalid_test_value('get_slide_subshape_paragraph', 'storage', request.storage, 'str')
        self.initialize('get_slide_subshape_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraph', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraph', 'storage')

    def __prepare_get_slide_subshape_paragraph_request(self):
        name = self.get_test_value('get_slide_subshape_paragraph', 'name', 'str')
        slide_index = self.get_test_value('get_slide_subshape_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('get_slide_subshape_paragraph', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_slide_subshape_paragraph', 'paragraph_index', 'int')
        path = self.get_test_value('get_slide_subshape_paragraph', 'path', 'str')
        password = self.get_test_value('get_slide_subshape_paragraph', 'password', 'str')
        folder = self.get_test_value('get_slide_subshape_paragraph', 'folder', 'str')
        storage = self.get_test_value('get_slide_subshape_paragraph', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlideSubshapeParagraphRequest(name, slide_index, shape_index, paragraph_index, path, password, folder, storage)

    def test_get_slide_subshape_paragraphs(self):
        """Test case for get_slide_subshape_paragraphs
        """
        request = self.__prepare_get_slide_subshape_paragraphs_request()
        self.initialize('get_slide_subshape_paragraphs', None, None)
        response = self.api.get_slide_subshape_paragraphs(request)
        self.assertIsNotNone(response)

    def test_get_slide_subshape_paragraphs_invalid_name(self):
        """Test case for get_slide_subshape_paragraphs with invalid name
        """
        request = self.__prepare_get_slide_subshape_paragraphs_request()
        request.name = self.get_invalid_test_value('get_slide_subshape_paragraphs', 'name', request.name, 'str')
        self.initialize('get_slide_subshape_paragraphs', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraphs', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraphs', 'name')

    def test_get_slide_subshape_paragraphs_invalid_slide_index(self):
        """Test case for get_slide_subshape_paragraphs with invalid slide_index
        """
        request = self.__prepare_get_slide_subshape_paragraphs_request()
        request.slide_index = self.get_invalid_test_value('get_slide_subshape_paragraphs', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slide_subshape_paragraphs', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraphs', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraphs', 'slide_index')

    def test_get_slide_subshape_paragraphs_invalid_shape_index(self):
        """Test case for get_slide_subshape_paragraphs with invalid shape_index
        """
        request = self.__prepare_get_slide_subshape_paragraphs_request()
        request.shape_index = self.get_invalid_test_value('get_slide_subshape_paragraphs', 'shape_index', request.shape_index, 'int')
        self.initialize('get_slide_subshape_paragraphs', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_slide_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraphs', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraphs', 'shape_index')

    def test_get_slide_subshape_paragraphs_invalid_path(self):
        """Test case for get_slide_subshape_paragraphs with invalid path
        """
        request = self.__prepare_get_slide_subshape_paragraphs_request()
        request.path = self.get_invalid_test_value('get_slide_subshape_paragraphs', 'path', request.path, 'str')
        self.initialize('get_slide_subshape_paragraphs', 'path', request.path)
        ok = False
        try:
            self.api.get_slide_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraphs', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraphs', 'path')

    def test_get_slide_subshape_paragraphs_invalid_password(self):
        """Test case for get_slide_subshape_paragraphs with invalid password
        """
        request = self.__prepare_get_slide_subshape_paragraphs_request()
        request.password = self.get_invalid_test_value('get_slide_subshape_paragraphs', 'password', request.password, 'str')
        self.initialize('get_slide_subshape_paragraphs', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraphs', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraphs', 'password')

    def test_get_slide_subshape_paragraphs_invalid_folder(self):
        """Test case for get_slide_subshape_paragraphs with invalid folder
        """
        request = self.__prepare_get_slide_subshape_paragraphs_request()
        request.folder = self.get_invalid_test_value('get_slide_subshape_paragraphs', 'folder', request.folder, 'str')
        self.initialize('get_slide_subshape_paragraphs', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraphs', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraphs', 'folder')

    def test_get_slide_subshape_paragraphs_invalid_storage(self):
        """Test case for get_slide_subshape_paragraphs with invalid storage
        """
        request = self.__prepare_get_slide_subshape_paragraphs_request()
        request.storage = self.get_invalid_test_value('get_slide_subshape_paragraphs', 'storage', request.storage, 'str')
        self.initialize('get_slide_subshape_paragraphs', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_subshape_paragraphs(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshape_paragraphs', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshape_paragraphs', 'storage')

    def __prepare_get_slide_subshape_paragraphs_request(self):
        name = self.get_test_value('get_slide_subshape_paragraphs', 'name', 'str')
        slide_index = self.get_test_value('get_slide_subshape_paragraphs', 'slide_index', 'int')
        shape_index = self.get_test_value('get_slide_subshape_paragraphs', 'shape_index', 'int')
        path = self.get_test_value('get_slide_subshape_paragraphs', 'path', 'str')
        password = self.get_test_value('get_slide_subshape_paragraphs', 'password', 'str')
        folder = self.get_test_value('get_slide_subshape_paragraphs', 'folder', 'str')
        storage = self.get_test_value('get_slide_subshape_paragraphs', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlideSubshapeParagraphsRequest(name, slide_index, shape_index, path, password, folder, storage)

    def test_get_slide_subshapes(self):
        """Test case for get_slide_subshapes
        """
        request = self.__prepare_get_slide_subshapes_request()
        self.initialize('get_slide_subshapes', None, None)
        response = self.api.get_slide_subshapes(request)
        self.assertIsNotNone(response)

    def test_get_slide_subshapes_invalid_name(self):
        """Test case for get_slide_subshapes with invalid name
        """
        request = self.__prepare_get_slide_subshapes_request()
        request.name = self.get_invalid_test_value('get_slide_subshapes', 'name', request.name, 'str')
        self.initialize('get_slide_subshapes', 'name', request.name)
        ok = False
        try:
            self.api.get_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshapes', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshapes', 'name')

    def test_get_slide_subshapes_invalid_slide_index(self):
        """Test case for get_slide_subshapes with invalid slide_index
        """
        request = self.__prepare_get_slide_subshapes_request()
        request.slide_index = self.get_invalid_test_value('get_slide_subshapes', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slide_subshapes', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshapes', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshapes', 'slide_index')

    def test_get_slide_subshapes_invalid_path(self):
        """Test case for get_slide_subshapes with invalid path
        """
        request = self.__prepare_get_slide_subshapes_request()
        request.path = self.get_invalid_test_value('get_slide_subshapes', 'path', request.path, 'str')
        self.initialize('get_slide_subshapes', 'path', request.path)
        ok = False
        try:
            self.api.get_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshapes', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshapes', 'path')

    def test_get_slide_subshapes_invalid_password(self):
        """Test case for get_slide_subshapes with invalid password
        """
        request = self.__prepare_get_slide_subshapes_request()
        request.password = self.get_invalid_test_value('get_slide_subshapes', 'password', request.password, 'str')
        self.initialize('get_slide_subshapes', 'password', request.password)
        ok = False
        try:
            self.api.get_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshapes', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshapes', 'password')

    def test_get_slide_subshapes_invalid_folder(self):
        """Test case for get_slide_subshapes with invalid folder
        """
        request = self.__prepare_get_slide_subshapes_request()
        request.folder = self.get_invalid_test_value('get_slide_subshapes', 'folder', request.folder, 'str')
        self.initialize('get_slide_subshapes', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshapes', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshapes', 'folder')

    def test_get_slide_subshapes_invalid_storage(self):
        """Test case for get_slide_subshapes with invalid storage
        """
        request = self.__prepare_get_slide_subshapes_request()
        request.storage = self.get_invalid_test_value('get_slide_subshapes', 'storage', request.storage, 'str')
        self.initialize('get_slide_subshapes', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slide_subshapes(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slide_subshapes', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slide_subshapes', 'storage')

    def __prepare_get_slide_subshapes_request(self):
        name = self.get_test_value('get_slide_subshapes', 'name', 'str')
        slide_index = self.get_test_value('get_slide_subshapes', 'slide_index', 'int')
        path = self.get_test_value('get_slide_subshapes', 'path', 'str')
        password = self.get_test_value('get_slide_subshapes', 'password', 'str')
        folder = self.get_test_value('get_slide_subshapes', 'folder', 'str')
        storage = self.get_test_value('get_slide_subshapes', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlideSubshapesRequest(name, slide_index, path, password, folder, storage)

    def test_get_slides_api_info(self):
        """Test case for get_slides_api_info
        """
        
        self.initialize('get_slides_api_info', None, None)
        response = self.api.get_slides_api_info()
        self.assertIsNotNone(response)


    def test_get_slides_document(self):
        """Test case for get_slides_document
        """
        request = self.__prepare_get_slides_document_request()
        self.initialize('get_slides_document', None, None)
        response = self.api.get_slides_document(request)
        self.assertIsNotNone(response)

    def test_get_slides_document_invalid_name(self):
        """Test case for get_slides_document with invalid name
        """
        request = self.__prepare_get_slides_document_request()
        request.name = self.get_invalid_test_value('get_slides_document', 'name', request.name, 'str')
        self.initialize('get_slides_document', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document', 'name')

    def test_get_slides_document_invalid_password(self):
        """Test case for get_slides_document with invalid password
        """
        request = self.__prepare_get_slides_document_request()
        request.password = self.get_invalid_test_value('get_slides_document', 'password', request.password, 'str')
        self.initialize('get_slides_document', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document', 'password')

    def test_get_slides_document_invalid_storage(self):
        """Test case for get_slides_document with invalid storage
        """
        request = self.__prepare_get_slides_document_request()
        request.storage = self.get_invalid_test_value('get_slides_document', 'storage', request.storage, 'str')
        self.initialize('get_slides_document', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document', 'storage')

    def test_get_slides_document_invalid_folder(self):
        """Test case for get_slides_document with invalid folder
        """
        request = self.__prepare_get_slides_document_request()
        request.folder = self.get_invalid_test_value('get_slides_document', 'folder', request.folder, 'str')
        self.initialize('get_slides_document', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document', 'folder')

    def __prepare_get_slides_document_request(self):
        name = self.get_test_value('get_slides_document', 'name', 'str')
        password = self.get_test_value('get_slides_document', 'password', 'str')
        storage = self.get_test_value('get_slides_document', 'storage', 'str')
        folder = self.get_test_value('get_slides_document', 'folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesDocumentRequest(name, password, storage, folder)

    def test_get_slides_document_properties(self):
        """Test case for get_slides_document_properties
        """
        request = self.__prepare_get_slides_document_properties_request()
        self.initialize('get_slides_document_properties', None, None)
        response = self.api.get_slides_document_properties(request)
        self.assertIsNotNone(response)

    def test_get_slides_document_properties_invalid_name(self):
        """Test case for get_slides_document_properties with invalid name
        """
        request = self.__prepare_get_slides_document_properties_request()
        request.name = self.get_invalid_test_value('get_slides_document_properties', 'name', request.name, 'str')
        self.initialize('get_slides_document_properties', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_properties', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document_properties', 'name')

    def test_get_slides_document_properties_invalid_password(self):
        """Test case for get_slides_document_properties with invalid password
        """
        request = self.__prepare_get_slides_document_properties_request()
        request.password = self.get_invalid_test_value('get_slides_document_properties', 'password', request.password, 'str')
        self.initialize('get_slides_document_properties', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_properties', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document_properties', 'password')

    def test_get_slides_document_properties_invalid_folder(self):
        """Test case for get_slides_document_properties with invalid folder
        """
        request = self.__prepare_get_slides_document_properties_request()
        request.folder = self.get_invalid_test_value('get_slides_document_properties', 'folder', request.folder, 'str')
        self.initialize('get_slides_document_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_properties', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document_properties', 'folder')

    def test_get_slides_document_properties_invalid_storage(self):
        """Test case for get_slides_document_properties with invalid storage
        """
        request = self.__prepare_get_slides_document_properties_request()
        request.storage = self.get_invalid_test_value('get_slides_document_properties', 'storage', request.storage, 'str')
        self.initialize('get_slides_document_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_properties', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document_properties', 'storage')

    def __prepare_get_slides_document_properties_request(self):
        name = self.get_test_value('get_slides_document_properties', 'name', 'str')
        password = self.get_test_value('get_slides_document_properties', 'password', 'str')
        folder = self.get_test_value('get_slides_document_properties', 'folder', 'str')
        storage = self.get_test_value('get_slides_document_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesDocumentPropertiesRequest(name, password, folder, storage)

    def test_get_slides_document_property(self):
        """Test case for get_slides_document_property
        """
        request = self.__prepare_get_slides_document_property_request()
        self.initialize('get_slides_document_property', None, None)
        response = self.api.get_slides_document_property(request)
        self.assertIsNotNone(response)

    def test_get_slides_document_property_invalid_name(self):
        """Test case for get_slides_document_property with invalid name
        """
        request = self.__prepare_get_slides_document_property_request()
        request.name = self.get_invalid_test_value('get_slides_document_property', 'name', request.name, 'str')
        self.initialize('get_slides_document_property', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_property', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document_property', 'name')

    def test_get_slides_document_property_invalid_property_name(self):
        """Test case for get_slides_document_property with invalid property_name
        """
        request = self.__prepare_get_slides_document_property_request()
        request.property_name = self.get_invalid_test_value('get_slides_document_property', 'property_name', request.property_name, 'str')
        self.initialize('get_slides_document_property', 'property_name', request.property_name)
        ok = False
        try:
            self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_property', 'property_name', request.property_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document_property', 'property_name')

    def test_get_slides_document_property_invalid_password(self):
        """Test case for get_slides_document_property with invalid password
        """
        request = self.__prepare_get_slides_document_property_request()
        request.password = self.get_invalid_test_value('get_slides_document_property', 'password', request.password, 'str')
        self.initialize('get_slides_document_property', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_property', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document_property', 'password')

    def test_get_slides_document_property_invalid_folder(self):
        """Test case for get_slides_document_property with invalid folder
        """
        request = self.__prepare_get_slides_document_property_request()
        request.folder = self.get_invalid_test_value('get_slides_document_property', 'folder', request.folder, 'str')
        self.initialize('get_slides_document_property', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_property', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document_property', 'folder')

    def test_get_slides_document_property_invalid_storage(self):
        """Test case for get_slides_document_property with invalid storage
        """
        request = self.__prepare_get_slides_document_property_request()
        request.storage = self.get_invalid_test_value('get_slides_document_property', 'storage', request.storage, 'str')
        self.initialize('get_slides_document_property', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_document_property', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_document_property', 'storage')

    def __prepare_get_slides_document_property_request(self):
        name = self.get_test_value('get_slides_document_property', 'name', 'str')
        property_name = self.get_test_value('get_slides_document_property', 'property_name', 'str')
        password = self.get_test_value('get_slides_document_property', 'password', 'str')
        folder = self.get_test_value('get_slides_document_property', 'folder', 'str')
        storage = self.get_test_value('get_slides_document_property', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesDocumentPropertyRequest(name, property_name, password, folder, storage)

    def test_get_slides_image_with_default_format(self):
        """Test case for get_slides_image_with_default_format
        """
        request = self.__prepare_get_slides_image_with_default_format_request()
        self.initialize('get_slides_image_with_default_format', None, None)
        response = self.api.get_slides_image_with_default_format(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_get_slides_image_with_default_format_invalid_name(self):
        """Test case for get_slides_image_with_default_format with invalid name
        """
        request = self.__prepare_get_slides_image_with_default_format_request()
        request.name = self.get_invalid_test_value('get_slides_image_with_default_format', 'name', request.name, 'str')
        self.initialize('get_slides_image_with_default_format', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_image_with_default_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_default_format', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_default_format', 'name')

    def test_get_slides_image_with_default_format_invalid_index(self):
        """Test case for get_slides_image_with_default_format with invalid index
        """
        request = self.__prepare_get_slides_image_with_default_format_request()
        request.index = self.get_invalid_test_value('get_slides_image_with_default_format', 'index', request.index, 'int')
        self.initialize('get_slides_image_with_default_format', 'index', request.index)
        ok = False
        try:
            self.api.get_slides_image_with_default_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_default_format', 'index', request.index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_default_format', 'index')

    def test_get_slides_image_with_default_format_invalid_password(self):
        """Test case for get_slides_image_with_default_format with invalid password
        """
        request = self.__prepare_get_slides_image_with_default_format_request()
        request.password = self.get_invalid_test_value('get_slides_image_with_default_format', 'password', request.password, 'str')
        self.initialize('get_slides_image_with_default_format', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_image_with_default_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_default_format', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_default_format', 'password')

    def test_get_slides_image_with_default_format_invalid_folder(self):
        """Test case for get_slides_image_with_default_format with invalid folder
        """
        request = self.__prepare_get_slides_image_with_default_format_request()
        request.folder = self.get_invalid_test_value('get_slides_image_with_default_format', 'folder', request.folder, 'str')
        self.initialize('get_slides_image_with_default_format', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_image_with_default_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_default_format', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_default_format', 'folder')

    def test_get_slides_image_with_default_format_invalid_storage(self):
        """Test case for get_slides_image_with_default_format with invalid storage
        """
        request = self.__prepare_get_slides_image_with_default_format_request()
        request.storage = self.get_invalid_test_value('get_slides_image_with_default_format', 'storage', request.storage, 'str')
        self.initialize('get_slides_image_with_default_format', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_image_with_default_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_default_format', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_default_format', 'storage')

    def __prepare_get_slides_image_with_default_format_request(self):
        name = self.get_test_value('get_slides_image_with_default_format', 'name', 'str')
        index = self.get_test_value('get_slides_image_with_default_format', 'index', 'int')
        password = self.get_test_value('get_slides_image_with_default_format', 'password', 'str')
        folder = self.get_test_value('get_slides_image_with_default_format', 'folder', 'str')
        storage = self.get_test_value('get_slides_image_with_default_format', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesImageWithDefaultFormatRequest(name, index, password, folder, storage)

    def test_get_slides_image_with_format(self):
        """Test case for get_slides_image_with_format
        """
        request = self.__prepare_get_slides_image_with_format_request()
        self.initialize('get_slides_image_with_format', None, None)
        response = self.api.get_slides_image_with_format(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_get_slides_image_with_format_invalid_name(self):
        """Test case for get_slides_image_with_format with invalid name
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.name = self.get_invalid_test_value('get_slides_image_with_format', 'name', request.name, 'str')
        self.initialize('get_slides_image_with_format', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'name')

    def test_get_slides_image_with_format_invalid_index(self):
        """Test case for get_slides_image_with_format with invalid index
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.index = self.get_invalid_test_value('get_slides_image_with_format', 'index', request.index, 'int')
        self.initialize('get_slides_image_with_format', 'index', request.index)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'index', request.index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'index')

    def test_get_slides_image_with_format_invalid_format(self):
        """Test case for get_slides_image_with_format with invalid format
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.format = self.get_invalid_test_value('get_slides_image_with_format', 'format', request.format, 'str')
        self.initialize('get_slides_image_with_format', 'format', request.format)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'format')

    def test_get_slides_image_with_format_invalid_password(self):
        """Test case for get_slides_image_with_format with invalid password
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.password = self.get_invalid_test_value('get_slides_image_with_format', 'password', request.password, 'str')
        self.initialize('get_slides_image_with_format', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'password')

    def test_get_slides_image_with_format_invalid_folder(self):
        """Test case for get_slides_image_with_format with invalid folder
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.folder = self.get_invalid_test_value('get_slides_image_with_format', 'folder', request.folder, 'str')
        self.initialize('get_slides_image_with_format', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'folder')

    def test_get_slides_image_with_format_invalid_storage(self):
        """Test case for get_slides_image_with_format with invalid storage
        """
        request = self.__prepare_get_slides_image_with_format_request()
        request.storage = self.get_invalid_test_value('get_slides_image_with_format', 'storage', request.storage, 'str')
        self.initialize('get_slides_image_with_format', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_image_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_image_with_format', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_image_with_format', 'storage')

    def __prepare_get_slides_image_with_format_request(self):
        name = self.get_test_value('get_slides_image_with_format', 'name', 'str')
        index = self.get_test_value('get_slides_image_with_format', 'index', 'int')
        format = self.get_test_value('get_slides_image_with_format', 'format', 'str')
        password = self.get_test_value('get_slides_image_with_format', 'password', 'str')
        folder = self.get_test_value('get_slides_image_with_format', 'folder', 'str')
        storage = self.get_test_value('get_slides_image_with_format', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesImageWithFormatRequest(name, index, format, password, folder, storage)

    def test_get_slides_images(self):
        """Test case for get_slides_images
        """
        request = self.__prepare_get_slides_images_request()
        self.initialize('get_slides_images', None, None)
        response = self.api.get_slides_images(request)
        self.assertIsNotNone(response)

    def test_get_slides_images_invalid_name(self):
        """Test case for get_slides_images with invalid name
        """
        request = self.__prepare_get_slides_images_request()
        request.name = self.get_invalid_test_value('get_slides_images', 'name', request.name, 'str')
        self.initialize('get_slides_images', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_images', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_images', 'name')

    def test_get_slides_images_invalid_password(self):
        """Test case for get_slides_images with invalid password
        """
        request = self.__prepare_get_slides_images_request()
        request.password = self.get_invalid_test_value('get_slides_images', 'password', request.password, 'str')
        self.initialize('get_slides_images', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_images', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_images', 'password')

    def test_get_slides_images_invalid_folder(self):
        """Test case for get_slides_images with invalid folder
        """
        request = self.__prepare_get_slides_images_request()
        request.folder = self.get_invalid_test_value('get_slides_images', 'folder', request.folder, 'str')
        self.initialize('get_slides_images', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_images', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_images', 'folder')

    def test_get_slides_images_invalid_storage(self):
        """Test case for get_slides_images with invalid storage
        """
        request = self.__prepare_get_slides_images_request()
        request.storage = self.get_invalid_test_value('get_slides_images', 'storage', request.storage, 'str')
        self.initialize('get_slides_images', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_images', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_images', 'storage')

    def __prepare_get_slides_images_request(self):
        name = self.get_test_value('get_slides_images', 'name', 'str')
        password = self.get_test_value('get_slides_images', 'password', 'str')
        folder = self.get_test_value('get_slides_images', 'folder', 'str')
        storage = self.get_test_value('get_slides_images', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesImagesRequest(name, password, folder, storage)

    def test_get_slides_placeholder(self):
        """Test case for get_slides_placeholder
        """
        request = self.__prepare_get_slides_placeholder_request()
        self.initialize('get_slides_placeholder', None, None)
        response = self.api.get_slides_placeholder(request)
        self.assertIsNotNone(response)

    def test_get_slides_placeholder_invalid_name(self):
        """Test case for get_slides_placeholder with invalid name
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.name = self.get_invalid_test_value('get_slides_placeholder', 'name', request.name, 'str')
        self.initialize('get_slides_placeholder', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'name')

    def test_get_slides_placeholder_invalid_slide_index(self):
        """Test case for get_slides_placeholder with invalid slide_index
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.slide_index = self.get_invalid_test_value('get_slides_placeholder', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_placeholder', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'slide_index')

    def test_get_slides_placeholder_invalid_placeholder_index(self):
        """Test case for get_slides_placeholder with invalid placeholder_index
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.placeholder_index = self.get_invalid_test_value('get_slides_placeholder', 'placeholder_index', request.placeholder_index, 'int')
        self.initialize('get_slides_placeholder', 'placeholder_index', request.placeholder_index)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'placeholder_index', request.placeholder_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'placeholder_index')

    def test_get_slides_placeholder_invalid_password(self):
        """Test case for get_slides_placeholder with invalid password
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.password = self.get_invalid_test_value('get_slides_placeholder', 'password', request.password, 'str')
        self.initialize('get_slides_placeholder', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'password')

    def test_get_slides_placeholder_invalid_folder(self):
        """Test case for get_slides_placeholder with invalid folder
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.folder = self.get_invalid_test_value('get_slides_placeholder', 'folder', request.folder, 'str')
        self.initialize('get_slides_placeholder', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'folder')

    def test_get_slides_placeholder_invalid_storage(self):
        """Test case for get_slides_placeholder with invalid storage
        """
        request = self.__prepare_get_slides_placeholder_request()
        request.storage = self.get_invalid_test_value('get_slides_placeholder', 'storage', request.storage, 'str')
        self.initialize('get_slides_placeholder', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_placeholder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholder', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholder', 'storage')

    def __prepare_get_slides_placeholder_request(self):
        name = self.get_test_value('get_slides_placeholder', 'name', 'str')
        slide_index = self.get_test_value('get_slides_placeholder', 'slide_index', 'int')
        placeholder_index = self.get_test_value('get_slides_placeholder', 'placeholder_index', 'int')
        password = self.get_test_value('get_slides_placeholder', 'password', 'str')
        folder = self.get_test_value('get_slides_placeholder', 'folder', 'str')
        storage = self.get_test_value('get_slides_placeholder', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesPlaceholderRequest(name, slide_index, placeholder_index, password, folder, storage)

    def test_get_slides_placeholders(self):
        """Test case for get_slides_placeholders
        """
        request = self.__prepare_get_slides_placeholders_request()
        self.initialize('get_slides_placeholders', None, None)
        response = self.api.get_slides_placeholders(request)
        self.assertIsNotNone(response)

    def test_get_slides_placeholders_invalid_name(self):
        """Test case for get_slides_placeholders with invalid name
        """
        request = self.__prepare_get_slides_placeholders_request()
        request.name = self.get_invalid_test_value('get_slides_placeholders', 'name', request.name, 'str')
        self.initialize('get_slides_placeholders', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholders', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholders', 'name')

    def test_get_slides_placeholders_invalid_slide_index(self):
        """Test case for get_slides_placeholders with invalid slide_index
        """
        request = self.__prepare_get_slides_placeholders_request()
        request.slide_index = self.get_invalid_test_value('get_slides_placeholders', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_placeholders', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholders', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholders', 'slide_index')

    def test_get_slides_placeholders_invalid_password(self):
        """Test case for get_slides_placeholders with invalid password
        """
        request = self.__prepare_get_slides_placeholders_request()
        request.password = self.get_invalid_test_value('get_slides_placeholders', 'password', request.password, 'str')
        self.initialize('get_slides_placeholders', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholders', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholders', 'password')

    def test_get_slides_placeholders_invalid_folder(self):
        """Test case for get_slides_placeholders with invalid folder
        """
        request = self.__prepare_get_slides_placeholders_request()
        request.folder = self.get_invalid_test_value('get_slides_placeholders', 'folder', request.folder, 'str')
        self.initialize('get_slides_placeholders', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholders', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholders', 'folder')

    def test_get_slides_placeholders_invalid_storage(self):
        """Test case for get_slides_placeholders with invalid storage
        """
        request = self.__prepare_get_slides_placeholders_request()
        request.storage = self.get_invalid_test_value('get_slides_placeholders', 'storage', request.storage, 'str')
        self.initialize('get_slides_placeholders', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_placeholders(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_placeholders', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_placeholders', 'storage')

    def __prepare_get_slides_placeholders_request(self):
        name = self.get_test_value('get_slides_placeholders', 'name', 'str')
        slide_index = self.get_test_value('get_slides_placeholders', 'slide_index', 'int')
        password = self.get_test_value('get_slides_placeholders', 'password', 'str')
        folder = self.get_test_value('get_slides_placeholders', 'folder', 'str')
        storage = self.get_test_value('get_slides_placeholders', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesPlaceholdersRequest(name, slide_index, password, folder, storage)

    def test_get_slides_presentation_text_items(self):
        """Test case for get_slides_presentation_text_items
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        self.initialize('get_slides_presentation_text_items', None, None)
        response = self.api.get_slides_presentation_text_items(request)
        self.assertIsNotNone(response)

    def test_get_slides_presentation_text_items_invalid_name(self):
        """Test case for get_slides_presentation_text_items with invalid name
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        request.name = self.get_invalid_test_value('get_slides_presentation_text_items', 'name', request.name, 'str')
        self.initialize('get_slides_presentation_text_items', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_presentation_text_items', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_presentation_text_items', 'name')

    def test_get_slides_presentation_text_items_invalid_with_empty(self):
        """Test case for get_slides_presentation_text_items with invalid with_empty
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        request.with_empty = self.get_invalid_test_value('get_slides_presentation_text_items', 'with_empty', request.with_empty, 'bool')
        self.initialize('get_slides_presentation_text_items', 'with_empty', request.with_empty)
        ok = False
        try:
            self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_presentation_text_items', 'with_empty', request.with_empty)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_presentation_text_items', 'with_empty')

    def test_get_slides_presentation_text_items_invalid_password(self):
        """Test case for get_slides_presentation_text_items with invalid password
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        request.password = self.get_invalid_test_value('get_slides_presentation_text_items', 'password', request.password, 'str')
        self.initialize('get_slides_presentation_text_items', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_presentation_text_items', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_presentation_text_items', 'password')

    def test_get_slides_presentation_text_items_invalid_folder(self):
        """Test case for get_slides_presentation_text_items with invalid folder
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        request.folder = self.get_invalid_test_value('get_slides_presentation_text_items', 'folder', request.folder, 'str')
        self.initialize('get_slides_presentation_text_items', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_presentation_text_items', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_presentation_text_items', 'folder')

    def test_get_slides_presentation_text_items_invalid_storage(self):
        """Test case for get_slides_presentation_text_items with invalid storage
        """
        request = self.__prepare_get_slides_presentation_text_items_request()
        request.storage = self.get_invalid_test_value('get_slides_presentation_text_items', 'storage', request.storage, 'str')
        self.initialize('get_slides_presentation_text_items', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_presentation_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_presentation_text_items', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_presentation_text_items', 'storage')

    def __prepare_get_slides_presentation_text_items_request(self):
        name = self.get_test_value('get_slides_presentation_text_items', 'name', 'str')
        with_empty = self.get_test_value('get_slides_presentation_text_items', 'with_empty', 'bool')
        password = self.get_test_value('get_slides_presentation_text_items', 'password', 'str')
        folder = self.get_test_value('get_slides_presentation_text_items', 'folder', 'str')
        storage = self.get_test_value('get_slides_presentation_text_items', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesPresentationTextItemsRequest(name, with_empty, password, folder, storage)

    def test_get_slides_slide(self):
        """Test case for get_slides_slide
        """
        request = self.__prepare_get_slides_slide_request()
        self.initialize('get_slides_slide', None, None)
        response = self.api.get_slides_slide(request)
        self.assertIsNotNone(response)

    def test_get_slides_slide_invalid_name(self):
        """Test case for get_slides_slide with invalid name
        """
        request = self.__prepare_get_slides_slide_request()
        request.name = self.get_invalid_test_value('get_slides_slide', 'name', request.name, 'str')
        self.initialize('get_slides_slide', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide', 'name')

    def test_get_slides_slide_invalid_slide_index(self):
        """Test case for get_slides_slide with invalid slide_index
        """
        request = self.__prepare_get_slides_slide_request()
        request.slide_index = self.get_invalid_test_value('get_slides_slide', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide', 'slide_index')

    def test_get_slides_slide_invalid_password(self):
        """Test case for get_slides_slide with invalid password
        """
        request = self.__prepare_get_slides_slide_request()
        request.password = self.get_invalid_test_value('get_slides_slide', 'password', request.password, 'str')
        self.initialize('get_slides_slide', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide', 'password')

    def test_get_slides_slide_invalid_folder(self):
        """Test case for get_slides_slide with invalid folder
        """
        request = self.__prepare_get_slides_slide_request()
        request.folder = self.get_invalid_test_value('get_slides_slide', 'folder', request.folder, 'str')
        self.initialize('get_slides_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide', 'folder')

    def test_get_slides_slide_invalid_storage(self):
        """Test case for get_slides_slide with invalid storage
        """
        request = self.__prepare_get_slides_slide_request()
        request.storage = self.get_invalid_test_value('get_slides_slide', 'storage', request.storage, 'str')
        self.initialize('get_slides_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide', 'storage')

    def __prepare_get_slides_slide_request(self):
        name = self.get_test_value('get_slides_slide', 'name', 'str')
        slide_index = self.get_test_value('get_slides_slide', 'slide_index', 'int')
        password = self.get_test_value('get_slides_slide', 'password', 'str')
        folder = self.get_test_value('get_slides_slide', 'folder', 'str')
        storage = self.get_test_value('get_slides_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesSlideRequest(name, slide_index, password, folder, storage)

    def test_get_slides_slide_background(self):
        """Test case for get_slides_slide_background
        """
        request = self.__prepare_get_slides_slide_background_request()
        self.initialize('get_slides_slide_background', None, None)
        response = self.api.get_slides_slide_background(request)
        self.assertIsNotNone(response)

    def test_get_slides_slide_background_invalid_name(self):
        """Test case for get_slides_slide_background with invalid name
        """
        request = self.__prepare_get_slides_slide_background_request()
        request.name = self.get_invalid_test_value('get_slides_slide_background', 'name', request.name, 'str')
        self.initialize('get_slides_slide_background', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_background', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_background', 'name')

    def test_get_slides_slide_background_invalid_slide_index(self):
        """Test case for get_slides_slide_background with invalid slide_index
        """
        request = self.__prepare_get_slides_slide_background_request()
        request.slide_index = self.get_invalid_test_value('get_slides_slide_background', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_slide_background', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_background', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_background', 'slide_index')

    def test_get_slides_slide_background_invalid_password(self):
        """Test case for get_slides_slide_background with invalid password
        """
        request = self.__prepare_get_slides_slide_background_request()
        request.password = self.get_invalid_test_value('get_slides_slide_background', 'password', request.password, 'str')
        self.initialize('get_slides_slide_background', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_background', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_background', 'password')

    def test_get_slides_slide_background_invalid_folder(self):
        """Test case for get_slides_slide_background with invalid folder
        """
        request = self.__prepare_get_slides_slide_background_request()
        request.folder = self.get_invalid_test_value('get_slides_slide_background', 'folder', request.folder, 'str')
        self.initialize('get_slides_slide_background', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_background', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_background', 'folder')

    def test_get_slides_slide_background_invalid_storage(self):
        """Test case for get_slides_slide_background with invalid storage
        """
        request = self.__prepare_get_slides_slide_background_request()
        request.storage = self.get_invalid_test_value('get_slides_slide_background', 'storage', request.storage, 'str')
        self.initialize('get_slides_slide_background', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_background', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_background', 'storage')

    def __prepare_get_slides_slide_background_request(self):
        name = self.get_test_value('get_slides_slide_background', 'name', 'str')
        slide_index = self.get_test_value('get_slides_slide_background', 'slide_index', 'int')
        password = self.get_test_value('get_slides_slide_background', 'password', 'str')
        folder = self.get_test_value('get_slides_slide_background', 'folder', 'str')
        storage = self.get_test_value('get_slides_slide_background', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesSlideBackgroundRequest(name, slide_index, password, folder, storage)

    def test_get_slides_slide_comments(self):
        """Test case for get_slides_slide_comments
        """
        request = self.__prepare_get_slides_slide_comments_request()
        self.initialize('get_slides_slide_comments', None, None)
        response = self.api.get_slides_slide_comments(request)
        self.assertIsNotNone(response)

    def test_get_slides_slide_comments_invalid_name(self):
        """Test case for get_slides_slide_comments with invalid name
        """
        request = self.__prepare_get_slides_slide_comments_request()
        request.name = self.get_invalid_test_value('get_slides_slide_comments', 'name', request.name, 'str')
        self.initialize('get_slides_slide_comments', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_comments', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_comments', 'name')

    def test_get_slides_slide_comments_invalid_slide_index(self):
        """Test case for get_slides_slide_comments with invalid slide_index
        """
        request = self.__prepare_get_slides_slide_comments_request()
        request.slide_index = self.get_invalid_test_value('get_slides_slide_comments', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_slide_comments', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_comments', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_comments', 'slide_index')

    def test_get_slides_slide_comments_invalid_password(self):
        """Test case for get_slides_slide_comments with invalid password
        """
        request = self.__prepare_get_slides_slide_comments_request()
        request.password = self.get_invalid_test_value('get_slides_slide_comments', 'password', request.password, 'str')
        self.initialize('get_slides_slide_comments', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_comments', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_comments', 'password')

    def test_get_slides_slide_comments_invalid_folder(self):
        """Test case for get_slides_slide_comments with invalid folder
        """
        request = self.__prepare_get_slides_slide_comments_request()
        request.folder = self.get_invalid_test_value('get_slides_slide_comments', 'folder', request.folder, 'str')
        self.initialize('get_slides_slide_comments', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_comments', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_comments', 'folder')

    def test_get_slides_slide_comments_invalid_storage(self):
        """Test case for get_slides_slide_comments with invalid storage
        """
        request = self.__prepare_get_slides_slide_comments_request()
        request.storage = self.get_invalid_test_value('get_slides_slide_comments', 'storage', request.storage, 'str')
        self.initialize('get_slides_slide_comments', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slide_comments(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_comments', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_comments', 'storage')

    def __prepare_get_slides_slide_comments_request(self):
        name = self.get_test_value('get_slides_slide_comments', 'name', 'str')
        slide_index = self.get_test_value('get_slides_slide_comments', 'slide_index', 'int')
        password = self.get_test_value('get_slides_slide_comments', 'password', 'str')
        folder = self.get_test_value('get_slides_slide_comments', 'folder', 'str')
        storage = self.get_test_value('get_slides_slide_comments', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesSlideCommentsRequest(name, slide_index, password, folder, storage)

    def test_get_slides_slide_images(self):
        """Test case for get_slides_slide_images
        """
        request = self.__prepare_get_slides_slide_images_request()
        self.initialize('get_slides_slide_images', None, None)
        response = self.api.get_slides_slide_images(request)
        self.assertIsNotNone(response)

    def test_get_slides_slide_images_invalid_name(self):
        """Test case for get_slides_slide_images with invalid name
        """
        request = self.__prepare_get_slides_slide_images_request()
        request.name = self.get_invalid_test_value('get_slides_slide_images', 'name', request.name, 'str')
        self.initialize('get_slides_slide_images', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_images', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_images', 'name')

    def test_get_slides_slide_images_invalid_slide_index(self):
        """Test case for get_slides_slide_images with invalid slide_index
        """
        request = self.__prepare_get_slides_slide_images_request()
        request.slide_index = self.get_invalid_test_value('get_slides_slide_images', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_slide_images', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_images', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_images', 'slide_index')

    def test_get_slides_slide_images_invalid_password(self):
        """Test case for get_slides_slide_images with invalid password
        """
        request = self.__prepare_get_slides_slide_images_request()
        request.password = self.get_invalid_test_value('get_slides_slide_images', 'password', request.password, 'str')
        self.initialize('get_slides_slide_images', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_images', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_images', 'password')

    def test_get_slides_slide_images_invalid_folder(self):
        """Test case for get_slides_slide_images with invalid folder
        """
        request = self.__prepare_get_slides_slide_images_request()
        request.folder = self.get_invalid_test_value('get_slides_slide_images', 'folder', request.folder, 'str')
        self.initialize('get_slides_slide_images', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_images', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_images', 'folder')

    def test_get_slides_slide_images_invalid_storage(self):
        """Test case for get_slides_slide_images with invalid storage
        """
        request = self.__prepare_get_slides_slide_images_request()
        request.storage = self.get_invalid_test_value('get_slides_slide_images', 'storage', request.storage, 'str')
        self.initialize('get_slides_slide_images', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slide_images(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_images', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_images', 'storage')

    def __prepare_get_slides_slide_images_request(self):
        name = self.get_test_value('get_slides_slide_images', 'name', 'str')
        slide_index = self.get_test_value('get_slides_slide_images', 'slide_index', 'int')
        password = self.get_test_value('get_slides_slide_images', 'password', 'str')
        folder = self.get_test_value('get_slides_slide_images', 'folder', 'str')
        storage = self.get_test_value('get_slides_slide_images', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesSlideImagesRequest(name, slide_index, password, folder, storage)

    def test_get_slides_slide_text_items(self):
        """Test case for get_slides_slide_text_items
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        self.initialize('get_slides_slide_text_items', None, None)
        response = self.api.get_slides_slide_text_items(request)
        self.assertIsNotNone(response)

    def test_get_slides_slide_text_items_invalid_name(self):
        """Test case for get_slides_slide_text_items with invalid name
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.name = self.get_invalid_test_value('get_slides_slide_text_items', 'name', request.name, 'str')
        self.initialize('get_slides_slide_text_items', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'name')

    def test_get_slides_slide_text_items_invalid_slide_index(self):
        """Test case for get_slides_slide_text_items with invalid slide_index
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.slide_index = self.get_invalid_test_value('get_slides_slide_text_items', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_slide_text_items', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'slide_index')

    def test_get_slides_slide_text_items_invalid_with_empty(self):
        """Test case for get_slides_slide_text_items with invalid with_empty
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.with_empty = self.get_invalid_test_value('get_slides_slide_text_items', 'with_empty', request.with_empty, 'bool')
        self.initialize('get_slides_slide_text_items', 'with_empty', request.with_empty)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'with_empty', request.with_empty)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'with_empty')

    def test_get_slides_slide_text_items_invalid_password(self):
        """Test case for get_slides_slide_text_items with invalid password
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.password = self.get_invalid_test_value('get_slides_slide_text_items', 'password', request.password, 'str')
        self.initialize('get_slides_slide_text_items', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'password')

    def test_get_slides_slide_text_items_invalid_folder(self):
        """Test case for get_slides_slide_text_items with invalid folder
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.folder = self.get_invalid_test_value('get_slides_slide_text_items', 'folder', request.folder, 'str')
        self.initialize('get_slides_slide_text_items', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'folder')

    def test_get_slides_slide_text_items_invalid_storage(self):
        """Test case for get_slides_slide_text_items with invalid storage
        """
        request = self.__prepare_get_slides_slide_text_items_request()
        request.storage = self.get_invalid_test_value('get_slides_slide_text_items', 'storage', request.storage, 'str')
        self.initialize('get_slides_slide_text_items', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slide_text_items(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slide_text_items', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slide_text_items', 'storage')

    def __prepare_get_slides_slide_text_items_request(self):
        name = self.get_test_value('get_slides_slide_text_items', 'name', 'str')
        slide_index = self.get_test_value('get_slides_slide_text_items', 'slide_index', 'int')
        with_empty = self.get_test_value('get_slides_slide_text_items', 'with_empty', 'bool')
        password = self.get_test_value('get_slides_slide_text_items', 'password', 'str')
        folder = self.get_test_value('get_slides_slide_text_items', 'folder', 'str')
        storage = self.get_test_value('get_slides_slide_text_items', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesSlideTextItemsRequest(name, slide_index, with_empty, password, folder, storage)

    def test_get_slides_slides_list(self):
        """Test case for get_slides_slides_list
        """
        request = self.__prepare_get_slides_slides_list_request()
        self.initialize('get_slides_slides_list', None, None)
        response = self.api.get_slides_slides_list(request)
        self.assertIsNotNone(response)

    def test_get_slides_slides_list_invalid_name(self):
        """Test case for get_slides_slides_list with invalid name
        """
        request = self.__prepare_get_slides_slides_list_request()
        request.name = self.get_invalid_test_value('get_slides_slides_list', 'name', request.name, 'str')
        self.initialize('get_slides_slides_list', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slides_list', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slides_list', 'name')

    def test_get_slides_slides_list_invalid_password(self):
        """Test case for get_slides_slides_list with invalid password
        """
        request = self.__prepare_get_slides_slides_list_request()
        request.password = self.get_invalid_test_value('get_slides_slides_list', 'password', request.password, 'str')
        self.initialize('get_slides_slides_list', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slides_list', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slides_list', 'password')

    def test_get_slides_slides_list_invalid_folder(self):
        """Test case for get_slides_slides_list with invalid folder
        """
        request = self.__prepare_get_slides_slides_list_request()
        request.folder = self.get_invalid_test_value('get_slides_slides_list', 'folder', request.folder, 'str')
        self.initialize('get_slides_slides_list', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slides_list', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slides_list', 'folder')

    def test_get_slides_slides_list_invalid_storage(self):
        """Test case for get_slides_slides_list with invalid storage
        """
        request = self.__prepare_get_slides_slides_list_request()
        request.storage = self.get_invalid_test_value('get_slides_slides_list', 'storage', request.storage, 'str')
        self.initialize('get_slides_slides_list', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_slides_list(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_slides_list', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_slides_list', 'storage')

    def __prepare_get_slides_slides_list_request(self):
        name = self.get_test_value('get_slides_slides_list', 'name', 'str')
        password = self.get_test_value('get_slides_slides_list', 'password', 'str')
        folder = self.get_test_value('get_slides_slides_list', 'folder', 'str')
        storage = self.get_test_value('get_slides_slides_list', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesSlidesListRequest(name, password, folder, storage)

    def test_get_slides_theme(self):
        """Test case for get_slides_theme
        """
        request = self.__prepare_get_slides_theme_request()
        self.initialize('get_slides_theme', None, None)
        response = self.api.get_slides_theme(request)
        self.assertIsNotNone(response)

    def test_get_slides_theme_invalid_name(self):
        """Test case for get_slides_theme with invalid name
        """
        request = self.__prepare_get_slides_theme_request()
        request.name = self.get_invalid_test_value('get_slides_theme', 'name', request.name, 'str')
        self.initialize('get_slides_theme', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme', 'name')

    def test_get_slides_theme_invalid_slide_index(self):
        """Test case for get_slides_theme with invalid slide_index
        """
        request = self.__prepare_get_slides_theme_request()
        request.slide_index = self.get_invalid_test_value('get_slides_theme', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_theme', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme', 'slide_index')

    def test_get_slides_theme_invalid_password(self):
        """Test case for get_slides_theme with invalid password
        """
        request = self.__prepare_get_slides_theme_request()
        request.password = self.get_invalid_test_value('get_slides_theme', 'password', request.password, 'str')
        self.initialize('get_slides_theme', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme', 'password')

    def test_get_slides_theme_invalid_folder(self):
        """Test case for get_slides_theme with invalid folder
        """
        request = self.__prepare_get_slides_theme_request()
        request.folder = self.get_invalid_test_value('get_slides_theme', 'folder', request.folder, 'str')
        self.initialize('get_slides_theme', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme', 'folder')

    def test_get_slides_theme_invalid_storage(self):
        """Test case for get_slides_theme with invalid storage
        """
        request = self.__prepare_get_slides_theme_request()
        request.storage = self.get_invalid_test_value('get_slides_theme', 'storage', request.storage, 'str')
        self.initialize('get_slides_theme', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_theme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme', 'storage')

    def __prepare_get_slides_theme_request(self):
        name = self.get_test_value('get_slides_theme', 'name', 'str')
        slide_index = self.get_test_value('get_slides_theme', 'slide_index', 'int')
        password = self.get_test_value('get_slides_theme', 'password', 'str')
        folder = self.get_test_value('get_slides_theme', 'folder', 'str')
        storage = self.get_test_value('get_slides_theme', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesThemeRequest(name, slide_index, password, folder, storage)

    def test_get_slides_theme_color_scheme(self):
        """Test case for get_slides_theme_color_scheme
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        self.initialize('get_slides_theme_color_scheme', None, None)
        response = self.api.get_slides_theme_color_scheme(request)
        self.assertIsNotNone(response)

    def test_get_slides_theme_color_scheme_invalid_name(self):
        """Test case for get_slides_theme_color_scheme with invalid name
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        request.name = self.get_invalid_test_value('get_slides_theme_color_scheme', 'name', request.name, 'str')
        self.initialize('get_slides_theme_color_scheme', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_color_scheme', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_color_scheme', 'name')

    def test_get_slides_theme_color_scheme_invalid_slide_index(self):
        """Test case for get_slides_theme_color_scheme with invalid slide_index
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        request.slide_index = self.get_invalid_test_value('get_slides_theme_color_scheme', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_theme_color_scheme', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_color_scheme', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_color_scheme', 'slide_index')

    def test_get_slides_theme_color_scheme_invalid_password(self):
        """Test case for get_slides_theme_color_scheme with invalid password
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        request.password = self.get_invalid_test_value('get_slides_theme_color_scheme', 'password', request.password, 'str')
        self.initialize('get_slides_theme_color_scheme', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_color_scheme', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_color_scheme', 'password')

    def test_get_slides_theme_color_scheme_invalid_folder(self):
        """Test case for get_slides_theme_color_scheme with invalid folder
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        request.folder = self.get_invalid_test_value('get_slides_theme_color_scheme', 'folder', request.folder, 'str')
        self.initialize('get_slides_theme_color_scheme', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_color_scheme', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_color_scheme', 'folder')

    def test_get_slides_theme_color_scheme_invalid_storage(self):
        """Test case for get_slides_theme_color_scheme with invalid storage
        """
        request = self.__prepare_get_slides_theme_color_scheme_request()
        request.storage = self.get_invalid_test_value('get_slides_theme_color_scheme', 'storage', request.storage, 'str')
        self.initialize('get_slides_theme_color_scheme', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_theme_color_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_color_scheme', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_color_scheme', 'storage')

    def __prepare_get_slides_theme_color_scheme_request(self):
        name = self.get_test_value('get_slides_theme_color_scheme', 'name', 'str')
        slide_index = self.get_test_value('get_slides_theme_color_scheme', 'slide_index', 'int')
        password = self.get_test_value('get_slides_theme_color_scheme', 'password', 'str')
        folder = self.get_test_value('get_slides_theme_color_scheme', 'folder', 'str')
        storage = self.get_test_value('get_slides_theme_color_scheme', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesThemeColorSchemeRequest(name, slide_index, password, folder, storage)

    def test_get_slides_theme_font_scheme(self):
        """Test case for get_slides_theme_font_scheme
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        self.initialize('get_slides_theme_font_scheme', None, None)
        response = self.api.get_slides_theme_font_scheme(request)
        self.assertIsNotNone(response)

    def test_get_slides_theme_font_scheme_invalid_name(self):
        """Test case for get_slides_theme_font_scheme with invalid name
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        request.name = self.get_invalid_test_value('get_slides_theme_font_scheme', 'name', request.name, 'str')
        self.initialize('get_slides_theme_font_scheme', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_font_scheme', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_font_scheme', 'name')

    def test_get_slides_theme_font_scheme_invalid_slide_index(self):
        """Test case for get_slides_theme_font_scheme with invalid slide_index
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        request.slide_index = self.get_invalid_test_value('get_slides_theme_font_scheme', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_theme_font_scheme', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_font_scheme', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_font_scheme', 'slide_index')

    def test_get_slides_theme_font_scheme_invalid_password(self):
        """Test case for get_slides_theme_font_scheme with invalid password
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        request.password = self.get_invalid_test_value('get_slides_theme_font_scheme', 'password', request.password, 'str')
        self.initialize('get_slides_theme_font_scheme', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_font_scheme', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_font_scheme', 'password')

    def test_get_slides_theme_font_scheme_invalid_folder(self):
        """Test case for get_slides_theme_font_scheme with invalid folder
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        request.folder = self.get_invalid_test_value('get_slides_theme_font_scheme', 'folder', request.folder, 'str')
        self.initialize('get_slides_theme_font_scheme', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_font_scheme', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_font_scheme', 'folder')

    def test_get_slides_theme_font_scheme_invalid_storage(self):
        """Test case for get_slides_theme_font_scheme with invalid storage
        """
        request = self.__prepare_get_slides_theme_font_scheme_request()
        request.storage = self.get_invalid_test_value('get_slides_theme_font_scheme', 'storage', request.storage, 'str')
        self.initialize('get_slides_theme_font_scheme', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_theme_font_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_font_scheme', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_font_scheme', 'storage')

    def __prepare_get_slides_theme_font_scheme_request(self):
        name = self.get_test_value('get_slides_theme_font_scheme', 'name', 'str')
        slide_index = self.get_test_value('get_slides_theme_font_scheme', 'slide_index', 'int')
        password = self.get_test_value('get_slides_theme_font_scheme', 'password', 'str')
        folder = self.get_test_value('get_slides_theme_font_scheme', 'folder', 'str')
        storage = self.get_test_value('get_slides_theme_font_scheme', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesThemeFontSchemeRequest(name, slide_index, password, folder, storage)

    def test_get_slides_theme_format_scheme(self):
        """Test case for get_slides_theme_format_scheme
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        self.initialize('get_slides_theme_format_scheme', None, None)
        response = self.api.get_slides_theme_format_scheme(request)
        self.assertIsNotNone(response)

    def test_get_slides_theme_format_scheme_invalid_name(self):
        """Test case for get_slides_theme_format_scheme with invalid name
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        request.name = self.get_invalid_test_value('get_slides_theme_format_scheme', 'name', request.name, 'str')
        self.initialize('get_slides_theme_format_scheme', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_format_scheme', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_format_scheme', 'name')

    def test_get_slides_theme_format_scheme_invalid_slide_index(self):
        """Test case for get_slides_theme_format_scheme with invalid slide_index
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        request.slide_index = self.get_invalid_test_value('get_slides_theme_format_scheme', 'slide_index', request.slide_index, 'int')
        self.initialize('get_slides_theme_format_scheme', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_format_scheme', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_format_scheme', 'slide_index')

    def test_get_slides_theme_format_scheme_invalid_password(self):
        """Test case for get_slides_theme_format_scheme with invalid password
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        request.password = self.get_invalid_test_value('get_slides_theme_format_scheme', 'password', request.password, 'str')
        self.initialize('get_slides_theme_format_scheme', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_format_scheme', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_format_scheme', 'password')

    def test_get_slides_theme_format_scheme_invalid_folder(self):
        """Test case for get_slides_theme_format_scheme with invalid folder
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        request.folder = self.get_invalid_test_value('get_slides_theme_format_scheme', 'folder', request.folder, 'str')
        self.initialize('get_slides_theme_format_scheme', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_format_scheme', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_format_scheme', 'folder')

    def test_get_slides_theme_format_scheme_invalid_storage(self):
        """Test case for get_slides_theme_format_scheme with invalid storage
        """
        request = self.__prepare_get_slides_theme_format_scheme_request()
        request.storage = self.get_invalid_test_value('get_slides_theme_format_scheme', 'storage', request.storage, 'str')
        self.initialize('get_slides_theme_format_scheme', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_theme_format_scheme(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_theme_format_scheme', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_theme_format_scheme', 'storage')

    def __prepare_get_slides_theme_format_scheme_request(self):
        name = self.get_test_value('get_slides_theme_format_scheme', 'name', 'str')
        slide_index = self.get_test_value('get_slides_theme_format_scheme', 'slide_index', 'int')
        password = self.get_test_value('get_slides_theme_format_scheme', 'password', 'str')
        folder = self.get_test_value('get_slides_theme_format_scheme', 'folder', 'str')
        storage = self.get_test_value('get_slides_theme_format_scheme', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesThemeFormatSchemeRequest(name, slide_index, password, folder, storage)

    def test_get_slides_view_properties(self):
        """Test case for get_slides_view_properties
        """
        request = self.__prepare_get_slides_view_properties_request()
        self.initialize('get_slides_view_properties', None, None)
        response = self.api.get_slides_view_properties(request)
        self.assertIsNotNone(response)

    def test_get_slides_view_properties_invalid_name(self):
        """Test case for get_slides_view_properties with invalid name
        """
        request = self.__prepare_get_slides_view_properties_request()
        request.name = self.get_invalid_test_value('get_slides_view_properties', 'name', request.name, 'str')
        self.initialize('get_slides_view_properties', 'name', request.name)
        ok = False
        try:
            self.api.get_slides_view_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_view_properties', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_view_properties', 'name')

    def test_get_slides_view_properties_invalid_password(self):
        """Test case for get_slides_view_properties with invalid password
        """
        request = self.__prepare_get_slides_view_properties_request()
        request.password = self.get_invalid_test_value('get_slides_view_properties', 'password', request.password, 'str')
        self.initialize('get_slides_view_properties', 'password', request.password)
        ok = False
        try:
            self.api.get_slides_view_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_view_properties', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_view_properties', 'password')

    def test_get_slides_view_properties_invalid_folder(self):
        """Test case for get_slides_view_properties with invalid folder
        """
        request = self.__prepare_get_slides_view_properties_request()
        request.folder = self.get_invalid_test_value('get_slides_view_properties', 'folder', request.folder, 'str')
        self.initialize('get_slides_view_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.get_slides_view_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_view_properties', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_view_properties', 'folder')

    def test_get_slides_view_properties_invalid_storage(self):
        """Test case for get_slides_view_properties with invalid storage
        """
        request = self.__prepare_get_slides_view_properties_request()
        request.storage = self.get_invalid_test_value('get_slides_view_properties', 'storage', request.storage, 'str')
        self.initialize('get_slides_view_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.get_slides_view_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_slides_view_properties', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_slides_view_properties', 'storage')

    def __prepare_get_slides_view_properties_request(self):
        name = self.get_test_value('get_slides_view_properties', 'name', 'str')
        password = self.get_test_value('get_slides_view_properties', 'password', 'str')
        folder = self.get_test_value('get_slides_view_properties', 'folder', 'str')
        storage = self.get_test_value('get_slides_view_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSlidesViewPropertiesRequest(name, password, folder, storage)

    def test_get_subshape_paragraph_portion(self):
        """Test case for get_subshape_paragraph_portion
        """
        request = self.__prepare_get_subshape_paragraph_portion_request()
        self.initialize('get_subshape_paragraph_portion', None, None)
        response = self.api.get_subshape_paragraph_portion(request)
        self.assertIsNotNone(response)

    def test_get_subshape_paragraph_portion_invalid_name(self):
        """Test case for get_subshape_paragraph_portion with invalid name
        """
        request = self.__prepare_get_subshape_paragraph_portion_request()
        request.name = self.get_invalid_test_value('get_subshape_paragraph_portion', 'name', request.name, 'str')
        self.initialize('get_subshape_paragraph_portion', 'name', request.name)
        ok = False
        try:
            self.api.get_subshape_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portion', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portion', 'name')

    def test_get_subshape_paragraph_portion_invalid_slide_index(self):
        """Test case for get_subshape_paragraph_portion with invalid slide_index
        """
        request = self.__prepare_get_subshape_paragraph_portion_request()
        request.slide_index = self.get_invalid_test_value('get_subshape_paragraph_portion', 'slide_index', request.slide_index, 'int')
        self.initialize('get_subshape_paragraph_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_subshape_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portion', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portion', 'slide_index')

    def test_get_subshape_paragraph_portion_invalid_shape_index(self):
        """Test case for get_subshape_paragraph_portion with invalid shape_index
        """
        request = self.__prepare_get_subshape_paragraph_portion_request()
        request.shape_index = self.get_invalid_test_value('get_subshape_paragraph_portion', 'shape_index', request.shape_index, 'int')
        self.initialize('get_subshape_paragraph_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_subshape_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portion', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portion', 'shape_index')

    def test_get_subshape_paragraph_portion_invalid_paragraph_index(self):
        """Test case for get_subshape_paragraph_portion with invalid paragraph_index
        """
        request = self.__prepare_get_subshape_paragraph_portion_request()
        request.paragraph_index = self.get_invalid_test_value('get_subshape_paragraph_portion', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_subshape_paragraph_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_subshape_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portion', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portion', 'paragraph_index')

    def test_get_subshape_paragraph_portion_invalid_portion_index(self):
        """Test case for get_subshape_paragraph_portion with invalid portion_index
        """
        request = self.__prepare_get_subshape_paragraph_portion_request()
        request.portion_index = self.get_invalid_test_value('get_subshape_paragraph_portion', 'portion_index', request.portion_index, 'int')
        self.initialize('get_subshape_paragraph_portion', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.get_subshape_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portion', 'portion_index', request.portion_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portion', 'portion_index')

    def test_get_subshape_paragraph_portion_invalid_path(self):
        """Test case for get_subshape_paragraph_portion with invalid path
        """
        request = self.__prepare_get_subshape_paragraph_portion_request()
        request.path = self.get_invalid_test_value('get_subshape_paragraph_portion', 'path', request.path, 'str')
        self.initialize('get_subshape_paragraph_portion', 'path', request.path)
        ok = False
        try:
            self.api.get_subshape_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portion', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portion', 'path')

    def test_get_subshape_paragraph_portion_invalid_password(self):
        """Test case for get_subshape_paragraph_portion with invalid password
        """
        request = self.__prepare_get_subshape_paragraph_portion_request()
        request.password = self.get_invalid_test_value('get_subshape_paragraph_portion', 'password', request.password, 'str')
        self.initialize('get_subshape_paragraph_portion', 'password', request.password)
        ok = False
        try:
            self.api.get_subshape_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portion', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portion', 'password')

    def test_get_subshape_paragraph_portion_invalid_folder(self):
        """Test case for get_subshape_paragraph_portion with invalid folder
        """
        request = self.__prepare_get_subshape_paragraph_portion_request()
        request.folder = self.get_invalid_test_value('get_subshape_paragraph_portion', 'folder', request.folder, 'str')
        self.initialize('get_subshape_paragraph_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.get_subshape_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portion', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portion', 'folder')

    def test_get_subshape_paragraph_portion_invalid_storage(self):
        """Test case for get_subshape_paragraph_portion with invalid storage
        """
        request = self.__prepare_get_subshape_paragraph_portion_request()
        request.storage = self.get_invalid_test_value('get_subshape_paragraph_portion', 'storage', request.storage, 'str')
        self.initialize('get_subshape_paragraph_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.get_subshape_paragraph_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portion', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portion', 'storage')

    def __prepare_get_subshape_paragraph_portion_request(self):
        name = self.get_test_value('get_subshape_paragraph_portion', 'name', 'str')
        slide_index = self.get_test_value('get_subshape_paragraph_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('get_subshape_paragraph_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_subshape_paragraph_portion', 'paragraph_index', 'int')
        portion_index = self.get_test_value('get_subshape_paragraph_portion', 'portion_index', 'int')
        path = self.get_test_value('get_subshape_paragraph_portion', 'path', 'str')
        password = self.get_test_value('get_subshape_paragraph_portion', 'password', 'str')
        folder = self.get_test_value('get_subshape_paragraph_portion', 'folder', 'str')
        storage = self.get_test_value('get_subshape_paragraph_portion', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSubshapeParagraphPortionRequest(name, slide_index, shape_index, paragraph_index, portion_index, path, password, folder, storage)

    def test_get_subshape_paragraph_portions(self):
        """Test case for get_subshape_paragraph_portions
        """
        request = self.__prepare_get_subshape_paragraph_portions_request()
        self.initialize('get_subshape_paragraph_portions', None, None)
        response = self.api.get_subshape_paragraph_portions(request)
        self.assertIsNotNone(response)

    def test_get_subshape_paragraph_portions_invalid_name(self):
        """Test case for get_subshape_paragraph_portions with invalid name
        """
        request = self.__prepare_get_subshape_paragraph_portions_request()
        request.name = self.get_invalid_test_value('get_subshape_paragraph_portions', 'name', request.name, 'str')
        self.initialize('get_subshape_paragraph_portions', 'name', request.name)
        ok = False
        try:
            self.api.get_subshape_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portions', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portions', 'name')

    def test_get_subshape_paragraph_portions_invalid_slide_index(self):
        """Test case for get_subshape_paragraph_portions with invalid slide_index
        """
        request = self.__prepare_get_subshape_paragraph_portions_request()
        request.slide_index = self.get_invalid_test_value('get_subshape_paragraph_portions', 'slide_index', request.slide_index, 'int')
        self.initialize('get_subshape_paragraph_portions', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.get_subshape_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portions', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portions', 'slide_index')

    def test_get_subshape_paragraph_portions_invalid_shape_index(self):
        """Test case for get_subshape_paragraph_portions with invalid shape_index
        """
        request = self.__prepare_get_subshape_paragraph_portions_request()
        request.shape_index = self.get_invalid_test_value('get_subshape_paragraph_portions', 'shape_index', request.shape_index, 'int')
        self.initialize('get_subshape_paragraph_portions', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.get_subshape_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portions', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portions', 'shape_index')

    def test_get_subshape_paragraph_portions_invalid_paragraph_index(self):
        """Test case for get_subshape_paragraph_portions with invalid paragraph_index
        """
        request = self.__prepare_get_subshape_paragraph_portions_request()
        request.paragraph_index = self.get_invalid_test_value('get_subshape_paragraph_portions', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('get_subshape_paragraph_portions', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.get_subshape_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portions', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portions', 'paragraph_index')

    def test_get_subshape_paragraph_portions_invalid_path(self):
        """Test case for get_subshape_paragraph_portions with invalid path
        """
        request = self.__prepare_get_subshape_paragraph_portions_request()
        request.path = self.get_invalid_test_value('get_subshape_paragraph_portions', 'path', request.path, 'str')
        self.initialize('get_subshape_paragraph_portions', 'path', request.path)
        ok = False
        try:
            self.api.get_subshape_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portions', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portions', 'path')

    def test_get_subshape_paragraph_portions_invalid_password(self):
        """Test case for get_subshape_paragraph_portions with invalid password
        """
        request = self.__prepare_get_subshape_paragraph_portions_request()
        request.password = self.get_invalid_test_value('get_subshape_paragraph_portions', 'password', request.password, 'str')
        self.initialize('get_subshape_paragraph_portions', 'password', request.password)
        ok = False
        try:
            self.api.get_subshape_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portions', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portions', 'password')

    def test_get_subshape_paragraph_portions_invalid_folder(self):
        """Test case for get_subshape_paragraph_portions with invalid folder
        """
        request = self.__prepare_get_subshape_paragraph_portions_request()
        request.folder = self.get_invalid_test_value('get_subshape_paragraph_portions', 'folder', request.folder, 'str')
        self.initialize('get_subshape_paragraph_portions', 'folder', request.folder)
        ok = False
        try:
            self.api.get_subshape_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portions', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portions', 'folder')

    def test_get_subshape_paragraph_portions_invalid_storage(self):
        """Test case for get_subshape_paragraph_portions with invalid storage
        """
        request = self.__prepare_get_subshape_paragraph_portions_request()
        request.storage = self.get_invalid_test_value('get_subshape_paragraph_portions', 'storage', request.storage, 'str')
        self.initialize('get_subshape_paragraph_portions', 'storage', request.storage)
        ok = False
        try:
            self.api.get_subshape_paragraph_portions(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'get_subshape_paragraph_portions', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('get_subshape_paragraph_portions', 'storage')

    def __prepare_get_subshape_paragraph_portions_request(self):
        name = self.get_test_value('get_subshape_paragraph_portions', 'name', 'str')
        slide_index = self.get_test_value('get_subshape_paragraph_portions', 'slide_index', 'int')
        shape_index = self.get_test_value('get_subshape_paragraph_portions', 'shape_index', 'int')
        paragraph_index = self.get_test_value('get_subshape_paragraph_portions', 'paragraph_index', 'int')
        path = self.get_test_value('get_subshape_paragraph_portions', 'path', 'str')
        password = self.get_test_value('get_subshape_paragraph_portions', 'password', 'str')
        folder = self.get_test_value('get_subshape_paragraph_portions', 'folder', 'str')
        storage = self.get_test_value('get_subshape_paragraph_portions', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.GetSubshapeParagraphPortionsRequest(name, slide_index, shape_index, paragraph_index, path, password, folder, storage)

    def test_move_file(self):
        """Test case for move_file
        """
        request = self.__prepare_move_file_request()
        self.initialize('move_file', None, None)
        response = self.api.move_file(request)
        self.assertIsNone(response)

    def test_move_file_invalid_src_path(self):
        """Test case for move_file with invalid src_path
        """
        request = self.__prepare_move_file_request()
        request.src_path = self.get_invalid_test_value('move_file', 'src_path', request.src_path, 'str')
        self.initialize('move_file', 'src_path', request.src_path)
        ok = False
        try:
            self.api.move_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'move_file', 'src_path', request.src_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('move_file', 'src_path')

    def test_move_file_invalid_dest_path(self):
        """Test case for move_file with invalid dest_path
        """
        request = self.__prepare_move_file_request()
        request.dest_path = self.get_invalid_test_value('move_file', 'dest_path', request.dest_path, 'str')
        self.initialize('move_file', 'dest_path', request.dest_path)
        ok = False
        try:
            self.api.move_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'move_file', 'dest_path', request.dest_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('move_file', 'dest_path')

    def test_move_file_invalid_src_storage_name(self):
        """Test case for move_file with invalid src_storage_name
        """
        request = self.__prepare_move_file_request()
        request.src_storage_name = self.get_invalid_test_value('move_file', 'src_storage_name', request.src_storage_name, 'str')
        self.initialize('move_file', 'src_storage_name', request.src_storage_name)
        ok = False
        try:
            self.api.move_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'move_file', 'src_storage_name', request.src_storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('move_file', 'src_storage_name')

    def test_move_file_invalid_dest_storage_name(self):
        """Test case for move_file with invalid dest_storage_name
        """
        request = self.__prepare_move_file_request()
        request.dest_storage_name = self.get_invalid_test_value('move_file', 'dest_storage_name', request.dest_storage_name, 'str')
        self.initialize('move_file', 'dest_storage_name', request.dest_storage_name)
        ok = False
        try:
            self.api.move_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'move_file', 'dest_storage_name', request.dest_storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('move_file', 'dest_storage_name')

    def test_move_file_invalid_version_id(self):
        """Test case for move_file with invalid version_id
        """
        request = self.__prepare_move_file_request()
        request.version_id = self.get_invalid_test_value('move_file', 'version_id', request.version_id, 'str')
        self.initialize('move_file', 'version_id', request.version_id)
        ok = False
        try:
            self.api.move_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'move_file', 'version_id', request.version_id)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('move_file', 'version_id')

    def __prepare_move_file_request(self):
        src_path = self.get_test_value('move_file', 'src_path', 'str')
        dest_path = self.get_test_value('move_file', 'dest_path', 'str')
        src_storage_name = self.get_test_value('move_file', 'src_storage_name', 'str')
        dest_storage_name = self.get_test_value('move_file', 'dest_storage_name', 'str')
        version_id = self.get_test_value('move_file', 'version_id', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.MoveFileRequest(src_path, dest_path, src_storage_name, dest_storage_name, version_id)

    def test_move_folder(self):
        """Test case for move_folder
        """
        request = self.__prepare_move_folder_request()
        self.initialize('move_folder', None, None)
        response = self.api.move_folder(request)
        self.assertIsNone(response)

    def test_move_folder_invalid_src_path(self):
        """Test case for move_folder with invalid src_path
        """
        request = self.__prepare_move_folder_request()
        request.src_path = self.get_invalid_test_value('move_folder', 'src_path', request.src_path, 'str')
        self.initialize('move_folder', 'src_path', request.src_path)
        ok = False
        try:
            self.api.move_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'move_folder', 'src_path', request.src_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('move_folder', 'src_path')

    def test_move_folder_invalid_dest_path(self):
        """Test case for move_folder with invalid dest_path
        """
        request = self.__prepare_move_folder_request()
        request.dest_path = self.get_invalid_test_value('move_folder', 'dest_path', request.dest_path, 'str')
        self.initialize('move_folder', 'dest_path', request.dest_path)
        ok = False
        try:
            self.api.move_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'move_folder', 'dest_path', request.dest_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('move_folder', 'dest_path')

    def test_move_folder_invalid_src_storage_name(self):
        """Test case for move_folder with invalid src_storage_name
        """
        request = self.__prepare_move_folder_request()
        request.src_storage_name = self.get_invalid_test_value('move_folder', 'src_storage_name', request.src_storage_name, 'str')
        self.initialize('move_folder', 'src_storage_name', request.src_storage_name)
        ok = False
        try:
            self.api.move_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'move_folder', 'src_storage_name', request.src_storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('move_folder', 'src_storage_name')

    def test_move_folder_invalid_dest_storage_name(self):
        """Test case for move_folder with invalid dest_storage_name
        """
        request = self.__prepare_move_folder_request()
        request.dest_storage_name = self.get_invalid_test_value('move_folder', 'dest_storage_name', request.dest_storage_name, 'str')
        self.initialize('move_folder', 'dest_storage_name', request.dest_storage_name)
        ok = False
        try:
            self.api.move_folder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'move_folder', 'dest_storage_name', request.dest_storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('move_folder', 'dest_storage_name')

    def __prepare_move_folder_request(self):
        src_path = self.get_test_value('move_folder', 'src_path', 'str')
        dest_path = self.get_test_value('move_folder', 'dest_path', 'str')
        src_storage_name = self.get_test_value('move_folder', 'src_storage_name', 'str')
        dest_storage_name = self.get_test_value('move_folder', 'dest_storage_name', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.MoveFolderRequest(src_path, dest_path, src_storage_name, dest_storage_name)

    def test_object_exists(self):
        """Test case for object_exists
        """
        request = self.__prepare_object_exists_request()
        self.initialize('object_exists', None, None)
        response = self.api.object_exists(request)
        self.assertIsNotNone(response)

    def test_object_exists_invalid_path(self):
        """Test case for object_exists with invalid path
        """
        request = self.__prepare_object_exists_request()
        request.path = self.get_invalid_test_value('object_exists', 'path', request.path, 'str')
        self.initialize('object_exists', 'path', request.path)
        ok = False
        try:
            self.api.object_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'object_exists', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('object_exists', 'path')

    def test_object_exists_invalid_storage_name(self):
        """Test case for object_exists with invalid storage_name
        """
        request = self.__prepare_object_exists_request()
        request.storage_name = self.get_invalid_test_value('object_exists', 'storage_name', request.storage_name, 'str')
        self.initialize('object_exists', 'storage_name', request.storage_name)
        ok = False
        try:
            self.api.object_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'object_exists', 'storage_name', request.storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('object_exists', 'storage_name')

    def test_object_exists_invalid_version_id(self):
        """Test case for object_exists with invalid version_id
        """
        request = self.__prepare_object_exists_request()
        request.version_id = self.get_invalid_test_value('object_exists', 'version_id', request.version_id, 'str')
        self.initialize('object_exists', 'version_id', request.version_id)
        ok = False
        try:
            self.api.object_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'object_exists', 'version_id', request.version_id)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('object_exists', 'version_id')

    def __prepare_object_exists_request(self):
        path = self.get_test_value('object_exists', 'path', 'str')
        storage_name = self.get_test_value('object_exists', 'storage_name', 'str')
        version_id = self.get_test_value('object_exists', 'version_id', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.ObjectExistsRequest(path, storage_name, version_id)

    def test_post_add_new_paragraph(self):
        """Test case for post_add_new_paragraph
        """
        request = self.__prepare_post_add_new_paragraph_request()
        self.initialize('post_add_new_paragraph', None, None)
        response = self.api.post_add_new_paragraph(request)
        self.assertIsNotNone(response)

    def test_post_add_new_paragraph_invalid_name(self):
        """Test case for post_add_new_paragraph with invalid name
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.name = self.get_invalid_test_value('post_add_new_paragraph', 'name', request.name, 'str')
        self.initialize('post_add_new_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'name')

    def test_post_add_new_paragraph_invalid_slide_index(self):
        """Test case for post_add_new_paragraph with invalid slide_index
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.slide_index = self.get_invalid_test_value('post_add_new_paragraph', 'slide_index', request.slide_index, 'int')
        self.initialize('post_add_new_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'slide_index')

    def test_post_add_new_paragraph_invalid_shape_index(self):
        """Test case for post_add_new_paragraph with invalid shape_index
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.shape_index = self.get_invalid_test_value('post_add_new_paragraph', 'shape_index', request.shape_index, 'int')
        self.initialize('post_add_new_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'shape_index')

    def test_post_add_new_paragraph_invalid_dto(self):
        """Test case for post_add_new_paragraph with invalid dto
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.dto = self.get_invalid_test_value('post_add_new_paragraph', 'dto', request.dto, 'Paragraph')
        self.initialize('post_add_new_paragraph', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'dto')

    def test_post_add_new_paragraph_invalid_password(self):
        """Test case for post_add_new_paragraph with invalid password
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.password = self.get_invalid_test_value('post_add_new_paragraph', 'password', request.password, 'str')
        self.initialize('post_add_new_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'password')

    def test_post_add_new_paragraph_invalid_folder(self):
        """Test case for post_add_new_paragraph with invalid folder
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.folder = self.get_invalid_test_value('post_add_new_paragraph', 'folder', request.folder, 'str')
        self.initialize('post_add_new_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'folder')

    def test_post_add_new_paragraph_invalid_storage(self):
        """Test case for post_add_new_paragraph with invalid storage
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.storage = self.get_invalid_test_value('post_add_new_paragraph', 'storage', request.storage, 'str')
        self.initialize('post_add_new_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'storage')

    def test_post_add_new_paragraph_invalid_position(self):
        """Test case for post_add_new_paragraph with invalid position
        """
        request = self.__prepare_post_add_new_paragraph_request()
        request.position = self.get_invalid_test_value('post_add_new_paragraph', 'position', request.position, 'int')
        self.initialize('post_add_new_paragraph', 'position', request.position)
        ok = False
        try:
            self.api.post_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_paragraph', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_paragraph', 'position')

    def __prepare_post_add_new_paragraph_request(self):
        name = self.get_test_value('post_add_new_paragraph', 'name', 'str')
        slide_index = self.get_test_value('post_add_new_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('post_add_new_paragraph', 'shape_index', 'int')
        dto = self.get_test_value('post_add_new_paragraph', 'dto', 'Paragraph')
        password = self.get_test_value('post_add_new_paragraph', 'password', 'str')
        folder = self.get_test_value('post_add_new_paragraph', 'folder', 'str')
        storage = self.get_test_value('post_add_new_paragraph', 'storage', 'str')
        position = self.get_test_value('post_add_new_paragraph', 'position', 'int')
        return asposeslidescloud.models.requests.slides_api_requests.PostAddNewParagraphRequest(name, slide_index, shape_index, dto, password, folder, storage, position)

    def test_post_add_new_portion(self):
        """Test case for post_add_new_portion
        """
        request = self.__prepare_post_add_new_portion_request()
        self.initialize('post_add_new_portion', None, None)
        response = self.api.post_add_new_portion(request)
        self.assertIsNotNone(response)

    def test_post_add_new_portion_invalid_name(self):
        """Test case for post_add_new_portion with invalid name
        """
        request = self.__prepare_post_add_new_portion_request()
        request.name = self.get_invalid_test_value('post_add_new_portion', 'name', request.name, 'str')
        self.initialize('post_add_new_portion', 'name', request.name)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_portion', 'name')

    def test_post_add_new_portion_invalid_slide_index(self):
        """Test case for post_add_new_portion with invalid slide_index
        """
        request = self.__prepare_post_add_new_portion_request()
        request.slide_index = self.get_invalid_test_value('post_add_new_portion', 'slide_index', request.slide_index, 'int')
        self.initialize('post_add_new_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_portion', 'slide_index')

    def test_post_add_new_portion_invalid_shape_index(self):
        """Test case for post_add_new_portion with invalid shape_index
        """
        request = self.__prepare_post_add_new_portion_request()
        request.shape_index = self.get_invalid_test_value('post_add_new_portion', 'shape_index', request.shape_index, 'int')
        self.initialize('post_add_new_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_portion', 'shape_index')

    def test_post_add_new_portion_invalid_paragraph_index(self):
        """Test case for post_add_new_portion with invalid paragraph_index
        """
        request = self.__prepare_post_add_new_portion_request()
        request.paragraph_index = self.get_invalid_test_value('post_add_new_portion', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('post_add_new_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_portion', 'paragraph_index')

    def test_post_add_new_portion_invalid_dto(self):
        """Test case for post_add_new_portion with invalid dto
        """
        request = self.__prepare_post_add_new_portion_request()
        request.dto = self.get_invalid_test_value('post_add_new_portion', 'dto', request.dto, 'Portion')
        self.initialize('post_add_new_portion', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_portion', 'dto')

    def test_post_add_new_portion_invalid_password(self):
        """Test case for post_add_new_portion with invalid password
        """
        request = self.__prepare_post_add_new_portion_request()
        request.password = self.get_invalid_test_value('post_add_new_portion', 'password', request.password, 'str')
        self.initialize('post_add_new_portion', 'password', request.password)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_portion', 'password')

    def test_post_add_new_portion_invalid_folder(self):
        """Test case for post_add_new_portion with invalid folder
        """
        request = self.__prepare_post_add_new_portion_request()
        request.folder = self.get_invalid_test_value('post_add_new_portion', 'folder', request.folder, 'str')
        self.initialize('post_add_new_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_portion', 'folder')

    def test_post_add_new_portion_invalid_storage(self):
        """Test case for post_add_new_portion with invalid storage
        """
        request = self.__prepare_post_add_new_portion_request()
        request.storage = self.get_invalid_test_value('post_add_new_portion', 'storage', request.storage, 'str')
        self.initialize('post_add_new_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_portion', 'storage')

    def test_post_add_new_portion_invalid_position(self):
        """Test case for post_add_new_portion with invalid position
        """
        request = self.__prepare_post_add_new_portion_request()
        request.position = self.get_invalid_test_value('post_add_new_portion', 'position', request.position, 'int')
        self.initialize('post_add_new_portion', 'position', request.position)
        ok = False
        try:
            self.api.post_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_portion', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_portion', 'position')

    def __prepare_post_add_new_portion_request(self):
        name = self.get_test_value('post_add_new_portion', 'name', 'str')
        slide_index = self.get_test_value('post_add_new_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('post_add_new_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('post_add_new_portion', 'paragraph_index', 'int')
        dto = self.get_test_value('post_add_new_portion', 'dto', 'Portion')
        password = self.get_test_value('post_add_new_portion', 'password', 'str')
        folder = self.get_test_value('post_add_new_portion', 'folder', 'str')
        storage = self.get_test_value('post_add_new_portion', 'storage', 'str')
        position = self.get_test_value('post_add_new_portion', 'position', 'int')
        return asposeslidescloud.models.requests.slides_api_requests.PostAddNewPortionRequest(name, slide_index, shape_index, paragraph_index, dto, password, folder, storage, position)

    def test_post_add_new_shape(self):
        """Test case for post_add_new_shape
        """
        request = self.__prepare_post_add_new_shape_request()
        self.initialize('post_add_new_shape', None, None)
        response = self.api.post_add_new_shape(request)
        self.assertIsNotNone(response)

    def test_post_add_new_shape_invalid_name(self):
        """Test case for post_add_new_shape with invalid name
        """
        request = self.__prepare_post_add_new_shape_request()
        request.name = self.get_invalid_test_value('post_add_new_shape', 'name', request.name, 'str')
        self.initialize('post_add_new_shape', 'name', request.name)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_shape', 'name')

    def test_post_add_new_shape_invalid_slide_index(self):
        """Test case for post_add_new_shape with invalid slide_index
        """
        request = self.__prepare_post_add_new_shape_request()
        request.slide_index = self.get_invalid_test_value('post_add_new_shape', 'slide_index', request.slide_index, 'int')
        self.initialize('post_add_new_shape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_shape', 'slide_index')

    def test_post_add_new_shape_invalid_dto(self):
        """Test case for post_add_new_shape with invalid dto
        """
        request = self.__prepare_post_add_new_shape_request()
        request.dto = self.get_invalid_test_value('post_add_new_shape', 'dto', request.dto, 'ShapeBase')
        self.initialize('post_add_new_shape', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_shape', 'dto')

    def test_post_add_new_shape_invalid_password(self):
        """Test case for post_add_new_shape with invalid password
        """
        request = self.__prepare_post_add_new_shape_request()
        request.password = self.get_invalid_test_value('post_add_new_shape', 'password', request.password, 'str')
        self.initialize('post_add_new_shape', 'password', request.password)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_shape', 'password')

    def test_post_add_new_shape_invalid_folder(self):
        """Test case for post_add_new_shape with invalid folder
        """
        request = self.__prepare_post_add_new_shape_request()
        request.folder = self.get_invalid_test_value('post_add_new_shape', 'folder', request.folder, 'str')
        self.initialize('post_add_new_shape', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_shape', 'folder')

    def test_post_add_new_shape_invalid_storage(self):
        """Test case for post_add_new_shape with invalid storage
        """
        request = self.__prepare_post_add_new_shape_request()
        request.storage = self.get_invalid_test_value('post_add_new_shape', 'storage', request.storage, 'str')
        self.initialize('post_add_new_shape', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_shape', 'storage')

    def test_post_add_new_shape_invalid_shape_to_clone(self):
        """Test case for post_add_new_shape with invalid shape_to_clone
        """
        request = self.__prepare_post_add_new_shape_request()
        request.shape_to_clone = self.get_invalid_test_value('post_add_new_shape', 'shape_to_clone', request.shape_to_clone, 'int')
        self.initialize('post_add_new_shape', 'shape_to_clone', request.shape_to_clone)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'shape_to_clone', request.shape_to_clone)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_shape', 'shape_to_clone')

    def test_post_add_new_shape_invalid_position(self):
        """Test case for post_add_new_shape with invalid position
        """
        request = self.__prepare_post_add_new_shape_request()
        request.position = self.get_invalid_test_value('post_add_new_shape', 'position', request.position, 'int')
        self.initialize('post_add_new_shape', 'position', request.position)
        ok = False
        try:
            self.api.post_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_shape', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_shape', 'position')

    def __prepare_post_add_new_shape_request(self):
        name = self.get_test_value('post_add_new_shape', 'name', 'str')
        slide_index = self.get_test_value('post_add_new_shape', 'slide_index', 'int')
        dto = self.get_test_value('post_add_new_shape', 'dto', 'ShapeBase')
        password = self.get_test_value('post_add_new_shape', 'password', 'str')
        folder = self.get_test_value('post_add_new_shape', 'folder', 'str')
        storage = self.get_test_value('post_add_new_shape', 'storage', 'str')
        shape_to_clone = self.get_test_value('post_add_new_shape', 'shape_to_clone', 'int')
        position = self.get_test_value('post_add_new_shape', 'position', 'int')
        return asposeslidescloud.models.requests.slides_api_requests.PostAddNewShapeRequest(name, slide_index, dto, password, folder, storage, shape_to_clone, position)

    def test_post_add_new_subshape(self):
        """Test case for post_add_new_subshape
        """
        request = self.__prepare_post_add_new_subshape_request()
        self.initialize('post_add_new_subshape', None, None)
        response = self.api.post_add_new_subshape(request)
        self.assertIsNotNone(response)

    def test_post_add_new_subshape_invalid_name(self):
        """Test case for post_add_new_subshape with invalid name
        """
        request = self.__prepare_post_add_new_subshape_request()
        request.name = self.get_invalid_test_value('post_add_new_subshape', 'name', request.name, 'str')
        self.initialize('post_add_new_subshape', 'name', request.name)
        ok = False
        try:
            self.api.post_add_new_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape', 'name')

    def test_post_add_new_subshape_invalid_slide_index(self):
        """Test case for post_add_new_subshape with invalid slide_index
        """
        request = self.__prepare_post_add_new_subshape_request()
        request.slide_index = self.get_invalid_test_value('post_add_new_subshape', 'slide_index', request.slide_index, 'int')
        self.initialize('post_add_new_subshape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_new_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape', 'slide_index')

    def test_post_add_new_subshape_invalid_path(self):
        """Test case for post_add_new_subshape with invalid path
        """
        request = self.__prepare_post_add_new_subshape_request()
        request.path = self.get_invalid_test_value('post_add_new_subshape', 'path', request.path, 'str')
        self.initialize('post_add_new_subshape', 'path', request.path)
        ok = False
        try:
            self.api.post_add_new_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape', 'path')

    def test_post_add_new_subshape_invalid_dto(self):
        """Test case for post_add_new_subshape with invalid dto
        """
        request = self.__prepare_post_add_new_subshape_request()
        request.dto = self.get_invalid_test_value('post_add_new_subshape', 'dto', request.dto, 'ShapeBase')
        self.initialize('post_add_new_subshape', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_new_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape', 'dto')

    def test_post_add_new_subshape_invalid_password(self):
        """Test case for post_add_new_subshape with invalid password
        """
        request = self.__prepare_post_add_new_subshape_request()
        request.password = self.get_invalid_test_value('post_add_new_subshape', 'password', request.password, 'str')
        self.initialize('post_add_new_subshape', 'password', request.password)
        ok = False
        try:
            self.api.post_add_new_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape', 'password')

    def test_post_add_new_subshape_invalid_folder(self):
        """Test case for post_add_new_subshape with invalid folder
        """
        request = self.__prepare_post_add_new_subshape_request()
        request.folder = self.get_invalid_test_value('post_add_new_subshape', 'folder', request.folder, 'str')
        self.initialize('post_add_new_subshape', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_new_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape', 'folder')

    def test_post_add_new_subshape_invalid_storage(self):
        """Test case for post_add_new_subshape with invalid storage
        """
        request = self.__prepare_post_add_new_subshape_request()
        request.storage = self.get_invalid_test_value('post_add_new_subshape', 'storage', request.storage, 'str')
        self.initialize('post_add_new_subshape', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_new_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape', 'storage')

    def test_post_add_new_subshape_invalid_shape_to_clone(self):
        """Test case for post_add_new_subshape with invalid shape_to_clone
        """
        request = self.__prepare_post_add_new_subshape_request()
        request.shape_to_clone = self.get_invalid_test_value('post_add_new_subshape', 'shape_to_clone', request.shape_to_clone, 'int')
        self.initialize('post_add_new_subshape', 'shape_to_clone', request.shape_to_clone)
        ok = False
        try:
            self.api.post_add_new_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape', 'shape_to_clone', request.shape_to_clone)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape', 'shape_to_clone')

    def test_post_add_new_subshape_invalid_position(self):
        """Test case for post_add_new_subshape with invalid position
        """
        request = self.__prepare_post_add_new_subshape_request()
        request.position = self.get_invalid_test_value('post_add_new_subshape', 'position', request.position, 'int')
        self.initialize('post_add_new_subshape', 'position', request.position)
        ok = False
        try:
            self.api.post_add_new_subshape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape', 'position')

    def __prepare_post_add_new_subshape_request(self):
        name = self.get_test_value('post_add_new_subshape', 'name', 'str')
        slide_index = self.get_test_value('post_add_new_subshape', 'slide_index', 'int')
        path = self.get_test_value('post_add_new_subshape', 'path', 'str')
        dto = self.get_test_value('post_add_new_subshape', 'dto', 'ShapeBase')
        password = self.get_test_value('post_add_new_subshape', 'password', 'str')
        folder = self.get_test_value('post_add_new_subshape', 'folder', 'str')
        storage = self.get_test_value('post_add_new_subshape', 'storage', 'str')
        shape_to_clone = self.get_test_value('post_add_new_subshape', 'shape_to_clone', 'int')
        position = self.get_test_value('post_add_new_subshape', 'position', 'int')
        return asposeslidescloud.models.requests.slides_api_requests.PostAddNewSubshapeRequest(name, slide_index, path, dto, password, folder, storage, shape_to_clone, position)

    def test_post_add_new_subshape_paragraph(self):
        """Test case for post_add_new_subshape_paragraph
        """
        request = self.__prepare_post_add_new_subshape_paragraph_request()
        self.initialize('post_add_new_subshape_paragraph', None, None)
        response = self.api.post_add_new_subshape_paragraph(request)
        self.assertIsNotNone(response)

    def test_post_add_new_subshape_paragraph_invalid_name(self):
        """Test case for post_add_new_subshape_paragraph with invalid name
        """
        request = self.__prepare_post_add_new_subshape_paragraph_request()
        request.name = self.get_invalid_test_value('post_add_new_subshape_paragraph', 'name', request.name, 'str')
        self.initialize('post_add_new_subshape_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.post_add_new_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_paragraph', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_paragraph', 'name')

    def test_post_add_new_subshape_paragraph_invalid_slide_index(self):
        """Test case for post_add_new_subshape_paragraph with invalid slide_index
        """
        request = self.__prepare_post_add_new_subshape_paragraph_request()
        request.slide_index = self.get_invalid_test_value('post_add_new_subshape_paragraph', 'slide_index', request.slide_index, 'int')
        self.initialize('post_add_new_subshape_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_new_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_paragraph', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_paragraph', 'slide_index')

    def test_post_add_new_subshape_paragraph_invalid_shape_index(self):
        """Test case for post_add_new_subshape_paragraph with invalid shape_index
        """
        request = self.__prepare_post_add_new_subshape_paragraph_request()
        request.shape_index = self.get_invalid_test_value('post_add_new_subshape_paragraph', 'shape_index', request.shape_index, 'int')
        self.initialize('post_add_new_subshape_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_add_new_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_paragraph', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_paragraph', 'shape_index')

    def test_post_add_new_subshape_paragraph_invalid_path(self):
        """Test case for post_add_new_subshape_paragraph with invalid path
        """
        request = self.__prepare_post_add_new_subshape_paragraph_request()
        request.path = self.get_invalid_test_value('post_add_new_subshape_paragraph', 'path', request.path, 'str')
        self.initialize('post_add_new_subshape_paragraph', 'path', request.path)
        ok = False
        try:
            self.api.post_add_new_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_paragraph', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_paragraph', 'path')

    def test_post_add_new_subshape_paragraph_invalid_dto(self):
        """Test case for post_add_new_subshape_paragraph with invalid dto
        """
        request = self.__prepare_post_add_new_subshape_paragraph_request()
        request.dto = self.get_invalid_test_value('post_add_new_subshape_paragraph', 'dto', request.dto, 'Paragraph')
        self.initialize('post_add_new_subshape_paragraph', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_new_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_paragraph', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_paragraph', 'dto')

    def test_post_add_new_subshape_paragraph_invalid_password(self):
        """Test case for post_add_new_subshape_paragraph with invalid password
        """
        request = self.__prepare_post_add_new_subshape_paragraph_request()
        request.password = self.get_invalid_test_value('post_add_new_subshape_paragraph', 'password', request.password, 'str')
        self.initialize('post_add_new_subshape_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.post_add_new_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_paragraph', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_paragraph', 'password')

    def test_post_add_new_subshape_paragraph_invalid_folder(self):
        """Test case for post_add_new_subshape_paragraph with invalid folder
        """
        request = self.__prepare_post_add_new_subshape_paragraph_request()
        request.folder = self.get_invalid_test_value('post_add_new_subshape_paragraph', 'folder', request.folder, 'str')
        self.initialize('post_add_new_subshape_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_new_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_paragraph', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_paragraph', 'folder')

    def test_post_add_new_subshape_paragraph_invalid_storage(self):
        """Test case for post_add_new_subshape_paragraph with invalid storage
        """
        request = self.__prepare_post_add_new_subshape_paragraph_request()
        request.storage = self.get_invalid_test_value('post_add_new_subshape_paragraph', 'storage', request.storage, 'str')
        self.initialize('post_add_new_subshape_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_new_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_paragraph', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_paragraph', 'storage')

    def test_post_add_new_subshape_paragraph_invalid_position(self):
        """Test case for post_add_new_subshape_paragraph with invalid position
        """
        request = self.__prepare_post_add_new_subshape_paragraph_request()
        request.position = self.get_invalid_test_value('post_add_new_subshape_paragraph', 'position', request.position, 'int')
        self.initialize('post_add_new_subshape_paragraph', 'position', request.position)
        ok = False
        try:
            self.api.post_add_new_subshape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_paragraph', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_paragraph', 'position')

    def __prepare_post_add_new_subshape_paragraph_request(self):
        name = self.get_test_value('post_add_new_subshape_paragraph', 'name', 'str')
        slide_index = self.get_test_value('post_add_new_subshape_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('post_add_new_subshape_paragraph', 'shape_index', 'int')
        path = self.get_test_value('post_add_new_subshape_paragraph', 'path', 'str')
        dto = self.get_test_value('post_add_new_subshape_paragraph', 'dto', 'Paragraph')
        password = self.get_test_value('post_add_new_subshape_paragraph', 'password', 'str')
        folder = self.get_test_value('post_add_new_subshape_paragraph', 'folder', 'str')
        storage = self.get_test_value('post_add_new_subshape_paragraph', 'storage', 'str')
        position = self.get_test_value('post_add_new_subshape_paragraph', 'position', 'int')
        return asposeslidescloud.models.requests.slides_api_requests.PostAddNewSubshapeParagraphRequest(name, slide_index, shape_index, path, dto, password, folder, storage, position)

    def test_post_add_new_subshape_portion(self):
        """Test case for post_add_new_subshape_portion
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        self.initialize('post_add_new_subshape_portion', None, None)
        response = self.api.post_add_new_subshape_portion(request)
        self.assertIsNotNone(response)

    def test_post_add_new_subshape_portion_invalid_name(self):
        """Test case for post_add_new_subshape_portion with invalid name
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        request.name = self.get_invalid_test_value('post_add_new_subshape_portion', 'name', request.name, 'str')
        self.initialize('post_add_new_subshape_portion', 'name', request.name)
        ok = False
        try:
            self.api.post_add_new_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_portion', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_portion', 'name')

    def test_post_add_new_subshape_portion_invalid_slide_index(self):
        """Test case for post_add_new_subshape_portion with invalid slide_index
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        request.slide_index = self.get_invalid_test_value('post_add_new_subshape_portion', 'slide_index', request.slide_index, 'int')
        self.initialize('post_add_new_subshape_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_new_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_portion', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_portion', 'slide_index')

    def test_post_add_new_subshape_portion_invalid_shape_index(self):
        """Test case for post_add_new_subshape_portion with invalid shape_index
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        request.shape_index = self.get_invalid_test_value('post_add_new_subshape_portion', 'shape_index', request.shape_index, 'int')
        self.initialize('post_add_new_subshape_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_add_new_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_portion', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_portion', 'shape_index')

    def test_post_add_new_subshape_portion_invalid_paragraph_index(self):
        """Test case for post_add_new_subshape_portion with invalid paragraph_index
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        request.paragraph_index = self.get_invalid_test_value('post_add_new_subshape_portion', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('post_add_new_subshape_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.post_add_new_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_portion', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_portion', 'paragraph_index')

    def test_post_add_new_subshape_portion_invalid_path(self):
        """Test case for post_add_new_subshape_portion with invalid path
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        request.path = self.get_invalid_test_value('post_add_new_subshape_portion', 'path', request.path, 'str')
        self.initialize('post_add_new_subshape_portion', 'path', request.path)
        ok = False
        try:
            self.api.post_add_new_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_portion', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_portion', 'path')

    def test_post_add_new_subshape_portion_invalid_dto(self):
        """Test case for post_add_new_subshape_portion with invalid dto
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        request.dto = self.get_invalid_test_value('post_add_new_subshape_portion', 'dto', request.dto, 'Portion')
        self.initialize('post_add_new_subshape_portion', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_new_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_portion', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_portion', 'dto')

    def test_post_add_new_subshape_portion_invalid_password(self):
        """Test case for post_add_new_subshape_portion with invalid password
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        request.password = self.get_invalid_test_value('post_add_new_subshape_portion', 'password', request.password, 'str')
        self.initialize('post_add_new_subshape_portion', 'password', request.password)
        ok = False
        try:
            self.api.post_add_new_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_portion', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_portion', 'password')

    def test_post_add_new_subshape_portion_invalid_folder(self):
        """Test case for post_add_new_subshape_portion with invalid folder
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        request.folder = self.get_invalid_test_value('post_add_new_subshape_portion', 'folder', request.folder, 'str')
        self.initialize('post_add_new_subshape_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_new_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_portion', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_portion', 'folder')

    def test_post_add_new_subshape_portion_invalid_storage(self):
        """Test case for post_add_new_subshape_portion with invalid storage
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        request.storage = self.get_invalid_test_value('post_add_new_subshape_portion', 'storage', request.storage, 'str')
        self.initialize('post_add_new_subshape_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_new_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_portion', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_portion', 'storage')

    def test_post_add_new_subshape_portion_invalid_position(self):
        """Test case for post_add_new_subshape_portion with invalid position
        """
        request = self.__prepare_post_add_new_subshape_portion_request()
        request.position = self.get_invalid_test_value('post_add_new_subshape_portion', 'position', request.position, 'int')
        self.initialize('post_add_new_subshape_portion', 'position', request.position)
        ok = False
        try:
            self.api.post_add_new_subshape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_new_subshape_portion', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_new_subshape_portion', 'position')

    def __prepare_post_add_new_subshape_portion_request(self):
        name = self.get_test_value('post_add_new_subshape_portion', 'name', 'str')
        slide_index = self.get_test_value('post_add_new_subshape_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('post_add_new_subshape_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('post_add_new_subshape_portion', 'paragraph_index', 'int')
        path = self.get_test_value('post_add_new_subshape_portion', 'path', 'str')
        dto = self.get_test_value('post_add_new_subshape_portion', 'dto', 'Portion')
        password = self.get_test_value('post_add_new_subshape_portion', 'password', 'str')
        folder = self.get_test_value('post_add_new_subshape_portion', 'folder', 'str')
        storage = self.get_test_value('post_add_new_subshape_portion', 'storage', 'str')
        position = self.get_test_value('post_add_new_subshape_portion', 'position', 'int')
        return asposeslidescloud.models.requests.slides_api_requests.PostAddNewSubshapePortionRequest(name, slide_index, shape_index, paragraph_index, path, dto, password, folder, storage, position)

    def test_post_add_notes_slide(self):
        """Test case for post_add_notes_slide
        """
        request = self.__prepare_post_add_notes_slide_request()
        self.initialize('post_add_notes_slide', None, None)
        response = self.api.post_add_notes_slide(request)
        self.assertIsNotNone(response)

    def test_post_add_notes_slide_invalid_name(self):
        """Test case for post_add_notes_slide with invalid name
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.name = self.get_invalid_test_value('post_add_notes_slide', 'name', request.name, 'str')
        self.initialize('post_add_notes_slide', 'name', request.name)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'name')

    def test_post_add_notes_slide_invalid_slide_index(self):
        """Test case for post_add_notes_slide with invalid slide_index
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.slide_index = self.get_invalid_test_value('post_add_notes_slide', 'slide_index', request.slide_index, 'int')
        self.initialize('post_add_notes_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'slide_index')

    def test_post_add_notes_slide_invalid_dto(self):
        """Test case for post_add_notes_slide with invalid dto
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.dto = self.get_invalid_test_value('post_add_notes_slide', 'dto', request.dto, 'NotesSlide')
        self.initialize('post_add_notes_slide', 'dto', request.dto)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'dto')

    def test_post_add_notes_slide_invalid_password(self):
        """Test case for post_add_notes_slide with invalid password
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.password = self.get_invalid_test_value('post_add_notes_slide', 'password', request.password, 'str')
        self.initialize('post_add_notes_slide', 'password', request.password)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'password')

    def test_post_add_notes_slide_invalid_folder(self):
        """Test case for post_add_notes_slide with invalid folder
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.folder = self.get_invalid_test_value('post_add_notes_slide', 'folder', request.folder, 'str')
        self.initialize('post_add_notes_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'folder')

    def test_post_add_notes_slide_invalid_storage(self):
        """Test case for post_add_notes_slide with invalid storage
        """
        request = self.__prepare_post_add_notes_slide_request()
        request.storage = self.get_invalid_test_value('post_add_notes_slide', 'storage', request.storage, 'str')
        self.initialize('post_add_notes_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.post_add_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_add_notes_slide', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_add_notes_slide', 'storage')

    def __prepare_post_add_notes_slide_request(self):
        name = self.get_test_value('post_add_notes_slide', 'name', 'str')
        slide_index = self.get_test_value('post_add_notes_slide', 'slide_index', 'int')
        dto = self.get_test_value('post_add_notes_slide', 'dto', 'NotesSlide')
        password = self.get_test_value('post_add_notes_slide', 'password', 'str')
        folder = self.get_test_value('post_add_notes_slide', 'folder', 'str')
        storage = self.get_test_value('post_add_notes_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostAddNotesSlideRequest(name, slide_index, dto, password, folder, storage)

    def test_post_copy_layout_slide_from_source_presentation(self):
        """Test case for post_copy_layout_slide_from_source_presentation
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        self.initialize('post_copy_layout_slide_from_source_presentation', None, None)
        response = self.api.post_copy_layout_slide_from_source_presentation(request)
        self.assertIsNotNone(response)

    def test_post_copy_layout_slide_from_source_presentation_invalid_name(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid name
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.name = self.get_invalid_test_value('post_copy_layout_slide_from_source_presentation', 'name', request.name, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'name', request.name)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'name')

    def test_post_copy_layout_slide_from_source_presentation_invalid_clone_from(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid clone_from
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.clone_from = self.get_invalid_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from', request.clone_from, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'clone_from', request.clone_from)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'clone_from', request.clone_from)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'clone_from')

    def test_post_copy_layout_slide_from_source_presentation_invalid_clone_from_position(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid clone_from_position
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.clone_from_position = self.get_invalid_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from_position', request.clone_from_position, 'int')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'clone_from_position', request.clone_from_position)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'clone_from_position', request.clone_from_position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'clone_from_position')

    def test_post_copy_layout_slide_from_source_presentation_invalid_clone_from_password(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid clone_from_password
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.clone_from_password = self.get_invalid_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from_password', request.clone_from_password, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'clone_from_password', request.clone_from_password)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'clone_from_password', request.clone_from_password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'clone_from_password')

    def test_post_copy_layout_slide_from_source_presentation_invalid_clone_from_storage(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid clone_from_storage
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.clone_from_storage = self.get_invalid_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from_storage', request.clone_from_storage, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'clone_from_storage', request.clone_from_storage)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'clone_from_storage', request.clone_from_storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'clone_from_storage')

    def test_post_copy_layout_slide_from_source_presentation_invalid_password(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid password
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.password = self.get_invalid_test_value('post_copy_layout_slide_from_source_presentation', 'password', request.password, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'password', request.password)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'password')

    def test_post_copy_layout_slide_from_source_presentation_invalid_folder(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid folder
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.folder = self.get_invalid_test_value('post_copy_layout_slide_from_source_presentation', 'folder', request.folder, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'folder', request.folder)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'folder')

    def test_post_copy_layout_slide_from_source_presentation_invalid_storage(self):
        """Test case for post_copy_layout_slide_from_source_presentation with invalid storage
        """
        request = self.__prepare_post_copy_layout_slide_from_source_presentation_request()
        request.storage = self.get_invalid_test_value('post_copy_layout_slide_from_source_presentation', 'storage', request.storage, 'str')
        self.initialize('post_copy_layout_slide_from_source_presentation', 'storage', request.storage)
        ok = False
        try:
            self.api.post_copy_layout_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_layout_slide_from_source_presentation', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_layout_slide_from_source_presentation', 'storage')

    def __prepare_post_copy_layout_slide_from_source_presentation_request(self):
        name = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'name', 'str')
        clone_from = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from', 'str')
        clone_from_position = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from_position', 'int')
        clone_from_password = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from_password', 'str')
        clone_from_storage = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'clone_from_storage', 'str')
        password = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'password', 'str')
        folder = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'folder', 'str')
        storage = self.get_test_value('post_copy_layout_slide_from_source_presentation', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostCopyLayoutSlideFromSourcePresentationRequest(name, clone_from, clone_from_position, clone_from_password, clone_from_storage, password, folder, storage)

    def test_post_copy_master_slide_from_source_presentation(self):
        """Test case for post_copy_master_slide_from_source_presentation
        """
        request = self.__prepare_post_copy_master_slide_from_source_presentation_request()
        self.initialize('post_copy_master_slide_from_source_presentation', None, None)
        response = self.api.post_copy_master_slide_from_source_presentation(request)
        self.assertIsNotNone(response)

    def test_post_copy_master_slide_from_source_presentation_invalid_name(self):
        """Test case for post_copy_master_slide_from_source_presentation with invalid name
        """
        request = self.__prepare_post_copy_master_slide_from_source_presentation_request()
        request.name = self.get_invalid_test_value('post_copy_master_slide_from_source_presentation', 'name', request.name, 'str')
        self.initialize('post_copy_master_slide_from_source_presentation', 'name', request.name)
        ok = False
        try:
            self.api.post_copy_master_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_master_slide_from_source_presentation', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_master_slide_from_source_presentation', 'name')

    def test_post_copy_master_slide_from_source_presentation_invalid_clone_from(self):
        """Test case for post_copy_master_slide_from_source_presentation with invalid clone_from
        """
        request = self.__prepare_post_copy_master_slide_from_source_presentation_request()
        request.clone_from = self.get_invalid_test_value('post_copy_master_slide_from_source_presentation', 'clone_from', request.clone_from, 'str')
        self.initialize('post_copy_master_slide_from_source_presentation', 'clone_from', request.clone_from)
        ok = False
        try:
            self.api.post_copy_master_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_master_slide_from_source_presentation', 'clone_from', request.clone_from)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_master_slide_from_source_presentation', 'clone_from')

    def test_post_copy_master_slide_from_source_presentation_invalid_clone_from_position(self):
        """Test case for post_copy_master_slide_from_source_presentation with invalid clone_from_position
        """
        request = self.__prepare_post_copy_master_slide_from_source_presentation_request()
        request.clone_from_position = self.get_invalid_test_value('post_copy_master_slide_from_source_presentation', 'clone_from_position', request.clone_from_position, 'int')
        self.initialize('post_copy_master_slide_from_source_presentation', 'clone_from_position', request.clone_from_position)
        ok = False
        try:
            self.api.post_copy_master_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_master_slide_from_source_presentation', 'clone_from_position', request.clone_from_position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_master_slide_from_source_presentation', 'clone_from_position')

    def test_post_copy_master_slide_from_source_presentation_invalid_clone_from_password(self):
        """Test case for post_copy_master_slide_from_source_presentation with invalid clone_from_password
        """
        request = self.__prepare_post_copy_master_slide_from_source_presentation_request()
        request.clone_from_password = self.get_invalid_test_value('post_copy_master_slide_from_source_presentation', 'clone_from_password', request.clone_from_password, 'str')
        self.initialize('post_copy_master_slide_from_source_presentation', 'clone_from_password', request.clone_from_password)
        ok = False
        try:
            self.api.post_copy_master_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_master_slide_from_source_presentation', 'clone_from_password', request.clone_from_password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_master_slide_from_source_presentation', 'clone_from_password')

    def test_post_copy_master_slide_from_source_presentation_invalid_clone_from_storage(self):
        """Test case for post_copy_master_slide_from_source_presentation with invalid clone_from_storage
        """
        request = self.__prepare_post_copy_master_slide_from_source_presentation_request()
        request.clone_from_storage = self.get_invalid_test_value('post_copy_master_slide_from_source_presentation', 'clone_from_storage', request.clone_from_storage, 'str')
        self.initialize('post_copy_master_slide_from_source_presentation', 'clone_from_storage', request.clone_from_storage)
        ok = False
        try:
            self.api.post_copy_master_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_master_slide_from_source_presentation', 'clone_from_storage', request.clone_from_storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_master_slide_from_source_presentation', 'clone_from_storage')

    def test_post_copy_master_slide_from_source_presentation_invalid_apply_to_all(self):
        """Test case for post_copy_master_slide_from_source_presentation with invalid apply_to_all
        """
        request = self.__prepare_post_copy_master_slide_from_source_presentation_request()
        request.apply_to_all = self.get_invalid_test_value('post_copy_master_slide_from_source_presentation', 'apply_to_all', request.apply_to_all, 'bool')
        self.initialize('post_copy_master_slide_from_source_presentation', 'apply_to_all', request.apply_to_all)
        ok = False
        try:
            self.api.post_copy_master_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_master_slide_from_source_presentation', 'apply_to_all', request.apply_to_all)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_master_slide_from_source_presentation', 'apply_to_all')

    def test_post_copy_master_slide_from_source_presentation_invalid_password(self):
        """Test case for post_copy_master_slide_from_source_presentation with invalid password
        """
        request = self.__prepare_post_copy_master_slide_from_source_presentation_request()
        request.password = self.get_invalid_test_value('post_copy_master_slide_from_source_presentation', 'password', request.password, 'str')
        self.initialize('post_copy_master_slide_from_source_presentation', 'password', request.password)
        ok = False
        try:
            self.api.post_copy_master_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_master_slide_from_source_presentation', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_master_slide_from_source_presentation', 'password')

    def test_post_copy_master_slide_from_source_presentation_invalid_folder(self):
        """Test case for post_copy_master_slide_from_source_presentation with invalid folder
        """
        request = self.__prepare_post_copy_master_slide_from_source_presentation_request()
        request.folder = self.get_invalid_test_value('post_copy_master_slide_from_source_presentation', 'folder', request.folder, 'str')
        self.initialize('post_copy_master_slide_from_source_presentation', 'folder', request.folder)
        ok = False
        try:
            self.api.post_copy_master_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_master_slide_from_source_presentation', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_master_slide_from_source_presentation', 'folder')

    def test_post_copy_master_slide_from_source_presentation_invalid_storage(self):
        """Test case for post_copy_master_slide_from_source_presentation with invalid storage
        """
        request = self.__prepare_post_copy_master_slide_from_source_presentation_request()
        request.storage = self.get_invalid_test_value('post_copy_master_slide_from_source_presentation', 'storage', request.storage, 'str')
        self.initialize('post_copy_master_slide_from_source_presentation', 'storage', request.storage)
        ok = False
        try:
            self.api.post_copy_master_slide_from_source_presentation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_copy_master_slide_from_source_presentation', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_copy_master_slide_from_source_presentation', 'storage')

    def __prepare_post_copy_master_slide_from_source_presentation_request(self):
        name = self.get_test_value('post_copy_master_slide_from_source_presentation', 'name', 'str')
        clone_from = self.get_test_value('post_copy_master_slide_from_source_presentation', 'clone_from', 'str')
        clone_from_position = self.get_test_value('post_copy_master_slide_from_source_presentation', 'clone_from_position', 'int')
        clone_from_password = self.get_test_value('post_copy_master_slide_from_source_presentation', 'clone_from_password', 'str')
        clone_from_storage = self.get_test_value('post_copy_master_slide_from_source_presentation', 'clone_from_storage', 'str')
        apply_to_all = self.get_test_value('post_copy_master_slide_from_source_presentation', 'apply_to_all', 'bool')
        password = self.get_test_value('post_copy_master_slide_from_source_presentation', 'password', 'str')
        folder = self.get_test_value('post_copy_master_slide_from_source_presentation', 'folder', 'str')
        storage = self.get_test_value('post_copy_master_slide_from_source_presentation', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostCopyMasterSlideFromSourcePresentationRequest(name, clone_from, clone_from_position, clone_from_password, clone_from_storage, apply_to_all, password, folder, storage)

    def test_post_get_notes_slide(self):
        """Test case for post_get_notes_slide
        """
        request = self.__prepare_post_get_notes_slide_request()
        self.initialize('post_get_notes_slide', None, None)
        response = self.api.post_get_notes_slide(request)
        self.assertIsNotNone(response)

    def test_post_get_notes_slide_invalid_slide_index(self):
        """Test case for post_get_notes_slide with invalid slide_index
        """
        request = self.__prepare_post_get_notes_slide_request()
        request.slide_index = self.get_invalid_test_value('post_get_notes_slide', 'slide_index', request.slide_index, 'int')
        self.initialize('post_get_notes_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide', 'slide_index')

    def test_post_get_notes_slide_invalid_document(self):
        """Test case for post_get_notes_slide with invalid document
        """
        request = self.__prepare_post_get_notes_slide_request()
        request.document = self.get_invalid_test_value('post_get_notes_slide', 'document', request.document, 'file')
        self.initialize('post_get_notes_slide', 'document', request.document)
        ok = False
        try:
            self.api.post_get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide', 'document', request.document)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide', 'document')

    def test_post_get_notes_slide_invalid_password(self):
        """Test case for post_get_notes_slide with invalid password
        """
        request = self.__prepare_post_get_notes_slide_request()
        request.password = self.get_invalid_test_value('post_get_notes_slide', 'password', request.password, 'str')
        self.initialize('post_get_notes_slide', 'password', request.password)
        ok = False
        try:
            self.api.post_get_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide', 'password')

    def __prepare_post_get_notes_slide_request(self):
        slide_index = self.get_test_value('post_get_notes_slide', 'slide_index', 'int')
        document = self.get_test_value('post_get_notes_slide', 'document', 'file')
        password = self.get_test_value('post_get_notes_slide', 'password', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostGetNotesSlideRequest(slide_index, document, password)

    def test_post_get_notes_slide_exists(self):
        """Test case for post_get_notes_slide_exists
        """
        request = self.__prepare_post_get_notes_slide_exists_request()
        self.initialize('post_get_notes_slide_exists', None, None)
        response = self.api.post_get_notes_slide_exists(request)
        self.assertIsNotNone(response)

    def test_post_get_notes_slide_exists_invalid_slide_index(self):
        """Test case for post_get_notes_slide_exists with invalid slide_index
        """
        request = self.__prepare_post_get_notes_slide_exists_request()
        request.slide_index = self.get_invalid_test_value('post_get_notes_slide_exists', 'slide_index', request.slide_index, 'int')
        self.initialize('post_get_notes_slide_exists', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_get_notes_slide_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide_exists', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide_exists', 'slide_index')

    def test_post_get_notes_slide_exists_invalid_document(self):
        """Test case for post_get_notes_slide_exists with invalid document
        """
        request = self.__prepare_post_get_notes_slide_exists_request()
        request.document = self.get_invalid_test_value('post_get_notes_slide_exists', 'document', request.document, 'file')
        self.initialize('post_get_notes_slide_exists', 'document', request.document)
        ok = False
        try:
            self.api.post_get_notes_slide_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide_exists', 'document', request.document)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide_exists', 'document')

    def test_post_get_notes_slide_exists_invalid_password(self):
        """Test case for post_get_notes_slide_exists with invalid password
        """
        request = self.__prepare_post_get_notes_slide_exists_request()
        request.password = self.get_invalid_test_value('post_get_notes_slide_exists', 'password', request.password, 'str')
        self.initialize('post_get_notes_slide_exists', 'password', request.password)
        ok = False
        try:
            self.api.post_get_notes_slide_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide_exists', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide_exists', 'password')

    def __prepare_post_get_notes_slide_exists_request(self):
        slide_index = self.get_test_value('post_get_notes_slide_exists', 'slide_index', 'int')
        document = self.get_test_value('post_get_notes_slide_exists', 'document', 'file')
        password = self.get_test_value('post_get_notes_slide_exists', 'password', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostGetNotesSlideExistsRequest(slide_index, document, password)

    def test_post_get_notes_slide_with_format(self):
        """Test case for post_get_notes_slide_with_format
        """
        request = self.__prepare_post_get_notes_slide_with_format_request()
        self.initialize('post_get_notes_slide_with_format', None, None)
        response = self.api.post_get_notes_slide_with_format(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_post_get_notes_slide_with_format_invalid_slide_index(self):
        """Test case for post_get_notes_slide_with_format with invalid slide_index
        """
        request = self.__prepare_post_get_notes_slide_with_format_request()
        request.slide_index = self.get_invalid_test_value('post_get_notes_slide_with_format', 'slide_index', request.slide_index, 'int')
        self.initialize('post_get_notes_slide_with_format', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide_with_format', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide_with_format', 'slide_index')

    def test_post_get_notes_slide_with_format_invalid_format(self):
        """Test case for post_get_notes_slide_with_format with invalid format
        """
        request = self.__prepare_post_get_notes_slide_with_format_request()
        request.format = self.get_invalid_test_value('post_get_notes_slide_with_format', 'format', request.format, 'str')
        self.initialize('post_get_notes_slide_with_format', 'format', request.format)
        ok = False
        try:
            self.api.post_get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide_with_format', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide_with_format', 'format')

    def test_post_get_notes_slide_with_format_invalid_document(self):
        """Test case for post_get_notes_slide_with_format with invalid document
        """
        request = self.__prepare_post_get_notes_slide_with_format_request()
        request.document = self.get_invalid_test_value('post_get_notes_slide_with_format', 'document', request.document, 'file')
        self.initialize('post_get_notes_slide_with_format', 'document', request.document)
        ok = False
        try:
            self.api.post_get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide_with_format', 'document', request.document)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide_with_format', 'document')

    def test_post_get_notes_slide_with_format_invalid_width(self):
        """Test case for post_get_notes_slide_with_format with invalid width
        """
        request = self.__prepare_post_get_notes_slide_with_format_request()
        request.width = self.get_invalid_test_value('post_get_notes_slide_with_format', 'width', request.width, 'int')
        self.initialize('post_get_notes_slide_with_format', 'width', request.width)
        ok = False
        try:
            self.api.post_get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide_with_format', 'width', request.width)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide_with_format', 'width')

    def test_post_get_notes_slide_with_format_invalid_height(self):
        """Test case for post_get_notes_slide_with_format with invalid height
        """
        request = self.__prepare_post_get_notes_slide_with_format_request()
        request.height = self.get_invalid_test_value('post_get_notes_slide_with_format', 'height', request.height, 'int')
        self.initialize('post_get_notes_slide_with_format', 'height', request.height)
        ok = False
        try:
            self.api.post_get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide_with_format', 'height', request.height)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide_with_format', 'height')

    def test_post_get_notes_slide_with_format_invalid_password(self):
        """Test case for post_get_notes_slide_with_format with invalid password
        """
        request = self.__prepare_post_get_notes_slide_with_format_request()
        request.password = self.get_invalid_test_value('post_get_notes_slide_with_format', 'password', request.password, 'str')
        self.initialize('post_get_notes_slide_with_format', 'password', request.password)
        ok = False
        try:
            self.api.post_get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide_with_format', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide_with_format', 'password')

    def test_post_get_notes_slide_with_format_invalid_fonts_folder(self):
        """Test case for post_get_notes_slide_with_format with invalid fonts_folder
        """
        request = self.__prepare_post_get_notes_slide_with_format_request()
        request.fonts_folder = self.get_invalid_test_value('post_get_notes_slide_with_format', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_get_notes_slide_with_format', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_get_notes_slide_with_format(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_get_notes_slide_with_format', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_get_notes_slide_with_format', 'fonts_folder')

    def __prepare_post_get_notes_slide_with_format_request(self):
        slide_index = self.get_test_value('post_get_notes_slide_with_format', 'slide_index', 'int')
        format = self.get_test_value('post_get_notes_slide_with_format', 'format', 'str')
        document = self.get_test_value('post_get_notes_slide_with_format', 'document', 'file')
        width = self.get_test_value('post_get_notes_slide_with_format', 'width', 'int')
        height = self.get_test_value('post_get_notes_slide_with_format', 'height', 'int')
        password = self.get_test_value('post_get_notes_slide_with_format', 'password', 'str')
        fonts_folder = self.get_test_value('post_get_notes_slide_with_format', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostGetNotesSlideWithFormatRequest(slide_index, format, document, width, height, password, fonts_folder)

    def test_post_notes_slide_add_new_paragraph(self):
        """Test case for post_notes_slide_add_new_paragraph
        """
        request = self.__prepare_post_notes_slide_add_new_paragraph_request()
        self.initialize('post_notes_slide_add_new_paragraph', None, None)
        response = self.api.post_notes_slide_add_new_paragraph(request)
        self.assertIsNotNone(response)

    def test_post_notes_slide_add_new_paragraph_invalid_name(self):
        """Test case for post_notes_slide_add_new_paragraph with invalid name
        """
        request = self.__prepare_post_notes_slide_add_new_paragraph_request()
        request.name = self.get_invalid_test_value('post_notes_slide_add_new_paragraph', 'name', request.name, 'str')
        self.initialize('post_notes_slide_add_new_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.post_notes_slide_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_paragraph', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_paragraph', 'name')

    def test_post_notes_slide_add_new_paragraph_invalid_slide_index(self):
        """Test case for post_notes_slide_add_new_paragraph with invalid slide_index
        """
        request = self.__prepare_post_notes_slide_add_new_paragraph_request()
        request.slide_index = self.get_invalid_test_value('post_notes_slide_add_new_paragraph', 'slide_index', request.slide_index, 'int')
        self.initialize('post_notes_slide_add_new_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_notes_slide_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_paragraph', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_paragraph', 'slide_index')

    def test_post_notes_slide_add_new_paragraph_invalid_shape_index(self):
        """Test case for post_notes_slide_add_new_paragraph with invalid shape_index
        """
        request = self.__prepare_post_notes_slide_add_new_paragraph_request()
        request.shape_index = self.get_invalid_test_value('post_notes_slide_add_new_paragraph', 'shape_index', request.shape_index, 'int')
        self.initialize('post_notes_slide_add_new_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_notes_slide_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_paragraph', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_paragraph', 'shape_index')

    def test_post_notes_slide_add_new_paragraph_invalid_dto(self):
        """Test case for post_notes_slide_add_new_paragraph with invalid dto
        """
        request = self.__prepare_post_notes_slide_add_new_paragraph_request()
        request.dto = self.get_invalid_test_value('post_notes_slide_add_new_paragraph', 'dto', request.dto, 'Paragraph')
        self.initialize('post_notes_slide_add_new_paragraph', 'dto', request.dto)
        ok = False
        try:
            self.api.post_notes_slide_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_paragraph', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_paragraph', 'dto')

    def test_post_notes_slide_add_new_paragraph_invalid_password(self):
        """Test case for post_notes_slide_add_new_paragraph with invalid password
        """
        request = self.__prepare_post_notes_slide_add_new_paragraph_request()
        request.password = self.get_invalid_test_value('post_notes_slide_add_new_paragraph', 'password', request.password, 'str')
        self.initialize('post_notes_slide_add_new_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.post_notes_slide_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_paragraph', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_paragraph', 'password')

    def test_post_notes_slide_add_new_paragraph_invalid_folder(self):
        """Test case for post_notes_slide_add_new_paragraph with invalid folder
        """
        request = self.__prepare_post_notes_slide_add_new_paragraph_request()
        request.folder = self.get_invalid_test_value('post_notes_slide_add_new_paragraph', 'folder', request.folder, 'str')
        self.initialize('post_notes_slide_add_new_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.post_notes_slide_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_paragraph', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_paragraph', 'folder')

    def test_post_notes_slide_add_new_paragraph_invalid_storage(self):
        """Test case for post_notes_slide_add_new_paragraph with invalid storage
        """
        request = self.__prepare_post_notes_slide_add_new_paragraph_request()
        request.storage = self.get_invalid_test_value('post_notes_slide_add_new_paragraph', 'storage', request.storage, 'str')
        self.initialize('post_notes_slide_add_new_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.post_notes_slide_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_paragraph', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_paragraph', 'storage')

    def test_post_notes_slide_add_new_paragraph_invalid_position(self):
        """Test case for post_notes_slide_add_new_paragraph with invalid position
        """
        request = self.__prepare_post_notes_slide_add_new_paragraph_request()
        request.position = self.get_invalid_test_value('post_notes_slide_add_new_paragraph', 'position', request.position, 'int')
        self.initialize('post_notes_slide_add_new_paragraph', 'position', request.position)
        ok = False
        try:
            self.api.post_notes_slide_add_new_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_paragraph', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_paragraph', 'position')

    def __prepare_post_notes_slide_add_new_paragraph_request(self):
        name = self.get_test_value('post_notes_slide_add_new_paragraph', 'name', 'str')
        slide_index = self.get_test_value('post_notes_slide_add_new_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('post_notes_slide_add_new_paragraph', 'shape_index', 'int')
        dto = self.get_test_value('post_notes_slide_add_new_paragraph', 'dto', 'Paragraph')
        password = self.get_test_value('post_notes_slide_add_new_paragraph', 'password', 'str')
        folder = self.get_test_value('post_notes_slide_add_new_paragraph', 'folder', 'str')
        storage = self.get_test_value('post_notes_slide_add_new_paragraph', 'storage', 'str')
        position = self.get_test_value('post_notes_slide_add_new_paragraph', 'position', 'int')
        return asposeslidescloud.models.requests.slides_api_requests.PostNotesSlideAddNewParagraphRequest(name, slide_index, shape_index, dto, password, folder, storage, position)

    def test_post_notes_slide_add_new_portion(self):
        """Test case for post_notes_slide_add_new_portion
        """
        request = self.__prepare_post_notes_slide_add_new_portion_request()
        self.initialize('post_notes_slide_add_new_portion', None, None)
        response = self.api.post_notes_slide_add_new_portion(request)
        self.assertIsNotNone(response)

    def test_post_notes_slide_add_new_portion_invalid_name(self):
        """Test case for post_notes_slide_add_new_portion with invalid name
        """
        request = self.__prepare_post_notes_slide_add_new_portion_request()
        request.name = self.get_invalid_test_value('post_notes_slide_add_new_portion', 'name', request.name, 'str')
        self.initialize('post_notes_slide_add_new_portion', 'name', request.name)
        ok = False
        try:
            self.api.post_notes_slide_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_portion', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_portion', 'name')

    def test_post_notes_slide_add_new_portion_invalid_slide_index(self):
        """Test case for post_notes_slide_add_new_portion with invalid slide_index
        """
        request = self.__prepare_post_notes_slide_add_new_portion_request()
        request.slide_index = self.get_invalid_test_value('post_notes_slide_add_new_portion', 'slide_index', request.slide_index, 'int')
        self.initialize('post_notes_slide_add_new_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_notes_slide_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_portion', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_portion', 'slide_index')

    def test_post_notes_slide_add_new_portion_invalid_shape_index(self):
        """Test case for post_notes_slide_add_new_portion with invalid shape_index
        """
        request = self.__prepare_post_notes_slide_add_new_portion_request()
        request.shape_index = self.get_invalid_test_value('post_notes_slide_add_new_portion', 'shape_index', request.shape_index, 'int')
        self.initialize('post_notes_slide_add_new_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_notes_slide_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_portion', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_portion', 'shape_index')

    def test_post_notes_slide_add_new_portion_invalid_paragraph_index(self):
        """Test case for post_notes_slide_add_new_portion with invalid paragraph_index
        """
        request = self.__prepare_post_notes_slide_add_new_portion_request()
        request.paragraph_index = self.get_invalid_test_value('post_notes_slide_add_new_portion', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('post_notes_slide_add_new_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.post_notes_slide_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_portion', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_portion', 'paragraph_index')

    def test_post_notes_slide_add_new_portion_invalid_dto(self):
        """Test case for post_notes_slide_add_new_portion with invalid dto
        """
        request = self.__prepare_post_notes_slide_add_new_portion_request()
        request.dto = self.get_invalid_test_value('post_notes_slide_add_new_portion', 'dto', request.dto, 'Portion')
        self.initialize('post_notes_slide_add_new_portion', 'dto', request.dto)
        ok = False
        try:
            self.api.post_notes_slide_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_portion', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_portion', 'dto')

    def test_post_notes_slide_add_new_portion_invalid_password(self):
        """Test case for post_notes_slide_add_new_portion with invalid password
        """
        request = self.__prepare_post_notes_slide_add_new_portion_request()
        request.password = self.get_invalid_test_value('post_notes_slide_add_new_portion', 'password', request.password, 'str')
        self.initialize('post_notes_slide_add_new_portion', 'password', request.password)
        ok = False
        try:
            self.api.post_notes_slide_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_portion', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_portion', 'password')

    def test_post_notes_slide_add_new_portion_invalid_folder(self):
        """Test case for post_notes_slide_add_new_portion with invalid folder
        """
        request = self.__prepare_post_notes_slide_add_new_portion_request()
        request.folder = self.get_invalid_test_value('post_notes_slide_add_new_portion', 'folder', request.folder, 'str')
        self.initialize('post_notes_slide_add_new_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.post_notes_slide_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_portion', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_portion', 'folder')

    def test_post_notes_slide_add_new_portion_invalid_storage(self):
        """Test case for post_notes_slide_add_new_portion with invalid storage
        """
        request = self.__prepare_post_notes_slide_add_new_portion_request()
        request.storage = self.get_invalid_test_value('post_notes_slide_add_new_portion', 'storage', request.storage, 'str')
        self.initialize('post_notes_slide_add_new_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.post_notes_slide_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_portion', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_portion', 'storage')

    def test_post_notes_slide_add_new_portion_invalid_position(self):
        """Test case for post_notes_slide_add_new_portion with invalid position
        """
        request = self.__prepare_post_notes_slide_add_new_portion_request()
        request.position = self.get_invalid_test_value('post_notes_slide_add_new_portion', 'position', request.position, 'int')
        self.initialize('post_notes_slide_add_new_portion', 'position', request.position)
        ok = False
        try:
            self.api.post_notes_slide_add_new_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_portion', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_portion', 'position')

    def __prepare_post_notes_slide_add_new_portion_request(self):
        name = self.get_test_value('post_notes_slide_add_new_portion', 'name', 'str')
        slide_index = self.get_test_value('post_notes_slide_add_new_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('post_notes_slide_add_new_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('post_notes_slide_add_new_portion', 'paragraph_index', 'int')
        dto = self.get_test_value('post_notes_slide_add_new_portion', 'dto', 'Portion')
        password = self.get_test_value('post_notes_slide_add_new_portion', 'password', 'str')
        folder = self.get_test_value('post_notes_slide_add_new_portion', 'folder', 'str')
        storage = self.get_test_value('post_notes_slide_add_new_portion', 'storage', 'str')
        position = self.get_test_value('post_notes_slide_add_new_portion', 'position', 'int')
        return asposeslidescloud.models.requests.slides_api_requests.PostNotesSlideAddNewPortionRequest(name, slide_index, shape_index, paragraph_index, dto, password, folder, storage, position)

    def test_post_notes_slide_add_new_shape(self):
        """Test case for post_notes_slide_add_new_shape
        """
        request = self.__prepare_post_notes_slide_add_new_shape_request()
        self.initialize('post_notes_slide_add_new_shape', None, None)
        response = self.api.post_notes_slide_add_new_shape(request)
        self.assertIsNotNone(response)

    def test_post_notes_slide_add_new_shape_invalid_name(self):
        """Test case for post_notes_slide_add_new_shape with invalid name
        """
        request = self.__prepare_post_notes_slide_add_new_shape_request()
        request.name = self.get_invalid_test_value('post_notes_slide_add_new_shape', 'name', request.name, 'str')
        self.initialize('post_notes_slide_add_new_shape', 'name', request.name)
        ok = False
        try:
            self.api.post_notes_slide_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_shape', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_shape', 'name')

    def test_post_notes_slide_add_new_shape_invalid_slide_index(self):
        """Test case for post_notes_slide_add_new_shape with invalid slide_index
        """
        request = self.__prepare_post_notes_slide_add_new_shape_request()
        request.slide_index = self.get_invalid_test_value('post_notes_slide_add_new_shape', 'slide_index', request.slide_index, 'int')
        self.initialize('post_notes_slide_add_new_shape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_notes_slide_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_shape', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_shape', 'slide_index')

    def test_post_notes_slide_add_new_shape_invalid_dto(self):
        """Test case for post_notes_slide_add_new_shape with invalid dto
        """
        request = self.__prepare_post_notes_slide_add_new_shape_request()
        request.dto = self.get_invalid_test_value('post_notes_slide_add_new_shape', 'dto', request.dto, 'ShapeBase')
        self.initialize('post_notes_slide_add_new_shape', 'dto', request.dto)
        ok = False
        try:
            self.api.post_notes_slide_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_shape', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_shape', 'dto')

    def test_post_notes_slide_add_new_shape_invalid_password(self):
        """Test case for post_notes_slide_add_new_shape with invalid password
        """
        request = self.__prepare_post_notes_slide_add_new_shape_request()
        request.password = self.get_invalid_test_value('post_notes_slide_add_new_shape', 'password', request.password, 'str')
        self.initialize('post_notes_slide_add_new_shape', 'password', request.password)
        ok = False
        try:
            self.api.post_notes_slide_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_shape', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_shape', 'password')

    def test_post_notes_slide_add_new_shape_invalid_folder(self):
        """Test case for post_notes_slide_add_new_shape with invalid folder
        """
        request = self.__prepare_post_notes_slide_add_new_shape_request()
        request.folder = self.get_invalid_test_value('post_notes_slide_add_new_shape', 'folder', request.folder, 'str')
        self.initialize('post_notes_slide_add_new_shape', 'folder', request.folder)
        ok = False
        try:
            self.api.post_notes_slide_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_shape', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_shape', 'folder')

    def test_post_notes_slide_add_new_shape_invalid_storage(self):
        """Test case for post_notes_slide_add_new_shape with invalid storage
        """
        request = self.__prepare_post_notes_slide_add_new_shape_request()
        request.storage = self.get_invalid_test_value('post_notes_slide_add_new_shape', 'storage', request.storage, 'str')
        self.initialize('post_notes_slide_add_new_shape', 'storage', request.storage)
        ok = False
        try:
            self.api.post_notes_slide_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_shape', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_shape', 'storage')

    def test_post_notes_slide_add_new_shape_invalid_shape_to_clone(self):
        """Test case for post_notes_slide_add_new_shape with invalid shape_to_clone
        """
        request = self.__prepare_post_notes_slide_add_new_shape_request()
        request.shape_to_clone = self.get_invalid_test_value('post_notes_slide_add_new_shape', 'shape_to_clone', request.shape_to_clone, 'int')
        self.initialize('post_notes_slide_add_new_shape', 'shape_to_clone', request.shape_to_clone)
        ok = False
        try:
            self.api.post_notes_slide_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_shape', 'shape_to_clone', request.shape_to_clone)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_shape', 'shape_to_clone')

    def test_post_notes_slide_add_new_shape_invalid_position(self):
        """Test case for post_notes_slide_add_new_shape with invalid position
        """
        request = self.__prepare_post_notes_slide_add_new_shape_request()
        request.position = self.get_invalid_test_value('post_notes_slide_add_new_shape', 'position', request.position, 'int')
        self.initialize('post_notes_slide_add_new_shape', 'position', request.position)
        ok = False
        try:
            self.api.post_notes_slide_add_new_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_add_new_shape', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_add_new_shape', 'position')

    def __prepare_post_notes_slide_add_new_shape_request(self):
        name = self.get_test_value('post_notes_slide_add_new_shape', 'name', 'str')
        slide_index = self.get_test_value('post_notes_slide_add_new_shape', 'slide_index', 'int')
        dto = self.get_test_value('post_notes_slide_add_new_shape', 'dto', 'ShapeBase')
        password = self.get_test_value('post_notes_slide_add_new_shape', 'password', 'str')
        folder = self.get_test_value('post_notes_slide_add_new_shape', 'folder', 'str')
        storage = self.get_test_value('post_notes_slide_add_new_shape', 'storage', 'str')
        shape_to_clone = self.get_test_value('post_notes_slide_add_new_shape', 'shape_to_clone', 'int')
        position = self.get_test_value('post_notes_slide_add_new_shape', 'position', 'int')
        return asposeslidescloud.models.requests.slides_api_requests.PostNotesSlideAddNewShapeRequest(name, slide_index, dto, password, folder, storage, shape_to_clone, position)

    def test_post_notes_slide_shape_save_as(self):
        """Test case for post_notes_slide_shape_save_as
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        self.initialize('post_notes_slide_shape_save_as', None, None)
        response = self.api.post_notes_slide_shape_save_as(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_post_notes_slide_shape_save_as_invalid_name(self):
        """Test case for post_notes_slide_shape_save_as with invalid name
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.name = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'name', request.name, 'str')
        self.initialize('post_notes_slide_shape_save_as', 'name', request.name)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'name')

    def test_post_notes_slide_shape_save_as_invalid_slide_index(self):
        """Test case for post_notes_slide_shape_save_as with invalid slide_index
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.slide_index = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'slide_index', request.slide_index, 'int')
        self.initialize('post_notes_slide_shape_save_as', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'slide_index')

    def test_post_notes_slide_shape_save_as_invalid_shape_index(self):
        """Test case for post_notes_slide_shape_save_as with invalid shape_index
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.shape_index = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'shape_index', request.shape_index, 'int')
        self.initialize('post_notes_slide_shape_save_as', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'shape_index')

    def test_post_notes_slide_shape_save_as_invalid_format(self):
        """Test case for post_notes_slide_shape_save_as with invalid format
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.format = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'format', request.format, 'str')
        self.initialize('post_notes_slide_shape_save_as', 'format', request.format)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'format')

    def test_post_notes_slide_shape_save_as_invalid_options(self):
        """Test case for post_notes_slide_shape_save_as with invalid options
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.options = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'options', request.options, 'IShapeExportOptions')
        self.initialize('post_notes_slide_shape_save_as', 'options', request.options)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'options')

    def test_post_notes_slide_shape_save_as_invalid_password(self):
        """Test case for post_notes_slide_shape_save_as with invalid password
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.password = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'password', request.password, 'str')
        self.initialize('post_notes_slide_shape_save_as', 'password', request.password)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'password')

    def test_post_notes_slide_shape_save_as_invalid_folder(self):
        """Test case for post_notes_slide_shape_save_as with invalid folder
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.folder = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'folder', request.folder, 'str')
        self.initialize('post_notes_slide_shape_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'folder')

    def test_post_notes_slide_shape_save_as_invalid_storage(self):
        """Test case for post_notes_slide_shape_save_as with invalid storage
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.storage = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'storage', request.storage, 'str')
        self.initialize('post_notes_slide_shape_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'storage')

    def test_post_notes_slide_shape_save_as_invalid_scale_x(self):
        """Test case for post_notes_slide_shape_save_as with invalid scale_x
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.scale_x = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'scale_x', request.scale_x, 'float')
        self.initialize('post_notes_slide_shape_save_as', 'scale_x', request.scale_x)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'scale_x', request.scale_x)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'scale_x')

    def test_post_notes_slide_shape_save_as_invalid_scale_y(self):
        """Test case for post_notes_slide_shape_save_as with invalid scale_y
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.scale_y = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'scale_y', request.scale_y, 'float')
        self.initialize('post_notes_slide_shape_save_as', 'scale_y', request.scale_y)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'scale_y', request.scale_y)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'scale_y')

    def test_post_notes_slide_shape_save_as_invalid_bounds(self):
        """Test case for post_notes_slide_shape_save_as with invalid bounds
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.bounds = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'bounds', request.bounds, 'str')
        self.initialize('post_notes_slide_shape_save_as', 'bounds', request.bounds)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'bounds', request.bounds)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'bounds')

    def test_post_notes_slide_shape_save_as_invalid_fonts_folder(self):
        """Test case for post_notes_slide_shape_save_as with invalid fonts_folder
        """
        request = self.__prepare_post_notes_slide_shape_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('post_notes_slide_shape_save_as', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_notes_slide_shape_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_notes_slide_shape_save_as', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_notes_slide_shape_save_as', 'fonts_folder')

    def __prepare_post_notes_slide_shape_save_as_request(self):
        name = self.get_test_value('post_notes_slide_shape_save_as', 'name', 'str')
        slide_index = self.get_test_value('post_notes_slide_shape_save_as', 'slide_index', 'int')
        shape_index = self.get_test_value('post_notes_slide_shape_save_as', 'shape_index', 'int')
        format = self.get_test_value('post_notes_slide_shape_save_as', 'format', 'str')
        options = self.get_test_value('post_notes_slide_shape_save_as', 'options', 'IShapeExportOptions')
        password = self.get_test_value('post_notes_slide_shape_save_as', 'password', 'str')
        folder = self.get_test_value('post_notes_slide_shape_save_as', 'folder', 'str')
        storage = self.get_test_value('post_notes_slide_shape_save_as', 'storage', 'str')
        scale_x = self.get_test_value('post_notes_slide_shape_save_as', 'scale_x', 'float')
        scale_y = self.get_test_value('post_notes_slide_shape_save_as', 'scale_y', 'float')
        bounds = self.get_test_value('post_notes_slide_shape_save_as', 'bounds', 'str')
        fonts_folder = self.get_test_value('post_notes_slide_shape_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostNotesSlideShapeSaveAsRequest(name, slide_index, shape_index, format, options, password, folder, storage, scale_x, scale_y, bounds, fonts_folder)

    def test_post_presentation_merge(self):
        """Test case for post_presentation_merge
        """
        request = self.__prepare_post_presentation_merge_request()
        self.initialize('post_presentation_merge', None, None)
        response = self.api.post_presentation_merge(request)
        self.assertIsNotNone(response)

    def test_post_presentation_merge_invalid_name(self):
        """Test case for post_presentation_merge with invalid name
        """
        request = self.__prepare_post_presentation_merge_request()
        request.name = self.get_invalid_test_value('post_presentation_merge', 'name', request.name, 'str')
        self.initialize('post_presentation_merge', 'name', request.name)
        ok = False
        try:
            self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_presentation_merge', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_presentation_merge', 'name')

    def test_post_presentation_merge_invalid_request(self):
        """Test case for post_presentation_merge with invalid request
        """
        request = self.__prepare_post_presentation_merge_request()
        request.request = self.get_invalid_test_value('post_presentation_merge', 'request', request.request, 'PresentationsMergeRequest')
        self.initialize('post_presentation_merge', 'request', request.request)
        ok = False
        try:
            self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_presentation_merge', 'request', request.request)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_presentation_merge', 'request')

    def test_post_presentation_merge_invalid_password(self):
        """Test case for post_presentation_merge with invalid password
        """
        request = self.__prepare_post_presentation_merge_request()
        request.password = self.get_invalid_test_value('post_presentation_merge', 'password', request.password, 'str')
        self.initialize('post_presentation_merge', 'password', request.password)
        ok = False
        try:
            self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_presentation_merge', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_presentation_merge', 'password')

    def test_post_presentation_merge_invalid_storage(self):
        """Test case for post_presentation_merge with invalid storage
        """
        request = self.__prepare_post_presentation_merge_request()
        request.storage = self.get_invalid_test_value('post_presentation_merge', 'storage', request.storage, 'str')
        self.initialize('post_presentation_merge', 'storage', request.storage)
        ok = False
        try:
            self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_presentation_merge', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_presentation_merge', 'storage')

    def test_post_presentation_merge_invalid_folder(self):
        """Test case for post_presentation_merge with invalid folder
        """
        request = self.__prepare_post_presentation_merge_request()
        request.folder = self.get_invalid_test_value('post_presentation_merge', 'folder', request.folder, 'str')
        self.initialize('post_presentation_merge', 'folder', request.folder)
        ok = False
        try:
            self.api.post_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_presentation_merge', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_presentation_merge', 'folder')

    def __prepare_post_presentation_merge_request(self):
        name = self.get_test_value('post_presentation_merge', 'name', 'str')
        request = self.get_test_value('post_presentation_merge', 'request', 'PresentationsMergeRequest')
        password = self.get_test_value('post_presentation_merge', 'password', 'str')
        storage = self.get_test_value('post_presentation_merge', 'storage', 'str')
        folder = self.get_test_value('post_presentation_merge', 'folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostPresentationMergeRequest(name, request, password, storage, folder)

    def test_post_shape_save_as(self):
        """Test case for post_shape_save_as
        """
        request = self.__prepare_post_shape_save_as_request()
        self.initialize('post_shape_save_as', None, None)
        response = self.api.post_shape_save_as(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_post_shape_save_as_invalid_name(self):
        """Test case for post_shape_save_as with invalid name
        """
        request = self.__prepare_post_shape_save_as_request()
        request.name = self.get_invalid_test_value('post_shape_save_as', 'name', request.name, 'str')
        self.initialize('post_shape_save_as', 'name', request.name)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'name')

    def test_post_shape_save_as_invalid_slide_index(self):
        """Test case for post_shape_save_as with invalid slide_index
        """
        request = self.__prepare_post_shape_save_as_request()
        request.slide_index = self.get_invalid_test_value('post_shape_save_as', 'slide_index', request.slide_index, 'int')
        self.initialize('post_shape_save_as', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'slide_index')

    def test_post_shape_save_as_invalid_shape_index(self):
        """Test case for post_shape_save_as with invalid shape_index
        """
        request = self.__prepare_post_shape_save_as_request()
        request.shape_index = self.get_invalid_test_value('post_shape_save_as', 'shape_index', request.shape_index, 'int')
        self.initialize('post_shape_save_as', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'shape_index')

    def test_post_shape_save_as_invalid_format(self):
        """Test case for post_shape_save_as with invalid format
        """
        request = self.__prepare_post_shape_save_as_request()
        request.format = self.get_invalid_test_value('post_shape_save_as', 'format', request.format, 'str')
        self.initialize('post_shape_save_as', 'format', request.format)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'format')

    def test_post_shape_save_as_invalid_options(self):
        """Test case for post_shape_save_as with invalid options
        """
        request = self.__prepare_post_shape_save_as_request()
        request.options = self.get_invalid_test_value('post_shape_save_as', 'options', request.options, 'IShapeExportOptions')
        self.initialize('post_shape_save_as', 'options', request.options)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'options')

    def test_post_shape_save_as_invalid_password(self):
        """Test case for post_shape_save_as with invalid password
        """
        request = self.__prepare_post_shape_save_as_request()
        request.password = self.get_invalid_test_value('post_shape_save_as', 'password', request.password, 'str')
        self.initialize('post_shape_save_as', 'password', request.password)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'password')

    def test_post_shape_save_as_invalid_folder(self):
        """Test case for post_shape_save_as with invalid folder
        """
        request = self.__prepare_post_shape_save_as_request()
        request.folder = self.get_invalid_test_value('post_shape_save_as', 'folder', request.folder, 'str')
        self.initialize('post_shape_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'folder')

    def test_post_shape_save_as_invalid_storage(self):
        """Test case for post_shape_save_as with invalid storage
        """
        request = self.__prepare_post_shape_save_as_request()
        request.storage = self.get_invalid_test_value('post_shape_save_as', 'storage', request.storage, 'str')
        self.initialize('post_shape_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'storage')

    def test_post_shape_save_as_invalid_scale_x(self):
        """Test case for post_shape_save_as with invalid scale_x
        """
        request = self.__prepare_post_shape_save_as_request()
        request.scale_x = self.get_invalid_test_value('post_shape_save_as', 'scale_x', request.scale_x, 'float')
        self.initialize('post_shape_save_as', 'scale_x', request.scale_x)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'scale_x', request.scale_x)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'scale_x')

    def test_post_shape_save_as_invalid_scale_y(self):
        """Test case for post_shape_save_as with invalid scale_y
        """
        request = self.__prepare_post_shape_save_as_request()
        request.scale_y = self.get_invalid_test_value('post_shape_save_as', 'scale_y', request.scale_y, 'float')
        self.initialize('post_shape_save_as', 'scale_y', request.scale_y)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'scale_y', request.scale_y)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'scale_y')

    def test_post_shape_save_as_invalid_bounds(self):
        """Test case for post_shape_save_as with invalid bounds
        """
        request = self.__prepare_post_shape_save_as_request()
        request.bounds = self.get_invalid_test_value('post_shape_save_as', 'bounds', request.bounds, 'str')
        self.initialize('post_shape_save_as', 'bounds', request.bounds)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'bounds', request.bounds)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'bounds')

    def test_post_shape_save_as_invalid_fonts_folder(self):
        """Test case for post_shape_save_as with invalid fonts_folder
        """
        request = self.__prepare_post_shape_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('post_shape_save_as', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_shape_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_shape_save_as', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_shape_save_as', 'fonts_folder')

    def __prepare_post_shape_save_as_request(self):
        name = self.get_test_value('post_shape_save_as', 'name', 'str')
        slide_index = self.get_test_value('post_shape_save_as', 'slide_index', 'int')
        shape_index = self.get_test_value('post_shape_save_as', 'shape_index', 'int')
        format = self.get_test_value('post_shape_save_as', 'format', 'str')
        options = self.get_test_value('post_shape_save_as', 'options', 'IShapeExportOptions')
        password = self.get_test_value('post_shape_save_as', 'password', 'str')
        folder = self.get_test_value('post_shape_save_as', 'folder', 'str')
        storage = self.get_test_value('post_shape_save_as', 'storage', 'str')
        scale_x = self.get_test_value('post_shape_save_as', 'scale_x', 'float')
        scale_y = self.get_test_value('post_shape_save_as', 'scale_y', 'float')
        bounds = self.get_test_value('post_shape_save_as', 'bounds', 'str')
        fonts_folder = self.get_test_value('post_shape_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostShapeSaveAsRequest(name, slide_index, shape_index, format, options, password, folder, storage, scale_x, scale_y, bounds, fonts_folder)

    def test_post_slide_animation_effect(self):
        """Test case for post_slide_animation_effect
        """
        request = self.__prepare_post_slide_animation_effect_request()
        self.initialize('post_slide_animation_effect', None, None)
        response = self.api.post_slide_animation_effect(request)
        self.assertIsNotNone(response)

    def test_post_slide_animation_effect_invalid_name(self):
        """Test case for post_slide_animation_effect with invalid name
        """
        request = self.__prepare_post_slide_animation_effect_request()
        request.name = self.get_invalid_test_value('post_slide_animation_effect', 'name', request.name, 'str')
        self.initialize('post_slide_animation_effect', 'name', request.name)
        ok = False
        try:
            self.api.post_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_effect', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_effect', 'name')

    def test_post_slide_animation_effect_invalid_slide_index(self):
        """Test case for post_slide_animation_effect with invalid slide_index
        """
        request = self.__prepare_post_slide_animation_effect_request()
        request.slide_index = self.get_invalid_test_value('post_slide_animation_effect', 'slide_index', request.slide_index, 'int')
        self.initialize('post_slide_animation_effect', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_effect', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_effect', 'slide_index')

    def test_post_slide_animation_effect_invalid_effect(self):
        """Test case for post_slide_animation_effect with invalid effect
        """
        request = self.__prepare_post_slide_animation_effect_request()
        request.effect = self.get_invalid_test_value('post_slide_animation_effect', 'effect', request.effect, 'Effect')
        self.initialize('post_slide_animation_effect', 'effect', request.effect)
        ok = False
        try:
            self.api.post_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_effect', 'effect', request.effect)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_effect', 'effect')

    def test_post_slide_animation_effect_invalid_password(self):
        """Test case for post_slide_animation_effect with invalid password
        """
        request = self.__prepare_post_slide_animation_effect_request()
        request.password = self.get_invalid_test_value('post_slide_animation_effect', 'password', request.password, 'str')
        self.initialize('post_slide_animation_effect', 'password', request.password)
        ok = False
        try:
            self.api.post_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_effect', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_effect', 'password')

    def test_post_slide_animation_effect_invalid_folder(self):
        """Test case for post_slide_animation_effect with invalid folder
        """
        request = self.__prepare_post_slide_animation_effect_request()
        request.folder = self.get_invalid_test_value('post_slide_animation_effect', 'folder', request.folder, 'str')
        self.initialize('post_slide_animation_effect', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_effect', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_effect', 'folder')

    def test_post_slide_animation_effect_invalid_storage(self):
        """Test case for post_slide_animation_effect with invalid storage
        """
        request = self.__prepare_post_slide_animation_effect_request()
        request.storage = self.get_invalid_test_value('post_slide_animation_effect', 'storage', request.storage, 'str')
        self.initialize('post_slide_animation_effect', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_effect', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_effect', 'storage')

    def __prepare_post_slide_animation_effect_request(self):
        name = self.get_test_value('post_slide_animation_effect', 'name', 'str')
        slide_index = self.get_test_value('post_slide_animation_effect', 'slide_index', 'int')
        effect = self.get_test_value('post_slide_animation_effect', 'effect', 'Effect')
        password = self.get_test_value('post_slide_animation_effect', 'password', 'str')
        folder = self.get_test_value('post_slide_animation_effect', 'folder', 'str')
        storage = self.get_test_value('post_slide_animation_effect', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlideAnimationEffectRequest(name, slide_index, effect, password, folder, storage)

    def test_post_slide_animation_interactive_sequence(self):
        """Test case for post_slide_animation_interactive_sequence
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_request()
        self.initialize('post_slide_animation_interactive_sequence', None, None)
        response = self.api.post_slide_animation_interactive_sequence(request)
        self.assertIsNotNone(response)

    def test_post_slide_animation_interactive_sequence_invalid_name(self):
        """Test case for post_slide_animation_interactive_sequence with invalid name
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_request()
        request.name = self.get_invalid_test_value('post_slide_animation_interactive_sequence', 'name', request.name, 'str')
        self.initialize('post_slide_animation_interactive_sequence', 'name', request.name)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence', 'name')

    def test_post_slide_animation_interactive_sequence_invalid_slide_index(self):
        """Test case for post_slide_animation_interactive_sequence with invalid slide_index
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_request()
        request.slide_index = self.get_invalid_test_value('post_slide_animation_interactive_sequence', 'slide_index', request.slide_index, 'int')
        self.initialize('post_slide_animation_interactive_sequence', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence', 'slide_index')

    def test_post_slide_animation_interactive_sequence_invalid_sequence(self):
        """Test case for post_slide_animation_interactive_sequence with invalid sequence
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_request()
        request.sequence = self.get_invalid_test_value('post_slide_animation_interactive_sequence', 'sequence', request.sequence, 'InteractiveSequence')
        self.initialize('post_slide_animation_interactive_sequence', 'sequence', request.sequence)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence', 'sequence', request.sequence)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence', 'sequence')

    def test_post_slide_animation_interactive_sequence_invalid_password(self):
        """Test case for post_slide_animation_interactive_sequence with invalid password
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_request()
        request.password = self.get_invalid_test_value('post_slide_animation_interactive_sequence', 'password', request.password, 'str')
        self.initialize('post_slide_animation_interactive_sequence', 'password', request.password)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence', 'password')

    def test_post_slide_animation_interactive_sequence_invalid_folder(self):
        """Test case for post_slide_animation_interactive_sequence with invalid folder
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_request()
        request.folder = self.get_invalid_test_value('post_slide_animation_interactive_sequence', 'folder', request.folder, 'str')
        self.initialize('post_slide_animation_interactive_sequence', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence', 'folder')

    def test_post_slide_animation_interactive_sequence_invalid_storage(self):
        """Test case for post_slide_animation_interactive_sequence with invalid storage
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_request()
        request.storage = self.get_invalid_test_value('post_slide_animation_interactive_sequence', 'storage', request.storage, 'str')
        self.initialize('post_slide_animation_interactive_sequence', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence', 'storage')

    def __prepare_post_slide_animation_interactive_sequence_request(self):
        name = self.get_test_value('post_slide_animation_interactive_sequence', 'name', 'str')
        slide_index = self.get_test_value('post_slide_animation_interactive_sequence', 'slide_index', 'int')
        sequence = self.get_test_value('post_slide_animation_interactive_sequence', 'sequence', 'InteractiveSequence')
        password = self.get_test_value('post_slide_animation_interactive_sequence', 'password', 'str')
        folder = self.get_test_value('post_slide_animation_interactive_sequence', 'folder', 'str')
        storage = self.get_test_value('post_slide_animation_interactive_sequence', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlideAnimationInteractiveSequenceRequest(name, slide_index, sequence, password, folder, storage)

    def test_post_slide_animation_interactive_sequence_effect(self):
        """Test case for post_slide_animation_interactive_sequence_effect
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_effect_request()
        self.initialize('post_slide_animation_interactive_sequence_effect', None, None)
        response = self.api.post_slide_animation_interactive_sequence_effect(request)
        self.assertIsNotNone(response)

    def test_post_slide_animation_interactive_sequence_effect_invalid_name(self):
        """Test case for post_slide_animation_interactive_sequence_effect with invalid name
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_effect_request()
        request.name = self.get_invalid_test_value('post_slide_animation_interactive_sequence_effect', 'name', request.name, 'str')
        self.initialize('post_slide_animation_interactive_sequence_effect', 'name', request.name)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence_effect', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence_effect', 'name')

    def test_post_slide_animation_interactive_sequence_effect_invalid_slide_index(self):
        """Test case for post_slide_animation_interactive_sequence_effect with invalid slide_index
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_effect_request()
        request.slide_index = self.get_invalid_test_value('post_slide_animation_interactive_sequence_effect', 'slide_index', request.slide_index, 'int')
        self.initialize('post_slide_animation_interactive_sequence_effect', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence_effect', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence_effect', 'slide_index')

    def test_post_slide_animation_interactive_sequence_effect_invalid_sequence_index(self):
        """Test case for post_slide_animation_interactive_sequence_effect with invalid sequence_index
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_effect_request()
        request.sequence_index = self.get_invalid_test_value('post_slide_animation_interactive_sequence_effect', 'sequence_index', request.sequence_index, 'int')
        self.initialize('post_slide_animation_interactive_sequence_effect', 'sequence_index', request.sequence_index)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence_effect', 'sequence_index', request.sequence_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence_effect', 'sequence_index')

    def test_post_slide_animation_interactive_sequence_effect_invalid_effect(self):
        """Test case for post_slide_animation_interactive_sequence_effect with invalid effect
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_effect_request()
        request.effect = self.get_invalid_test_value('post_slide_animation_interactive_sequence_effect', 'effect', request.effect, 'Effect')
        self.initialize('post_slide_animation_interactive_sequence_effect', 'effect', request.effect)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence_effect', 'effect', request.effect)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence_effect', 'effect')

    def test_post_slide_animation_interactive_sequence_effect_invalid_password(self):
        """Test case for post_slide_animation_interactive_sequence_effect with invalid password
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_effect_request()
        request.password = self.get_invalid_test_value('post_slide_animation_interactive_sequence_effect', 'password', request.password, 'str')
        self.initialize('post_slide_animation_interactive_sequence_effect', 'password', request.password)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence_effect', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence_effect', 'password')

    def test_post_slide_animation_interactive_sequence_effect_invalid_folder(self):
        """Test case for post_slide_animation_interactive_sequence_effect with invalid folder
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_effect_request()
        request.folder = self.get_invalid_test_value('post_slide_animation_interactive_sequence_effect', 'folder', request.folder, 'str')
        self.initialize('post_slide_animation_interactive_sequence_effect', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence_effect', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence_effect', 'folder')

    def test_post_slide_animation_interactive_sequence_effect_invalid_storage(self):
        """Test case for post_slide_animation_interactive_sequence_effect with invalid storage
        """
        request = self.__prepare_post_slide_animation_interactive_sequence_effect_request()
        request.storage = self.get_invalid_test_value('post_slide_animation_interactive_sequence_effect', 'storage', request.storage, 'str')
        self.initialize('post_slide_animation_interactive_sequence_effect', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_animation_interactive_sequence_effect', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_animation_interactive_sequence_effect', 'storage')

    def __prepare_post_slide_animation_interactive_sequence_effect_request(self):
        name = self.get_test_value('post_slide_animation_interactive_sequence_effect', 'name', 'str')
        slide_index = self.get_test_value('post_slide_animation_interactive_sequence_effect', 'slide_index', 'int')
        sequence_index = self.get_test_value('post_slide_animation_interactive_sequence_effect', 'sequence_index', 'int')
        effect = self.get_test_value('post_slide_animation_interactive_sequence_effect', 'effect', 'Effect')
        password = self.get_test_value('post_slide_animation_interactive_sequence_effect', 'password', 'str')
        folder = self.get_test_value('post_slide_animation_interactive_sequence_effect', 'folder', 'str')
        storage = self.get_test_value('post_slide_animation_interactive_sequence_effect', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlideAnimationInteractiveSequenceEffectRequest(name, slide_index, sequence_index, effect, password, folder, storage)

    def test_post_slide_save_as(self):
        """Test case for post_slide_save_as
        """
        request = self.__prepare_post_slide_save_as_request()
        self.initialize('post_slide_save_as', None, None)
        response = self.api.post_slide_save_as(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_post_slide_save_as_invalid_name(self):
        """Test case for post_slide_save_as with invalid name
        """
        request = self.__prepare_post_slide_save_as_request()
        request.name = self.get_invalid_test_value('post_slide_save_as', 'name', request.name, 'str')
        self.initialize('post_slide_save_as', 'name', request.name)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_save_as', 'name')

    def test_post_slide_save_as_invalid_slide_index(self):
        """Test case for post_slide_save_as with invalid slide_index
        """
        request = self.__prepare_post_slide_save_as_request()
        request.slide_index = self.get_invalid_test_value('post_slide_save_as', 'slide_index', request.slide_index, 'int')
        self.initialize('post_slide_save_as', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_save_as', 'slide_index')

    def test_post_slide_save_as_invalid_format(self):
        """Test case for post_slide_save_as with invalid format
        """
        request = self.__prepare_post_slide_save_as_request()
        request.format = self.get_invalid_test_value('post_slide_save_as', 'format', request.format, 'str')
        self.initialize('post_slide_save_as', 'format', request.format)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_save_as', 'format')

    def test_post_slide_save_as_invalid_options(self):
        """Test case for post_slide_save_as with invalid options
        """
        request = self.__prepare_post_slide_save_as_request()
        request.options = self.get_invalid_test_value('post_slide_save_as', 'options', request.options, 'ExportOptions')
        self.initialize('post_slide_save_as', 'options', request.options)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_save_as', 'options')

    def test_post_slide_save_as_invalid_width(self):
        """Test case for post_slide_save_as with invalid width
        """
        request = self.__prepare_post_slide_save_as_request()
        request.width = self.get_invalid_test_value('post_slide_save_as', 'width', request.width, 'int')
        self.initialize('post_slide_save_as', 'width', request.width)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'width', request.width)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_save_as', 'width')

    def test_post_slide_save_as_invalid_height(self):
        """Test case for post_slide_save_as with invalid height
        """
        request = self.__prepare_post_slide_save_as_request()
        request.height = self.get_invalid_test_value('post_slide_save_as', 'height', request.height, 'int')
        self.initialize('post_slide_save_as', 'height', request.height)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'height', request.height)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_save_as', 'height')

    def test_post_slide_save_as_invalid_password(self):
        """Test case for post_slide_save_as with invalid password
        """
        request = self.__prepare_post_slide_save_as_request()
        request.password = self.get_invalid_test_value('post_slide_save_as', 'password', request.password, 'str')
        self.initialize('post_slide_save_as', 'password', request.password)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_save_as', 'password')

    def test_post_slide_save_as_invalid_folder(self):
        """Test case for post_slide_save_as with invalid folder
        """
        request = self.__prepare_post_slide_save_as_request()
        request.folder = self.get_invalid_test_value('post_slide_save_as', 'folder', request.folder, 'str')
        self.initialize('post_slide_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_save_as', 'folder')

    def test_post_slide_save_as_invalid_storage(self):
        """Test case for post_slide_save_as with invalid storage
        """
        request = self.__prepare_post_slide_save_as_request()
        request.storage = self.get_invalid_test_value('post_slide_save_as', 'storage', request.storage, 'str')
        self.initialize('post_slide_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_save_as', 'storage')

    def test_post_slide_save_as_invalid_fonts_folder(self):
        """Test case for post_slide_save_as with invalid fonts_folder
        """
        request = self.__prepare_post_slide_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('post_slide_save_as', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_slide_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slide_save_as', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slide_save_as', 'fonts_folder')

    def __prepare_post_slide_save_as_request(self):
        name = self.get_test_value('post_slide_save_as', 'name', 'str')
        slide_index = self.get_test_value('post_slide_save_as', 'slide_index', 'int')
        format = self.get_test_value('post_slide_save_as', 'format', 'str')
        options = self.get_test_value('post_slide_save_as', 'options', 'ExportOptions')
        width = self.get_test_value('post_slide_save_as', 'width', 'int')
        height = self.get_test_value('post_slide_save_as', 'height', 'int')
        password = self.get_test_value('post_slide_save_as', 'password', 'str')
        folder = self.get_test_value('post_slide_save_as', 'folder', 'str')
        storage = self.get_test_value('post_slide_save_as', 'storage', 'str')
        fonts_folder = self.get_test_value('post_slide_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlideSaveAsRequest(name, slide_index, format, options, width, height, password, folder, storage, fonts_folder)

    def test_post_slides_add(self):
        """Test case for post_slides_add
        """
        request = self.__prepare_post_slides_add_request()
        self.initialize('post_slides_add', None, None)
        response = self.api.post_slides_add(request)
        self.assertIsNotNone(response)

    def test_post_slides_add_invalid_name(self):
        """Test case for post_slides_add with invalid name
        """
        request = self.__prepare_post_slides_add_request()
        request.name = self.get_invalid_test_value('post_slides_add', 'name', request.name, 'str')
        self.initialize('post_slides_add', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_add', 'name')

    def test_post_slides_add_invalid_position(self):
        """Test case for post_slides_add with invalid position
        """
        request = self.__prepare_post_slides_add_request()
        request.position = self.get_invalid_test_value('post_slides_add', 'position', request.position, 'int')
        self.initialize('post_slides_add', 'position', request.position)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_add', 'position')

    def test_post_slides_add_invalid_password(self):
        """Test case for post_slides_add with invalid password
        """
        request = self.__prepare_post_slides_add_request()
        request.password = self.get_invalid_test_value('post_slides_add', 'password', request.password, 'str')
        self.initialize('post_slides_add', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_add', 'password')

    def test_post_slides_add_invalid_folder(self):
        """Test case for post_slides_add with invalid folder
        """
        request = self.__prepare_post_slides_add_request()
        request.folder = self.get_invalid_test_value('post_slides_add', 'folder', request.folder, 'str')
        self.initialize('post_slides_add', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_add', 'folder')

    def test_post_slides_add_invalid_storage(self):
        """Test case for post_slides_add with invalid storage
        """
        request = self.__prepare_post_slides_add_request()
        request.storage = self.get_invalid_test_value('post_slides_add', 'storage', request.storage, 'str')
        self.initialize('post_slides_add', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_add', 'storage')

    def test_post_slides_add_invalid_layout_alias(self):
        """Test case for post_slides_add with invalid layout_alias
        """
        request = self.__prepare_post_slides_add_request()
        request.layout_alias = self.get_invalid_test_value('post_slides_add', 'layout_alias', request.layout_alias, 'str')
        self.initialize('post_slides_add', 'layout_alias', request.layout_alias)
        ok = False
        try:
            self.api.post_slides_add(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_add', 'layout_alias', request.layout_alias)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_add', 'layout_alias')

    def __prepare_post_slides_add_request(self):
        name = self.get_test_value('post_slides_add', 'name', 'str')
        position = self.get_test_value('post_slides_add', 'position', 'int')
        password = self.get_test_value('post_slides_add', 'password', 'str')
        folder = self.get_test_value('post_slides_add', 'folder', 'str')
        storage = self.get_test_value('post_slides_add', 'storage', 'str')
        layout_alias = self.get_test_value('post_slides_add', 'layout_alias', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesAddRequest(name, position, password, folder, storage, layout_alias)

    def test_post_slides_convert(self):
        """Test case for post_slides_convert
        """
        request = self.__prepare_post_slides_convert_request()
        self.initialize('post_slides_convert', None, None)
        response = self.api.post_slides_convert(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_post_slides_convert_invalid_format(self):
        """Test case for post_slides_convert with invalid format
        """
        request = self.__prepare_post_slides_convert_request()
        request.format = self.get_invalid_test_value('post_slides_convert', 'format', request.format, 'str')
        self.initialize('post_slides_convert', 'format', request.format)
        ok = False
        try:
            self.api.post_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_convert', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_convert', 'format')

    def test_post_slides_convert_invalid_document(self):
        """Test case for post_slides_convert with invalid document
        """
        request = self.__prepare_post_slides_convert_request()
        request.document = self.get_invalid_test_value('post_slides_convert', 'document', request.document, 'file')
        self.initialize('post_slides_convert', 'document', request.document)
        ok = False
        try:
            self.api.post_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_convert', 'document', request.document)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_convert', 'document')

    def test_post_slides_convert_invalid_password(self):
        """Test case for post_slides_convert with invalid password
        """
        request = self.__prepare_post_slides_convert_request()
        request.password = self.get_invalid_test_value('post_slides_convert', 'password', request.password, 'str')
        self.initialize('post_slides_convert', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_convert', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_convert', 'password')

    def test_post_slides_convert_invalid_fonts_folder(self):
        """Test case for post_slides_convert with invalid fonts_folder
        """
        request = self.__prepare_post_slides_convert_request()
        request.fonts_folder = self.get_invalid_test_value('post_slides_convert', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_slides_convert', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_convert', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_convert', 'fonts_folder')

    def __prepare_post_slides_convert_request(self):
        format = self.get_test_value('post_slides_convert', 'format', 'str')
        document = self.get_test_value('post_slides_convert', 'document', 'file')
        password = self.get_test_value('post_slides_convert', 'password', 'str')
        fonts_folder = self.get_test_value('post_slides_convert', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesConvertRequest(format, document, password, fonts_folder)

    def test_post_slides_copy(self):
        """Test case for post_slides_copy
        """
        request = self.__prepare_post_slides_copy_request()
        self.initialize('post_slides_copy', None, None)
        response = self.api.post_slides_copy(request)
        self.assertIsNotNone(response)

    def test_post_slides_copy_invalid_name(self):
        """Test case for post_slides_copy with invalid name
        """
        request = self.__prepare_post_slides_copy_request()
        request.name = self.get_invalid_test_value('post_slides_copy', 'name', request.name, 'str')
        self.initialize('post_slides_copy', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_copy', 'name')

    def test_post_slides_copy_invalid_slide_to_copy(self):
        """Test case for post_slides_copy with invalid slide_to_copy
        """
        request = self.__prepare_post_slides_copy_request()
        request.slide_to_copy = self.get_invalid_test_value('post_slides_copy', 'slide_to_copy', request.slide_to_copy, 'int')
        self.initialize('post_slides_copy', 'slide_to_copy', request.slide_to_copy)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'slide_to_copy', request.slide_to_copy)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_copy', 'slide_to_copy')

    def test_post_slides_copy_invalid_position(self):
        """Test case for post_slides_copy with invalid position
        """
        request = self.__prepare_post_slides_copy_request()
        request.position = self.get_invalid_test_value('post_slides_copy', 'position', request.position, 'int')
        self.initialize('post_slides_copy', 'position', request.position)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'position', request.position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_copy', 'position')

    def test_post_slides_copy_invalid_source(self):
        """Test case for post_slides_copy with invalid source
        """
        request = self.__prepare_post_slides_copy_request()
        request.source = self.get_invalid_test_value('post_slides_copy', 'source', request.source, 'str')
        self.initialize('post_slides_copy', 'source', request.source)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'source', request.source)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_copy', 'source')

    def test_post_slides_copy_invalid_source_password(self):
        """Test case for post_slides_copy with invalid source_password
        """
        request = self.__prepare_post_slides_copy_request()
        request.source_password = self.get_invalid_test_value('post_slides_copy', 'source_password', request.source_password, 'str')
        self.initialize('post_slides_copy', 'source_password', request.source_password)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'source_password', request.source_password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_copy', 'source_password')

    def test_post_slides_copy_invalid_source_storage(self):
        """Test case for post_slides_copy with invalid source_storage
        """
        request = self.__prepare_post_slides_copy_request()
        request.source_storage = self.get_invalid_test_value('post_slides_copy', 'source_storage', request.source_storage, 'str')
        self.initialize('post_slides_copy', 'source_storage', request.source_storage)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'source_storage', request.source_storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_copy', 'source_storage')

    def test_post_slides_copy_invalid_password(self):
        """Test case for post_slides_copy with invalid password
        """
        request = self.__prepare_post_slides_copy_request()
        request.password = self.get_invalid_test_value('post_slides_copy', 'password', request.password, 'str')
        self.initialize('post_slides_copy', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_copy', 'password')

    def test_post_slides_copy_invalid_folder(self):
        """Test case for post_slides_copy with invalid folder
        """
        request = self.__prepare_post_slides_copy_request()
        request.folder = self.get_invalid_test_value('post_slides_copy', 'folder', request.folder, 'str')
        self.initialize('post_slides_copy', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_copy', 'folder')

    def test_post_slides_copy_invalid_storage(self):
        """Test case for post_slides_copy with invalid storage
        """
        request = self.__prepare_post_slides_copy_request()
        request.storage = self.get_invalid_test_value('post_slides_copy', 'storage', request.storage, 'str')
        self.initialize('post_slides_copy', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_copy(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_copy', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_copy', 'storage')

    def __prepare_post_slides_copy_request(self):
        name = self.get_test_value('post_slides_copy', 'name', 'str')
        slide_to_copy = self.get_test_value('post_slides_copy', 'slide_to_copy', 'int')
        position = self.get_test_value('post_slides_copy', 'position', 'int')
        source = self.get_test_value('post_slides_copy', 'source', 'str')
        source_password = self.get_test_value('post_slides_copy', 'source_password', 'str')
        source_storage = self.get_test_value('post_slides_copy', 'source_storage', 'str')
        password = self.get_test_value('post_slides_copy', 'password', 'str')
        folder = self.get_test_value('post_slides_copy', 'folder', 'str')
        storage = self.get_test_value('post_slides_copy', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesCopyRequest(name, slide_to_copy, position, source, source_password, source_storage, password, folder, storage)

    def test_post_slides_document(self):
        """Test case for post_slides_document
        """
        request = self.__prepare_post_slides_document_request()
        self.initialize('post_slides_document', None, None)
        response = self.api.post_slides_document(request)
        self.assertIsNotNone(response)

    def test_post_slides_document_invalid_name(self):
        """Test case for post_slides_document with invalid name
        """
        request = self.__prepare_post_slides_document_request()
        request.name = self.get_invalid_test_value('post_slides_document', 'name', request.name, 'str')
        self.initialize('post_slides_document', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document', 'name')

    def test_post_slides_document_invalid_data(self):
        """Test case for post_slides_document with invalid data
        """
        request = self.__prepare_post_slides_document_request()
        request.data = self.get_invalid_test_value('post_slides_document', 'data', request.data, 'file')
        self.initialize('post_slides_document', 'data', request.data)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'data', request.data)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document', 'data')

    def test_post_slides_document_invalid_input_password(self):
        """Test case for post_slides_document with invalid input_password
        """
        request = self.__prepare_post_slides_document_request()
        request.input_password = self.get_invalid_test_value('post_slides_document', 'input_password', request.input_password, 'str')
        self.initialize('post_slides_document', 'input_password', request.input_password)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'input_password', request.input_password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document', 'input_password')

    def test_post_slides_document_invalid_password(self):
        """Test case for post_slides_document with invalid password
        """
        request = self.__prepare_post_slides_document_request()
        request.password = self.get_invalid_test_value('post_slides_document', 'password', request.password, 'str')
        self.initialize('post_slides_document', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document', 'password')

    def test_post_slides_document_invalid_storage(self):
        """Test case for post_slides_document with invalid storage
        """
        request = self.__prepare_post_slides_document_request()
        request.storage = self.get_invalid_test_value('post_slides_document', 'storage', request.storage, 'str')
        self.initialize('post_slides_document', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document', 'storage')

    def test_post_slides_document_invalid_folder(self):
        """Test case for post_slides_document with invalid folder
        """
        request = self.__prepare_post_slides_document_request()
        request.folder = self.get_invalid_test_value('post_slides_document', 'folder', request.folder, 'str')
        self.initialize('post_slides_document', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_document(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document', 'folder')

    def __prepare_post_slides_document_request(self):
        name = self.get_test_value('post_slides_document', 'name', 'str')
        data = self.get_test_value('post_slides_document', 'data', 'file')
        input_password = self.get_test_value('post_slides_document', 'input_password', 'str')
        password = self.get_test_value('post_slides_document', 'password', 'str')
        storage = self.get_test_value('post_slides_document', 'storage', 'str')
        folder = self.get_test_value('post_slides_document', 'folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesDocumentRequest(name, data, input_password, password, storage, folder)

    def test_post_slides_document_from_html(self):
        """Test case for post_slides_document_from_html
        """
        request = self.__prepare_post_slides_document_from_html_request()
        self.initialize('post_slides_document_from_html', None, None)
        response = self.api.post_slides_document_from_html(request)
        self.assertIsNotNone(response)

    def test_post_slides_document_from_html_invalid_name(self):
        """Test case for post_slides_document_from_html with invalid name
        """
        request = self.__prepare_post_slides_document_from_html_request()
        request.name = self.get_invalid_test_value('post_slides_document_from_html', 'name', request.name, 'str')
        self.initialize('post_slides_document_from_html', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_html', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_html', 'name')

    def test_post_slides_document_from_html_invalid_html(self):
        """Test case for post_slides_document_from_html with invalid html
        """
        request = self.__prepare_post_slides_document_from_html_request()
        request.html = self.get_invalid_test_value('post_slides_document_from_html', 'html', request.html, 'str')
        self.initialize('post_slides_document_from_html', 'html', request.html)
        ok = False
        try:
            self.api.post_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_html', 'html', request.html)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_html', 'html')

    def test_post_slides_document_from_html_invalid_password(self):
        """Test case for post_slides_document_from_html with invalid password
        """
        request = self.__prepare_post_slides_document_from_html_request()
        request.password = self.get_invalid_test_value('post_slides_document_from_html', 'password', request.password, 'str')
        self.initialize('post_slides_document_from_html', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_html', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_html', 'password')

    def test_post_slides_document_from_html_invalid_storage(self):
        """Test case for post_slides_document_from_html with invalid storage
        """
        request = self.__prepare_post_slides_document_from_html_request()
        request.storage = self.get_invalid_test_value('post_slides_document_from_html', 'storage', request.storage, 'str')
        self.initialize('post_slides_document_from_html', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_html', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_html', 'storage')

    def test_post_slides_document_from_html_invalid_folder(self):
        """Test case for post_slides_document_from_html with invalid folder
        """
        request = self.__prepare_post_slides_document_from_html_request()
        request.folder = self.get_invalid_test_value('post_slides_document_from_html', 'folder', request.folder, 'str')
        self.initialize('post_slides_document_from_html', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_html', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_html', 'folder')

    def __prepare_post_slides_document_from_html_request(self):
        name = self.get_test_value('post_slides_document_from_html', 'name', 'str')
        html = self.get_test_value('post_slides_document_from_html', 'html', 'str')
        password = self.get_test_value('post_slides_document_from_html', 'password', 'str')
        storage = self.get_test_value('post_slides_document_from_html', 'storage', 'str')
        folder = self.get_test_value('post_slides_document_from_html', 'folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesDocumentFromHtmlRequest(name, html, password, storage, folder)

    def test_post_slides_document_from_source(self):
        """Test case for post_slides_document_from_source
        """
        request = self.__prepare_post_slides_document_from_source_request()
        self.initialize('post_slides_document_from_source', None, None)
        response = self.api.post_slides_document_from_source(request)
        self.assertIsNotNone(response)

    def test_post_slides_document_from_source_invalid_name(self):
        """Test case for post_slides_document_from_source with invalid name
        """
        request = self.__prepare_post_slides_document_from_source_request()
        request.name = self.get_invalid_test_value('post_slides_document_from_source', 'name', request.name, 'str')
        self.initialize('post_slides_document_from_source', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_document_from_source(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_source', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_source', 'name')

    def test_post_slides_document_from_source_invalid_source_path(self):
        """Test case for post_slides_document_from_source with invalid source_path
        """
        request = self.__prepare_post_slides_document_from_source_request()
        request.source_path = self.get_invalid_test_value('post_slides_document_from_source', 'source_path', request.source_path, 'str')
        self.initialize('post_slides_document_from_source', 'source_path', request.source_path)
        ok = False
        try:
            self.api.post_slides_document_from_source(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_source', 'source_path', request.source_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_source', 'source_path')

    def test_post_slides_document_from_source_invalid_source_password(self):
        """Test case for post_slides_document_from_source with invalid source_password
        """
        request = self.__prepare_post_slides_document_from_source_request()
        request.source_password = self.get_invalid_test_value('post_slides_document_from_source', 'source_password', request.source_password, 'str')
        self.initialize('post_slides_document_from_source', 'source_password', request.source_password)
        ok = False
        try:
            self.api.post_slides_document_from_source(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_source', 'source_password', request.source_password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_source', 'source_password')

    def test_post_slides_document_from_source_invalid_source_storage(self):
        """Test case for post_slides_document_from_source with invalid source_storage
        """
        request = self.__prepare_post_slides_document_from_source_request()
        request.source_storage = self.get_invalid_test_value('post_slides_document_from_source', 'source_storage', request.source_storage, 'str')
        self.initialize('post_slides_document_from_source', 'source_storage', request.source_storage)
        ok = False
        try:
            self.api.post_slides_document_from_source(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_source', 'source_storage', request.source_storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_source', 'source_storage')

    def test_post_slides_document_from_source_invalid_password(self):
        """Test case for post_slides_document_from_source with invalid password
        """
        request = self.__prepare_post_slides_document_from_source_request()
        request.password = self.get_invalid_test_value('post_slides_document_from_source', 'password', request.password, 'str')
        self.initialize('post_slides_document_from_source', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_document_from_source(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_source', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_source', 'password')

    def test_post_slides_document_from_source_invalid_storage(self):
        """Test case for post_slides_document_from_source with invalid storage
        """
        request = self.__prepare_post_slides_document_from_source_request()
        request.storage = self.get_invalid_test_value('post_slides_document_from_source', 'storage', request.storage, 'str')
        self.initialize('post_slides_document_from_source', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_document_from_source(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_source', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_source', 'storage')

    def test_post_slides_document_from_source_invalid_folder(self):
        """Test case for post_slides_document_from_source with invalid folder
        """
        request = self.__prepare_post_slides_document_from_source_request()
        request.folder = self.get_invalid_test_value('post_slides_document_from_source', 'folder', request.folder, 'str')
        self.initialize('post_slides_document_from_source', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_document_from_source(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_source', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_source', 'folder')

    def __prepare_post_slides_document_from_source_request(self):
        name = self.get_test_value('post_slides_document_from_source', 'name', 'str')
        source_path = self.get_test_value('post_slides_document_from_source', 'source_path', 'str')
        source_password = self.get_test_value('post_slides_document_from_source', 'source_password', 'str')
        source_storage = self.get_test_value('post_slides_document_from_source', 'source_storage', 'str')
        password = self.get_test_value('post_slides_document_from_source', 'password', 'str')
        storage = self.get_test_value('post_slides_document_from_source', 'storage', 'str')
        folder = self.get_test_value('post_slides_document_from_source', 'folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesDocumentFromSourceRequest(name, source_path, source_password, source_storage, password, storage, folder)

    def test_post_slides_document_from_template(self):
        """Test case for post_slides_document_from_template
        """
        request = self.__prepare_post_slides_document_from_template_request()
        self.initialize('post_slides_document_from_template', None, None)
        response = self.api.post_slides_document_from_template(request)
        self.assertIsNotNone(response)

    def test_post_slides_document_from_template_invalid_name(self):
        """Test case for post_slides_document_from_template with invalid name
        """
        request = self.__prepare_post_slides_document_from_template_request()
        request.name = self.get_invalid_test_value('post_slides_document_from_template', 'name', request.name, 'str')
        self.initialize('post_slides_document_from_template', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_document_from_template(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_template', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_template', 'name')

    def test_post_slides_document_from_template_invalid_template_path(self):
        """Test case for post_slides_document_from_template with invalid template_path
        """
        request = self.__prepare_post_slides_document_from_template_request()
        request.template_path = self.get_invalid_test_value('post_slides_document_from_template', 'template_path', request.template_path, 'str')
        self.initialize('post_slides_document_from_template', 'template_path', request.template_path)
        ok = False
        try:
            self.api.post_slides_document_from_template(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_template', 'template_path', request.template_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_template', 'template_path')

    def test_post_slides_document_from_template_invalid_data(self):
        """Test case for post_slides_document_from_template with invalid data
        """
        request = self.__prepare_post_slides_document_from_template_request()
        request.data = self.get_invalid_test_value('post_slides_document_from_template', 'data', request.data, 'str')
        self.initialize('post_slides_document_from_template', 'data', request.data)
        ok = False
        try:
            self.api.post_slides_document_from_template(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_template', 'data', request.data)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_template', 'data')

    def test_post_slides_document_from_template_invalid_template_password(self):
        """Test case for post_slides_document_from_template with invalid template_password
        """
        request = self.__prepare_post_slides_document_from_template_request()
        request.template_password = self.get_invalid_test_value('post_slides_document_from_template', 'template_password', request.template_password, 'str')
        self.initialize('post_slides_document_from_template', 'template_password', request.template_password)
        ok = False
        try:
            self.api.post_slides_document_from_template(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_template', 'template_password', request.template_password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_template', 'template_password')

    def test_post_slides_document_from_template_invalid_template_storage(self):
        """Test case for post_slides_document_from_template with invalid template_storage
        """
        request = self.__prepare_post_slides_document_from_template_request()
        request.template_storage = self.get_invalid_test_value('post_slides_document_from_template', 'template_storage', request.template_storage, 'str')
        self.initialize('post_slides_document_from_template', 'template_storage', request.template_storage)
        ok = False
        try:
            self.api.post_slides_document_from_template(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_template', 'template_storage', request.template_storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_template', 'template_storage')

    def test_post_slides_document_from_template_invalid_is_image_data_embedded(self):
        """Test case for post_slides_document_from_template with invalid is_image_data_embedded
        """
        request = self.__prepare_post_slides_document_from_template_request()
        request.is_image_data_embedded = self.get_invalid_test_value('post_slides_document_from_template', 'is_image_data_embedded', request.is_image_data_embedded, 'bool')
        self.initialize('post_slides_document_from_template', 'is_image_data_embedded', request.is_image_data_embedded)
        ok = False
        try:
            self.api.post_slides_document_from_template(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_template', 'is_image_data_embedded', request.is_image_data_embedded)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_template', 'is_image_data_embedded')

    def test_post_slides_document_from_template_invalid_password(self):
        """Test case for post_slides_document_from_template with invalid password
        """
        request = self.__prepare_post_slides_document_from_template_request()
        request.password = self.get_invalid_test_value('post_slides_document_from_template', 'password', request.password, 'str')
        self.initialize('post_slides_document_from_template', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_document_from_template(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_template', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_template', 'password')

    def test_post_slides_document_from_template_invalid_storage(self):
        """Test case for post_slides_document_from_template with invalid storage
        """
        request = self.__prepare_post_slides_document_from_template_request()
        request.storage = self.get_invalid_test_value('post_slides_document_from_template', 'storage', request.storage, 'str')
        self.initialize('post_slides_document_from_template', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_document_from_template(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_template', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_template', 'storage')

    def test_post_slides_document_from_template_invalid_folder(self):
        """Test case for post_slides_document_from_template with invalid folder
        """
        request = self.__prepare_post_slides_document_from_template_request()
        request.folder = self.get_invalid_test_value('post_slides_document_from_template', 'folder', request.folder, 'str')
        self.initialize('post_slides_document_from_template', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_document_from_template(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_document_from_template', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_document_from_template', 'folder')

    def __prepare_post_slides_document_from_template_request(self):
        name = self.get_test_value('post_slides_document_from_template', 'name', 'str')
        template_path = self.get_test_value('post_slides_document_from_template', 'template_path', 'str')
        data = self.get_test_value('post_slides_document_from_template', 'data', 'str')
        template_password = self.get_test_value('post_slides_document_from_template', 'template_password', 'str')
        template_storage = self.get_test_value('post_slides_document_from_template', 'template_storage', 'str')
        is_image_data_embedded = self.get_test_value('post_slides_document_from_template', 'is_image_data_embedded', 'bool')
        password = self.get_test_value('post_slides_document_from_template', 'password', 'str')
        storage = self.get_test_value('post_slides_document_from_template', 'storage', 'str')
        folder = self.get_test_value('post_slides_document_from_template', 'folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesDocumentFromTemplateRequest(name, template_path, data, template_password, template_storage, is_image_data_embedded, password, storage, folder)

    def test_post_slides_pipeline(self):
        """Test case for post_slides_pipeline
        """
        request = self.__prepare_post_slides_pipeline_request()
        self.initialize('post_slides_pipeline', None, None)
        response = self.api.post_slides_pipeline(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_post_slides_pipeline_invalid_pipeline(self):
        """Test case for post_slides_pipeline with invalid pipeline
        """
        request = self.__prepare_post_slides_pipeline_request()
        request.pipeline = self.get_invalid_test_value('post_slides_pipeline', 'pipeline', request.pipeline, 'Pipeline')
        self.initialize('post_slides_pipeline', 'pipeline', request.pipeline)
        ok = False
        try:
            self.api.post_slides_pipeline(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_pipeline', 'pipeline', request.pipeline)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_pipeline', 'pipeline')

    def test_post_slides_pipeline_invalid_files(self):
        """Test case for post_slides_pipeline with invalid files
        """
        request = self.__prepare_post_slides_pipeline_request()
        request.files = self.get_invalid_test_value('post_slides_pipeline', 'files', request.files, 'dict')
        self.initialize('post_slides_pipeline', 'files', request.files)
        ok = False
        try:
            self.api.post_slides_pipeline(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_pipeline', 'files', request.files)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_pipeline', 'files')

    def __prepare_post_slides_pipeline_request(self):
        pipeline = self.get_test_value('post_slides_pipeline', 'pipeline', 'Pipeline')
        files = self.get_test_value('post_slides_pipeline', 'files', 'dict')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesPipelineRequest(pipeline, files)

    def test_post_slides_presentation_replace_text(self):
        """Test case for post_slides_presentation_replace_text
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        self.initialize('post_slides_presentation_replace_text', None, None)
        response = self.api.post_slides_presentation_replace_text(request)
        self.assertIsNotNone(response)

    def test_post_slides_presentation_replace_text_invalid_name(self):
        """Test case for post_slides_presentation_replace_text with invalid name
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.name = self.get_invalid_test_value('post_slides_presentation_replace_text', 'name', request.name, 'str')
        self.initialize('post_slides_presentation_replace_text', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'name')

    def test_post_slides_presentation_replace_text_invalid_old_value(self):
        """Test case for post_slides_presentation_replace_text with invalid old_value
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.old_value = self.get_invalid_test_value('post_slides_presentation_replace_text', 'old_value', request.old_value, 'str')
        self.initialize('post_slides_presentation_replace_text', 'old_value', request.old_value)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'old_value', request.old_value)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'old_value')

    def test_post_slides_presentation_replace_text_invalid_new_value(self):
        """Test case for post_slides_presentation_replace_text with invalid new_value
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.new_value = self.get_invalid_test_value('post_slides_presentation_replace_text', 'new_value', request.new_value, 'str')
        self.initialize('post_slides_presentation_replace_text', 'new_value', request.new_value)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'new_value', request.new_value)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'new_value')

    def test_post_slides_presentation_replace_text_invalid_ignore_case(self):
        """Test case for post_slides_presentation_replace_text with invalid ignore_case
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.ignore_case = self.get_invalid_test_value('post_slides_presentation_replace_text', 'ignore_case', request.ignore_case, 'bool')
        self.initialize('post_slides_presentation_replace_text', 'ignore_case', request.ignore_case)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'ignore_case', request.ignore_case)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'ignore_case')

    def test_post_slides_presentation_replace_text_invalid_password(self):
        """Test case for post_slides_presentation_replace_text with invalid password
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.password = self.get_invalid_test_value('post_slides_presentation_replace_text', 'password', request.password, 'str')
        self.initialize('post_slides_presentation_replace_text', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'password')

    def test_post_slides_presentation_replace_text_invalid_folder(self):
        """Test case for post_slides_presentation_replace_text with invalid folder
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.folder = self.get_invalid_test_value('post_slides_presentation_replace_text', 'folder', request.folder, 'str')
        self.initialize('post_slides_presentation_replace_text', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'folder')

    def test_post_slides_presentation_replace_text_invalid_storage(self):
        """Test case for post_slides_presentation_replace_text with invalid storage
        """
        request = self.__prepare_post_slides_presentation_replace_text_request()
        request.storage = self.get_invalid_test_value('post_slides_presentation_replace_text', 'storage', request.storage, 'str')
        self.initialize('post_slides_presentation_replace_text', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_presentation_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_presentation_replace_text', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_presentation_replace_text', 'storage')

    def __prepare_post_slides_presentation_replace_text_request(self):
        name = self.get_test_value('post_slides_presentation_replace_text', 'name', 'str')
        old_value = self.get_test_value('post_slides_presentation_replace_text', 'old_value', 'str')
        new_value = self.get_test_value('post_slides_presentation_replace_text', 'new_value', 'str')
        ignore_case = self.get_test_value('post_slides_presentation_replace_text', 'ignore_case', 'bool')
        password = self.get_test_value('post_slides_presentation_replace_text', 'password', 'str')
        folder = self.get_test_value('post_slides_presentation_replace_text', 'folder', 'str')
        storage = self.get_test_value('post_slides_presentation_replace_text', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesPresentationReplaceTextRequest(name, old_value, new_value, ignore_case, password, folder, storage)

    def test_post_slides_reorder(self):
        """Test case for post_slides_reorder
        """
        request = self.__prepare_post_slides_reorder_request()
        self.initialize('post_slides_reorder', None, None)
        response = self.api.post_slides_reorder(request)
        self.assertIsNotNone(response)

    def test_post_slides_reorder_invalid_name(self):
        """Test case for post_slides_reorder with invalid name
        """
        request = self.__prepare_post_slides_reorder_request()
        request.name = self.get_invalid_test_value('post_slides_reorder', 'name', request.name, 'str')
        self.initialize('post_slides_reorder', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder', 'name')

    def test_post_slides_reorder_invalid_slide_index(self):
        """Test case for post_slides_reorder with invalid slide_index
        """
        request = self.__prepare_post_slides_reorder_request()
        request.slide_index = self.get_invalid_test_value('post_slides_reorder', 'slide_index', request.slide_index, 'int')
        self.initialize('post_slides_reorder', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder', 'slide_index')

    def test_post_slides_reorder_invalid_new_position(self):
        """Test case for post_slides_reorder with invalid new_position
        """
        request = self.__prepare_post_slides_reorder_request()
        request.new_position = self.get_invalid_test_value('post_slides_reorder', 'new_position', request.new_position, 'int')
        self.initialize('post_slides_reorder', 'new_position', request.new_position)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'new_position', request.new_position)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder', 'new_position')

    def test_post_slides_reorder_invalid_password(self):
        """Test case for post_slides_reorder with invalid password
        """
        request = self.__prepare_post_slides_reorder_request()
        request.password = self.get_invalid_test_value('post_slides_reorder', 'password', request.password, 'str')
        self.initialize('post_slides_reorder', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder', 'password')

    def test_post_slides_reorder_invalid_folder(self):
        """Test case for post_slides_reorder with invalid folder
        """
        request = self.__prepare_post_slides_reorder_request()
        request.folder = self.get_invalid_test_value('post_slides_reorder', 'folder', request.folder, 'str')
        self.initialize('post_slides_reorder', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder', 'folder')

    def test_post_slides_reorder_invalid_storage(self):
        """Test case for post_slides_reorder with invalid storage
        """
        request = self.__prepare_post_slides_reorder_request()
        request.storage = self.get_invalid_test_value('post_slides_reorder', 'storage', request.storage, 'str')
        self.initialize('post_slides_reorder', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_reorder(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder', 'storage')

    def __prepare_post_slides_reorder_request(self):
        name = self.get_test_value('post_slides_reorder', 'name', 'str')
        slide_index = self.get_test_value('post_slides_reorder', 'slide_index', 'int')
        new_position = self.get_test_value('post_slides_reorder', 'new_position', 'int')
        password = self.get_test_value('post_slides_reorder', 'password', 'str')
        folder = self.get_test_value('post_slides_reorder', 'folder', 'str')
        storage = self.get_test_value('post_slides_reorder', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesReorderRequest(name, slide_index, new_position, password, folder, storage)

    def test_post_slides_reorder_many(self):
        """Test case for post_slides_reorder_many
        """
        request = self.__prepare_post_slides_reorder_many_request()
        self.initialize('post_slides_reorder_many', None, None)
        response = self.api.post_slides_reorder_many(request)
        self.assertIsNotNone(response)

    def test_post_slides_reorder_many_invalid_name(self):
        """Test case for post_slides_reorder_many with invalid name
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.name = self.get_invalid_test_value('post_slides_reorder_many', 'name', request.name, 'str')
        self.initialize('post_slides_reorder_many', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'name')

    def test_post_slides_reorder_many_invalid_old_positions(self):
        """Test case for post_slides_reorder_many with invalid old_positions
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.old_positions = self.get_invalid_test_value('post_slides_reorder_many', 'old_positions', request.old_positions, 'list[int]')
        self.initialize('post_slides_reorder_many', 'old_positions', request.old_positions)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'old_positions', request.old_positions)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'old_positions')

    def test_post_slides_reorder_many_invalid_new_positions(self):
        """Test case for post_slides_reorder_many with invalid new_positions
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.new_positions = self.get_invalid_test_value('post_slides_reorder_many', 'new_positions', request.new_positions, 'list[int]')
        self.initialize('post_slides_reorder_many', 'new_positions', request.new_positions)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'new_positions', request.new_positions)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'new_positions')

    def test_post_slides_reorder_many_invalid_password(self):
        """Test case for post_slides_reorder_many with invalid password
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.password = self.get_invalid_test_value('post_slides_reorder_many', 'password', request.password, 'str')
        self.initialize('post_slides_reorder_many', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'password')

    def test_post_slides_reorder_many_invalid_folder(self):
        """Test case for post_slides_reorder_many with invalid folder
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.folder = self.get_invalid_test_value('post_slides_reorder_many', 'folder', request.folder, 'str')
        self.initialize('post_slides_reorder_many', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'folder')

    def test_post_slides_reorder_many_invalid_storage(self):
        """Test case for post_slides_reorder_many with invalid storage
        """
        request = self.__prepare_post_slides_reorder_many_request()
        request.storage = self.get_invalid_test_value('post_slides_reorder_many', 'storage', request.storage, 'str')
        self.initialize('post_slides_reorder_many', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_reorder_many(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_reorder_many', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_reorder_many', 'storage')

    def __prepare_post_slides_reorder_many_request(self):
        name = self.get_test_value('post_slides_reorder_many', 'name', 'str')
        old_positions = self.get_test_value('post_slides_reorder_many', 'old_positions', 'list[int]')
        new_positions = self.get_test_value('post_slides_reorder_many', 'new_positions', 'list[int]')
        password = self.get_test_value('post_slides_reorder_many', 'password', 'str')
        folder = self.get_test_value('post_slides_reorder_many', 'folder', 'str')
        storage = self.get_test_value('post_slides_reorder_many', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesReorderManyRequest(name, old_positions, new_positions, password, folder, storage)

    def test_post_slides_save_as(self):
        """Test case for post_slides_save_as
        """
        request = self.__prepare_post_slides_save_as_request()
        self.initialize('post_slides_save_as', None, None)
        response = self.api.post_slides_save_as(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_post_slides_save_as_invalid_name(self):
        """Test case for post_slides_save_as with invalid name
        """
        request = self.__prepare_post_slides_save_as_request()
        request.name = self.get_invalid_test_value('post_slides_save_as', 'name', request.name, 'str')
        self.initialize('post_slides_save_as', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_save_as', 'name')

    def test_post_slides_save_as_invalid_format(self):
        """Test case for post_slides_save_as with invalid format
        """
        request = self.__prepare_post_slides_save_as_request()
        request.format = self.get_invalid_test_value('post_slides_save_as', 'format', request.format, 'str')
        self.initialize('post_slides_save_as', 'format', request.format)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_save_as', 'format')

    def test_post_slides_save_as_invalid_options(self):
        """Test case for post_slides_save_as with invalid options
        """
        request = self.__prepare_post_slides_save_as_request()
        request.options = self.get_invalid_test_value('post_slides_save_as', 'options', request.options, 'ExportOptions')
        self.initialize('post_slides_save_as', 'options', request.options)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_save_as', 'options')

    def test_post_slides_save_as_invalid_password(self):
        """Test case for post_slides_save_as with invalid password
        """
        request = self.__prepare_post_slides_save_as_request()
        request.password = self.get_invalid_test_value('post_slides_save_as', 'password', request.password, 'str')
        self.initialize('post_slides_save_as', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_save_as', 'password')

    def test_post_slides_save_as_invalid_storage(self):
        """Test case for post_slides_save_as with invalid storage
        """
        request = self.__prepare_post_slides_save_as_request()
        request.storage = self.get_invalid_test_value('post_slides_save_as', 'storage', request.storage, 'str')
        self.initialize('post_slides_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_save_as', 'storage')

    def test_post_slides_save_as_invalid_folder(self):
        """Test case for post_slides_save_as with invalid folder
        """
        request = self.__prepare_post_slides_save_as_request()
        request.folder = self.get_invalid_test_value('post_slides_save_as', 'folder', request.folder, 'str')
        self.initialize('post_slides_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_save_as', 'folder')

    def test_post_slides_save_as_invalid_fonts_folder(self):
        """Test case for post_slides_save_as with invalid fonts_folder
        """
        request = self.__prepare_post_slides_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('post_slides_save_as', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_slides_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_save_as', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_save_as', 'fonts_folder')

    def __prepare_post_slides_save_as_request(self):
        name = self.get_test_value('post_slides_save_as', 'name', 'str')
        format = self.get_test_value('post_slides_save_as', 'format', 'str')
        options = self.get_test_value('post_slides_save_as', 'options', 'ExportOptions')
        password = self.get_test_value('post_slides_save_as', 'password', 'str')
        storage = self.get_test_value('post_slides_save_as', 'storage', 'str')
        folder = self.get_test_value('post_slides_save_as', 'folder', 'str')
        fonts_folder = self.get_test_value('post_slides_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesSaveAsRequest(name, format, options, password, storage, folder, fonts_folder)

    def test_post_slides_set_document_properties(self):
        """Test case for post_slides_set_document_properties
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        self.initialize('post_slides_set_document_properties', None, None)
        response = self.api.post_slides_set_document_properties(request)
        self.assertIsNotNone(response)

    def test_post_slides_set_document_properties_invalid_name(self):
        """Test case for post_slides_set_document_properties with invalid name
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        request.name = self.get_invalid_test_value('post_slides_set_document_properties', 'name', request.name, 'str')
        self.initialize('post_slides_set_document_properties', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_set_document_properties', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_set_document_properties', 'name')

    def test_post_slides_set_document_properties_invalid_properties(self):
        """Test case for post_slides_set_document_properties with invalid properties
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        request.properties = self.get_invalid_test_value('post_slides_set_document_properties', 'properties', request.properties, 'DocumentProperties')
        self.initialize('post_slides_set_document_properties', 'properties', request.properties)
        ok = False
        try:
            self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_set_document_properties', 'properties', request.properties)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_set_document_properties', 'properties')

    def test_post_slides_set_document_properties_invalid_password(self):
        """Test case for post_slides_set_document_properties with invalid password
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        request.password = self.get_invalid_test_value('post_slides_set_document_properties', 'password', request.password, 'str')
        self.initialize('post_slides_set_document_properties', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_set_document_properties', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_set_document_properties', 'password')

    def test_post_slides_set_document_properties_invalid_folder(self):
        """Test case for post_slides_set_document_properties with invalid folder
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        request.folder = self.get_invalid_test_value('post_slides_set_document_properties', 'folder', request.folder, 'str')
        self.initialize('post_slides_set_document_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_set_document_properties', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_set_document_properties', 'folder')

    def test_post_slides_set_document_properties_invalid_storage(self):
        """Test case for post_slides_set_document_properties with invalid storage
        """
        request = self.__prepare_post_slides_set_document_properties_request()
        request.storage = self.get_invalid_test_value('post_slides_set_document_properties', 'storage', request.storage, 'str')
        self.initialize('post_slides_set_document_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_set_document_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_set_document_properties', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_set_document_properties', 'storage')

    def __prepare_post_slides_set_document_properties_request(self):
        name = self.get_test_value('post_slides_set_document_properties', 'name', 'str')
        properties = self.get_test_value('post_slides_set_document_properties', 'properties', 'DocumentProperties')
        password = self.get_test_value('post_slides_set_document_properties', 'password', 'str')
        folder = self.get_test_value('post_slides_set_document_properties', 'folder', 'str')
        storage = self.get_test_value('post_slides_set_document_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesSetDocumentPropertiesRequest(name, properties, password, folder, storage)

    def test_post_slides_slide_replace_text(self):
        """Test case for post_slides_slide_replace_text
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        self.initialize('post_slides_slide_replace_text', None, None)
        response = self.api.post_slides_slide_replace_text(request)
        self.assertIsNotNone(response)

    def test_post_slides_slide_replace_text_invalid_name(self):
        """Test case for post_slides_slide_replace_text with invalid name
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.name = self.get_invalid_test_value('post_slides_slide_replace_text', 'name', request.name, 'str')
        self.initialize('post_slides_slide_replace_text', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'name')

    def test_post_slides_slide_replace_text_invalid_slide_index(self):
        """Test case for post_slides_slide_replace_text with invalid slide_index
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.slide_index = self.get_invalid_test_value('post_slides_slide_replace_text', 'slide_index', request.slide_index, 'int')
        self.initialize('post_slides_slide_replace_text', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'slide_index')

    def test_post_slides_slide_replace_text_invalid_old_value(self):
        """Test case for post_slides_slide_replace_text with invalid old_value
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.old_value = self.get_invalid_test_value('post_slides_slide_replace_text', 'old_value', request.old_value, 'str')
        self.initialize('post_slides_slide_replace_text', 'old_value', request.old_value)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'old_value', request.old_value)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'old_value')

    def test_post_slides_slide_replace_text_invalid_new_value(self):
        """Test case for post_slides_slide_replace_text with invalid new_value
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.new_value = self.get_invalid_test_value('post_slides_slide_replace_text', 'new_value', request.new_value, 'str')
        self.initialize('post_slides_slide_replace_text', 'new_value', request.new_value)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'new_value', request.new_value)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'new_value')

    def test_post_slides_slide_replace_text_invalid_ignore_case(self):
        """Test case for post_slides_slide_replace_text with invalid ignore_case
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.ignore_case = self.get_invalid_test_value('post_slides_slide_replace_text', 'ignore_case', request.ignore_case, 'bool')
        self.initialize('post_slides_slide_replace_text', 'ignore_case', request.ignore_case)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'ignore_case', request.ignore_case)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'ignore_case')

    def test_post_slides_slide_replace_text_invalid_password(self):
        """Test case for post_slides_slide_replace_text with invalid password
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.password = self.get_invalid_test_value('post_slides_slide_replace_text', 'password', request.password, 'str')
        self.initialize('post_slides_slide_replace_text', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'password')

    def test_post_slides_slide_replace_text_invalid_folder(self):
        """Test case for post_slides_slide_replace_text with invalid folder
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.folder = self.get_invalid_test_value('post_slides_slide_replace_text', 'folder', request.folder, 'str')
        self.initialize('post_slides_slide_replace_text', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'folder')

    def test_post_slides_slide_replace_text_invalid_storage(self):
        """Test case for post_slides_slide_replace_text with invalid storage
        """
        request = self.__prepare_post_slides_slide_replace_text_request()
        request.storage = self.get_invalid_test_value('post_slides_slide_replace_text', 'storage', request.storage, 'str')
        self.initialize('post_slides_slide_replace_text', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_slide_replace_text(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_slide_replace_text', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_slide_replace_text', 'storage')

    def __prepare_post_slides_slide_replace_text_request(self):
        name = self.get_test_value('post_slides_slide_replace_text', 'name', 'str')
        slide_index = self.get_test_value('post_slides_slide_replace_text', 'slide_index', 'int')
        old_value = self.get_test_value('post_slides_slide_replace_text', 'old_value', 'str')
        new_value = self.get_test_value('post_slides_slide_replace_text', 'new_value', 'str')
        ignore_case = self.get_test_value('post_slides_slide_replace_text', 'ignore_case', 'bool')
        password = self.get_test_value('post_slides_slide_replace_text', 'password', 'str')
        folder = self.get_test_value('post_slides_slide_replace_text', 'folder', 'str')
        storage = self.get_test_value('post_slides_slide_replace_text', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesSlideReplaceTextRequest(name, slide_index, old_value, new_value, ignore_case, password, folder, storage)

    def test_post_slides_split(self):
        """Test case for post_slides_split
        """
        request = self.__prepare_post_slides_split_request()
        self.initialize('post_slides_split', None, None)
        response = self.api.post_slides_split(request)
        self.assertIsNotNone(response)

    def test_post_slides_split_invalid_name(self):
        """Test case for post_slides_split with invalid name
        """
        request = self.__prepare_post_slides_split_request()
        request.name = self.get_invalid_test_value('post_slides_split', 'name', request.name, 'str')
        self.initialize('post_slides_split', 'name', request.name)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'name')

    def test_post_slides_split_invalid_options(self):
        """Test case for post_slides_split with invalid options
        """
        request = self.__prepare_post_slides_split_request()
        request.options = self.get_invalid_test_value('post_slides_split', 'options', request.options, 'ExportOptions')
        self.initialize('post_slides_split', 'options', request.options)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'options')

    def test_post_slides_split_invalid_format(self):
        """Test case for post_slides_split with invalid format
        """
        request = self.__prepare_post_slides_split_request()
        request.format = self.get_invalid_test_value('post_slides_split', 'format', request.format, 'str')
        self.initialize('post_slides_split', 'format', request.format)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'format')

    def test_post_slides_split_invalid_width(self):
        """Test case for post_slides_split with invalid width
        """
        request = self.__prepare_post_slides_split_request()
        request.width = self.get_invalid_test_value('post_slides_split', 'width', request.width, 'int')
        self.initialize('post_slides_split', 'width', request.width)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'width', request.width)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'width')

    def test_post_slides_split_invalid_height(self):
        """Test case for post_slides_split with invalid height
        """
        request = self.__prepare_post_slides_split_request()
        request.height = self.get_invalid_test_value('post_slides_split', 'height', request.height, 'int')
        self.initialize('post_slides_split', 'height', request.height)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'height', request.height)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'height')

    def test_post_slides_split_invalid_to(self):
        """Test case for post_slides_split with invalid to
        """
        request = self.__prepare_post_slides_split_request()
        request.to = self.get_invalid_test_value('post_slides_split', 'to', request.to, 'int')
        self.initialize('post_slides_split', 'to', request.to)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'to', request.to)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'to')

    def test_post_slides_split_invalid__from(self):
        """Test case for post_slides_split with invalid _from
        """
        request = self.__prepare_post_slides_split_request()
        request._from = self.get_invalid_test_value('post_slides_split', '_from', request._from, 'int')
        self.initialize('post_slides_split', '_from', request._from)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', '_from', request._from)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', '_from')

    def test_post_slides_split_invalid_dest_folder(self):
        """Test case for post_slides_split with invalid dest_folder
        """
        request = self.__prepare_post_slides_split_request()
        request.dest_folder = self.get_invalid_test_value('post_slides_split', 'dest_folder', request.dest_folder, 'str')
        self.initialize('post_slides_split', 'dest_folder', request.dest_folder)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'dest_folder', request.dest_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'dest_folder')

    def test_post_slides_split_invalid_password(self):
        """Test case for post_slides_split with invalid password
        """
        request = self.__prepare_post_slides_split_request()
        request.password = self.get_invalid_test_value('post_slides_split', 'password', request.password, 'str')
        self.initialize('post_slides_split', 'password', request.password)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'password')

    def test_post_slides_split_invalid_storage(self):
        """Test case for post_slides_split with invalid storage
        """
        request = self.__prepare_post_slides_split_request()
        request.storage = self.get_invalid_test_value('post_slides_split', 'storage', request.storage, 'str')
        self.initialize('post_slides_split', 'storage', request.storage)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'storage')

    def test_post_slides_split_invalid_folder(self):
        """Test case for post_slides_split with invalid folder
        """
        request = self.__prepare_post_slides_split_request()
        request.folder = self.get_invalid_test_value('post_slides_split', 'folder', request.folder, 'str')
        self.initialize('post_slides_split', 'folder', request.folder)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'folder')

    def test_post_slides_split_invalid_fonts_folder(self):
        """Test case for post_slides_split with invalid fonts_folder
        """
        request = self.__prepare_post_slides_split_request()
        request.fonts_folder = self.get_invalid_test_value('post_slides_split', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_slides_split', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_slides_split(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_slides_split', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_slides_split', 'fonts_folder')

    def __prepare_post_slides_split_request(self):
        name = self.get_test_value('post_slides_split', 'name', 'str')
        options = self.get_test_value('post_slides_split', 'options', 'ExportOptions')
        format = self.get_test_value('post_slides_split', 'format', 'str')
        width = self.get_test_value('post_slides_split', 'width', 'int')
        height = self.get_test_value('post_slides_split', 'height', 'int')
        to = self.get_test_value('post_slides_split', 'to', 'int')
        _from = self.get_test_value('post_slides_split', '_from', 'int')
        dest_folder = self.get_test_value('post_slides_split', 'dest_folder', 'str')
        password = self.get_test_value('post_slides_split', 'password', 'str')
        storage = self.get_test_value('post_slides_split', 'storage', 'str')
        folder = self.get_test_value('post_slides_split', 'folder', 'str')
        fonts_folder = self.get_test_value('post_slides_split', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSlidesSplitRequest(name, options, format, width, height, to, _from, dest_folder, password, storage, folder, fonts_folder)

    def test_post_subshape_save_as(self):
        """Test case for post_subshape_save_as
        """
        request = self.__prepare_post_subshape_save_as_request()
        self.initialize('post_subshape_save_as', None, None)
        response = self.api.post_subshape_save_as(request)
        self.assertTrue(isinstance(response, str))
        self.assertTrue(len(response) > 0)

    def test_post_subshape_save_as_invalid_name(self):
        """Test case for post_subshape_save_as with invalid name
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.name = self.get_invalid_test_value('post_subshape_save_as', 'name', request.name, 'str')
        self.initialize('post_subshape_save_as', 'name', request.name)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'name')

    def test_post_subshape_save_as_invalid_slide_index(self):
        """Test case for post_subshape_save_as with invalid slide_index
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.slide_index = self.get_invalid_test_value('post_subshape_save_as', 'slide_index', request.slide_index, 'int')
        self.initialize('post_subshape_save_as', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'slide_index')

    def test_post_subshape_save_as_invalid_shape_index(self):
        """Test case for post_subshape_save_as with invalid shape_index
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.shape_index = self.get_invalid_test_value('post_subshape_save_as', 'shape_index', request.shape_index, 'int')
        self.initialize('post_subshape_save_as', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'shape_index')

    def test_post_subshape_save_as_invalid_format(self):
        """Test case for post_subshape_save_as with invalid format
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.format = self.get_invalid_test_value('post_subshape_save_as', 'format', request.format, 'str')
        self.initialize('post_subshape_save_as', 'format', request.format)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'format')

    def test_post_subshape_save_as_invalid_path(self):
        """Test case for post_subshape_save_as with invalid path
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.path = self.get_invalid_test_value('post_subshape_save_as', 'path', request.path, 'str')
        self.initialize('post_subshape_save_as', 'path', request.path)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'path')

    def test_post_subshape_save_as_invalid_options(self):
        """Test case for post_subshape_save_as with invalid options
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.options = self.get_invalid_test_value('post_subshape_save_as', 'options', request.options, 'IShapeExportOptions')
        self.initialize('post_subshape_save_as', 'options', request.options)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'options')

    def test_post_subshape_save_as_invalid_password(self):
        """Test case for post_subshape_save_as with invalid password
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.password = self.get_invalid_test_value('post_subshape_save_as', 'password', request.password, 'str')
        self.initialize('post_subshape_save_as', 'password', request.password)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'password')

    def test_post_subshape_save_as_invalid_folder(self):
        """Test case for post_subshape_save_as with invalid folder
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.folder = self.get_invalid_test_value('post_subshape_save_as', 'folder', request.folder, 'str')
        self.initialize('post_subshape_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'folder')

    def test_post_subshape_save_as_invalid_storage(self):
        """Test case for post_subshape_save_as with invalid storage
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.storage = self.get_invalid_test_value('post_subshape_save_as', 'storage', request.storage, 'str')
        self.initialize('post_subshape_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'storage')

    def test_post_subshape_save_as_invalid_scale_x(self):
        """Test case for post_subshape_save_as with invalid scale_x
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.scale_x = self.get_invalid_test_value('post_subshape_save_as', 'scale_x', request.scale_x, 'float')
        self.initialize('post_subshape_save_as', 'scale_x', request.scale_x)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'scale_x', request.scale_x)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'scale_x')

    def test_post_subshape_save_as_invalid_scale_y(self):
        """Test case for post_subshape_save_as with invalid scale_y
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.scale_y = self.get_invalid_test_value('post_subshape_save_as', 'scale_y', request.scale_y, 'float')
        self.initialize('post_subshape_save_as', 'scale_y', request.scale_y)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'scale_y', request.scale_y)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'scale_y')

    def test_post_subshape_save_as_invalid_bounds(self):
        """Test case for post_subshape_save_as with invalid bounds
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.bounds = self.get_invalid_test_value('post_subshape_save_as', 'bounds', request.bounds, 'str')
        self.initialize('post_subshape_save_as', 'bounds', request.bounds)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'bounds', request.bounds)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'bounds')

    def test_post_subshape_save_as_invalid_fonts_folder(self):
        """Test case for post_subshape_save_as with invalid fonts_folder
        """
        request = self.__prepare_post_subshape_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('post_subshape_save_as', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('post_subshape_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.post_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'post_subshape_save_as', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('post_subshape_save_as', 'fonts_folder')

    def __prepare_post_subshape_save_as_request(self):
        name = self.get_test_value('post_subshape_save_as', 'name', 'str')
        slide_index = self.get_test_value('post_subshape_save_as', 'slide_index', 'int')
        shape_index = self.get_test_value('post_subshape_save_as', 'shape_index', 'int')
        format = self.get_test_value('post_subshape_save_as', 'format', 'str')
        path = self.get_test_value('post_subshape_save_as', 'path', 'str')
        options = self.get_test_value('post_subshape_save_as', 'options', 'IShapeExportOptions')
        password = self.get_test_value('post_subshape_save_as', 'password', 'str')
        folder = self.get_test_value('post_subshape_save_as', 'folder', 'str')
        storage = self.get_test_value('post_subshape_save_as', 'storage', 'str')
        scale_x = self.get_test_value('post_subshape_save_as', 'scale_x', 'float')
        scale_y = self.get_test_value('post_subshape_save_as', 'scale_y', 'float')
        bounds = self.get_test_value('post_subshape_save_as', 'bounds', 'str')
        fonts_folder = self.get_test_value('post_subshape_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PostSubshapeSaveAsRequest(name, slide_index, shape_index, format, path, options, password, folder, storage, scale_x, scale_y, bounds, fonts_folder)

    def test_put_layout_slide(self):
        """Test case for put_layout_slide
        """
        request = self.__prepare_put_layout_slide_request()
        self.initialize('put_layout_slide', None, None)
        response = self.api.put_layout_slide(request)
        self.assertIsNotNone(response)

    def test_put_layout_slide_invalid_name(self):
        """Test case for put_layout_slide with invalid name
        """
        request = self.__prepare_put_layout_slide_request()
        request.name = self.get_invalid_test_value('put_layout_slide', 'name', request.name, 'str')
        self.initialize('put_layout_slide', 'name', request.name)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_layout_slide', 'name')

    def test_put_layout_slide_invalid_slide_index(self):
        """Test case for put_layout_slide with invalid slide_index
        """
        request = self.__prepare_put_layout_slide_request()
        request.slide_index = self.get_invalid_test_value('put_layout_slide', 'slide_index', request.slide_index, 'int')
        self.initialize('put_layout_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_layout_slide', 'slide_index')

    def test_put_layout_slide_invalid_slide_dto(self):
        """Test case for put_layout_slide with invalid slide_dto
        """
        request = self.__prepare_put_layout_slide_request()
        request.slide_dto = self.get_invalid_test_value('put_layout_slide', 'slide_dto', request.slide_dto, 'LayoutSlide')
        self.initialize('put_layout_slide', 'slide_dto', request.slide_dto)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'slide_dto', request.slide_dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_layout_slide', 'slide_dto')

    def test_put_layout_slide_invalid_password(self):
        """Test case for put_layout_slide with invalid password
        """
        request = self.__prepare_put_layout_slide_request()
        request.password = self.get_invalid_test_value('put_layout_slide', 'password', request.password, 'str')
        self.initialize('put_layout_slide', 'password', request.password)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_layout_slide', 'password')

    def test_put_layout_slide_invalid_folder(self):
        """Test case for put_layout_slide with invalid folder
        """
        request = self.__prepare_put_layout_slide_request()
        request.folder = self.get_invalid_test_value('put_layout_slide', 'folder', request.folder, 'str')
        self.initialize('put_layout_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_layout_slide', 'folder')

    def test_put_layout_slide_invalid_storage(self):
        """Test case for put_layout_slide with invalid storage
        """
        request = self.__prepare_put_layout_slide_request()
        request.storage = self.get_invalid_test_value('put_layout_slide', 'storage', request.storage, 'str')
        self.initialize('put_layout_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.put_layout_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_layout_slide', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_layout_slide', 'storage')

    def __prepare_put_layout_slide_request(self):
        name = self.get_test_value('put_layout_slide', 'name', 'str')
        slide_index = self.get_test_value('put_layout_slide', 'slide_index', 'int')
        slide_dto = self.get_test_value('put_layout_slide', 'slide_dto', 'LayoutSlide')
        password = self.get_test_value('put_layout_slide', 'password', 'str')
        folder = self.get_test_value('put_layout_slide', 'folder', 'str')
        storage = self.get_test_value('put_layout_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutLayoutSlideRequest(name, slide_index, slide_dto, password, folder, storage)

    def test_put_notes_slide_shape_save_as(self):
        """Test case for put_notes_slide_shape_save_as
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        self.initialize('put_notes_slide_shape_save_as', None, None)
        response = self.api.put_notes_slide_shape_save_as(request)
        self.assertIsNone(response)

    def test_put_notes_slide_shape_save_as_invalid_name(self):
        """Test case for put_notes_slide_shape_save_as with invalid name
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.name = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'name', request.name, 'str')
        self.initialize('put_notes_slide_shape_save_as', 'name', request.name)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'name')

    def test_put_notes_slide_shape_save_as_invalid_slide_index(self):
        """Test case for put_notes_slide_shape_save_as with invalid slide_index
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.slide_index = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'slide_index', request.slide_index, 'int')
        self.initialize('put_notes_slide_shape_save_as', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'slide_index')

    def test_put_notes_slide_shape_save_as_invalid_shape_index(self):
        """Test case for put_notes_slide_shape_save_as with invalid shape_index
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.shape_index = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'shape_index', request.shape_index, 'int')
        self.initialize('put_notes_slide_shape_save_as', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'shape_index')

    def test_put_notes_slide_shape_save_as_invalid_format(self):
        """Test case for put_notes_slide_shape_save_as with invalid format
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.format = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'format', request.format, 'str')
        self.initialize('put_notes_slide_shape_save_as', 'format', request.format)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'format')

    def test_put_notes_slide_shape_save_as_invalid_out_path(self):
        """Test case for put_notes_slide_shape_save_as with invalid out_path
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.out_path = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'out_path', request.out_path, 'str')
        self.initialize('put_notes_slide_shape_save_as', 'out_path', request.out_path)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'out_path', request.out_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'out_path')

    def test_put_notes_slide_shape_save_as_invalid_options(self):
        """Test case for put_notes_slide_shape_save_as with invalid options
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.options = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'options', request.options, 'IShapeExportOptions')
        self.initialize('put_notes_slide_shape_save_as', 'options', request.options)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'options')

    def test_put_notes_slide_shape_save_as_invalid_password(self):
        """Test case for put_notes_slide_shape_save_as with invalid password
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.password = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'password', request.password, 'str')
        self.initialize('put_notes_slide_shape_save_as', 'password', request.password)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'password')

    def test_put_notes_slide_shape_save_as_invalid_folder(self):
        """Test case for put_notes_slide_shape_save_as with invalid folder
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.folder = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'folder', request.folder, 'str')
        self.initialize('put_notes_slide_shape_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'folder')

    def test_put_notes_slide_shape_save_as_invalid_storage(self):
        """Test case for put_notes_slide_shape_save_as with invalid storage
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.storage = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'storage', request.storage, 'str')
        self.initialize('put_notes_slide_shape_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'storage')

    def test_put_notes_slide_shape_save_as_invalid_scale_x(self):
        """Test case for put_notes_slide_shape_save_as with invalid scale_x
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.scale_x = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'scale_x', request.scale_x, 'float')
        self.initialize('put_notes_slide_shape_save_as', 'scale_x', request.scale_x)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'scale_x', request.scale_x)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'scale_x')

    def test_put_notes_slide_shape_save_as_invalid_scale_y(self):
        """Test case for put_notes_slide_shape_save_as with invalid scale_y
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.scale_y = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'scale_y', request.scale_y, 'float')
        self.initialize('put_notes_slide_shape_save_as', 'scale_y', request.scale_y)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'scale_y', request.scale_y)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'scale_y')

    def test_put_notes_slide_shape_save_as_invalid_bounds(self):
        """Test case for put_notes_slide_shape_save_as with invalid bounds
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.bounds = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'bounds', request.bounds, 'str')
        self.initialize('put_notes_slide_shape_save_as', 'bounds', request.bounds)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'bounds', request.bounds)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'bounds')

    def test_put_notes_slide_shape_save_as_invalid_fonts_folder(self):
        """Test case for put_notes_slide_shape_save_as with invalid fonts_folder
        """
        request = self.__prepare_put_notes_slide_shape_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('put_notes_slide_shape_save_as', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('put_notes_slide_shape_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.put_notes_slide_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_notes_slide_shape_save_as', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_notes_slide_shape_save_as', 'fonts_folder')

    def __prepare_put_notes_slide_shape_save_as_request(self):
        name = self.get_test_value('put_notes_slide_shape_save_as', 'name', 'str')
        slide_index = self.get_test_value('put_notes_slide_shape_save_as', 'slide_index', 'int')
        shape_index = self.get_test_value('put_notes_slide_shape_save_as', 'shape_index', 'int')
        format = self.get_test_value('put_notes_slide_shape_save_as', 'format', 'str')
        out_path = self.get_test_value('put_notes_slide_shape_save_as', 'out_path', 'str')
        options = self.get_test_value('put_notes_slide_shape_save_as', 'options', 'IShapeExportOptions')
        password = self.get_test_value('put_notes_slide_shape_save_as', 'password', 'str')
        folder = self.get_test_value('put_notes_slide_shape_save_as', 'folder', 'str')
        storage = self.get_test_value('put_notes_slide_shape_save_as', 'storage', 'str')
        scale_x = self.get_test_value('put_notes_slide_shape_save_as', 'scale_x', 'float')
        scale_y = self.get_test_value('put_notes_slide_shape_save_as', 'scale_y', 'float')
        bounds = self.get_test_value('put_notes_slide_shape_save_as', 'bounds', 'str')
        fonts_folder = self.get_test_value('put_notes_slide_shape_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutNotesSlideShapeSaveAsRequest(name, slide_index, shape_index, format, out_path, options, password, folder, storage, scale_x, scale_y, bounds, fonts_folder)

    def test_put_presentation_merge(self):
        """Test case for put_presentation_merge
        """
        request = self.__prepare_put_presentation_merge_request()
        self.initialize('put_presentation_merge', None, None)
        response = self.api.put_presentation_merge(request)
        self.assertIsNotNone(response)

    def test_put_presentation_merge_invalid_name(self):
        """Test case for put_presentation_merge with invalid name
        """
        request = self.__prepare_put_presentation_merge_request()
        request.name = self.get_invalid_test_value('put_presentation_merge', 'name', request.name, 'str')
        self.initialize('put_presentation_merge', 'name', request.name)
        ok = False
        try:
            self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_presentation_merge', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_presentation_merge', 'name')

    def test_put_presentation_merge_invalid_request(self):
        """Test case for put_presentation_merge with invalid request
        """
        request = self.__prepare_put_presentation_merge_request()
        request.request = self.get_invalid_test_value('put_presentation_merge', 'request', request.request, 'OrderedMergeRequest')
        self.initialize('put_presentation_merge', 'request', request.request)
        ok = False
        try:
            self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_presentation_merge', 'request', request.request)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_presentation_merge', 'request')

    def test_put_presentation_merge_invalid_password(self):
        """Test case for put_presentation_merge with invalid password
        """
        request = self.__prepare_put_presentation_merge_request()
        request.password = self.get_invalid_test_value('put_presentation_merge', 'password', request.password, 'str')
        self.initialize('put_presentation_merge', 'password', request.password)
        ok = False
        try:
            self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_presentation_merge', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_presentation_merge', 'password')

    def test_put_presentation_merge_invalid_storage(self):
        """Test case for put_presentation_merge with invalid storage
        """
        request = self.__prepare_put_presentation_merge_request()
        request.storage = self.get_invalid_test_value('put_presentation_merge', 'storage', request.storage, 'str')
        self.initialize('put_presentation_merge', 'storage', request.storage)
        ok = False
        try:
            self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_presentation_merge', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_presentation_merge', 'storage')

    def test_put_presentation_merge_invalid_folder(self):
        """Test case for put_presentation_merge with invalid folder
        """
        request = self.__prepare_put_presentation_merge_request()
        request.folder = self.get_invalid_test_value('put_presentation_merge', 'folder', request.folder, 'str')
        self.initialize('put_presentation_merge', 'folder', request.folder)
        ok = False
        try:
            self.api.put_presentation_merge(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_presentation_merge', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_presentation_merge', 'folder')

    def __prepare_put_presentation_merge_request(self):
        name = self.get_test_value('put_presentation_merge', 'name', 'str')
        request = self.get_test_value('put_presentation_merge', 'request', 'OrderedMergeRequest')
        password = self.get_test_value('put_presentation_merge', 'password', 'str')
        storage = self.get_test_value('put_presentation_merge', 'storage', 'str')
        folder = self.get_test_value('put_presentation_merge', 'folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutPresentationMergeRequest(name, request, password, storage, folder)

    def test_put_set_paragraph_portion_properties(self):
        """Test case for put_set_paragraph_portion_properties
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        self.initialize('put_set_paragraph_portion_properties', None, None)
        response = self.api.put_set_paragraph_portion_properties(request)
        self.assertIsNotNone(response)

    def test_put_set_paragraph_portion_properties_invalid_name(self):
        """Test case for put_set_paragraph_portion_properties with invalid name
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.name = self.get_invalid_test_value('put_set_paragraph_portion_properties', 'name', request.name, 'str')
        self.initialize('put_set_paragraph_portion_properties', 'name', request.name)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'name')

    def test_put_set_paragraph_portion_properties_invalid_slide_index(self):
        """Test case for put_set_paragraph_portion_properties with invalid slide_index
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.slide_index = self.get_invalid_test_value('put_set_paragraph_portion_properties', 'slide_index', request.slide_index, 'int')
        self.initialize('put_set_paragraph_portion_properties', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'slide_index')

    def test_put_set_paragraph_portion_properties_invalid_shape_index(self):
        """Test case for put_set_paragraph_portion_properties with invalid shape_index
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.shape_index = self.get_invalid_test_value('put_set_paragraph_portion_properties', 'shape_index', request.shape_index, 'int')
        self.initialize('put_set_paragraph_portion_properties', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'shape_index')

    def test_put_set_paragraph_portion_properties_invalid_paragraph_index(self):
        """Test case for put_set_paragraph_portion_properties with invalid paragraph_index
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.paragraph_index = self.get_invalid_test_value('put_set_paragraph_portion_properties', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('put_set_paragraph_portion_properties', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'paragraph_index')

    def test_put_set_paragraph_portion_properties_invalid_portion_index(self):
        """Test case for put_set_paragraph_portion_properties with invalid portion_index
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.portion_index = self.get_invalid_test_value('put_set_paragraph_portion_properties', 'portion_index', request.portion_index, 'int')
        self.initialize('put_set_paragraph_portion_properties', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'portion_index', request.portion_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'portion_index')

    def test_put_set_paragraph_portion_properties_invalid_dto(self):
        """Test case for put_set_paragraph_portion_properties with invalid dto
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.dto = self.get_invalid_test_value('put_set_paragraph_portion_properties', 'dto', request.dto, 'Portion')
        self.initialize('put_set_paragraph_portion_properties', 'dto', request.dto)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'dto')

    def test_put_set_paragraph_portion_properties_invalid_password(self):
        """Test case for put_set_paragraph_portion_properties with invalid password
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.password = self.get_invalid_test_value('put_set_paragraph_portion_properties', 'password', request.password, 'str')
        self.initialize('put_set_paragraph_portion_properties', 'password', request.password)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'password')

    def test_put_set_paragraph_portion_properties_invalid_folder(self):
        """Test case for put_set_paragraph_portion_properties with invalid folder
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.folder = self.get_invalid_test_value('put_set_paragraph_portion_properties', 'folder', request.folder, 'str')
        self.initialize('put_set_paragraph_portion_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'folder')

    def test_put_set_paragraph_portion_properties_invalid_storage(self):
        """Test case for put_set_paragraph_portion_properties with invalid storage
        """
        request = self.__prepare_put_set_paragraph_portion_properties_request()
        request.storage = self.get_invalid_test_value('put_set_paragraph_portion_properties', 'storage', request.storage, 'str')
        self.initialize('put_set_paragraph_portion_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.put_set_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_portion_properties', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_portion_properties', 'storage')

    def __prepare_put_set_paragraph_portion_properties_request(self):
        name = self.get_test_value('put_set_paragraph_portion_properties', 'name', 'str')
        slide_index = self.get_test_value('put_set_paragraph_portion_properties', 'slide_index', 'int')
        shape_index = self.get_test_value('put_set_paragraph_portion_properties', 'shape_index', 'int')
        paragraph_index = self.get_test_value('put_set_paragraph_portion_properties', 'paragraph_index', 'int')
        portion_index = self.get_test_value('put_set_paragraph_portion_properties', 'portion_index', 'int')
        dto = self.get_test_value('put_set_paragraph_portion_properties', 'dto', 'Portion')
        password = self.get_test_value('put_set_paragraph_portion_properties', 'password', 'str')
        folder = self.get_test_value('put_set_paragraph_portion_properties', 'folder', 'str')
        storage = self.get_test_value('put_set_paragraph_portion_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSetParagraphPortionPropertiesRequest(name, slide_index, shape_index, paragraph_index, portion_index, dto, password, folder, storage)

    def test_put_set_paragraph_properties(self):
        """Test case for put_set_paragraph_properties
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        self.initialize('put_set_paragraph_properties', None, None)
        response = self.api.put_set_paragraph_properties(request)
        self.assertIsNotNone(response)

    def test_put_set_paragraph_properties_invalid_name(self):
        """Test case for put_set_paragraph_properties with invalid name
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.name = self.get_invalid_test_value('put_set_paragraph_properties', 'name', request.name, 'str')
        self.initialize('put_set_paragraph_properties', 'name', request.name)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'name')

    def test_put_set_paragraph_properties_invalid_slide_index(self):
        """Test case for put_set_paragraph_properties with invalid slide_index
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.slide_index = self.get_invalid_test_value('put_set_paragraph_properties', 'slide_index', request.slide_index, 'int')
        self.initialize('put_set_paragraph_properties', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'slide_index')

    def test_put_set_paragraph_properties_invalid_shape_index(self):
        """Test case for put_set_paragraph_properties with invalid shape_index
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.shape_index = self.get_invalid_test_value('put_set_paragraph_properties', 'shape_index', request.shape_index, 'int')
        self.initialize('put_set_paragraph_properties', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'shape_index')

    def test_put_set_paragraph_properties_invalid_paragraph_index(self):
        """Test case for put_set_paragraph_properties with invalid paragraph_index
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.paragraph_index = self.get_invalid_test_value('put_set_paragraph_properties', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('put_set_paragraph_properties', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'paragraph_index')

    def test_put_set_paragraph_properties_invalid_dto(self):
        """Test case for put_set_paragraph_properties with invalid dto
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.dto = self.get_invalid_test_value('put_set_paragraph_properties', 'dto', request.dto, 'Paragraph')
        self.initialize('put_set_paragraph_properties', 'dto', request.dto)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'dto')

    def test_put_set_paragraph_properties_invalid_password(self):
        """Test case for put_set_paragraph_properties with invalid password
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.password = self.get_invalid_test_value('put_set_paragraph_properties', 'password', request.password, 'str')
        self.initialize('put_set_paragraph_properties', 'password', request.password)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'password')

    def test_put_set_paragraph_properties_invalid_folder(self):
        """Test case for put_set_paragraph_properties with invalid folder
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.folder = self.get_invalid_test_value('put_set_paragraph_properties', 'folder', request.folder, 'str')
        self.initialize('put_set_paragraph_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'folder')

    def test_put_set_paragraph_properties_invalid_storage(self):
        """Test case for put_set_paragraph_properties with invalid storage
        """
        request = self.__prepare_put_set_paragraph_properties_request()
        request.storage = self.get_invalid_test_value('put_set_paragraph_properties', 'storage', request.storage, 'str')
        self.initialize('put_set_paragraph_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.put_set_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_paragraph_properties', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_paragraph_properties', 'storage')

    def __prepare_put_set_paragraph_properties_request(self):
        name = self.get_test_value('put_set_paragraph_properties', 'name', 'str')
        slide_index = self.get_test_value('put_set_paragraph_properties', 'slide_index', 'int')
        shape_index = self.get_test_value('put_set_paragraph_properties', 'shape_index', 'int')
        paragraph_index = self.get_test_value('put_set_paragraph_properties', 'paragraph_index', 'int')
        dto = self.get_test_value('put_set_paragraph_properties', 'dto', 'Paragraph')
        password = self.get_test_value('put_set_paragraph_properties', 'password', 'str')
        folder = self.get_test_value('put_set_paragraph_properties', 'folder', 'str')
        storage = self.get_test_value('put_set_paragraph_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSetParagraphPropertiesRequest(name, slide_index, shape_index, paragraph_index, dto, password, folder, storage)

    def test_put_set_subshape_paragraph_portion_properties(self):
        """Test case for put_set_subshape_paragraph_portion_properties
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        self.initialize('put_set_subshape_paragraph_portion_properties', None, None)
        response = self.api.put_set_subshape_paragraph_portion_properties(request)
        self.assertIsNotNone(response)

    def test_put_set_subshape_paragraph_portion_properties_invalid_name(self):
        """Test case for put_set_subshape_paragraph_portion_properties with invalid name
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        request.name = self.get_invalid_test_value('put_set_subshape_paragraph_portion_properties', 'name', request.name, 'str')
        self.initialize('put_set_subshape_paragraph_portion_properties', 'name', request.name)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_portion_properties', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_portion_properties', 'name')

    def test_put_set_subshape_paragraph_portion_properties_invalid_slide_index(self):
        """Test case for put_set_subshape_paragraph_portion_properties with invalid slide_index
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        request.slide_index = self.get_invalid_test_value('put_set_subshape_paragraph_portion_properties', 'slide_index', request.slide_index, 'int')
        self.initialize('put_set_subshape_paragraph_portion_properties', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_portion_properties', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_portion_properties', 'slide_index')

    def test_put_set_subshape_paragraph_portion_properties_invalid_shape_index(self):
        """Test case for put_set_subshape_paragraph_portion_properties with invalid shape_index
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        request.shape_index = self.get_invalid_test_value('put_set_subshape_paragraph_portion_properties', 'shape_index', request.shape_index, 'int')
        self.initialize('put_set_subshape_paragraph_portion_properties', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_portion_properties', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_portion_properties', 'shape_index')

    def test_put_set_subshape_paragraph_portion_properties_invalid_paragraph_index(self):
        """Test case for put_set_subshape_paragraph_portion_properties with invalid paragraph_index
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        request.paragraph_index = self.get_invalid_test_value('put_set_subshape_paragraph_portion_properties', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('put_set_subshape_paragraph_portion_properties', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_portion_properties', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_portion_properties', 'paragraph_index')

    def test_put_set_subshape_paragraph_portion_properties_invalid_portion_index(self):
        """Test case for put_set_subshape_paragraph_portion_properties with invalid portion_index
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        request.portion_index = self.get_invalid_test_value('put_set_subshape_paragraph_portion_properties', 'portion_index', request.portion_index, 'int')
        self.initialize('put_set_subshape_paragraph_portion_properties', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_portion_properties', 'portion_index', request.portion_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_portion_properties', 'portion_index')

    def test_put_set_subshape_paragraph_portion_properties_invalid_path(self):
        """Test case for put_set_subshape_paragraph_portion_properties with invalid path
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        request.path = self.get_invalid_test_value('put_set_subshape_paragraph_portion_properties', 'path', request.path, 'str')
        self.initialize('put_set_subshape_paragraph_portion_properties', 'path', request.path)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_portion_properties', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_portion_properties', 'path')

    def test_put_set_subshape_paragraph_portion_properties_invalid_dto(self):
        """Test case for put_set_subshape_paragraph_portion_properties with invalid dto
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        request.dto = self.get_invalid_test_value('put_set_subshape_paragraph_portion_properties', 'dto', request.dto, 'Portion')
        self.initialize('put_set_subshape_paragraph_portion_properties', 'dto', request.dto)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_portion_properties', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_portion_properties', 'dto')

    def test_put_set_subshape_paragraph_portion_properties_invalid_password(self):
        """Test case for put_set_subshape_paragraph_portion_properties with invalid password
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        request.password = self.get_invalid_test_value('put_set_subshape_paragraph_portion_properties', 'password', request.password, 'str')
        self.initialize('put_set_subshape_paragraph_portion_properties', 'password', request.password)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_portion_properties', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_portion_properties', 'password')

    def test_put_set_subshape_paragraph_portion_properties_invalid_folder(self):
        """Test case for put_set_subshape_paragraph_portion_properties with invalid folder
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        request.folder = self.get_invalid_test_value('put_set_subshape_paragraph_portion_properties', 'folder', request.folder, 'str')
        self.initialize('put_set_subshape_paragraph_portion_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_portion_properties', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_portion_properties', 'folder')

    def test_put_set_subshape_paragraph_portion_properties_invalid_storage(self):
        """Test case for put_set_subshape_paragraph_portion_properties with invalid storage
        """
        request = self.__prepare_put_set_subshape_paragraph_portion_properties_request()
        request.storage = self.get_invalid_test_value('put_set_subshape_paragraph_portion_properties', 'storage', request.storage, 'str')
        self.initialize('put_set_subshape_paragraph_portion_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_portion_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_portion_properties', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_portion_properties', 'storage')

    def __prepare_put_set_subshape_paragraph_portion_properties_request(self):
        name = self.get_test_value('put_set_subshape_paragraph_portion_properties', 'name', 'str')
        slide_index = self.get_test_value('put_set_subshape_paragraph_portion_properties', 'slide_index', 'int')
        shape_index = self.get_test_value('put_set_subshape_paragraph_portion_properties', 'shape_index', 'int')
        paragraph_index = self.get_test_value('put_set_subshape_paragraph_portion_properties', 'paragraph_index', 'int')
        portion_index = self.get_test_value('put_set_subshape_paragraph_portion_properties', 'portion_index', 'int')
        path = self.get_test_value('put_set_subshape_paragraph_portion_properties', 'path', 'str')
        dto = self.get_test_value('put_set_subshape_paragraph_portion_properties', 'dto', 'Portion')
        password = self.get_test_value('put_set_subshape_paragraph_portion_properties', 'password', 'str')
        folder = self.get_test_value('put_set_subshape_paragraph_portion_properties', 'folder', 'str')
        storage = self.get_test_value('put_set_subshape_paragraph_portion_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSetSubshapeParagraphPortionPropertiesRequest(name, slide_index, shape_index, paragraph_index, portion_index, path, dto, password, folder, storage)

    def test_put_set_subshape_paragraph_properties(self):
        """Test case for put_set_subshape_paragraph_properties
        """
        request = self.__prepare_put_set_subshape_paragraph_properties_request()
        self.initialize('put_set_subshape_paragraph_properties', None, None)
        response = self.api.put_set_subshape_paragraph_properties(request)
        self.assertIsNotNone(response)

    def test_put_set_subshape_paragraph_properties_invalid_name(self):
        """Test case for put_set_subshape_paragraph_properties with invalid name
        """
        request = self.__prepare_put_set_subshape_paragraph_properties_request()
        request.name = self.get_invalid_test_value('put_set_subshape_paragraph_properties', 'name', request.name, 'str')
        self.initialize('put_set_subshape_paragraph_properties', 'name', request.name)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_properties', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_properties', 'name')

    def test_put_set_subshape_paragraph_properties_invalid_slide_index(self):
        """Test case for put_set_subshape_paragraph_properties with invalid slide_index
        """
        request = self.__prepare_put_set_subshape_paragraph_properties_request()
        request.slide_index = self.get_invalid_test_value('put_set_subshape_paragraph_properties', 'slide_index', request.slide_index, 'int')
        self.initialize('put_set_subshape_paragraph_properties', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_properties', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_properties', 'slide_index')

    def test_put_set_subshape_paragraph_properties_invalid_shape_index(self):
        """Test case for put_set_subshape_paragraph_properties with invalid shape_index
        """
        request = self.__prepare_put_set_subshape_paragraph_properties_request()
        request.shape_index = self.get_invalid_test_value('put_set_subshape_paragraph_properties', 'shape_index', request.shape_index, 'int')
        self.initialize('put_set_subshape_paragraph_properties', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_properties', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_properties', 'shape_index')

    def test_put_set_subshape_paragraph_properties_invalid_paragraph_index(self):
        """Test case for put_set_subshape_paragraph_properties with invalid paragraph_index
        """
        request = self.__prepare_put_set_subshape_paragraph_properties_request()
        request.paragraph_index = self.get_invalid_test_value('put_set_subshape_paragraph_properties', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('put_set_subshape_paragraph_properties', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_properties', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_properties', 'paragraph_index')

    def test_put_set_subshape_paragraph_properties_invalid_path(self):
        """Test case for put_set_subshape_paragraph_properties with invalid path
        """
        request = self.__prepare_put_set_subshape_paragraph_properties_request()
        request.path = self.get_invalid_test_value('put_set_subshape_paragraph_properties', 'path', request.path, 'str')
        self.initialize('put_set_subshape_paragraph_properties', 'path', request.path)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_properties', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_properties', 'path')

    def test_put_set_subshape_paragraph_properties_invalid_dto(self):
        """Test case for put_set_subshape_paragraph_properties with invalid dto
        """
        request = self.__prepare_put_set_subshape_paragraph_properties_request()
        request.dto = self.get_invalid_test_value('put_set_subshape_paragraph_properties', 'dto', request.dto, 'Paragraph')
        self.initialize('put_set_subshape_paragraph_properties', 'dto', request.dto)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_properties', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_properties', 'dto')

    def test_put_set_subshape_paragraph_properties_invalid_password(self):
        """Test case for put_set_subshape_paragraph_properties with invalid password
        """
        request = self.__prepare_put_set_subshape_paragraph_properties_request()
        request.password = self.get_invalid_test_value('put_set_subshape_paragraph_properties', 'password', request.password, 'str')
        self.initialize('put_set_subshape_paragraph_properties', 'password', request.password)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_properties', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_properties', 'password')

    def test_put_set_subshape_paragraph_properties_invalid_folder(self):
        """Test case for put_set_subshape_paragraph_properties with invalid folder
        """
        request = self.__prepare_put_set_subshape_paragraph_properties_request()
        request.folder = self.get_invalid_test_value('put_set_subshape_paragraph_properties', 'folder', request.folder, 'str')
        self.initialize('put_set_subshape_paragraph_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_properties', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_properties', 'folder')

    def test_put_set_subshape_paragraph_properties_invalid_storage(self):
        """Test case for put_set_subshape_paragraph_properties with invalid storage
        """
        request = self.__prepare_put_set_subshape_paragraph_properties_request()
        request.storage = self.get_invalid_test_value('put_set_subshape_paragraph_properties', 'storage', request.storage, 'str')
        self.initialize('put_set_subshape_paragraph_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.put_set_subshape_paragraph_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_set_subshape_paragraph_properties', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_set_subshape_paragraph_properties', 'storage')

    def __prepare_put_set_subshape_paragraph_properties_request(self):
        name = self.get_test_value('put_set_subshape_paragraph_properties', 'name', 'str')
        slide_index = self.get_test_value('put_set_subshape_paragraph_properties', 'slide_index', 'int')
        shape_index = self.get_test_value('put_set_subshape_paragraph_properties', 'shape_index', 'int')
        paragraph_index = self.get_test_value('put_set_subshape_paragraph_properties', 'paragraph_index', 'int')
        path = self.get_test_value('put_set_subshape_paragraph_properties', 'path', 'str')
        dto = self.get_test_value('put_set_subshape_paragraph_properties', 'dto', 'Paragraph')
        password = self.get_test_value('put_set_subshape_paragraph_properties', 'password', 'str')
        folder = self.get_test_value('put_set_subshape_paragraph_properties', 'folder', 'str')
        storage = self.get_test_value('put_set_subshape_paragraph_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSetSubshapeParagraphPropertiesRequest(name, slide_index, shape_index, paragraph_index, path, dto, password, folder, storage)

    def test_put_shape_save_as(self):
        """Test case for put_shape_save_as
        """
        request = self.__prepare_put_shape_save_as_request()
        self.initialize('put_shape_save_as', None, None)
        response = self.api.put_shape_save_as(request)
        self.assertIsNone(response)

    def test_put_shape_save_as_invalid_name(self):
        """Test case for put_shape_save_as with invalid name
        """
        request = self.__prepare_put_shape_save_as_request()
        request.name = self.get_invalid_test_value('put_shape_save_as', 'name', request.name, 'str')
        self.initialize('put_shape_save_as', 'name', request.name)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'name')

    def test_put_shape_save_as_invalid_slide_index(self):
        """Test case for put_shape_save_as with invalid slide_index
        """
        request = self.__prepare_put_shape_save_as_request()
        request.slide_index = self.get_invalid_test_value('put_shape_save_as', 'slide_index', request.slide_index, 'int')
        self.initialize('put_shape_save_as', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'slide_index')

    def test_put_shape_save_as_invalid_shape_index(self):
        """Test case for put_shape_save_as with invalid shape_index
        """
        request = self.__prepare_put_shape_save_as_request()
        request.shape_index = self.get_invalid_test_value('put_shape_save_as', 'shape_index', request.shape_index, 'int')
        self.initialize('put_shape_save_as', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'shape_index')

    def test_put_shape_save_as_invalid_format(self):
        """Test case for put_shape_save_as with invalid format
        """
        request = self.__prepare_put_shape_save_as_request()
        request.format = self.get_invalid_test_value('put_shape_save_as', 'format', request.format, 'str')
        self.initialize('put_shape_save_as', 'format', request.format)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'format')

    def test_put_shape_save_as_invalid_out_path(self):
        """Test case for put_shape_save_as with invalid out_path
        """
        request = self.__prepare_put_shape_save_as_request()
        request.out_path = self.get_invalid_test_value('put_shape_save_as', 'out_path', request.out_path, 'str')
        self.initialize('put_shape_save_as', 'out_path', request.out_path)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'out_path', request.out_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'out_path')

    def test_put_shape_save_as_invalid_options(self):
        """Test case for put_shape_save_as with invalid options
        """
        request = self.__prepare_put_shape_save_as_request()
        request.options = self.get_invalid_test_value('put_shape_save_as', 'options', request.options, 'IShapeExportOptions')
        self.initialize('put_shape_save_as', 'options', request.options)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'options')

    def test_put_shape_save_as_invalid_password(self):
        """Test case for put_shape_save_as with invalid password
        """
        request = self.__prepare_put_shape_save_as_request()
        request.password = self.get_invalid_test_value('put_shape_save_as', 'password', request.password, 'str')
        self.initialize('put_shape_save_as', 'password', request.password)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'password')

    def test_put_shape_save_as_invalid_folder(self):
        """Test case for put_shape_save_as with invalid folder
        """
        request = self.__prepare_put_shape_save_as_request()
        request.folder = self.get_invalid_test_value('put_shape_save_as', 'folder', request.folder, 'str')
        self.initialize('put_shape_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'folder')

    def test_put_shape_save_as_invalid_storage(self):
        """Test case for put_shape_save_as with invalid storage
        """
        request = self.__prepare_put_shape_save_as_request()
        request.storage = self.get_invalid_test_value('put_shape_save_as', 'storage', request.storage, 'str')
        self.initialize('put_shape_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'storage')

    def test_put_shape_save_as_invalid_scale_x(self):
        """Test case for put_shape_save_as with invalid scale_x
        """
        request = self.__prepare_put_shape_save_as_request()
        request.scale_x = self.get_invalid_test_value('put_shape_save_as', 'scale_x', request.scale_x, 'float')
        self.initialize('put_shape_save_as', 'scale_x', request.scale_x)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'scale_x', request.scale_x)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'scale_x')

    def test_put_shape_save_as_invalid_scale_y(self):
        """Test case for put_shape_save_as with invalid scale_y
        """
        request = self.__prepare_put_shape_save_as_request()
        request.scale_y = self.get_invalid_test_value('put_shape_save_as', 'scale_y', request.scale_y, 'float')
        self.initialize('put_shape_save_as', 'scale_y', request.scale_y)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'scale_y', request.scale_y)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'scale_y')

    def test_put_shape_save_as_invalid_bounds(self):
        """Test case for put_shape_save_as with invalid bounds
        """
        request = self.__prepare_put_shape_save_as_request()
        request.bounds = self.get_invalid_test_value('put_shape_save_as', 'bounds', request.bounds, 'str')
        self.initialize('put_shape_save_as', 'bounds', request.bounds)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'bounds', request.bounds)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'bounds')

    def test_put_shape_save_as_invalid_fonts_folder(self):
        """Test case for put_shape_save_as with invalid fonts_folder
        """
        request = self.__prepare_put_shape_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('put_shape_save_as', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('put_shape_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.put_shape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_shape_save_as', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_shape_save_as', 'fonts_folder')

    def __prepare_put_shape_save_as_request(self):
        name = self.get_test_value('put_shape_save_as', 'name', 'str')
        slide_index = self.get_test_value('put_shape_save_as', 'slide_index', 'int')
        shape_index = self.get_test_value('put_shape_save_as', 'shape_index', 'int')
        format = self.get_test_value('put_shape_save_as', 'format', 'str')
        out_path = self.get_test_value('put_shape_save_as', 'out_path', 'str')
        options = self.get_test_value('put_shape_save_as', 'options', 'IShapeExportOptions')
        password = self.get_test_value('put_shape_save_as', 'password', 'str')
        folder = self.get_test_value('put_shape_save_as', 'folder', 'str')
        storage = self.get_test_value('put_shape_save_as', 'storage', 'str')
        scale_x = self.get_test_value('put_shape_save_as', 'scale_x', 'float')
        scale_y = self.get_test_value('put_shape_save_as', 'scale_y', 'float')
        bounds = self.get_test_value('put_shape_save_as', 'bounds', 'str')
        fonts_folder = self.get_test_value('put_shape_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutShapeSaveAsRequest(name, slide_index, shape_index, format, out_path, options, password, folder, storage, scale_x, scale_y, bounds, fonts_folder)

    def test_put_slide_animation(self):
        """Test case for put_slide_animation
        """
        request = self.__prepare_put_slide_animation_request()
        self.initialize('put_slide_animation', None, None)
        response = self.api.put_slide_animation(request)
        self.assertIsNotNone(response)

    def test_put_slide_animation_invalid_name(self):
        """Test case for put_slide_animation with invalid name
        """
        request = self.__prepare_put_slide_animation_request()
        request.name = self.get_invalid_test_value('put_slide_animation', 'name', request.name, 'str')
        self.initialize('put_slide_animation', 'name', request.name)
        ok = False
        try:
            self.api.put_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation', 'name')

    def test_put_slide_animation_invalid_slide_index(self):
        """Test case for put_slide_animation with invalid slide_index
        """
        request = self.__prepare_put_slide_animation_request()
        request.slide_index = self.get_invalid_test_value('put_slide_animation', 'slide_index', request.slide_index, 'int')
        self.initialize('put_slide_animation', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation', 'slide_index')

    def test_put_slide_animation_invalid_animation(self):
        """Test case for put_slide_animation with invalid animation
        """
        request = self.__prepare_put_slide_animation_request()
        request.animation = self.get_invalid_test_value('put_slide_animation', 'animation', request.animation, 'SlideAnimation')
        self.initialize('put_slide_animation', 'animation', request.animation)
        ok = False
        try:
            self.api.put_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation', 'animation', request.animation)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation', 'animation')

    def test_put_slide_animation_invalid_password(self):
        """Test case for put_slide_animation with invalid password
        """
        request = self.__prepare_put_slide_animation_request()
        request.password = self.get_invalid_test_value('put_slide_animation', 'password', request.password, 'str')
        self.initialize('put_slide_animation', 'password', request.password)
        ok = False
        try:
            self.api.put_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation', 'password')

    def test_put_slide_animation_invalid_folder(self):
        """Test case for put_slide_animation with invalid folder
        """
        request = self.__prepare_put_slide_animation_request()
        request.folder = self.get_invalid_test_value('put_slide_animation', 'folder', request.folder, 'str')
        self.initialize('put_slide_animation', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation', 'folder')

    def test_put_slide_animation_invalid_storage(self):
        """Test case for put_slide_animation with invalid storage
        """
        request = self.__prepare_put_slide_animation_request()
        request.storage = self.get_invalid_test_value('put_slide_animation', 'storage', request.storage, 'str')
        self.initialize('put_slide_animation', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slide_animation(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation', 'storage')

    def __prepare_put_slide_animation_request(self):
        name = self.get_test_value('put_slide_animation', 'name', 'str')
        slide_index = self.get_test_value('put_slide_animation', 'slide_index', 'int')
        animation = self.get_test_value('put_slide_animation', 'animation', 'SlideAnimation')
        password = self.get_test_value('put_slide_animation', 'password', 'str')
        folder = self.get_test_value('put_slide_animation', 'folder', 'str')
        storage = self.get_test_value('put_slide_animation', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlideAnimationRequest(name, slide_index, animation, password, folder, storage)

    def test_put_slide_animation_effect(self):
        """Test case for put_slide_animation_effect
        """
        request = self.__prepare_put_slide_animation_effect_request()
        self.initialize('put_slide_animation_effect', None, None)
        response = self.api.put_slide_animation_effect(request)
        self.assertIsNotNone(response)

    def test_put_slide_animation_effect_invalid_name(self):
        """Test case for put_slide_animation_effect with invalid name
        """
        request = self.__prepare_put_slide_animation_effect_request()
        request.name = self.get_invalid_test_value('put_slide_animation_effect', 'name', request.name, 'str')
        self.initialize('put_slide_animation_effect', 'name', request.name)
        ok = False
        try:
            self.api.put_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_effect', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_effect', 'name')

    def test_put_slide_animation_effect_invalid_slide_index(self):
        """Test case for put_slide_animation_effect with invalid slide_index
        """
        request = self.__prepare_put_slide_animation_effect_request()
        request.slide_index = self.get_invalid_test_value('put_slide_animation_effect', 'slide_index', request.slide_index, 'int')
        self.initialize('put_slide_animation_effect', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_effect', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_effect', 'slide_index')

    def test_put_slide_animation_effect_invalid_effect_index(self):
        """Test case for put_slide_animation_effect with invalid effect_index
        """
        request = self.__prepare_put_slide_animation_effect_request()
        request.effect_index = self.get_invalid_test_value('put_slide_animation_effect', 'effect_index', request.effect_index, 'int')
        self.initialize('put_slide_animation_effect', 'effect_index', request.effect_index)
        ok = False
        try:
            self.api.put_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_effect', 'effect_index', request.effect_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_effect', 'effect_index')

    def test_put_slide_animation_effect_invalid_effect(self):
        """Test case for put_slide_animation_effect with invalid effect
        """
        request = self.__prepare_put_slide_animation_effect_request()
        request.effect = self.get_invalid_test_value('put_slide_animation_effect', 'effect', request.effect, 'Effect')
        self.initialize('put_slide_animation_effect', 'effect', request.effect)
        ok = False
        try:
            self.api.put_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_effect', 'effect', request.effect)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_effect', 'effect')

    def test_put_slide_animation_effect_invalid_password(self):
        """Test case for put_slide_animation_effect with invalid password
        """
        request = self.__prepare_put_slide_animation_effect_request()
        request.password = self.get_invalid_test_value('put_slide_animation_effect', 'password', request.password, 'str')
        self.initialize('put_slide_animation_effect', 'password', request.password)
        ok = False
        try:
            self.api.put_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_effect', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_effect', 'password')

    def test_put_slide_animation_effect_invalid_folder(self):
        """Test case for put_slide_animation_effect with invalid folder
        """
        request = self.__prepare_put_slide_animation_effect_request()
        request.folder = self.get_invalid_test_value('put_slide_animation_effect', 'folder', request.folder, 'str')
        self.initialize('put_slide_animation_effect', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_effect', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_effect', 'folder')

    def test_put_slide_animation_effect_invalid_storage(self):
        """Test case for put_slide_animation_effect with invalid storage
        """
        request = self.__prepare_put_slide_animation_effect_request()
        request.storage = self.get_invalid_test_value('put_slide_animation_effect', 'storage', request.storage, 'str')
        self.initialize('put_slide_animation_effect', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slide_animation_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_effect', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_effect', 'storage')

    def __prepare_put_slide_animation_effect_request(self):
        name = self.get_test_value('put_slide_animation_effect', 'name', 'str')
        slide_index = self.get_test_value('put_slide_animation_effect', 'slide_index', 'int')
        effect_index = self.get_test_value('put_slide_animation_effect', 'effect_index', 'int')
        effect = self.get_test_value('put_slide_animation_effect', 'effect', 'Effect')
        password = self.get_test_value('put_slide_animation_effect', 'password', 'str')
        folder = self.get_test_value('put_slide_animation_effect', 'folder', 'str')
        storage = self.get_test_value('put_slide_animation_effect', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlideAnimationEffectRequest(name, slide_index, effect_index, effect, password, folder, storage)

    def test_put_slide_animation_interactive_sequence_effect(self):
        """Test case for put_slide_animation_interactive_sequence_effect
        """
        request = self.__prepare_put_slide_animation_interactive_sequence_effect_request()
        self.initialize('put_slide_animation_interactive_sequence_effect', None, None)
        response = self.api.put_slide_animation_interactive_sequence_effect(request)
        self.assertIsNotNone(response)

    def test_put_slide_animation_interactive_sequence_effect_invalid_name(self):
        """Test case for put_slide_animation_interactive_sequence_effect with invalid name
        """
        request = self.__prepare_put_slide_animation_interactive_sequence_effect_request()
        request.name = self.get_invalid_test_value('put_slide_animation_interactive_sequence_effect', 'name', request.name, 'str')
        self.initialize('put_slide_animation_interactive_sequence_effect', 'name', request.name)
        ok = False
        try:
            self.api.put_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_interactive_sequence_effect', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_interactive_sequence_effect', 'name')

    def test_put_slide_animation_interactive_sequence_effect_invalid_slide_index(self):
        """Test case for put_slide_animation_interactive_sequence_effect with invalid slide_index
        """
        request = self.__prepare_put_slide_animation_interactive_sequence_effect_request()
        request.slide_index = self.get_invalid_test_value('put_slide_animation_interactive_sequence_effect', 'slide_index', request.slide_index, 'int')
        self.initialize('put_slide_animation_interactive_sequence_effect', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_interactive_sequence_effect', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_interactive_sequence_effect', 'slide_index')

    def test_put_slide_animation_interactive_sequence_effect_invalid_sequence_index(self):
        """Test case for put_slide_animation_interactive_sequence_effect with invalid sequence_index
        """
        request = self.__prepare_put_slide_animation_interactive_sequence_effect_request()
        request.sequence_index = self.get_invalid_test_value('put_slide_animation_interactive_sequence_effect', 'sequence_index', request.sequence_index, 'int')
        self.initialize('put_slide_animation_interactive_sequence_effect', 'sequence_index', request.sequence_index)
        ok = False
        try:
            self.api.put_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_interactive_sequence_effect', 'sequence_index', request.sequence_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_interactive_sequence_effect', 'sequence_index')

    def test_put_slide_animation_interactive_sequence_effect_invalid_effect_index(self):
        """Test case for put_slide_animation_interactive_sequence_effect with invalid effect_index
        """
        request = self.__prepare_put_slide_animation_interactive_sequence_effect_request()
        request.effect_index = self.get_invalid_test_value('put_slide_animation_interactive_sequence_effect', 'effect_index', request.effect_index, 'int')
        self.initialize('put_slide_animation_interactive_sequence_effect', 'effect_index', request.effect_index)
        ok = False
        try:
            self.api.put_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_interactive_sequence_effect', 'effect_index', request.effect_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_interactive_sequence_effect', 'effect_index')

    def test_put_slide_animation_interactive_sequence_effect_invalid_effect(self):
        """Test case for put_slide_animation_interactive_sequence_effect with invalid effect
        """
        request = self.__prepare_put_slide_animation_interactive_sequence_effect_request()
        request.effect = self.get_invalid_test_value('put_slide_animation_interactive_sequence_effect', 'effect', request.effect, 'Effect')
        self.initialize('put_slide_animation_interactive_sequence_effect', 'effect', request.effect)
        ok = False
        try:
            self.api.put_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_interactive_sequence_effect', 'effect', request.effect)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_interactive_sequence_effect', 'effect')

    def test_put_slide_animation_interactive_sequence_effect_invalid_password(self):
        """Test case for put_slide_animation_interactive_sequence_effect with invalid password
        """
        request = self.__prepare_put_slide_animation_interactive_sequence_effect_request()
        request.password = self.get_invalid_test_value('put_slide_animation_interactive_sequence_effect', 'password', request.password, 'str')
        self.initialize('put_slide_animation_interactive_sequence_effect', 'password', request.password)
        ok = False
        try:
            self.api.put_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_interactive_sequence_effect', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_interactive_sequence_effect', 'password')

    def test_put_slide_animation_interactive_sequence_effect_invalid_folder(self):
        """Test case for put_slide_animation_interactive_sequence_effect with invalid folder
        """
        request = self.__prepare_put_slide_animation_interactive_sequence_effect_request()
        request.folder = self.get_invalid_test_value('put_slide_animation_interactive_sequence_effect', 'folder', request.folder, 'str')
        self.initialize('put_slide_animation_interactive_sequence_effect', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_interactive_sequence_effect', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_interactive_sequence_effect', 'folder')

    def test_put_slide_animation_interactive_sequence_effect_invalid_storage(self):
        """Test case for put_slide_animation_interactive_sequence_effect with invalid storage
        """
        request = self.__prepare_put_slide_animation_interactive_sequence_effect_request()
        request.storage = self.get_invalid_test_value('put_slide_animation_interactive_sequence_effect', 'storage', request.storage, 'str')
        self.initialize('put_slide_animation_interactive_sequence_effect', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slide_animation_interactive_sequence_effect(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_animation_interactive_sequence_effect', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_animation_interactive_sequence_effect', 'storage')

    def __prepare_put_slide_animation_interactive_sequence_effect_request(self):
        name = self.get_test_value('put_slide_animation_interactive_sequence_effect', 'name', 'str')
        slide_index = self.get_test_value('put_slide_animation_interactive_sequence_effect', 'slide_index', 'int')
        sequence_index = self.get_test_value('put_slide_animation_interactive_sequence_effect', 'sequence_index', 'int')
        effect_index = self.get_test_value('put_slide_animation_interactive_sequence_effect', 'effect_index', 'int')
        effect = self.get_test_value('put_slide_animation_interactive_sequence_effect', 'effect', 'Effect')
        password = self.get_test_value('put_slide_animation_interactive_sequence_effect', 'password', 'str')
        folder = self.get_test_value('put_slide_animation_interactive_sequence_effect', 'folder', 'str')
        storage = self.get_test_value('put_slide_animation_interactive_sequence_effect', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlideAnimationInteractiveSequenceEffectRequest(name, slide_index, sequence_index, effect_index, effect, password, folder, storage)

    def test_put_slide_save_as(self):
        """Test case for put_slide_save_as
        """
        request = self.__prepare_put_slide_save_as_request()
        self.initialize('put_slide_save_as', None, None)
        response = self.api.put_slide_save_as(request)
        self.assertIsNone(response)

    def test_put_slide_save_as_invalid_name(self):
        """Test case for put_slide_save_as with invalid name
        """
        request = self.__prepare_put_slide_save_as_request()
        request.name = self.get_invalid_test_value('put_slide_save_as', 'name', request.name, 'str')
        self.initialize('put_slide_save_as', 'name', request.name)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'name')

    def test_put_slide_save_as_invalid_slide_index(self):
        """Test case for put_slide_save_as with invalid slide_index
        """
        request = self.__prepare_put_slide_save_as_request()
        request.slide_index = self.get_invalid_test_value('put_slide_save_as', 'slide_index', request.slide_index, 'int')
        self.initialize('put_slide_save_as', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'slide_index')

    def test_put_slide_save_as_invalid_format(self):
        """Test case for put_slide_save_as with invalid format
        """
        request = self.__prepare_put_slide_save_as_request()
        request.format = self.get_invalid_test_value('put_slide_save_as', 'format', request.format, 'str')
        self.initialize('put_slide_save_as', 'format', request.format)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'format')

    def test_put_slide_save_as_invalid_out_path(self):
        """Test case for put_slide_save_as with invalid out_path
        """
        request = self.__prepare_put_slide_save_as_request()
        request.out_path = self.get_invalid_test_value('put_slide_save_as', 'out_path', request.out_path, 'str')
        self.initialize('put_slide_save_as', 'out_path', request.out_path)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'out_path', request.out_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'out_path')

    def test_put_slide_save_as_invalid_options(self):
        """Test case for put_slide_save_as with invalid options
        """
        request = self.__prepare_put_slide_save_as_request()
        request.options = self.get_invalid_test_value('put_slide_save_as', 'options', request.options, 'ExportOptions')
        self.initialize('put_slide_save_as', 'options', request.options)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'options')

    def test_put_slide_save_as_invalid_width(self):
        """Test case for put_slide_save_as with invalid width
        """
        request = self.__prepare_put_slide_save_as_request()
        request.width = self.get_invalid_test_value('put_slide_save_as', 'width', request.width, 'int')
        self.initialize('put_slide_save_as', 'width', request.width)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'width', request.width)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'width')

    def test_put_slide_save_as_invalid_height(self):
        """Test case for put_slide_save_as with invalid height
        """
        request = self.__prepare_put_slide_save_as_request()
        request.height = self.get_invalid_test_value('put_slide_save_as', 'height', request.height, 'int')
        self.initialize('put_slide_save_as', 'height', request.height)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'height', request.height)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'height')

    def test_put_slide_save_as_invalid_password(self):
        """Test case for put_slide_save_as with invalid password
        """
        request = self.__prepare_put_slide_save_as_request()
        request.password = self.get_invalid_test_value('put_slide_save_as', 'password', request.password, 'str')
        self.initialize('put_slide_save_as', 'password', request.password)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'password')

    def test_put_slide_save_as_invalid_folder(self):
        """Test case for put_slide_save_as with invalid folder
        """
        request = self.__prepare_put_slide_save_as_request()
        request.folder = self.get_invalid_test_value('put_slide_save_as', 'folder', request.folder, 'str')
        self.initialize('put_slide_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'folder')

    def test_put_slide_save_as_invalid_storage(self):
        """Test case for put_slide_save_as with invalid storage
        """
        request = self.__prepare_put_slide_save_as_request()
        request.storage = self.get_invalid_test_value('put_slide_save_as', 'storage', request.storage, 'str')
        self.initialize('put_slide_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'storage')

    def test_put_slide_save_as_invalid_fonts_folder(self):
        """Test case for put_slide_save_as with invalid fonts_folder
        """
        request = self.__prepare_put_slide_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('put_slide_save_as', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('put_slide_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.put_slide_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_save_as', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_save_as', 'fonts_folder')

    def __prepare_put_slide_save_as_request(self):
        name = self.get_test_value('put_slide_save_as', 'name', 'str')
        slide_index = self.get_test_value('put_slide_save_as', 'slide_index', 'int')
        format = self.get_test_value('put_slide_save_as', 'format', 'str')
        out_path = self.get_test_value('put_slide_save_as', 'out_path', 'str')
        options = self.get_test_value('put_slide_save_as', 'options', 'ExportOptions')
        width = self.get_test_value('put_slide_save_as', 'width', 'int')
        height = self.get_test_value('put_slide_save_as', 'height', 'int')
        password = self.get_test_value('put_slide_save_as', 'password', 'str')
        folder = self.get_test_value('put_slide_save_as', 'folder', 'str')
        storage = self.get_test_value('put_slide_save_as', 'storage', 'str')
        fonts_folder = self.get_test_value('put_slide_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlideSaveAsRequest(name, slide_index, format, out_path, options, width, height, password, folder, storage, fonts_folder)

    def test_put_slide_shape_info(self):
        """Test case for put_slide_shape_info
        """
        request = self.__prepare_put_slide_shape_info_request()
        self.initialize('put_slide_shape_info', None, None)
        response = self.api.put_slide_shape_info(request)
        self.assertIsNotNone(response)

    def test_put_slide_shape_info_invalid_name(self):
        """Test case for put_slide_shape_info with invalid name
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.name = self.get_invalid_test_value('put_slide_shape_info', 'name', request.name, 'str')
        self.initialize('put_slide_shape_info', 'name', request.name)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'name')

    def test_put_slide_shape_info_invalid_slide_index(self):
        """Test case for put_slide_shape_info with invalid slide_index
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.slide_index = self.get_invalid_test_value('put_slide_shape_info', 'slide_index', request.slide_index, 'int')
        self.initialize('put_slide_shape_info', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'slide_index')

    def test_put_slide_shape_info_invalid_shape_index(self):
        """Test case for put_slide_shape_info with invalid shape_index
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.shape_index = self.get_invalid_test_value('put_slide_shape_info', 'shape_index', request.shape_index, 'int')
        self.initialize('put_slide_shape_info', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'shape_index')

    def test_put_slide_shape_info_invalid_dto(self):
        """Test case for put_slide_shape_info with invalid dto
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.dto = self.get_invalid_test_value('put_slide_shape_info', 'dto', request.dto, 'ShapeBase')
        self.initialize('put_slide_shape_info', 'dto', request.dto)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'dto')

    def test_put_slide_shape_info_invalid_password(self):
        """Test case for put_slide_shape_info with invalid password
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.password = self.get_invalid_test_value('put_slide_shape_info', 'password', request.password, 'str')
        self.initialize('put_slide_shape_info', 'password', request.password)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'password')

    def test_put_slide_shape_info_invalid_folder(self):
        """Test case for put_slide_shape_info with invalid folder
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.folder = self.get_invalid_test_value('put_slide_shape_info', 'folder', request.folder, 'str')
        self.initialize('put_slide_shape_info', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'folder')

    def test_put_slide_shape_info_invalid_storage(self):
        """Test case for put_slide_shape_info with invalid storage
        """
        request = self.__prepare_put_slide_shape_info_request()
        request.storage = self.get_invalid_test_value('put_slide_shape_info', 'storage', request.storage, 'str')
        self.initialize('put_slide_shape_info', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slide_shape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_shape_info', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_shape_info', 'storage')

    def __prepare_put_slide_shape_info_request(self):
        name = self.get_test_value('put_slide_shape_info', 'name', 'str')
        slide_index = self.get_test_value('put_slide_shape_info', 'slide_index', 'int')
        shape_index = self.get_test_value('put_slide_shape_info', 'shape_index', 'int')
        dto = self.get_test_value('put_slide_shape_info', 'dto', 'ShapeBase')
        password = self.get_test_value('put_slide_shape_info', 'password', 'str')
        folder = self.get_test_value('put_slide_shape_info', 'folder', 'str')
        storage = self.get_test_value('put_slide_shape_info', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlideShapeInfoRequest(name, slide_index, shape_index, dto, password, folder, storage)

    def test_put_slide_subshape_info(self):
        """Test case for put_slide_subshape_info
        """
        request = self.__prepare_put_slide_subshape_info_request()
        self.initialize('put_slide_subshape_info', None, None)
        response = self.api.put_slide_subshape_info(request)
        self.assertIsNotNone(response)

    def test_put_slide_subshape_info_invalid_name(self):
        """Test case for put_slide_subshape_info with invalid name
        """
        request = self.__prepare_put_slide_subshape_info_request()
        request.name = self.get_invalid_test_value('put_slide_subshape_info', 'name', request.name, 'str')
        self.initialize('put_slide_subshape_info', 'name', request.name)
        ok = False
        try:
            self.api.put_slide_subshape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_subshape_info', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_subshape_info', 'name')

    def test_put_slide_subshape_info_invalid_slide_index(self):
        """Test case for put_slide_subshape_info with invalid slide_index
        """
        request = self.__prepare_put_slide_subshape_info_request()
        request.slide_index = self.get_invalid_test_value('put_slide_subshape_info', 'slide_index', request.slide_index, 'int')
        self.initialize('put_slide_subshape_info', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slide_subshape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_subshape_info', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_subshape_info', 'slide_index')

    def test_put_slide_subshape_info_invalid_shape_index(self):
        """Test case for put_slide_subshape_info with invalid shape_index
        """
        request = self.__prepare_put_slide_subshape_info_request()
        request.shape_index = self.get_invalid_test_value('put_slide_subshape_info', 'shape_index', request.shape_index, 'int')
        self.initialize('put_slide_subshape_info', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_slide_subshape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_subshape_info', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_subshape_info', 'shape_index')

    def test_put_slide_subshape_info_invalid_path(self):
        """Test case for put_slide_subshape_info with invalid path
        """
        request = self.__prepare_put_slide_subshape_info_request()
        request.path = self.get_invalid_test_value('put_slide_subshape_info', 'path', request.path, 'str')
        self.initialize('put_slide_subshape_info', 'path', request.path)
        ok = False
        try:
            self.api.put_slide_subshape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_subshape_info', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_subshape_info', 'path')

    def test_put_slide_subshape_info_invalid_dto(self):
        """Test case for put_slide_subshape_info with invalid dto
        """
        request = self.__prepare_put_slide_subshape_info_request()
        request.dto = self.get_invalid_test_value('put_slide_subshape_info', 'dto', request.dto, 'ShapeBase')
        self.initialize('put_slide_subshape_info', 'dto', request.dto)
        ok = False
        try:
            self.api.put_slide_subshape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_subshape_info', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_subshape_info', 'dto')

    def test_put_slide_subshape_info_invalid_password(self):
        """Test case for put_slide_subshape_info with invalid password
        """
        request = self.__prepare_put_slide_subshape_info_request()
        request.password = self.get_invalid_test_value('put_slide_subshape_info', 'password', request.password, 'str')
        self.initialize('put_slide_subshape_info', 'password', request.password)
        ok = False
        try:
            self.api.put_slide_subshape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_subshape_info', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_subshape_info', 'password')

    def test_put_slide_subshape_info_invalid_folder(self):
        """Test case for put_slide_subshape_info with invalid folder
        """
        request = self.__prepare_put_slide_subshape_info_request()
        request.folder = self.get_invalid_test_value('put_slide_subshape_info', 'folder', request.folder, 'str')
        self.initialize('put_slide_subshape_info', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slide_subshape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_subshape_info', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_subshape_info', 'folder')

    def test_put_slide_subshape_info_invalid_storage(self):
        """Test case for put_slide_subshape_info with invalid storage
        """
        request = self.__prepare_put_slide_subshape_info_request()
        request.storage = self.get_invalid_test_value('put_slide_subshape_info', 'storage', request.storage, 'str')
        self.initialize('put_slide_subshape_info', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slide_subshape_info(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slide_subshape_info', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slide_subshape_info', 'storage')

    def __prepare_put_slide_subshape_info_request(self):
        name = self.get_test_value('put_slide_subshape_info', 'name', 'str')
        slide_index = self.get_test_value('put_slide_subshape_info', 'slide_index', 'int')
        shape_index = self.get_test_value('put_slide_subshape_info', 'shape_index', 'int')
        path = self.get_test_value('put_slide_subshape_info', 'path', 'str')
        dto = self.get_test_value('put_slide_subshape_info', 'dto', 'ShapeBase')
        password = self.get_test_value('put_slide_subshape_info', 'password', 'str')
        folder = self.get_test_value('put_slide_subshape_info', 'folder', 'str')
        storage = self.get_test_value('put_slide_subshape_info', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlideSubshapeInfoRequest(name, slide_index, shape_index, path, dto, password, folder, storage)

    def test_put_slides_convert(self):
        """Test case for put_slides_convert
        """
        request = self.__prepare_put_slides_convert_request()
        self.initialize('put_slides_convert', None, None)
        response = self.api.put_slides_convert(request)
        self.assertIsNone(response)

    def test_put_slides_convert_invalid_format(self):
        """Test case for put_slides_convert with invalid format
        """
        request = self.__prepare_put_slides_convert_request()
        request.format = self.get_invalid_test_value('put_slides_convert', 'format', request.format, 'str')
        self.initialize('put_slides_convert', 'format', request.format)
        ok = False
        try:
            self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_convert', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_convert', 'format')

    def test_put_slides_convert_invalid_out_path(self):
        """Test case for put_slides_convert with invalid out_path
        """
        request = self.__prepare_put_slides_convert_request()
        request.out_path = self.get_invalid_test_value('put_slides_convert', 'out_path', request.out_path, 'str')
        self.initialize('put_slides_convert', 'out_path', request.out_path)
        ok = False
        try:
            self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_convert', 'out_path', request.out_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_convert', 'out_path')

    def test_put_slides_convert_invalid_document(self):
        """Test case for put_slides_convert with invalid document
        """
        request = self.__prepare_put_slides_convert_request()
        request.document = self.get_invalid_test_value('put_slides_convert', 'document', request.document, 'file')
        self.initialize('put_slides_convert', 'document', request.document)
        ok = False
        try:
            self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_convert', 'document', request.document)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_convert', 'document')

    def test_put_slides_convert_invalid_password(self):
        """Test case for put_slides_convert with invalid password
        """
        request = self.__prepare_put_slides_convert_request()
        request.password = self.get_invalid_test_value('put_slides_convert', 'password', request.password, 'str')
        self.initialize('put_slides_convert', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_convert', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_convert', 'password')

    def test_put_slides_convert_invalid_fonts_folder(self):
        """Test case for put_slides_convert with invalid fonts_folder
        """
        request = self.__prepare_put_slides_convert_request()
        request.fonts_folder = self.get_invalid_test_value('put_slides_convert', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('put_slides_convert', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.put_slides_convert(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_convert', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_convert', 'fonts_folder')

    def __prepare_put_slides_convert_request(self):
        format = self.get_test_value('put_slides_convert', 'format', 'str')
        out_path = self.get_test_value('put_slides_convert', 'out_path', 'str')
        document = self.get_test_value('put_slides_convert', 'document', 'file')
        password = self.get_test_value('put_slides_convert', 'password', 'str')
        fonts_folder = self.get_test_value('put_slides_convert', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesConvertRequest(format, out_path, document, password, fonts_folder)

    def test_put_slides_document_from_html(self):
        """Test case for put_slides_document_from_html
        """
        request = self.__prepare_put_slides_document_from_html_request()
        self.initialize('put_slides_document_from_html', None, None)
        response = self.api.put_slides_document_from_html(request)
        self.assertIsNotNone(response)

    def test_put_slides_document_from_html_invalid_name(self):
        """Test case for put_slides_document_from_html with invalid name
        """
        request = self.__prepare_put_slides_document_from_html_request()
        request.name = self.get_invalid_test_value('put_slides_document_from_html', 'name', request.name, 'str')
        self.initialize('put_slides_document_from_html', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_document_from_html', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_document_from_html', 'name')

    def test_put_slides_document_from_html_invalid_html(self):
        """Test case for put_slides_document_from_html with invalid html
        """
        request = self.__prepare_put_slides_document_from_html_request()
        request.html = self.get_invalid_test_value('put_slides_document_from_html', 'html', request.html, 'str')
        self.initialize('put_slides_document_from_html', 'html', request.html)
        ok = False
        try:
            self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_document_from_html', 'html', request.html)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_document_from_html', 'html')

    def test_put_slides_document_from_html_invalid_password(self):
        """Test case for put_slides_document_from_html with invalid password
        """
        request = self.__prepare_put_slides_document_from_html_request()
        request.password = self.get_invalid_test_value('put_slides_document_from_html', 'password', request.password, 'str')
        self.initialize('put_slides_document_from_html', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_document_from_html', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_document_from_html', 'password')

    def test_put_slides_document_from_html_invalid_storage(self):
        """Test case for put_slides_document_from_html with invalid storage
        """
        request = self.__prepare_put_slides_document_from_html_request()
        request.storage = self.get_invalid_test_value('put_slides_document_from_html', 'storage', request.storage, 'str')
        self.initialize('put_slides_document_from_html', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_document_from_html', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_document_from_html', 'storage')

    def test_put_slides_document_from_html_invalid_folder(self):
        """Test case for put_slides_document_from_html with invalid folder
        """
        request = self.__prepare_put_slides_document_from_html_request()
        request.folder = self.get_invalid_test_value('put_slides_document_from_html', 'folder', request.folder, 'str')
        self.initialize('put_slides_document_from_html', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_document_from_html(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_document_from_html', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_document_from_html', 'folder')

    def __prepare_put_slides_document_from_html_request(self):
        name = self.get_test_value('put_slides_document_from_html', 'name', 'str')
        html = self.get_test_value('put_slides_document_from_html', 'html', 'str')
        password = self.get_test_value('put_slides_document_from_html', 'password', 'str')
        storage = self.get_test_value('put_slides_document_from_html', 'storage', 'str')
        folder = self.get_test_value('put_slides_document_from_html', 'folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesDocumentFromHtmlRequest(name, html, password, storage, folder)

    def test_put_slides_save_as(self):
        """Test case for put_slides_save_as
        """
        request = self.__prepare_put_slides_save_as_request()
        self.initialize('put_slides_save_as', None, None)
        response = self.api.put_slides_save_as(request)
        self.assertIsNone(response)

    def test_put_slides_save_as_invalid_name(self):
        """Test case for put_slides_save_as with invalid name
        """
        request = self.__prepare_put_slides_save_as_request()
        request.name = self.get_invalid_test_value('put_slides_save_as', 'name', request.name, 'str')
        self.initialize('put_slides_save_as', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_save_as', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_save_as', 'name')

    def test_put_slides_save_as_invalid_out_path(self):
        """Test case for put_slides_save_as with invalid out_path
        """
        request = self.__prepare_put_slides_save_as_request()
        request.out_path = self.get_invalid_test_value('put_slides_save_as', 'out_path', request.out_path, 'str')
        self.initialize('put_slides_save_as', 'out_path', request.out_path)
        ok = False
        try:
            self.api.put_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_save_as', 'out_path', request.out_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_save_as', 'out_path')

    def test_put_slides_save_as_invalid_format(self):
        """Test case for put_slides_save_as with invalid format
        """
        request = self.__prepare_put_slides_save_as_request()
        request.format = self.get_invalid_test_value('put_slides_save_as', 'format', request.format, 'str')
        self.initialize('put_slides_save_as', 'format', request.format)
        ok = False
        try:
            self.api.put_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_save_as', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_save_as', 'format')

    def test_put_slides_save_as_invalid_options(self):
        """Test case for put_slides_save_as with invalid options
        """
        request = self.__prepare_put_slides_save_as_request()
        request.options = self.get_invalid_test_value('put_slides_save_as', 'options', request.options, 'ExportOptions')
        self.initialize('put_slides_save_as', 'options', request.options)
        ok = False
        try:
            self.api.put_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_save_as', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_save_as', 'options')

    def test_put_slides_save_as_invalid_password(self):
        """Test case for put_slides_save_as with invalid password
        """
        request = self.__prepare_put_slides_save_as_request()
        request.password = self.get_invalid_test_value('put_slides_save_as', 'password', request.password, 'str')
        self.initialize('put_slides_save_as', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_save_as', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_save_as', 'password')

    def test_put_slides_save_as_invalid_storage(self):
        """Test case for put_slides_save_as with invalid storage
        """
        request = self.__prepare_put_slides_save_as_request()
        request.storage = self.get_invalid_test_value('put_slides_save_as', 'storage', request.storage, 'str')
        self.initialize('put_slides_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_save_as', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_save_as', 'storage')

    def test_put_slides_save_as_invalid_folder(self):
        """Test case for put_slides_save_as with invalid folder
        """
        request = self.__prepare_put_slides_save_as_request()
        request.folder = self.get_invalid_test_value('put_slides_save_as', 'folder', request.folder, 'str')
        self.initialize('put_slides_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_save_as', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_save_as', 'folder')

    def test_put_slides_save_as_invalid_fonts_folder(self):
        """Test case for put_slides_save_as with invalid fonts_folder
        """
        request = self.__prepare_put_slides_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('put_slides_save_as', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('put_slides_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.put_slides_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_save_as', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_save_as', 'fonts_folder')

    def __prepare_put_slides_save_as_request(self):
        name = self.get_test_value('put_slides_save_as', 'name', 'str')
        out_path = self.get_test_value('put_slides_save_as', 'out_path', 'str')
        format = self.get_test_value('put_slides_save_as', 'format', 'str')
        options = self.get_test_value('put_slides_save_as', 'options', 'ExportOptions')
        password = self.get_test_value('put_slides_save_as', 'password', 'str')
        storage = self.get_test_value('put_slides_save_as', 'storage', 'str')
        folder = self.get_test_value('put_slides_save_as', 'folder', 'str')
        fonts_folder = self.get_test_value('put_slides_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesSaveAsRequest(name, out_path, format, options, password, storage, folder, fonts_folder)

    def test_put_slides_set_document_property(self):
        """Test case for put_slides_set_document_property
        """
        request = self.__prepare_put_slides_set_document_property_request()
        self.initialize('put_slides_set_document_property', None, None)
        response = self.api.put_slides_set_document_property(request)
        self.assertIsNotNone(response)

    def test_put_slides_set_document_property_invalid_name(self):
        """Test case for put_slides_set_document_property with invalid name
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request.name = self.get_invalid_test_value('put_slides_set_document_property', 'name', request.name, 'str')
        self.initialize('put_slides_set_document_property', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_set_document_property', 'name')

    def test_put_slides_set_document_property_invalid_property_name(self):
        """Test case for put_slides_set_document_property with invalid property_name
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request.property_name = self.get_invalid_test_value('put_slides_set_document_property', 'property_name', request.property_name, 'str')
        self.initialize('put_slides_set_document_property', 'property_name', request.property_name)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', 'property_name', request.property_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_set_document_property', 'property_name')

    def test_put_slides_set_document_property_invalid__property(self):
        """Test case for put_slides_set_document_property with invalid _property
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request._property = self.get_invalid_test_value('put_slides_set_document_property', '_property', request._property, 'DocumentProperty')
        self.initialize('put_slides_set_document_property', '_property', request._property)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', '_property', request._property)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_set_document_property', '_property')

    def test_put_slides_set_document_property_invalid_password(self):
        """Test case for put_slides_set_document_property with invalid password
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request.password = self.get_invalid_test_value('put_slides_set_document_property', 'password', request.password, 'str')
        self.initialize('put_slides_set_document_property', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_set_document_property', 'password')

    def test_put_slides_set_document_property_invalid_folder(self):
        """Test case for put_slides_set_document_property with invalid folder
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request.folder = self.get_invalid_test_value('put_slides_set_document_property', 'folder', request.folder, 'str')
        self.initialize('put_slides_set_document_property', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_set_document_property', 'folder')

    def test_put_slides_set_document_property_invalid_storage(self):
        """Test case for put_slides_set_document_property with invalid storage
        """
        request = self.__prepare_put_slides_set_document_property_request()
        request.storage = self.get_invalid_test_value('put_slides_set_document_property', 'storage', request.storage, 'str')
        self.initialize('put_slides_set_document_property', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_set_document_property(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_set_document_property', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_set_document_property', 'storage')

    def __prepare_put_slides_set_document_property_request(self):
        name = self.get_test_value('put_slides_set_document_property', 'name', 'str')
        property_name = self.get_test_value('put_slides_set_document_property', 'property_name', 'str')
        _property = self.get_test_value('put_slides_set_document_property', '_property', 'DocumentProperty')
        password = self.get_test_value('put_slides_set_document_property', 'password', 'str')
        folder = self.get_test_value('put_slides_set_document_property', 'folder', 'str')
        storage = self.get_test_value('put_slides_set_document_property', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesSetDocumentPropertyRequest(name, property_name, _property, password, folder, storage)

    def test_put_slides_slide(self):
        """Test case for put_slides_slide
        """
        request = self.__prepare_put_slides_slide_request()
        self.initialize('put_slides_slide', None, None)
        response = self.api.put_slides_slide(request)
        self.assertIsNotNone(response)

    def test_put_slides_slide_invalid_name(self):
        """Test case for put_slides_slide with invalid name
        """
        request = self.__prepare_put_slides_slide_request()
        request.name = self.get_invalid_test_value('put_slides_slide', 'name', request.name, 'str')
        self.initialize('put_slides_slide', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide', 'name')

    def test_put_slides_slide_invalid_slide_index(self):
        """Test case for put_slides_slide with invalid slide_index
        """
        request = self.__prepare_put_slides_slide_request()
        request.slide_index = self.get_invalid_test_value('put_slides_slide', 'slide_index', request.slide_index, 'int')
        self.initialize('put_slides_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide', 'slide_index')

    def test_put_slides_slide_invalid_slide_dto(self):
        """Test case for put_slides_slide with invalid slide_dto
        """
        request = self.__prepare_put_slides_slide_request()
        request.slide_dto = self.get_invalid_test_value('put_slides_slide', 'slide_dto', request.slide_dto, 'Slide')
        self.initialize('put_slides_slide', 'slide_dto', request.slide_dto)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'slide_dto', request.slide_dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide', 'slide_dto')

    def test_put_slides_slide_invalid_password(self):
        """Test case for put_slides_slide with invalid password
        """
        request = self.__prepare_put_slides_slide_request()
        request.password = self.get_invalid_test_value('put_slides_slide', 'password', request.password, 'str')
        self.initialize('put_slides_slide', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide', 'password')

    def test_put_slides_slide_invalid_folder(self):
        """Test case for put_slides_slide with invalid folder
        """
        request = self.__prepare_put_slides_slide_request()
        request.folder = self.get_invalid_test_value('put_slides_slide', 'folder', request.folder, 'str')
        self.initialize('put_slides_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide', 'folder')

    def test_put_slides_slide_invalid_storage(self):
        """Test case for put_slides_slide with invalid storage
        """
        request = self.__prepare_put_slides_slide_request()
        request.storage = self.get_invalid_test_value('put_slides_slide', 'storage', request.storage, 'str')
        self.initialize('put_slides_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide', 'storage')

    def __prepare_put_slides_slide_request(self):
        name = self.get_test_value('put_slides_slide', 'name', 'str')
        slide_index = self.get_test_value('put_slides_slide', 'slide_index', 'int')
        slide_dto = self.get_test_value('put_slides_slide', 'slide_dto', 'Slide')
        password = self.get_test_value('put_slides_slide', 'password', 'str')
        folder = self.get_test_value('put_slides_slide', 'folder', 'str')
        storage = self.get_test_value('put_slides_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesSlideRequest(name, slide_index, slide_dto, password, folder, storage)

    def test_put_slides_slide_background(self):
        """Test case for put_slides_slide_background
        """
        request = self.__prepare_put_slides_slide_background_request()
        self.initialize('put_slides_slide_background', None, None)
        response = self.api.put_slides_slide_background(request)
        self.assertIsNotNone(response)

    def test_put_slides_slide_background_invalid_name(self):
        """Test case for put_slides_slide_background with invalid name
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.name = self.get_invalid_test_value('put_slides_slide_background', 'name', request.name, 'str')
        self.initialize('put_slides_slide_background', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'name')

    def test_put_slides_slide_background_invalid_slide_index(self):
        """Test case for put_slides_slide_background with invalid slide_index
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.slide_index = self.get_invalid_test_value('put_slides_slide_background', 'slide_index', request.slide_index, 'int')
        self.initialize('put_slides_slide_background', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'slide_index')

    def test_put_slides_slide_background_invalid_background(self):
        """Test case for put_slides_slide_background with invalid background
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.background = self.get_invalid_test_value('put_slides_slide_background', 'background', request.background, 'SlideBackground')
        self.initialize('put_slides_slide_background', 'background', request.background)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'background', request.background)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'background')

    def test_put_slides_slide_background_invalid_folder(self):
        """Test case for put_slides_slide_background with invalid folder
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.folder = self.get_invalid_test_value('put_slides_slide_background', 'folder', request.folder, 'str')
        self.initialize('put_slides_slide_background', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'folder')

    def test_put_slides_slide_background_invalid_password(self):
        """Test case for put_slides_slide_background with invalid password
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.password = self.get_invalid_test_value('put_slides_slide_background', 'password', request.password, 'str')
        self.initialize('put_slides_slide_background', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'password')

    def test_put_slides_slide_background_invalid_storage(self):
        """Test case for put_slides_slide_background with invalid storage
        """
        request = self.__prepare_put_slides_slide_background_request()
        request.storage = self.get_invalid_test_value('put_slides_slide_background', 'storage', request.storage, 'str')
        self.initialize('put_slides_slide_background', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_slide_background(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background', 'storage')

    def __prepare_put_slides_slide_background_request(self):
        name = self.get_test_value('put_slides_slide_background', 'name', 'str')
        slide_index = self.get_test_value('put_slides_slide_background', 'slide_index', 'int')
        background = self.get_test_value('put_slides_slide_background', 'background', 'SlideBackground')
        folder = self.get_test_value('put_slides_slide_background', 'folder', 'str')
        password = self.get_test_value('put_slides_slide_background', 'password', 'str')
        storage = self.get_test_value('put_slides_slide_background', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesSlideBackgroundRequest(name, slide_index, background, folder, password, storage)

    def test_put_slides_slide_background_color(self):
        """Test case for put_slides_slide_background_color
        """
        request = self.__prepare_put_slides_slide_background_color_request()
        self.initialize('put_slides_slide_background_color', None, None)
        response = self.api.put_slides_slide_background_color(request)
        self.assertIsNotNone(response)

    def test_put_slides_slide_background_color_invalid_name(self):
        """Test case for put_slides_slide_background_color with invalid name
        """
        request = self.__prepare_put_slides_slide_background_color_request()
        request.name = self.get_invalid_test_value('put_slides_slide_background_color', 'name', request.name, 'str')
        self.initialize('put_slides_slide_background_color', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_slide_background_color(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background_color', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background_color', 'name')

    def test_put_slides_slide_background_color_invalid_slide_index(self):
        """Test case for put_slides_slide_background_color with invalid slide_index
        """
        request = self.__prepare_put_slides_slide_background_color_request()
        request.slide_index = self.get_invalid_test_value('put_slides_slide_background_color', 'slide_index', request.slide_index, 'int')
        self.initialize('put_slides_slide_background_color', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_slides_slide_background_color(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background_color', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background_color', 'slide_index')

    def test_put_slides_slide_background_color_invalid_color(self):
        """Test case for put_slides_slide_background_color with invalid color
        """
        request = self.__prepare_put_slides_slide_background_color_request()
        request.color = self.get_invalid_test_value('put_slides_slide_background_color', 'color', request.color, 'str')
        self.initialize('put_slides_slide_background_color', 'color', request.color)
        ok = False
        try:
            self.api.put_slides_slide_background_color(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background_color', 'color', request.color)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background_color', 'color')

    def test_put_slides_slide_background_color_invalid_folder(self):
        """Test case for put_slides_slide_background_color with invalid folder
        """
        request = self.__prepare_put_slides_slide_background_color_request()
        request.folder = self.get_invalid_test_value('put_slides_slide_background_color', 'folder', request.folder, 'str')
        self.initialize('put_slides_slide_background_color', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_slide_background_color(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background_color', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background_color', 'folder')

    def test_put_slides_slide_background_color_invalid_password(self):
        """Test case for put_slides_slide_background_color with invalid password
        """
        request = self.__prepare_put_slides_slide_background_color_request()
        request.password = self.get_invalid_test_value('put_slides_slide_background_color', 'password', request.password, 'str')
        self.initialize('put_slides_slide_background_color', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_slide_background_color(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background_color', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background_color', 'password')

    def test_put_slides_slide_background_color_invalid_storage(self):
        """Test case for put_slides_slide_background_color with invalid storage
        """
        request = self.__prepare_put_slides_slide_background_color_request()
        request.storage = self.get_invalid_test_value('put_slides_slide_background_color', 'storage', request.storage, 'str')
        self.initialize('put_slides_slide_background_color', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_slide_background_color(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_background_color', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_background_color', 'storage')

    def __prepare_put_slides_slide_background_color_request(self):
        name = self.get_test_value('put_slides_slide_background_color', 'name', 'str')
        slide_index = self.get_test_value('put_slides_slide_background_color', 'slide_index', 'int')
        color = self.get_test_value('put_slides_slide_background_color', 'color', 'str')
        folder = self.get_test_value('put_slides_slide_background_color', 'folder', 'str')
        password = self.get_test_value('put_slides_slide_background_color', 'password', 'str')
        storage = self.get_test_value('put_slides_slide_background_color', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesSlideBackgroundColorRequest(name, slide_index, color, folder, password, storage)

    def test_put_slides_slide_size(self):
        """Test case for put_slides_slide_size
        """
        request = self.__prepare_put_slides_slide_size_request()
        self.initialize('put_slides_slide_size', None, None)
        response = self.api.put_slides_slide_size(request)
        self.assertIsNotNone(response)

    def test_put_slides_slide_size_invalid_name(self):
        """Test case for put_slides_slide_size with invalid name
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.name = self.get_invalid_test_value('put_slides_slide_size', 'name', request.name, 'str')
        self.initialize('put_slides_slide_size', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'name')

    def test_put_slides_slide_size_invalid_password(self):
        """Test case for put_slides_slide_size with invalid password
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.password = self.get_invalid_test_value('put_slides_slide_size', 'password', request.password, 'str')
        self.initialize('put_slides_slide_size', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'password')

    def test_put_slides_slide_size_invalid_storage(self):
        """Test case for put_slides_slide_size with invalid storage
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.storage = self.get_invalid_test_value('put_slides_slide_size', 'storage', request.storage, 'str')
        self.initialize('put_slides_slide_size', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'storage')

    def test_put_slides_slide_size_invalid_folder(self):
        """Test case for put_slides_slide_size with invalid folder
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.folder = self.get_invalid_test_value('put_slides_slide_size', 'folder', request.folder, 'str')
        self.initialize('put_slides_slide_size', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'folder')

    def test_put_slides_slide_size_invalid_width(self):
        """Test case for put_slides_slide_size with invalid width
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.width = self.get_invalid_test_value('put_slides_slide_size', 'width', request.width, 'int')
        self.initialize('put_slides_slide_size', 'width', request.width)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'width', request.width)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'width')

    def test_put_slides_slide_size_invalid_height(self):
        """Test case for put_slides_slide_size with invalid height
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.height = self.get_invalid_test_value('put_slides_slide_size', 'height', request.height, 'int')
        self.initialize('put_slides_slide_size', 'height', request.height)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'height', request.height)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'height')

    def test_put_slides_slide_size_invalid_size_type(self):
        """Test case for put_slides_slide_size with invalid size_type
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.size_type = self.get_invalid_test_value('put_slides_slide_size', 'size_type', request.size_type, 'str')
        self.initialize('put_slides_slide_size', 'size_type', request.size_type)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'size_type', request.size_type)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'size_type')

    def test_put_slides_slide_size_invalid_scale_type(self):
        """Test case for put_slides_slide_size with invalid scale_type
        """
        request = self.__prepare_put_slides_slide_size_request()
        request.scale_type = self.get_invalid_test_value('put_slides_slide_size', 'scale_type', request.scale_type, 'str')
        self.initialize('put_slides_slide_size', 'scale_type', request.scale_type)
        ok = False
        try:
            self.api.put_slides_slide_size(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_slide_size', 'scale_type', request.scale_type)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_slide_size', 'scale_type')

    def __prepare_put_slides_slide_size_request(self):
        name = self.get_test_value('put_slides_slide_size', 'name', 'str')
        password = self.get_test_value('put_slides_slide_size', 'password', 'str')
        storage = self.get_test_value('put_slides_slide_size', 'storage', 'str')
        folder = self.get_test_value('put_slides_slide_size', 'folder', 'str')
        width = self.get_test_value('put_slides_slide_size', 'width', 'int')
        height = self.get_test_value('put_slides_slide_size', 'height', 'int')
        size_type = self.get_test_value('put_slides_slide_size', 'size_type', 'str')
        scale_type = self.get_test_value('put_slides_slide_size', 'scale_type', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesSlideSizeRequest(name, password, storage, folder, width, height, size_type, scale_type)

    def test_put_slides_view_properties(self):
        """Test case for put_slides_view_properties
        """
        request = self.__prepare_put_slides_view_properties_request()
        self.initialize('put_slides_view_properties', None, None)
        response = self.api.put_slides_view_properties(request)
        self.assertIsNotNone(response)

    def test_put_slides_view_properties_invalid_name(self):
        """Test case for put_slides_view_properties with invalid name
        """
        request = self.__prepare_put_slides_view_properties_request()
        request.name = self.get_invalid_test_value('put_slides_view_properties', 'name', request.name, 'str')
        self.initialize('put_slides_view_properties', 'name', request.name)
        ok = False
        try:
            self.api.put_slides_view_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_view_properties', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_view_properties', 'name')

    def test_put_slides_view_properties_invalid_dto(self):
        """Test case for put_slides_view_properties with invalid dto
        """
        request = self.__prepare_put_slides_view_properties_request()
        request.dto = self.get_invalid_test_value('put_slides_view_properties', 'dto', request.dto, 'ViewProperties')
        self.initialize('put_slides_view_properties', 'dto', request.dto)
        ok = False
        try:
            self.api.put_slides_view_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_view_properties', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_view_properties', 'dto')

    def test_put_slides_view_properties_invalid_password(self):
        """Test case for put_slides_view_properties with invalid password
        """
        request = self.__prepare_put_slides_view_properties_request()
        request.password = self.get_invalid_test_value('put_slides_view_properties', 'password', request.password, 'str')
        self.initialize('put_slides_view_properties', 'password', request.password)
        ok = False
        try:
            self.api.put_slides_view_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_view_properties', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_view_properties', 'password')

    def test_put_slides_view_properties_invalid_folder(self):
        """Test case for put_slides_view_properties with invalid folder
        """
        request = self.__prepare_put_slides_view_properties_request()
        request.folder = self.get_invalid_test_value('put_slides_view_properties', 'folder', request.folder, 'str')
        self.initialize('put_slides_view_properties', 'folder', request.folder)
        ok = False
        try:
            self.api.put_slides_view_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_view_properties', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_view_properties', 'folder')

    def test_put_slides_view_properties_invalid_storage(self):
        """Test case for put_slides_view_properties with invalid storage
        """
        request = self.__prepare_put_slides_view_properties_request()
        request.storage = self.get_invalid_test_value('put_slides_view_properties', 'storage', request.storage, 'str')
        self.initialize('put_slides_view_properties', 'storage', request.storage)
        ok = False
        try:
            self.api.put_slides_view_properties(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_slides_view_properties', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_slides_view_properties', 'storage')

    def __prepare_put_slides_view_properties_request(self):
        name = self.get_test_value('put_slides_view_properties', 'name', 'str')
        dto = self.get_test_value('put_slides_view_properties', 'dto', 'ViewProperties')
        password = self.get_test_value('put_slides_view_properties', 'password', 'str')
        folder = self.get_test_value('put_slides_view_properties', 'folder', 'str')
        storage = self.get_test_value('put_slides_view_properties', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSlidesViewPropertiesRequest(name, dto, password, folder, storage)

    def test_put_subshape_save_as(self):
        """Test case for put_subshape_save_as
        """
        request = self.__prepare_put_subshape_save_as_request()
        self.initialize('put_subshape_save_as', None, None)
        response = self.api.put_subshape_save_as(request)
        self.assertIsNone(response)

    def test_put_subshape_save_as_invalid_name(self):
        """Test case for put_subshape_save_as with invalid name
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.name = self.get_invalid_test_value('put_subshape_save_as', 'name', request.name, 'str')
        self.initialize('put_subshape_save_as', 'name', request.name)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'name')

    def test_put_subshape_save_as_invalid_slide_index(self):
        """Test case for put_subshape_save_as with invalid slide_index
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.slide_index = self.get_invalid_test_value('put_subshape_save_as', 'slide_index', request.slide_index, 'int')
        self.initialize('put_subshape_save_as', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'slide_index')

    def test_put_subshape_save_as_invalid_shape_index(self):
        """Test case for put_subshape_save_as with invalid shape_index
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.shape_index = self.get_invalid_test_value('put_subshape_save_as', 'shape_index', request.shape_index, 'int')
        self.initialize('put_subshape_save_as', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'shape_index')

    def test_put_subshape_save_as_invalid_format(self):
        """Test case for put_subshape_save_as with invalid format
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.format = self.get_invalid_test_value('put_subshape_save_as', 'format', request.format, 'str')
        self.initialize('put_subshape_save_as', 'format', request.format)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'format', request.format)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'format')

    def test_put_subshape_save_as_invalid_out_path(self):
        """Test case for put_subshape_save_as with invalid out_path
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.out_path = self.get_invalid_test_value('put_subshape_save_as', 'out_path', request.out_path, 'str')
        self.initialize('put_subshape_save_as', 'out_path', request.out_path)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'out_path', request.out_path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'out_path')

    def test_put_subshape_save_as_invalid_path(self):
        """Test case for put_subshape_save_as with invalid path
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.path = self.get_invalid_test_value('put_subshape_save_as', 'path', request.path, 'str')
        self.initialize('put_subshape_save_as', 'path', request.path)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'path')

    def test_put_subshape_save_as_invalid_options(self):
        """Test case for put_subshape_save_as with invalid options
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.options = self.get_invalid_test_value('put_subshape_save_as', 'options', request.options, 'IShapeExportOptions')
        self.initialize('put_subshape_save_as', 'options', request.options)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'options', request.options)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'options')

    def test_put_subshape_save_as_invalid_password(self):
        """Test case for put_subshape_save_as with invalid password
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.password = self.get_invalid_test_value('put_subshape_save_as', 'password', request.password, 'str')
        self.initialize('put_subshape_save_as', 'password', request.password)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'password')

    def test_put_subshape_save_as_invalid_folder(self):
        """Test case for put_subshape_save_as with invalid folder
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.folder = self.get_invalid_test_value('put_subshape_save_as', 'folder', request.folder, 'str')
        self.initialize('put_subshape_save_as', 'folder', request.folder)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'folder')

    def test_put_subshape_save_as_invalid_storage(self):
        """Test case for put_subshape_save_as with invalid storage
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.storage = self.get_invalid_test_value('put_subshape_save_as', 'storage', request.storage, 'str')
        self.initialize('put_subshape_save_as', 'storage', request.storage)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'storage')

    def test_put_subshape_save_as_invalid_scale_x(self):
        """Test case for put_subshape_save_as with invalid scale_x
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.scale_x = self.get_invalid_test_value('put_subshape_save_as', 'scale_x', request.scale_x, 'float')
        self.initialize('put_subshape_save_as', 'scale_x', request.scale_x)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'scale_x', request.scale_x)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'scale_x')

    def test_put_subshape_save_as_invalid_scale_y(self):
        """Test case for put_subshape_save_as with invalid scale_y
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.scale_y = self.get_invalid_test_value('put_subshape_save_as', 'scale_y', request.scale_y, 'float')
        self.initialize('put_subshape_save_as', 'scale_y', request.scale_y)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'scale_y', request.scale_y)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'scale_y')

    def test_put_subshape_save_as_invalid_bounds(self):
        """Test case for put_subshape_save_as with invalid bounds
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.bounds = self.get_invalid_test_value('put_subshape_save_as', 'bounds', request.bounds, 'str')
        self.initialize('put_subshape_save_as', 'bounds', request.bounds)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'bounds', request.bounds)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'bounds')

    def test_put_subshape_save_as_invalid_fonts_folder(self):
        """Test case for put_subshape_save_as with invalid fonts_folder
        """
        request = self.__prepare_put_subshape_save_as_request()
        request.fonts_folder = self.get_invalid_test_value('put_subshape_save_as', 'fonts_folder', request.fonts_folder, 'str')
        self.initialize('put_subshape_save_as', 'fonts_folder', request.fonts_folder)
        ok = False
        try:
            self.api.put_subshape_save_as(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_subshape_save_as', 'fonts_folder', request.fonts_folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_subshape_save_as', 'fonts_folder')

    def __prepare_put_subshape_save_as_request(self):
        name = self.get_test_value('put_subshape_save_as', 'name', 'str')
        slide_index = self.get_test_value('put_subshape_save_as', 'slide_index', 'int')
        shape_index = self.get_test_value('put_subshape_save_as', 'shape_index', 'int')
        format = self.get_test_value('put_subshape_save_as', 'format', 'str')
        out_path = self.get_test_value('put_subshape_save_as', 'out_path', 'str')
        path = self.get_test_value('put_subshape_save_as', 'path', 'str')
        options = self.get_test_value('put_subshape_save_as', 'options', 'IShapeExportOptions')
        password = self.get_test_value('put_subshape_save_as', 'password', 'str')
        folder = self.get_test_value('put_subshape_save_as', 'folder', 'str')
        storage = self.get_test_value('put_subshape_save_as', 'storage', 'str')
        scale_x = self.get_test_value('put_subshape_save_as', 'scale_x', 'float')
        scale_y = self.get_test_value('put_subshape_save_as', 'scale_y', 'float')
        bounds = self.get_test_value('put_subshape_save_as', 'bounds', 'str')
        fonts_folder = self.get_test_value('put_subshape_save_as', 'fonts_folder', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutSubshapeSaveAsRequest(name, slide_index, shape_index, format, out_path, path, options, password, folder, storage, scale_x, scale_y, bounds, fonts_folder)

    def test_put_update_notes_slide(self):
        """Test case for put_update_notes_slide
        """
        request = self.__prepare_put_update_notes_slide_request()
        self.initialize('put_update_notes_slide', None, None)
        response = self.api.put_update_notes_slide(request)
        self.assertIsNotNone(response)

    def test_put_update_notes_slide_invalid_name(self):
        """Test case for put_update_notes_slide with invalid name
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.name = self.get_invalid_test_value('put_update_notes_slide', 'name', request.name, 'str')
        self.initialize('put_update_notes_slide', 'name', request.name)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'name')

    def test_put_update_notes_slide_invalid_slide_index(self):
        """Test case for put_update_notes_slide with invalid slide_index
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.slide_index = self.get_invalid_test_value('put_update_notes_slide', 'slide_index', request.slide_index, 'int')
        self.initialize('put_update_notes_slide', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'slide_index')

    def test_put_update_notes_slide_invalid_dto(self):
        """Test case for put_update_notes_slide with invalid dto
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.dto = self.get_invalid_test_value('put_update_notes_slide', 'dto', request.dto, 'NotesSlide')
        self.initialize('put_update_notes_slide', 'dto', request.dto)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'dto')

    def test_put_update_notes_slide_invalid_password(self):
        """Test case for put_update_notes_slide with invalid password
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.password = self.get_invalid_test_value('put_update_notes_slide', 'password', request.password, 'str')
        self.initialize('put_update_notes_slide', 'password', request.password)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'password')

    def test_put_update_notes_slide_invalid_folder(self):
        """Test case for put_update_notes_slide with invalid folder
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.folder = self.get_invalid_test_value('put_update_notes_slide', 'folder', request.folder, 'str')
        self.initialize('put_update_notes_slide', 'folder', request.folder)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'folder')

    def test_put_update_notes_slide_invalid_storage(self):
        """Test case for put_update_notes_slide with invalid storage
        """
        request = self.__prepare_put_update_notes_slide_request()
        request.storage = self.get_invalid_test_value('put_update_notes_slide', 'storage', request.storage, 'str')
        self.initialize('put_update_notes_slide', 'storage', request.storage)
        ok = False
        try:
            self.api.put_update_notes_slide(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide', 'storage')

    def __prepare_put_update_notes_slide_request(self):
        name = self.get_test_value('put_update_notes_slide', 'name', 'str')
        slide_index = self.get_test_value('put_update_notes_slide', 'slide_index', 'int')
        dto = self.get_test_value('put_update_notes_slide', 'dto', 'NotesSlide')
        password = self.get_test_value('put_update_notes_slide', 'password', 'str')
        folder = self.get_test_value('put_update_notes_slide', 'folder', 'str')
        storage = self.get_test_value('put_update_notes_slide', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutUpdateNotesSlideRequest(name, slide_index, dto, password, folder, storage)

    def test_put_update_notes_slide_shape(self):
        """Test case for put_update_notes_slide_shape
        """
        request = self.__prepare_put_update_notes_slide_shape_request()
        self.initialize('put_update_notes_slide_shape', None, None)
        response = self.api.put_update_notes_slide_shape(request)
        self.assertIsNotNone(response)

    def test_put_update_notes_slide_shape_invalid_name(self):
        """Test case for put_update_notes_slide_shape with invalid name
        """
        request = self.__prepare_put_update_notes_slide_shape_request()
        request.name = self.get_invalid_test_value('put_update_notes_slide_shape', 'name', request.name, 'str')
        self.initialize('put_update_notes_slide_shape', 'name', request.name)
        ok = False
        try:
            self.api.put_update_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape', 'name')

    def test_put_update_notes_slide_shape_invalid_slide_index(self):
        """Test case for put_update_notes_slide_shape with invalid slide_index
        """
        request = self.__prepare_put_update_notes_slide_shape_request()
        request.slide_index = self.get_invalid_test_value('put_update_notes_slide_shape', 'slide_index', request.slide_index, 'int')
        self.initialize('put_update_notes_slide_shape', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_update_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape', 'slide_index')

    def test_put_update_notes_slide_shape_invalid_shape_index(self):
        """Test case for put_update_notes_slide_shape with invalid shape_index
        """
        request = self.__prepare_put_update_notes_slide_shape_request()
        request.shape_index = self.get_invalid_test_value('put_update_notes_slide_shape', 'shape_index', request.shape_index, 'int')
        self.initialize('put_update_notes_slide_shape', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_update_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape', 'shape_index')

    def test_put_update_notes_slide_shape_invalid_dto(self):
        """Test case for put_update_notes_slide_shape with invalid dto
        """
        request = self.__prepare_put_update_notes_slide_shape_request()
        request.dto = self.get_invalid_test_value('put_update_notes_slide_shape', 'dto', request.dto, 'ShapeBase')
        self.initialize('put_update_notes_slide_shape', 'dto', request.dto)
        ok = False
        try:
            self.api.put_update_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape', 'dto')

    def test_put_update_notes_slide_shape_invalid_password(self):
        """Test case for put_update_notes_slide_shape with invalid password
        """
        request = self.__prepare_put_update_notes_slide_shape_request()
        request.password = self.get_invalid_test_value('put_update_notes_slide_shape', 'password', request.password, 'str')
        self.initialize('put_update_notes_slide_shape', 'password', request.password)
        ok = False
        try:
            self.api.put_update_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape', 'password')

    def test_put_update_notes_slide_shape_invalid_folder(self):
        """Test case for put_update_notes_slide_shape with invalid folder
        """
        request = self.__prepare_put_update_notes_slide_shape_request()
        request.folder = self.get_invalid_test_value('put_update_notes_slide_shape', 'folder', request.folder, 'str')
        self.initialize('put_update_notes_slide_shape', 'folder', request.folder)
        ok = False
        try:
            self.api.put_update_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape', 'folder')

    def test_put_update_notes_slide_shape_invalid_storage(self):
        """Test case for put_update_notes_slide_shape with invalid storage
        """
        request = self.__prepare_put_update_notes_slide_shape_request()
        request.storage = self.get_invalid_test_value('put_update_notes_slide_shape', 'storage', request.storage, 'str')
        self.initialize('put_update_notes_slide_shape', 'storage', request.storage)
        ok = False
        try:
            self.api.put_update_notes_slide_shape(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape', 'storage')

    def __prepare_put_update_notes_slide_shape_request(self):
        name = self.get_test_value('put_update_notes_slide_shape', 'name', 'str')
        slide_index = self.get_test_value('put_update_notes_slide_shape', 'slide_index', 'int')
        shape_index = self.get_test_value('put_update_notes_slide_shape', 'shape_index', 'int')
        dto = self.get_test_value('put_update_notes_slide_shape', 'dto', 'ShapeBase')
        password = self.get_test_value('put_update_notes_slide_shape', 'password', 'str')
        folder = self.get_test_value('put_update_notes_slide_shape', 'folder', 'str')
        storage = self.get_test_value('put_update_notes_slide_shape', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutUpdateNotesSlideShapeRequest(name, slide_index, shape_index, dto, password, folder, storage)

    def test_put_update_notes_slide_shape_paragraph(self):
        """Test case for put_update_notes_slide_shape_paragraph
        """
        request = self.__prepare_put_update_notes_slide_shape_paragraph_request()
        self.initialize('put_update_notes_slide_shape_paragraph', None, None)
        response = self.api.put_update_notes_slide_shape_paragraph(request)
        self.assertIsNotNone(response)

    def test_put_update_notes_slide_shape_paragraph_invalid_name(self):
        """Test case for put_update_notes_slide_shape_paragraph with invalid name
        """
        request = self.__prepare_put_update_notes_slide_shape_paragraph_request()
        request.name = self.get_invalid_test_value('put_update_notes_slide_shape_paragraph', 'name', request.name, 'str')
        self.initialize('put_update_notes_slide_shape_paragraph', 'name', request.name)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_paragraph', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_paragraph', 'name')

    def test_put_update_notes_slide_shape_paragraph_invalid_slide_index(self):
        """Test case for put_update_notes_slide_shape_paragraph with invalid slide_index
        """
        request = self.__prepare_put_update_notes_slide_shape_paragraph_request()
        request.slide_index = self.get_invalid_test_value('put_update_notes_slide_shape_paragraph', 'slide_index', request.slide_index, 'int')
        self.initialize('put_update_notes_slide_shape_paragraph', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_paragraph', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_paragraph', 'slide_index')

    def test_put_update_notes_slide_shape_paragraph_invalid_shape_index(self):
        """Test case for put_update_notes_slide_shape_paragraph with invalid shape_index
        """
        request = self.__prepare_put_update_notes_slide_shape_paragraph_request()
        request.shape_index = self.get_invalid_test_value('put_update_notes_slide_shape_paragraph', 'shape_index', request.shape_index, 'int')
        self.initialize('put_update_notes_slide_shape_paragraph', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_paragraph', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_paragraph', 'shape_index')

    def test_put_update_notes_slide_shape_paragraph_invalid_paragraph_index(self):
        """Test case for put_update_notes_slide_shape_paragraph with invalid paragraph_index
        """
        request = self.__prepare_put_update_notes_slide_shape_paragraph_request()
        request.paragraph_index = self.get_invalid_test_value('put_update_notes_slide_shape_paragraph', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('put_update_notes_slide_shape_paragraph', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_paragraph', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_paragraph', 'paragraph_index')

    def test_put_update_notes_slide_shape_paragraph_invalid_dto(self):
        """Test case for put_update_notes_slide_shape_paragraph with invalid dto
        """
        request = self.__prepare_put_update_notes_slide_shape_paragraph_request()
        request.dto = self.get_invalid_test_value('put_update_notes_slide_shape_paragraph', 'dto', request.dto, 'Paragraph')
        self.initialize('put_update_notes_slide_shape_paragraph', 'dto', request.dto)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_paragraph', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_paragraph', 'dto')

    def test_put_update_notes_slide_shape_paragraph_invalid_password(self):
        """Test case for put_update_notes_slide_shape_paragraph with invalid password
        """
        request = self.__prepare_put_update_notes_slide_shape_paragraph_request()
        request.password = self.get_invalid_test_value('put_update_notes_slide_shape_paragraph', 'password', request.password, 'str')
        self.initialize('put_update_notes_slide_shape_paragraph', 'password', request.password)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_paragraph', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_paragraph', 'password')

    def test_put_update_notes_slide_shape_paragraph_invalid_folder(self):
        """Test case for put_update_notes_slide_shape_paragraph with invalid folder
        """
        request = self.__prepare_put_update_notes_slide_shape_paragraph_request()
        request.folder = self.get_invalid_test_value('put_update_notes_slide_shape_paragraph', 'folder', request.folder, 'str')
        self.initialize('put_update_notes_slide_shape_paragraph', 'folder', request.folder)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_paragraph', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_paragraph', 'folder')

    def test_put_update_notes_slide_shape_paragraph_invalid_storage(self):
        """Test case for put_update_notes_slide_shape_paragraph with invalid storage
        """
        request = self.__prepare_put_update_notes_slide_shape_paragraph_request()
        request.storage = self.get_invalid_test_value('put_update_notes_slide_shape_paragraph', 'storage', request.storage, 'str')
        self.initialize('put_update_notes_slide_shape_paragraph', 'storage', request.storage)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_paragraph(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_paragraph', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_paragraph', 'storage')

    def __prepare_put_update_notes_slide_shape_paragraph_request(self):
        name = self.get_test_value('put_update_notes_slide_shape_paragraph', 'name', 'str')
        slide_index = self.get_test_value('put_update_notes_slide_shape_paragraph', 'slide_index', 'int')
        shape_index = self.get_test_value('put_update_notes_slide_shape_paragraph', 'shape_index', 'int')
        paragraph_index = self.get_test_value('put_update_notes_slide_shape_paragraph', 'paragraph_index', 'int')
        dto = self.get_test_value('put_update_notes_slide_shape_paragraph', 'dto', 'Paragraph')
        password = self.get_test_value('put_update_notes_slide_shape_paragraph', 'password', 'str')
        folder = self.get_test_value('put_update_notes_slide_shape_paragraph', 'folder', 'str')
        storage = self.get_test_value('put_update_notes_slide_shape_paragraph', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutUpdateNotesSlideShapeParagraphRequest(name, slide_index, shape_index, paragraph_index, dto, password, folder, storage)

    def test_put_update_notes_slide_shape_portion(self):
        """Test case for put_update_notes_slide_shape_portion
        """
        request = self.__prepare_put_update_notes_slide_shape_portion_request()
        self.initialize('put_update_notes_slide_shape_portion', None, None)
        response = self.api.put_update_notes_slide_shape_portion(request)
        self.assertIsNotNone(response)

    def test_put_update_notes_slide_shape_portion_invalid_name(self):
        """Test case for put_update_notes_slide_shape_portion with invalid name
        """
        request = self.__prepare_put_update_notes_slide_shape_portion_request()
        request.name = self.get_invalid_test_value('put_update_notes_slide_shape_portion', 'name', request.name, 'str')
        self.initialize('put_update_notes_slide_shape_portion', 'name', request.name)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_portion', 'name', request.name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_portion', 'name')

    def test_put_update_notes_slide_shape_portion_invalid_slide_index(self):
        """Test case for put_update_notes_slide_shape_portion with invalid slide_index
        """
        request = self.__prepare_put_update_notes_slide_shape_portion_request()
        request.slide_index = self.get_invalid_test_value('put_update_notes_slide_shape_portion', 'slide_index', request.slide_index, 'int')
        self.initialize('put_update_notes_slide_shape_portion', 'slide_index', request.slide_index)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_portion', 'slide_index', request.slide_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_portion', 'slide_index')

    def test_put_update_notes_slide_shape_portion_invalid_shape_index(self):
        """Test case for put_update_notes_slide_shape_portion with invalid shape_index
        """
        request = self.__prepare_put_update_notes_slide_shape_portion_request()
        request.shape_index = self.get_invalid_test_value('put_update_notes_slide_shape_portion', 'shape_index', request.shape_index, 'int')
        self.initialize('put_update_notes_slide_shape_portion', 'shape_index', request.shape_index)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_portion', 'shape_index', request.shape_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_portion', 'shape_index')

    def test_put_update_notes_slide_shape_portion_invalid_paragraph_index(self):
        """Test case for put_update_notes_slide_shape_portion with invalid paragraph_index
        """
        request = self.__prepare_put_update_notes_slide_shape_portion_request()
        request.paragraph_index = self.get_invalid_test_value('put_update_notes_slide_shape_portion', 'paragraph_index', request.paragraph_index, 'int')
        self.initialize('put_update_notes_slide_shape_portion', 'paragraph_index', request.paragraph_index)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_portion', 'paragraph_index', request.paragraph_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_portion', 'paragraph_index')

    def test_put_update_notes_slide_shape_portion_invalid_portion_index(self):
        """Test case for put_update_notes_slide_shape_portion with invalid portion_index
        """
        request = self.__prepare_put_update_notes_slide_shape_portion_request()
        request.portion_index = self.get_invalid_test_value('put_update_notes_slide_shape_portion', 'portion_index', request.portion_index, 'int')
        self.initialize('put_update_notes_slide_shape_portion', 'portion_index', request.portion_index)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_portion', 'portion_index', request.portion_index)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_portion', 'portion_index')

    def test_put_update_notes_slide_shape_portion_invalid_dto(self):
        """Test case for put_update_notes_slide_shape_portion with invalid dto
        """
        request = self.__prepare_put_update_notes_slide_shape_portion_request()
        request.dto = self.get_invalid_test_value('put_update_notes_slide_shape_portion', 'dto', request.dto, 'Portion')
        self.initialize('put_update_notes_slide_shape_portion', 'dto', request.dto)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_portion', 'dto', request.dto)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_portion', 'dto')

    def test_put_update_notes_slide_shape_portion_invalid_password(self):
        """Test case for put_update_notes_slide_shape_portion with invalid password
        """
        request = self.__prepare_put_update_notes_slide_shape_portion_request()
        request.password = self.get_invalid_test_value('put_update_notes_slide_shape_portion', 'password', request.password, 'str')
        self.initialize('put_update_notes_slide_shape_portion', 'password', request.password)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_portion', 'password', request.password)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_portion', 'password')

    def test_put_update_notes_slide_shape_portion_invalid_folder(self):
        """Test case for put_update_notes_slide_shape_portion with invalid folder
        """
        request = self.__prepare_put_update_notes_slide_shape_portion_request()
        request.folder = self.get_invalid_test_value('put_update_notes_slide_shape_portion', 'folder', request.folder, 'str')
        self.initialize('put_update_notes_slide_shape_portion', 'folder', request.folder)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_portion', 'folder', request.folder)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_portion', 'folder')

    def test_put_update_notes_slide_shape_portion_invalid_storage(self):
        """Test case for put_update_notes_slide_shape_portion with invalid storage
        """
        request = self.__prepare_put_update_notes_slide_shape_portion_request()
        request.storage = self.get_invalid_test_value('put_update_notes_slide_shape_portion', 'storage', request.storage, 'str')
        self.initialize('put_update_notes_slide_shape_portion', 'storage', request.storage)
        ok = False
        try:
            self.api.put_update_notes_slide_shape_portion(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'put_update_notes_slide_shape_portion', 'storage', request.storage)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('put_update_notes_slide_shape_portion', 'storage')

    def __prepare_put_update_notes_slide_shape_portion_request(self):
        name = self.get_test_value('put_update_notes_slide_shape_portion', 'name', 'str')
        slide_index = self.get_test_value('put_update_notes_slide_shape_portion', 'slide_index', 'int')
        shape_index = self.get_test_value('put_update_notes_slide_shape_portion', 'shape_index', 'int')
        paragraph_index = self.get_test_value('put_update_notes_slide_shape_portion', 'paragraph_index', 'int')
        portion_index = self.get_test_value('put_update_notes_slide_shape_portion', 'portion_index', 'int')
        dto = self.get_test_value('put_update_notes_slide_shape_portion', 'dto', 'Portion')
        password = self.get_test_value('put_update_notes_slide_shape_portion', 'password', 'str')
        folder = self.get_test_value('put_update_notes_slide_shape_portion', 'folder', 'str')
        storage = self.get_test_value('put_update_notes_slide_shape_portion', 'storage', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.PutUpdateNotesSlideShapePortionRequest(name, slide_index, shape_index, paragraph_index, portion_index, dto, password, folder, storage)

    def test_storage_exists(self):
        """Test case for storage_exists
        """
        request = self.__prepare_storage_exists_request()
        self.initialize('storage_exists', None, None)
        response = self.api.storage_exists(request)
        self.assertIsNotNone(response)

    def test_storage_exists_invalid_storage_name(self):
        """Test case for storage_exists with invalid storage_name
        """
        request = self.__prepare_storage_exists_request()
        request.storage_name = self.get_invalid_test_value('storage_exists', 'storage_name', request.storage_name, 'str')
        self.initialize('storage_exists', 'storage_name', request.storage_name)
        ok = False
        try:
            self.api.storage_exists(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'storage_exists', 'storage_name', request.storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('storage_exists', 'storage_name')

    def __prepare_storage_exists_request(self):
        storage_name = self.get_test_value('storage_exists', 'storage_name', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.StorageExistsRequest(storage_name)

    def test_upload_file(self):
        """Test case for upload_file
        """
        request = self.__prepare_upload_file_request()
        self.initialize('upload_file', None, None)
        response = self.api.upload_file(request)
        self.assertIsNotNone(response)

    def test_upload_file_invalid_file(self):
        """Test case for upload_file with invalid file
        """
        request = self.__prepare_upload_file_request()
        request.file = self.get_invalid_test_value('upload_file', 'file', request.file, 'file')
        self.initialize('upload_file', 'file', request.file)
        ok = False
        try:
            self.api.upload_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'upload_file', 'file', request.file)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('upload_file', 'file')

    def test_upload_file_invalid_path(self):
        """Test case for upload_file with invalid path
        """
        request = self.__prepare_upload_file_request()
        request.path = self.get_invalid_test_value('upload_file', 'path', request.path, 'str')
        self.initialize('upload_file', 'path', request.path)
        ok = False
        try:
            self.api.upload_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'upload_file', 'path', request.path)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('upload_file', 'path')

    def test_upload_file_invalid_storage_name(self):
        """Test case for upload_file with invalid storage_name
        """
        request = self.__prepare_upload_file_request()
        request.storage_name = self.get_invalid_test_value('upload_file', 'storage_name', request.storage_name, 'str')
        self.initialize('upload_file', 'storage_name', request.storage_name)
        ok = False
        try:
            self.api.upload_file(request)
            ok = True
        except ApiException as ex:
            self.assert_exception(ex, 'upload_file', 'storage_name', request.storage_name)
        except Exception:
            pass
        if ok:
            self.assert_no_exception('upload_file', 'storage_name')

    def __prepare_upload_file_request(self):
        file = self.get_test_value('upload_file', 'file', 'file')
        path = self.get_test_value('upload_file', 'path', 'str')
        storage_name = self.get_test_value('upload_file', 'storage_name', 'str')
        return asposeslidescloud.models.requests.slides_api_requests.UploadFileRequest(file, path, storage_name)


if __name__ == '__main__':
    unittest.main()
