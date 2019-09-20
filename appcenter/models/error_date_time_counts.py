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


class ErrorDateTimeCounts(object):
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
        '_datetime': 'str',
        'count': 'int'
    }

    attribute_map = {
        '_datetime': 'datetime',
        'count': 'count'
    }

    def __init__(self, _datetime=None, count=None):  # noqa: E501
        """ErrorDateTimeCounts - a model defined in Swagger"""  # noqa: E501
        self.__datetime = None
        self._count = None
        self.discriminator = None
        if _datetime is not None:
            self._datetime = _datetime
        if count is not None:
            self.count = count

    @property
    def _datetime(self):
        """Gets the _datetime of this ErrorDateTimeCounts.  # noqa: E501

        the ISO 8601 datetime  # noqa: E501

        :return: The _datetime of this ErrorDateTimeCounts.  # noqa: E501
        :rtype: str
        """
        return self.__datetime

    @_datetime.setter
    def _datetime(self, _datetime):
        """Sets the _datetime of this ErrorDateTimeCounts.

        the ISO 8601 datetime  # noqa: E501

        :param _datetime: The _datetime of this ErrorDateTimeCounts.  # noqa: E501
        :type: str
        """

        self.__datetime = _datetime

    @property
    def count(self):
        """Gets the count of this ErrorDateTimeCounts.  # noqa: E501

        count of the object  # noqa: E501

        :return: The count of this ErrorDateTimeCounts.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ErrorDateTimeCounts.

        count of the object  # noqa: E501

        :param count: The count of this ErrorDateTimeCounts.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(ErrorDateTimeCounts, dict):
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
        if not isinstance(other, ErrorDateTimeCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
