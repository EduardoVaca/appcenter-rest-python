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


class ErrorAttachment(object):
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
        'size': 'int'
    }

    attribute_map = {
        'app_id': 'appId',
        'attachment_id': 'attachmentId',
        'crash_id': 'crashId',
        'blob_location': 'blobLocation',
        'content_type': 'contentType',
        'file_name': 'fileName',
        'created_time': 'createdTime',
        'size': 'size'
    }

    def __init__(self, app_id=None, attachment_id=None, crash_id=None, blob_location=None, content_type=None, file_name=None, created_time=None, size=None):  # noqa: E501
        """ErrorAttachment - a model defined in Swagger"""  # noqa: E501
        self._app_id = None
        self._attachment_id = None
        self._crash_id = None
        self._blob_location = None
        self._content_type = None
        self._file_name = None
        self._created_time = None
        self._size = None
        self.discriminator = None
        if app_id is not None:
            self.app_id = app_id
        if attachment_id is not None:
            self.attachment_id = attachment_id
        if crash_id is not None:
            self.crash_id = crash_id
        if blob_location is not None:
            self.blob_location = blob_location
        if content_type is not None:
            self.content_type = content_type
        if file_name is not None:
            self.file_name = file_name
        if created_time is not None:
            self.created_time = created_time
        if size is not None:
            self.size = size

    @property
    def app_id(self):
        """Gets the app_id of this ErrorAttachment.  # noqa: E501


        :return: The app_id of this ErrorAttachment.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ErrorAttachment.


        :param app_id: The app_id of this ErrorAttachment.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def attachment_id(self):
        """Gets the attachment_id of this ErrorAttachment.  # noqa: E501


        :return: The attachment_id of this ErrorAttachment.  # noqa: E501
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this ErrorAttachment.


        :param attachment_id: The attachment_id of this ErrorAttachment.  # noqa: E501
        :type: str
        """

        self._attachment_id = attachment_id

    @property
    def crash_id(self):
        """Gets the crash_id of this ErrorAttachment.  # noqa: E501


        :return: The crash_id of this ErrorAttachment.  # noqa: E501
        :rtype: str
        """
        return self._crash_id

    @crash_id.setter
    def crash_id(self, crash_id):
        """Sets the crash_id of this ErrorAttachment.


        :param crash_id: The crash_id of this ErrorAttachment.  # noqa: E501
        :type: str
        """

        self._crash_id = crash_id

    @property
    def blob_location(self):
        """Gets the blob_location of this ErrorAttachment.  # noqa: E501


        :return: The blob_location of this ErrorAttachment.  # noqa: E501
        :rtype: str
        """
        return self._blob_location

    @blob_location.setter
    def blob_location(self, blob_location):
        """Sets the blob_location of this ErrorAttachment.


        :param blob_location: The blob_location of this ErrorAttachment.  # noqa: E501
        :type: str
        """

        self._blob_location = blob_location

    @property
    def content_type(self):
        """Gets the content_type of this ErrorAttachment.  # noqa: E501


        :return: The content_type of this ErrorAttachment.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ErrorAttachment.


        :param content_type: The content_type of this ErrorAttachment.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def file_name(self):
        """Gets the file_name of this ErrorAttachment.  # noqa: E501


        :return: The file_name of this ErrorAttachment.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ErrorAttachment.


        :param file_name: The file_name of this ErrorAttachment.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def created_time(self):
        """Gets the created_time of this ErrorAttachment.  # noqa: E501


        :return: The created_time of this ErrorAttachment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ErrorAttachment.


        :param created_time: The created_time of this ErrorAttachment.  # noqa: E501
        :type: datetime
        """

        self._created_time = created_time

    @property
    def size(self):
        """Gets the size of this ErrorAttachment.  # noqa: E501


        :return: The size of this ErrorAttachment.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ErrorAttachment.


        :param size: The size of this ErrorAttachment.  # noqa: E501
        :type: int
        """

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
        if issubclass(ErrorAttachment, dict):
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
        if not isinstance(other, ErrorAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
