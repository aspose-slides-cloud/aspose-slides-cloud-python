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

import inspect
import json
import os
import re
import unittest
import asposeslidescloud
from asposeslidescloud import models
from asposeslidescloud.api_client import ApiClient
from asposeslidescloud.apis.slides_api import SlidesApi
from asposeslidescloud.configuration import Configuration
from asposeslidescloud.rest import ApiException

base_test_path = '../'
if inspect.stack().pop().filename.endswith('run_tests.py'):
    base_test_path = ''

class BaseTest(unittest.TestCase):

    __test__ = False
    
    slides_api_configuration = None
    slides_async_api_configuration = None
    slides_api = None
    slides_async_api = None
    
    def __init__(self, *args, **kwargs):
        super(BaseTest, self).__init__(*args, **kwargs)

        self.test_data_path = "TestData"
        self.folder_name = "TempSlidesSDK"
        self.changed_file_name = "changedtest.pptx"
        self.file_name = "test.pptx"
        self.file_password = "password"

        if not BaseTest.slides_api:
            with open(base_test_path + 'testConfig.json') as f:
                config = json.loads(f.read())
            BaseTest.slides_api_configuration = self.create_configuration(config)
            BaseTest.slides_async_api_configuration = self.create_configuration(config)
            if 'AsyncBaseUrl' in config:
                BaseTest.slides_async_api_configuration.base_url = config['AsyncBaseUrl']

            with open(base_test_path + 'testRules.json') as f:
                BaseTest.test_rules = json.loads(f.read())

            BaseTest.slides_api = asposeslidescloud.apis.slides_api.SlidesApi(self.slides_api_configuration)  # noqa: E501
            BaseTest.slides_async_api = asposeslidescloud.apis.slides_async_api.SlidesAsyncApi(self.slides_async_api_configuration)  # noqa: E501
    
    def create_configuration(self, config):
        configuration = Configuration()
        configuration.app_sid = config['ClientId']
        configuration.app_key = config['ClientSecret']
        configuration.base_url = config['BaseUrl']
        configuration.auth_base_url = config['BaseUrl']
        if 'AuthBaseUrl' in config:
            configuration.auth_base_url = config['AuthBaseUrl']
        configuration.debug = config['Debug']
        configuration.verify_ssl = not 'AllowInsecureRequests' in config or not config['AllowInsecureRequests']
        return configuration
