from __future__ import absolute_import

import os
import time

from test.base_test import BaseTest

class TestAsync(BaseTest):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_async_convert(self):
        with open(self.local_path, 'rb') as f:
            source = f.read()
        operation_id = BaseTest.slides_async_api.start_convert(source, 'pdf', self.password)
        self.await_good_operation(operation_id)
        converted = BaseTest.slides_async_api.get_operation_result(operation_id)
        self.assertGreater(os.path.getsize(converted), 0)

    def test_async_download_presentation(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        operation_id = BaseTest.slides_async_api.start_download_presentation(self.file_name, 'pdf', None, self.password, self.folder_name)
        self.await_good_operation(operation_id)
        converted = BaseTest.slides_async_api.get_operation_result(operation_id)
        self.assertGreater(os.path.getsize(converted), 0)

    def test_async_convert_and_save(self):
        out_path = self.folder_name + "/converted.pptx"
        BaseTest.slides_api.delete_file(out_path)
        with open(self.local_path, 'rb') as f:
            source = f.read()
        operation_id = BaseTest.slides_async_api.start_convert_and_save(source, 'pdf', out_path, self.password)
        self.await_good_operation(operation_id)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_async_save_presentation(self):
        out_path = self.folder_name + "/converted.pptx"
        BaseTest.slides_api.delete_file(out_path)
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        operation_id = BaseTest.slides_async_api.start_save_presentation(
            self.file_name, 'pdf', out_path, None, self.password, self.folder_name)
        self.await_good_operation(operation_id)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_async_merge(self):
        with open(self.test_data_path + "/TemplateCV.pptx", 'rb') as f:
            source1 = f.read()
        with open(self.test_data_path + "/test-unprotected.pptx", 'rb') as f:
            source2 = f.read()
        files = [ source1, source2 ]
        operation_id = BaseTest.slides_async_api.start_merge(files)
        operation = self.await_good_operation(operation_id)
        self.assertIsNotNone(operation.progress)
        self.assertEqual(2, operation.progress.step_count)
        self.assertEqual(operation.progress.step_count, operation.progress.step_index)

        merged = BaseTest.slides_async_api.get_operation_result(operation_id)
        self.assertGreater(os.path.getsize(merged), 0)

    def test_async_merge_and_save(self):
        out_path = self.folder_name + "/merged.pptx"
        BaseTest.slides_api.delete_file(out_path)
        with open(self.test_data_path + "/TemplateCV.pptx", 'rb') as f:
            source1 = f.read()
        with open(self.test_data_path + "/test-unprotected.pptx", 'rb') as f:
            source2 = f.read()
        files = [ source1, source2 ]
        operation_id = BaseTest.slides_async_api.start_merge_and_save(out_path, files)
        operation = self.await_good_operation(operation_id)
        self.assertIsNotNone(operation.progress)
        self.assertEqual(2, operation.progress.step_count)
        self.assertEqual(operation.progress.step_count, operation.progress.step_index)

        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_async_bad_operation(self):
        operation_id = BaseTest.slides_async_api.start_download_presentation('IDoNotExist.pptx', 'pdf')
        operation = self.await_operation(operation_id)
        self.assertEqual('Failed', operation.status)
        self.assertIsNotNone(operation.error)

    def await_good_operation(self, id):
        operation = self.await_operation(id)
        self.assertEqual('Finished', operation.status)
        self.assertIsNone(operation.error)
        return operation

    def await_operation(self, id):
        for i in range(10):
            time.sleep(3)
            operation = BaseTest.slides_async_api.get_operation_status(id)
            if operation.status != 'Created' and operation.status != 'Enqueued' and operation.status != 'Started':
                return operation
        return None     