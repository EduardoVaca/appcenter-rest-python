# coding: utf-8

"""
    App Center Client

    Microsoft Visual Studio App Center API  # noqa: E501

    OpenAPI spec version: preview
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CrashAttachment(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'app_id': 'str',
        'attachment_id': 'str',
        'crash_id': 'str',
        'blob_location': 'str',
        'content_type': 'str',
        'file_name': 'str',
        'created_time': 'datetime',
        'size': 'float'
    }

    attribute_map = {
        'app_id': 'app_id',
        'attachment_id': 'attachment_id',
        'crash_id': 'crash_id',
        'blob_location': 'blob_location',
        'content_type': 'content_type',
        'file_name': 'file_name',
        'created_time': 'created_time',
        'size': 'size'
    }

    def __init__(self, app_id=None, attachment_id=None, crash_id=None, blob_location=None, content_type=None, file_name=None, created_time=None, size=None):  # noqa: E501
        """CrashAttachment - a model defined in Swagger"""  # noqa: E501
        self._app_id = None
        self._attachment_id = None
        self._crash_id = None
        self._blob_location = None
        self._content_type = None
        self._file_name = None
        self._created_time = None
        self._size = None
        self.discriminator = None
        self.app_id = app_id
        self.attachment_id = attachment_id
        self.crash_id = crash_id
        self.blob_location = blob_location
        self.content_type = content_type
        self.file_name = file_name
        self.created_time = created_time
        self.size = size

    @property
    def app_id(self):
        """Gets the app_id of this CrashAttachment.  # noqa: E501


        :return: The app_id of this CrashAttachment.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CrashAttachment.


        :param app_id: The app_id of this CrashAttachment.  # noqa: E501
        :type: str
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def attachment_id(self):
        """Gets the attachment_id of this CrashAttachment.  # noqa: E501


        :return: The attachment_id of this CrashAttachment.  # noqa: E501
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this CrashAttachment.


        :param attachment_id: The attachment_id of this CrashAttachment.  # noqa: E501
        :type: str
        """
        if attachment_id is None:
            raise ValueError("Invalid value for `attachment_id`, must not be `None`")  # noqa: E501

        self._attachment_id = attachment_id

    @property
    def crash_id(self):
        """Gets the crash_id of this CrashAttachment.  # noqa: E501


        :return: The crash_id of this CrashAttachment.  # noqa: E501
        :rtype: str
        """
        return self._crash_id

    @crash_id.setter
    def crash_id(self, crash_id):
        """Sets the crash_id of this CrashAttachment.


        :param crash_id: The crash_id of this CrashAttachment.  # noqa: E501
        :type: str
        """
        if crash_id is None:
            raise ValueError("Invalid value for `crash_id`, must not be `None`")  # noqa: E501

        self._crash_id = crash_id

    @property
    def blob_location(self):
        """Gets the blob_location of this CrashAttachment.  # noqa: E501


        :return: The blob_location of this CrashAttachment.  # noqa: E501
        :rtype: str
        """
        return self._blob_location

    @blob_location.setter
    def blob_location(self, blob_location):
        """Sets the blob_location of this CrashAttachment.


        :param blob_location: The blob_location of this CrashAttachment.  # noqa: E501
        :type: str
        """
        if blob_location is None:
            raise ValueError("Invalid value for `blob_location`, must not be `None`")  # noqa: E501

        self._blob_location = blob_location

    @property
    def content_type(self):
        """Gets the content_type of this CrashAttachment.  # noqa: E501


        :return: The content_type of this CrashAttachment.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this CrashAttachment.


        :param content_type: The content_type of this CrashAttachment.  # noqa: E501
        :type: str
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

    @property
    def file_name(self):
        """Gets the file_name of this CrashAttachment.  # noqa: E501


        :return: The file_name of this CrashAttachment.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CrashAttachment.


        :param file_name: The file_name of this CrashAttachment.  # noqa: E501
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def created_time(self):
        """Gets the created_time of this CrashAttachment.  # noqa: E501


        :return: The created_time of this CrashAttachment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this CrashAttachment.


        :param created_time: The created_time of this CrashAttachment.  # noqa: E501
        :type: datetime
        """
        if created_time is None:
            raise ValueError("Invalid value for `created_time`, must not be `None`")  # noqa: E501

        self._created_time = created_time

    @property
    def size(self):
        """Gets the size of this CrashAttachment.  # noqa: E501


        :return: The size of this CrashAttachment.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CrashAttachment.


        :param size: The size of this CrashAttachment.  # noqa: E501
        :type: float
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

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
        if issubclass(CrashAttachment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CrashAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
