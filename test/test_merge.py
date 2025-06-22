from __future__ import absolute_import

from asposeslidescloud import PresentationToMerge, OrderedMergeRequest, PresentationsMergeRequest
from test.base_test import BaseTest

class TestMerge(BaseTest):
    def setUp(self):
        self.file_name2 = "test-unprotected.pptx"
        self.path2 = self.folder_name + "/" + self.file_name2
        self.local_path2 = self.test_data_path + "/" + self.file_name2
        self.temp_path2 = self.temp_folder_name + "/" + self.file_name2

    def tearDown(self):
        pass

    def test_merge(self):
        file_name_pdf = "test.pdf"
        path_pdf = self.folder_name + "/" + file_name_pdf
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.copy_file(self.temp_path2, self.path2)
        BaseTest.slides_api.copy_file(self.temp_folder_name + "/" + file_name_pdf, path_pdf)
        request = PresentationsMergeRequest()
        request.presentation_paths = [ self.path2, path_pdf ]
        BaseTest.slides_api.merge(self.file_name, request, self.password, self.folder_name)

    def test_ordered_merge(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.copy_file(self.temp_path2, self.path2)
        request = OrderedMergeRequest()
        presentation = PresentationToMerge()
        presentation.path = self.path2
        presentation.slides = [ 2, 1 ]
        request.presentations = [ presentation ]
        BaseTest.slides_api.ordered_merge(self.file_name, request, self.password, self.folder_name)

    def test_merge_online(self):
        with open(self.test_data_path + "/TemplateCV.pptx", 'rb') as f:
            source1 = f.read()
        with open(self.local_path2, 'rb') as f:
            source2 = f.read()
        files = [ source1, source2 ]
        BaseTest.slides_api.merge_online(files)

    def test_merge_and_save_request(self):
        out_path = "out/out.pptx"
        with open(self.test_data_path + "/TemplateCV.pptx", 'rb') as f:
            source1 = f.read()
        with open(self.local_path2, 'rb') as f:
            source2 = f.read()
        files = [ source1, source2 ]
        BaseTest.slides_api.merge_and_save_online(out_path, files)
        self.assertTrue(BaseTest.slides_api.object_exists(out_path).exists)

    def test_merge_online_with_request(self):
        with open(self.local_path, 'rb') as f:
            source1 = f.read()
        with open(self.local_path2, 'rb') as f:
            source2 = f.read()
        files = [ source1, source2 ]
        request = OrderedMergeRequest()
        presentation1 = PresentationToMerge()
        presentation1.path = "file1"
        presentation1.password = self.password
        presentation2 = PresentationToMerge()
        presentation2.path = "file2"
        presentation2.slides = [ 1, 2 ]
        request.presentations = [ presentation1, presentation2 ]
        BaseTest.slides_api.merge_online(files, request)

    def test_merge_online_combined(self):
        BaseTest.slides_api.copy_file(self.temp_path2, self.path2)
        with open(self.local_path, 'rb') as f:
            source = f.read()
        files = [ source ]
        request = OrderedMergeRequest()
        presentation1 = PresentationToMerge()
        presentation1.path = "file1"
        presentation1.password = self.password
        presentation2 = PresentationToMerge()
        presentation2.path = "test-unprotected.pptx"
        presentation2.slides = [ 1, 2 ]
        presentation2.source = 'Storage'
        presentation2.path = self.path2
        request.presentations = [ presentation1, presentation2 ]
        BaseTest.slides_api.merge_online(files, request)

    def test_merge_online_url(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        request = OrderedMergeRequest()
        presentation1 = PresentationToMerge()
        presentation1.path = self.path
        presentation1.password = self.password
        presentation1.source = "Storage"
        presentation1.slides = [1, 2]
        presentation2 = PresentationToMerge()
        presentation2.path = "https://www.dropbox.com/scl/fi/nz3yt2wpg4eugiw12bz3g/info.pptx?rlkey=wju4vbi6h46q8733tzzvfgufz&e=1&st=pqt66x86&dl=1"
        presentation2.slides = [1]
        presentation2.source = 'Url'
        request.presentations = [presentation1, presentation2]
        BaseTest.slides_api.merge_online(None, request)
