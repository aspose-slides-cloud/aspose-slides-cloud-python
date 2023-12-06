from __future__ import absolute_import

import os
import time

from test.base_test import BaseTest
import asposeslidescloud
from test import constant

class TestAsync(BaseTest):
    def setUp(self):
        self.max_tries = 10
        self.sleep_timeout = 3
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.slides_api_configuration)  # noqa: E501
        self.async_api = asposeslidescloud.apis.slides_async_api.SlidesAsyncApi(self.slides_async_api_configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_async_convert(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        operation_id = BaseTest.slides_async_api.start_convert(source, 'pdf', "password")

        for i in range(self.max_tries):
            time.sleep(self.sleep_timeout)
            operation = BaseTest.slides_async_api.get_operation_status(operation_id)
            if operation.status != 'Created' and operation.status != 'Enqueued' and operation.status != 'Started':
                break

        self.assertEqual('Finished', operation.status)
        self.assertIsNone(operation.error)

        converted = BaseTest.slides_async_api.get_operation_result(operation_id)
        self.assertGreater(os.path.getsize(converted), 0)

    def test_async_download_presentation(self):
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        operation_id = BaseTest.slides_async_api.start_download_presentation(file_name, 'pdf', None, "password", folder_name)

        for i in range(self.max_tries):
            time.sleep(self.sleep_timeout)
            operation = BaseTest.slides_async_api.get_operation_status(operation_id)
            if operation.status != 'Created' and operation.status != 'Enqueued' and operation.status != 'Started':
                break

        self.assertEqual('Finished', operation.status)
        self.assertIsNone(operation.error)

        converted = BaseTest.slides_async_api.get_operation_result(operation_id)
        self.assertGreater(os.path.getsize(converted), 0)

    def test_async_convert_and_save(self):
        out_path = constant.FOLDER_NAME + "/converted.pptx"
        BaseTest.slides_api.delete_file(out_path)
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/" + constant.FILE_NAME, 'rb') as f:
            source = f.read()
        operation_id = BaseTest.slides_async_api.start_convert_and_save(source, 'pdf', out_path, "password")

        for i in range(self.max_tries):
            time.sleep(self.sleep_timeout)
            operation = BaseTest.slides_async_api.get_operation_status(operation_id)
            if operation.status != 'Created' and operation.status != 'Enqueued' and operation.status != 'Started':
                break

        self.assertEqual('Finished', operation.status)
        self.assertIsNone(operation.error)

        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_async_save_presentation(self):
        out_path = constant.FOLDER_NAME + "/converted.pptx"
        BaseTest.slides_api.delete_file(out_path)
        folder_name = "TempSlidesSDK"
        file_name = "test.pptx"
        BaseTest.slides_api.copy_file("TempTests/" + file_name, folder_name + "/" + file_name)
        operation_id = BaseTest.slides_async_api.start_save_presentation(file_name, 'pdf', out_path, None, "password", folder_name)

        for i in range(self.max_tries):
            time.sleep(self.sleep_timeout)
            operation = BaseTest.slides_async_api.get_operation_status(operation_id)
            if operation.status != 'Created' and operation.status != 'Enqueued' and operation.status != 'Started':
                break

        self.assertEqual('Finished', operation.status)
        self.assertIsNone(operation.error)

        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_async_merge(self):
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/TemplateCV.pptx", 'rb') as f:
            source1 = f.read()
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/test-unprotected.pptx", 'rb') as f:
            source2 = f.read()
        files = [ source1, source2 ]
        operation_id = BaseTest.slides_async_api.start_merge(files)

        for i in range(self.max_tries):
            time.sleep(self.sleep_timeout)
            print(operation_id)
            operation = BaseTest.slides_async_api.get_operation_status(operation_id)
            if operation.status != 'Created' and operation.status != 'Enqueued' and operation.status != 'Started':
                break

        self.assertEqual('Finished', operation.status)
        self.assertIsNotNone(operation.progress)
        self.assertEqual(2, operation.progress.step_count)
        self.assertEqual(operation.progress.step_count, operation.progress.step_index)
        self.assertIsNone(operation.error)

        merged = BaseTest.slides_async_api.get_operation_result(operation_id)
        self.assertGreater(os.path.getsize(merged), 0)

    def test_async_merge_and_save(self):
        out_path = constant.FOLDER_NAME + "/merged.pptx"
        BaseTest.slides_api.delete_file(out_path)
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/TemplateCV.pptx", 'rb') as f:
            source1 = f.read()
        with open(constant.LOCAL_TEST_DATA_FOLDER + "/test-unprotected.pptx", 'rb') as f:
            source2 = f.read()
        files = [ source1, source2 ]
        operation_id = BaseTest.slides_async_api.start_merge_and_save(out_path, files)

        for i in range(self.max_tries):
            time.sleep(self.sleep_timeout)
            operation = BaseTest.slides_async_api.get_operation_status(operation_id)
            if operation.status != 'Created' and operation.status != 'Enqueued' and operation.status != 'Started':
                break

        self.assertEqual('Finished', operation.status)
        self.assertIsNotNone(operation.progress)
        self.assertEqual(2, operation.progress.step_count)
        self.assertEqual(operation.progress.step_count, operation.progress.step_index)
        self.assertIsNone(operation.error)

        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_async_bad_operation(self):
        operation_id = BaseTest.slides_async_api.start_download_presentation('IDoNotExist.pptx', 'pdf')

        for i in range(self.max_tries):
            time.sleep(self.sleep_timeout)
            operation = BaseTest.slides_async_api.get_operation_status(operation_id)
            if operation.status != 'Created' and operation.status != 'Enqueued' and operation.status != 'Started':
                break

        self.assertEqual('Failed', operation.status)
        self.assertIsNotNone(operation.error)
