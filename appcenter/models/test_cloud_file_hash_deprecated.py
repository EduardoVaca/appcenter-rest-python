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


class TestCloudFileHashDeprecated(object):
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
        'file_type': 'str',
        'checksum': 'str',
        'relative_path': 'str',
        'byte_range': 'str'
    }

    attribute_map = {
        'file_type': 'file_type',
        'checksum': 'checksum',
        'relative_path': 'relative_path',
        'byte_range': 'byte_range'
    }

    def __init__(self, file_type=None, checksum=None, relative_path=None, byte_range=None):  # noqa: E501
        """TestCloudFileHashDeprecated - a model defined in Swagger"""  # noqa: E501
        self._file_type = None
        self._checksum = None
        self._relative_path = None
        self._byte_range = None
        self.discriminator = None
        self.file_type = file_type
        self.checksum = checksum
        self.relative_path = relative_path
        if byte_range is not None:
            self.byte_range = byte_range

    @property
    def file_type(self):
        """Gets the file_type of this TestCloudFileHashDeprecated.  # noqa: E501

        Type of the file  # noqa: E501

        :return: The file_type of this TestCloudFileHashDeprecated.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this TestCloudFileHashDeprecated.

        Type of the file  # noqa: E501

        :param file_type: The file_type of this TestCloudFileHashDeprecated.  # noqa: E501
        :type: str
        """
        if file_type is None:
            raise ValueError("Invalid value for `file_type`, must not be `None`")  # noqa: E501
        allowed_values = ["dsym-file", "app-file", "test-file"]  # noqa: E501
        if file_type not in allowed_values:
            raise ValueError(
                "Invalid value for `file_type` ({0}), must be one of {1}"  # noqa: E501
                .format(file_type, allowed_values)
            )

        self._file_type = file_type

    @property
    def checksum(self):
        """Gets the checksum of this TestCloudFileHashDeprecated.  # noqa: E501

        SHA256 hash of the file  # noqa: E501

        :return: The checksum of this TestCloudFileHashDeprecated.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this TestCloudFileHashDeprecated.

        SHA256 hash of the file  # noqa: E501

        :param checksum: The checksum of this TestCloudFileHashDeprecated.  # noqa: E501
        :type: str
        """
        if checksum is None:
            raise ValueError("Invalid value for `checksum`, must not be `None`")  # noqa: E501

        self._checksum = checksum

    @property
    def relative_path(self):
        """Gets the relative_path of this TestCloudFileHashDeprecated.  # noqa: E501

        Relative path of the file  # noqa: E501

        :return: The relative_path of this TestCloudFileHashDeprecated.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this TestCloudFileHashDeprecated.

        Relative path of the file  # noqa: E501

        :param relative_path: The relative_path of this TestCloudFileHashDeprecated.  # noqa: E501
        :type: str
        """
        if relative_path is None:
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def byte_range(self):
        """Gets the byte_range of this TestCloudFileHashDeprecated.  # noqa: E501

        Range of bytes required to verify ownership of the file  # noqa: E501

        :return: The byte_range of this TestCloudFileHashDeprecated.  # noqa: E501
        :rtype: str
        """
        return self._byte_range

    @byte_range.setter
    def byte_range(self, byte_range):
        """Sets the byte_range of this TestCloudFileHashDeprecated.

        Range of bytes required to verify ownership of the file  # noqa: E501

        :param byte_range: The byte_range of this TestCloudFileHashDeprecated.  # noqa: E501
        :type: str
        """

        self._byte_range = byte_range

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
        if issubclass(TestCloudFileHashDeprecated, dict):
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
        if not isinstance(other, TestCloudFileHashDeprecated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other