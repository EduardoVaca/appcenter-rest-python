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


class AudienceDevicePropertiesListResult(object):
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
        'values': 'dict(str, str)'
    }

    attribute_map = {
        'values': 'values'
    }

    def __init__(self, values=None):  # noqa: E501
        """AudienceDevicePropertiesListResult - a model defined in Swagger"""  # noqa: E501
        self._values = None
        self.discriminator = None
        self.values = values

    @property
    def values(self):
        """Gets the values of this AudienceDevicePropertiesListResult.  # noqa: E501

        List of device properties.  # noqa: E501

        :return: The values of this AudienceDevicePropertiesListResult.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AudienceDevicePropertiesListResult.

        List of device properties.  # noqa: E501

        :param values: The values of this AudienceDevicePropertiesListResult.  # noqa: E501
        :type: dict(str, str)
        """
        if values is None:
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501
        allowed_values = ["string", "number", "boolean", "date_time"]  # noqa: E501
        if not set(values.keys()).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid keys in `values` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(values.keys()) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._values = values

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
        if issubclass(AudienceDevicePropertiesListResult, dict):
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
        if not isinstance(other, AudienceDevicePropertiesListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
