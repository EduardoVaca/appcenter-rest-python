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
from appcenter.models.error_group_list_item import ErrorGroupListItem  # noqa: F401,E501


class ErrorGroups(object):
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
        'next_link': 'str',
        'error_groups': 'list[ErrorGroupListItem]'
    }

    attribute_map = {
        'next_link': 'nextLink',
        'error_groups': 'errorGroups'
    }

    def __init__(self, next_link=None, error_groups=None):  # noqa: E501
        """ErrorGroups - a model defined in Swagger"""  # noqa: E501
        self._next_link = None
        self._error_groups = None
        self.discriminator = None
        if next_link is not None:
            self.next_link = next_link
        if error_groups is not None:
            self.error_groups = error_groups

    @property
    def next_link(self):
        """Gets the next_link of this ErrorGroups.  # noqa: E501


        :return: The next_link of this ErrorGroups.  # noqa: E501
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this ErrorGroups.


        :param next_link: The next_link of this ErrorGroups.  # noqa: E501
        :type: str
        """

        self._next_link = next_link

    @property
    def error_groups(self):
        """Gets the error_groups of this ErrorGroups.  # noqa: E501


        :return: The error_groups of this ErrorGroups.  # noqa: E501
        :rtype: list[ErrorGroupListItem]
        """
        return self._error_groups

    @error_groups.setter
    def error_groups(self, error_groups):
        """Sets the error_groups of this ErrorGroups.


        :param error_groups: The error_groups of this ErrorGroups.  # noqa: E501
        :type: list[ErrorGroupListItem]
        """

        self._error_groups = error_groups

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
        if issubclass(ErrorGroups, dict):
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
        if not isinstance(other, ErrorGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
