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


class Release(object):
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
        'release': 'str'
    }

    attribute_map = {
        'release': 'release'
    }

    def __init__(self, release=None):  # noqa: E501
        """Release - a model defined in Swagger"""  # noqa: E501
        self._release = None
        self.discriminator = None
        self.release = release

    @property
    def release(self):
        """Gets the release of this Release.  # noqa: E501

        Release Id.   # noqa: E501

        :return: The release of this Release.  # noqa: E501
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this Release.

        Release Id.   # noqa: E501

        :param release: The release of this Release.  # noqa: E501
        :type: str
        """
        if release is None:
            raise ValueError("Invalid value for `release`, must not be `None`")  # noqa: E501

        self._release = release

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
        if issubclass(Release, dict):
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
        if not isinstance(other, Release):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
