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


class OrganizationRequest(object):
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
        'display_name': 'str',
        'name': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'name': 'name'
    }

    def __init__(self, display_name=None, name=None):  # noqa: E501
        """OrganizationRequest - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._name = None
        self.discriminator = None
        if display_name is not None:
            self.display_name = display_name
        if name is not None:
            self.name = name

    @property
    def display_name(self):
        """Gets the display_name of this OrganizationRequest.  # noqa: E501

        The display name of the organization  # noqa: E501

        :return: The display_name of this OrganizationRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this OrganizationRequest.

        The display name of the organization  # noqa: E501

        :param display_name: The display_name of this OrganizationRequest.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def name(self):
        """Gets the name of this OrganizationRequest.  # noqa: E501

        The name of the organization used in URLs  # noqa: E501

        :return: The name of this OrganizationRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationRequest.

        The name of the organization used in URLs  # noqa: E501

        :param name: The name of this OrganizationRequest.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(OrganizationRequest, dict):
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
        if not isinstance(other, OrganizationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
