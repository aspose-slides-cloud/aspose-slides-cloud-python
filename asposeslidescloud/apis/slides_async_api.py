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

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from asposeslidescloud.apis.api_base import ApiBase
from asposeslidescloud.api_client import ApiClient
from asposeslidescloud.models import *

class SlidesAsyncApi(ApiBase):

    def __init__(self, configuration = None, app_sid = None, app_key = None):
        super(SlidesAsyncApi, self).__init__(configuration, app_sid, app_key)

    def get_operation_result(self, id, **kwargs):  # noqa: E501
        """get_operation_result  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.(id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param id 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.get_operation_result_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_operation_result_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_operation_result_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_operation_result  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_operation_result_with_http_info(id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param id 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_operation_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if not id:
            raise ValueError("Missing the required parameter `id` when calling `get_operation_result`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['id'] = id  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        param_files = {}

        body_params = None

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/slides/async/{id}/result', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=param_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_operation_status(self, id, **kwargs):  # noqa: E501
        """get_operation_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.(id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param id 
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.get_operation_status_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_operation_status_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_operation_status_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_operation_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_operation_status_with_http_info(id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param id 
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_operation_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if not id:
            raise ValueError("Missing the required parameter `id` when calling `get_operation_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['id'] = id  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        param_files = {}

        body_params = None

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/slides/async/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=param_files,
            response_type='Operation',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_convert(self, document, format, password = None, storage = None, fonts_folder = None, slides = None, options = None, **kwargs):  # noqa: E501
        """start_convert  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.(document, format, password, storage, fonts_folder, slides, options, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param document Document data.
        :param format 
        :param password 
        :param storage 
        :param fonts_folder 
        :param slides 
        :param options 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.start_convert_with_http_info(document, format, password, storage, fonts_folder, slides, options, **kwargs)  # noqa: E501
        else:
            (data) = self.start_convert_with_http_info(document, format, password, storage, fonts_folder, slides, options, **kwargs)  # noqa: E501
            return data

    def start_convert_with_http_info(self, document, format, password = None, storage = None, fonts_folder = None, slides = None, options = None, **kwargs):  # noqa: E501
        """start_convert  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.start_convert_with_http_info(document, format, password, storage, fonts_folder, slides, options, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param document Document data.
        :param format 
        :param password 
        :param storage 
        :param fonts_folder 
        :param slides 
        :param options 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_convert" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document' is set
        if not document:
            raise ValueError("Missing the required parameter `document` when calling `start_convert`")  # noqa: E501
        # verify the required parameter 'format' is set
        if not format:
            raise ValueError("Missing the required parameter `format` when calling `start_convert`")  # noqa: E501
        # verify the value of parameter 'format' is valid
        if not format.upper() in ExportFormat.__dict__:
            raise ValueError("Invalid value for parameter `format` when calling `start_convert`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['format'] = format  # noqa: E501

        query_params = []
        if storage:
            query_params.append(('storage', storage))  # noqa: E501
        if fonts_folder:
            query_params.append(('fontsFolder', fonts_folder))  # noqa: E501
        if slides:
            query_params.append(('slides', slides))  # noqa: E501
            collection_formats['slides'] = ''  # noqa: E501

        header_params = {}
        if password:
            header_params['password'] = password  # noqa: E501

        form_params = []
        param_files = {}
        if document:
            param_files['document'] = document  # noqa: E501

        body_params = None
        if options:
            body_params = options

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/slides/async/convert/{format}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=param_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_convert_and_save(self, document, format, out_path, password = None, storage = None, fonts_folder = None, slides = None, options = None, **kwargs):  # noqa: E501
        """start_convert_and_save  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.(document, format, out_path, password, storage, fonts_folder, slides, options, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param document Document data.
        :param format 
        :param out_path 
        :param password 
        :param storage 
        :param fonts_folder 
        :param slides 
        :param options 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.start_convert_and_save_with_http_info(document, format, out_path, password, storage, fonts_folder, slides, options, **kwargs)  # noqa: E501
        else:
            (data) = self.start_convert_and_save_with_http_info(document, format, out_path, password, storage, fonts_folder, slides, options, **kwargs)  # noqa: E501
            return data

    def start_convert_and_save_with_http_info(self, document, format, out_path, password = None, storage = None, fonts_folder = None, slides = None, options = None, **kwargs):  # noqa: E501
        """start_convert_and_save  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.start_convert_and_save_with_http_info(document, format, out_path, password, storage, fonts_folder, slides, options, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param document Document data.
        :param format 
        :param out_path 
        :param password 
        :param storage 
        :param fonts_folder 
        :param slides 
        :param options 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_convert_and_save" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document' is set
        if not document:
            raise ValueError("Missing the required parameter `document` when calling `start_convert_and_save`")  # noqa: E501
        # verify the required parameter 'format' is set
        if not format:
            raise ValueError("Missing the required parameter `format` when calling `start_convert_and_save`")  # noqa: E501
        # verify the value of parameter 'format' is valid
        if not format.upper() in ExportFormat.__dict__:
            raise ValueError("Invalid value for parameter `format` when calling `start_convert_and_save`")  # noqa: E501
        # verify the required parameter 'out_path' is set
        if not out_path:
            raise ValueError("Missing the required parameter `out_path` when calling `start_convert_and_save`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['format'] = format  # noqa: E501

        query_params = []
        if out_path:
            query_params.append(('outPath', out_path))  # noqa: E501
        if storage:
            query_params.append(('storage', storage))  # noqa: E501
        if fonts_folder:
            query_params.append(('fontsFolder', fonts_folder))  # noqa: E501
        if slides:
            query_params.append(('slides', slides))  # noqa: E501
            collection_formats['slides'] = ''  # noqa: E501

        header_params = {}
        if password:
            header_params['password'] = password  # noqa: E501

        form_params = []
        param_files = {}
        if document:
            param_files['document'] = document  # noqa: E501

        body_params = None
        if options:
            body_params = options

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/slides/async/convert/{format}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=param_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_download_presentation(self, name, format, options = None, password = None, folder = None, storage = None, fonts_folder = None, slides = None, **kwargs):  # noqa: E501
        """start_download_presentation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.(name, format, options, password, folder, storage, fonts_folder, slides, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param name 
        :param format 
        :param options 
        :param password 
        :param folder 
        :param storage 
        :param fonts_folder 
        :param slides 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.start_download_presentation_with_http_info(name, format, options, password, folder, storage, fonts_folder, slides, **kwargs)  # noqa: E501
        else:
            (data) = self.start_download_presentation_with_http_info(name, format, options, password, folder, storage, fonts_folder, slides, **kwargs)  # noqa: E501
            return data

    def start_download_presentation_with_http_info(self, name, format, options = None, password = None, folder = None, storage = None, fonts_folder = None, slides = None, **kwargs):  # noqa: E501
        """start_download_presentation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.start_download_presentation_with_http_info(name, format, options, password, folder, storage, fonts_folder, slides, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param name 
        :param format 
        :param options 
        :param password 
        :param folder 
        :param storage 
        :param fonts_folder 
        :param slides 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_download_presentation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if not name:
            raise ValueError("Missing the required parameter `name` when calling `start_download_presentation`")  # noqa: E501
        # verify the required parameter 'format' is set
        if not format:
            raise ValueError("Missing the required parameter `format` when calling `start_download_presentation`")  # noqa: E501
        # verify the value of parameter 'format' is valid
        if not format.upper() in ExportFormat.__dict__:
            raise ValueError("Invalid value for parameter `format` when calling `start_download_presentation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['name'] = name  # noqa: E501
        path_params['format'] = format  # noqa: E501

        query_params = []
        if folder:
            query_params.append(('folder', folder))  # noqa: E501
        if storage:
            query_params.append(('storage', storage))  # noqa: E501
        if fonts_folder:
            query_params.append(('fontsFolder', fonts_folder))  # noqa: E501
        if slides:
            query_params.append(('slides', slides))  # noqa: E501
            collection_formats['slides'] = ''  # noqa: E501

        header_params = {}
        if password:
            header_params['password'] = password  # noqa: E501

        form_params = []
        param_files = {}

        body_params = None
        if options:
            body_params = options

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/slides/async/{name}/{format}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=param_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_merge(self, files = None, request = None, storage = None, **kwargs):  # noqa: E501
        """start_merge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.(files, request, storage, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param files Files to merge
        :param request 
        :param storage 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.start_merge_with_http_info(files, request, storage, **kwargs)  # noqa: E501
        else:
            (data) = self.start_merge_with_http_info(files, request, storage, **kwargs)  # noqa: E501
            return data

    def start_merge_with_http_info(self, files = None, request = None, storage = None, **kwargs):  # noqa: E501
        """start_merge  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.start_merge_with_http_info(files, request, storage, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param files Files to merge
        :param request 
        :param storage 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_merge" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if storage:
            query_params.append(('storage', storage))  # noqa: E501

        header_params = {}

        form_params = []
        param_files = {}
        param_files = files

        body_params = None
        if request:
            body_params = request

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/slides/async/merge', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=param_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_merge_and_save(self, out_path, files = None, request = None, storage = None, **kwargs):  # noqa: E501
        """start_merge_and_save  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.(out_path, files, request, storage, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param out_path 
        :param files Files to merge
        :param request 
        :param storage 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.start_merge_and_save_with_http_info(out_path, files, request, storage, **kwargs)  # noqa: E501
        else:
            (data) = self.start_merge_and_save_with_http_info(out_path, files, request, storage, **kwargs)  # noqa: E501
            return data

    def start_merge_and_save_with_http_info(self, out_path, files = None, request = None, storage = None, **kwargs):  # noqa: E501
        """start_merge_and_save  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.start_merge_and_save_with_http_info(out_path, files, request, storage, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param out_path 
        :param files Files to merge
        :param request 
        :param storage 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_merge_and_save" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'out_path' is set
        if not out_path:
            raise ValueError("Missing the required parameter `out_path` when calling `start_merge_and_save`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if out_path:
            query_params.append(('outPath', out_path))  # noqa: E501
        if storage:
            query_params.append(('storage', storage))  # noqa: E501

        header_params = {}

        form_params = []
        param_files = {}
        param_files = files

        body_params = None
        if request:
            body_params = request

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/slides/async/merge', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=param_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_save_presentation(self, name, format, out_path, options = None, password = None, folder = None, storage = None, fonts_folder = None, slides = None, **kwargs):  # noqa: E501
        """start_save_presentation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.(name, format, out_path, options, password, folder, storage, fonts_folder, slides, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param name 
        :param format 
        :param out_path 
        :param options 
        :param password 
        :param folder 
        :param storage 
        :param fonts_folder 
        :param slides 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.start_save_presentation_with_http_info(name, format, out_path, options, password, folder, storage, fonts_folder, slides, **kwargs)  # noqa: E501
        else:
            (data) = self.start_save_presentation_with_http_info(name, format, out_path, options, password, folder, storage, fonts_folder, slides, **kwargs)  # noqa: E501
            return data

    def start_save_presentation_with_http_info(self, name, format, out_path, options = None, password = None, folder = None, storage = None, fonts_folder = None, slides = None, **kwargs):  # noqa: E501
        """start_save_presentation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.start_save_presentation_with_http_info(name, format, out_path, options, password, folder, storage, fonts_folder, slides, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param name 
        :param format 
        :param out_path 
        :param options 
        :param password 
        :param folder 
        :param storage 
        :param fonts_folder 
        :param slides 
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_save_presentation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if not name:
            raise ValueError("Missing the required parameter `name` when calling `start_save_presentation`")  # noqa: E501
        # verify the required parameter 'format' is set
        if not format:
            raise ValueError("Missing the required parameter `format` when calling `start_save_presentation`")  # noqa: E501
        # verify the value of parameter 'format' is valid
        if not format.upper() in ExportFormat.__dict__:
            raise ValueError("Invalid value for parameter `format` when calling `start_save_presentation`")  # noqa: E501
        # verify the required parameter 'out_path' is set
        if not out_path:
            raise ValueError("Missing the required parameter `out_path` when calling `start_save_presentation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['name'] = name  # noqa: E501
        path_params['format'] = format  # noqa: E501

        query_params = []
        if out_path:
            query_params.append(('outPath', out_path))  # noqa: E501
        if folder:
            query_params.append(('folder', folder))  # noqa: E501
        if storage:
            query_params.append(('storage', storage))  # noqa: E501
        if fonts_folder:
            query_params.append(('fontsFolder', fonts_folder))  # noqa: E501
        if slides:
            query_params.append(('slides', slides))  # noqa: E501
            collection_formats['slides'] = ''  # noqa: E501

        header_params = {}
        if password:
            header_params['password'] = password  # noqa: E501

        form_params = []
        param_files = {}

        body_params = None
        if options:
            body_params = options

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            '/slides/async/{name}/{format}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=param_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', False),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
