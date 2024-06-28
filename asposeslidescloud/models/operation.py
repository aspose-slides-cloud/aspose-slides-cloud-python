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

import pprint
import re  # noqa: F401

import six


class Operation(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'method': 'str',
        'status': 'str',
        'progress': 'OperationProgress',
        'created': 'datetime',
        'started': 'datetime',
        'failed': 'datetime',
        'canceled': 'datetime',
        'finished': 'datetime',
        'error': 'str'
    }

    attribute_map = {
        'id': 'id',
        'method': 'method',
        'status': 'status',
        'progress': 'progress',
        'created': 'created',
        'started': 'started',
        'failed': 'failed',
        'canceled': 'canceled',
        'finished': 'finished',
        'error': 'error'
    }

    type_determiners = {
    }

    def __init__(self, id=None, method=None, status=None, progress=None, created=None, started=None, failed=None, canceled=None, finished=None, error=None):  # noqa: E501
        """Operation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._method = None
        self._status = None
        self._progress = None
        self._created = None
        self._started = None
        self._failed = None
        self._canceled = None
        self._finished = None
        self._error = None

        self.id = id
        self.method = method
        self.status = status
        if progress is not None:
            self.progress = progress
        if created is not None:
            self.created = created
        if started is not None:
            self.started = started
        if failed is not None:
            self.failed = failed
        if canceled is not None:
            self.canceled = canceled
        if finished is not None:
            self.finished = finished
        if error is not None:
            self.error = error

    @property
    def id(self):
        """Gets the id of this Operation.  # noqa: E501


        :return: The id of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Operation.


        :param id: The id of this Operation.  # noqa: E501
        :type: str
        """
        self._id = id

    @property
    def method(self):
        """Gets the method of this Operation.  # noqa: E501


        :return: The method of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Operation.


        :param method: The method of this Operation.  # noqa: E501
        :type: str
        """
        if method is not None:
            allowed_values = ["Convert", "DownloadPresentation", "ConvertAndSave", "SavePresentation", "Merge", "MergeAndSave"]  # noqa: E501
            if method.isdigit():
                int_method = int(method)
                if int_method < 0 or int_method >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                        .format(method, allowed_values)
                    )
                self._method = allowed_values[int_method]
                return
            if method not in allowed_values:
                raise ValueError(
                    "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                    .format(method, allowed_values)
                )
        self._method = method

    @property
    def status(self):
        """Gets the status of this Operation.  # noqa: E501


        :return: The status of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Operation.


        :param status: The status of this Operation.  # noqa: E501
        :type: str
        """
        if status is not None:
            allowed_values = ["Created", "Enqueued", "Started", "Failed", "Canceled", "Finished"]  # noqa: E501
            if status.isdigit():
                int_status = int(status)
                if int_status < 0 or int_status >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                        .format(status, allowed_values)
                    )
                self._status = allowed_values[int_status]
                return
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                    .format(status, allowed_values)
                )
        self._status = status

    @property
    def progress(self):
        """Gets the progress of this Operation.  # noqa: E501


        :return: The progress of this Operation.  # noqa: E501
        :rtype: OperationProgress
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Operation.


        :param progress: The progress of this Operation.  # noqa: E501
        :type: OperationProgress
        """
        self._progress = progress

    @property
    def created(self):
        """Gets the created of this Operation.  # noqa: E501


        :return: The created of this Operation.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Operation.


        :param created: The created of this Operation.  # noqa: E501
        :type: datetime
        """
        self._created = created

    @property
    def started(self):
        """Gets the started of this Operation.  # noqa: E501


        :return: The started of this Operation.  # noqa: E501
        :rtype: datetime
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this Operation.


        :param started: The started of this Operation.  # noqa: E501
        :type: datetime
        """
        self._started = started

    @property
    def failed(self):
        """Gets the failed of this Operation.  # noqa: E501


        :return: The failed of this Operation.  # noqa: E501
        :rtype: datetime
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this Operation.


        :param failed: The failed of this Operation.  # noqa: E501
        :type: datetime
        """
        self._failed = failed

    @property
    def canceled(self):
        """Gets the canceled of this Operation.  # noqa: E501


        :return: The canceled of this Operation.  # noqa: E501
        :rtype: datetime
        """
        return self._canceled

    @canceled.setter
    def canceled(self, canceled):
        """Sets the canceled of this Operation.


        :param canceled: The canceled of this Operation.  # noqa: E501
        :type: datetime
        """
        self._canceled = canceled

    @property
    def finished(self):
        """Gets the finished of this Operation.  # noqa: E501


        :return: The finished of this Operation.  # noqa: E501
        :rtype: datetime
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this Operation.


        :param finished: The finished of this Operation.  # noqa: E501
        :type: datetime
        """
        self._finished = finished

    @property
    def error(self):
        """Gets the error of this Operation.  # noqa: E501


        :return: The error of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Operation.


        :param error: The error of this Operation.  # noqa: E501
        :type: str
        """
        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Operation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
