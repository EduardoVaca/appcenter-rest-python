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


class HockeyAppCrashForwardingChange(object):
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
        'enable_forwarding': 'bool'
    }

    attribute_map = {
        'enable_forwarding': 'enable_forwarding'
    }

    def __init__(self, enable_forwarding=None):  # noqa: E501
        """HockeyAppCrashForwardingChange - a model defined in Swagger"""  # noqa: E501
        self._enable_forwarding = None
        self.discriminator = None
        if enable_forwarding is not None:
            self.enable_forwarding = enable_forwarding

    @property
    def enable_forwarding(self):
        """Gets the enable_forwarding of this HockeyAppCrashForwardingChange.  # noqa: E501


        :return: The enable_forwarding of this HockeyAppCrashForwardingChange.  # noqa: E501
        :rtype: bool
        """
        return self._enable_forwarding

    @enable_forwarding.setter
    def enable_forwarding(self, enable_forwarding):
        """Sets the enable_forwarding of this HockeyAppCrashForwardingChange.


        :param enable_forwarding: The enable_forwarding of this HockeyAppCrashForwardingChange.  # noqa: E501
        :type: bool
        """

        self._enable_forwarding = enable_forwarding

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
        if issubclass(HockeyAppCrashForwardingChange, dict):
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
        if not isinstance(other, HockeyAppCrashForwardingChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
