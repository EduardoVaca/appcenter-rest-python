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


class CrashGroupPlace(object):
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
        'place_name': 'str',
        'crash_count': 'int'
    }

    attribute_map = {
        'place_name': 'place_name',
        'crash_count': 'crash_count'
    }

    def __init__(self, place_name=None, crash_count=None):  # noqa: E501
        """CrashGroupPlace - a model defined in Swagger"""  # noqa: E501
        self._place_name = None
        self._crash_count = None
        self.discriminator = None
        if place_name is not None:
            self.place_name = place_name
        if crash_count is not None:
            self.crash_count = crash_count

    @property
    def place_name(self):
        """Gets the place_name of this CrashGroupPlace.  # noqa: E501

        Place name.  # noqa: E501

        :return: The place_name of this CrashGroupPlace.  # noqa: E501
        :rtype: str
        """
        return self._place_name

    @place_name.setter
    def place_name(self, place_name):
        """Sets the place_name of this CrashGroupPlace.

        Place name.  # noqa: E501

        :param place_name: The place_name of this CrashGroupPlace.  # noqa: E501
        :type: str
        """

        self._place_name = place_name

    @property
    def crash_count(self):
        """Gets the crash_count of this CrashGroupPlace.  # noqa: E501

        Count of places.  # noqa: E501

        :return: The crash_count of this CrashGroupPlace.  # noqa: E501
        :rtype: int
        """
        return self._crash_count

    @crash_count.setter
    def crash_count(self, crash_count):
        """Sets the crash_count of this CrashGroupPlace.

        Count of places.  # noqa: E501

        :param crash_count: The crash_count of this CrashGroupPlace.  # noqa: E501
        :type: int
        """

        self._crash_count = crash_count

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
        if issubclass(CrashGroupPlace, dict):
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
        if not isinstance(other, CrashGroupPlace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
