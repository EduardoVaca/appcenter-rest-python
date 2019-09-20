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


class DeviceAvailability(object):
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
        'registered': 'float',
        'available': 'float',
        'maximum': 'float'
    }

    attribute_map = {
        'registered': 'registered',
        'available': 'available',
        'maximum': 'maximum'
    }

    def __init__(self, registered=None, available=None, maximum=None):  # noqa: E501
        """DeviceAvailability - a model defined in Swagger"""  # noqa: E501
        self._registered = None
        self._available = None
        self._maximum = None
        self.discriminator = None
        self.registered = registered
        self.available = available
        self.maximum = maximum

    @property
    def registered(self):
        """Gets the registered of this DeviceAvailability.  # noqa: E501


        :return: The registered of this DeviceAvailability.  # noqa: E501
        :rtype: float
        """
        return self._registered

    @registered.setter
    def registered(self, registered):
        """Sets the registered of this DeviceAvailability.


        :param registered: The registered of this DeviceAvailability.  # noqa: E501
        :type: float
        """
        if registered is None:
            raise ValueError("Invalid value for `registered`, must not be `None`")  # noqa: E501

        self._registered = registered

    @property
    def available(self):
        """Gets the available of this DeviceAvailability.  # noqa: E501


        :return: The available of this DeviceAvailability.  # noqa: E501
        :rtype: float
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this DeviceAvailability.


        :param available: The available of this DeviceAvailability.  # noqa: E501
        :type: float
        """
        if available is None:
            raise ValueError("Invalid value for `available`, must not be `None`")  # noqa: E501

        self._available = available

    @property
    def maximum(self):
        """Gets the maximum of this DeviceAvailability.  # noqa: E501


        :return: The maximum of this DeviceAvailability.  # noqa: E501
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this DeviceAvailability.


        :param maximum: The maximum of this DeviceAvailability.  # noqa: E501
        :type: float
        """
        if maximum is None:
            raise ValueError("Invalid value for `maximum`, must not be `None`")  # noqa: E501

        self._maximum = maximum

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
        if issubclass(DeviceAvailability, dict):
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
        if not isinstance(other, DeviceAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
