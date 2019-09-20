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


class EventPropertyValue(object):
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
        'name': 'str',
        'count': 'int',
        'previous_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'count': 'count',
        'previous_count': 'previous_count'
    }

    def __init__(self, name=None, count=None, previous_count=None):  # noqa: E501
        """EventPropertyValue - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._count = None
        self._previous_count = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if count is not None:
            self.count = count
        if previous_count is not None:
            self.previous_count = previous_count

    @property
    def name(self):
        """Gets the name of this EventPropertyValue.  # noqa: E501

        The event property value name.  # noqa: E501

        :return: The name of this EventPropertyValue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventPropertyValue.

        The event property value name.  # noqa: E501

        :param name: The name of this EventPropertyValue.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def count(self):
        """Gets the count of this EventPropertyValue.  # noqa: E501

        The count of the the event property value.  # noqa: E501

        :return: The count of this EventPropertyValue.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this EventPropertyValue.

        The count of the the event property value.  # noqa: E501

        :param count: The count of this EventPropertyValue.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def previous_count(self):
        """Gets the previous_count of this EventPropertyValue.  # noqa: E501

        The count of previous time range of the event property value.  # noqa: E501

        :return: The previous_count of this EventPropertyValue.  # noqa: E501
        :rtype: int
        """
        return self._previous_count

    @previous_count.setter
    def previous_count(self, previous_count):
        """Sets the previous_count of this EventPropertyValue.

        The count of previous time range of the event property value.  # noqa: E501

        :param previous_count: The previous_count of this EventPropertyValue.  # noqa: E501
        :type: int
        """

        self._previous_count = previous_count

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
        if issubclass(EventPropertyValue, dict):
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
        if not isinstance(other, EventPropertyValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
