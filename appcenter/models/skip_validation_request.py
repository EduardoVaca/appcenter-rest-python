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


class SkipValidationRequest(object):
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
        'skip_validation': 'bool'
    }

    attribute_map = {
        'skip_validation': 'skip_validation'
    }

    def __init__(self, skip_validation=None):  # noqa: E501
        """SkipValidationRequest - a model defined in Swagger"""  # noqa: E501
        self._skip_validation = None
        self.discriminator = None
        if skip_validation is not None:
            self.skip_validation = skip_validation

    @property
    def skip_validation(self):
        """Gets the skip_validation of this SkipValidationRequest.  # noqa: E501

        true if we want to skip the validation, false otherwise  # noqa: E501

        :return: The skip_validation of this SkipValidationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._skip_validation

    @skip_validation.setter
    def skip_validation(self, skip_validation):
        """Sets the skip_validation of this SkipValidationRequest.

        true if we want to skip the validation, false otherwise  # noqa: E501

        :param skip_validation: The skip_validation of this SkipValidationRequest.  # noqa: E501
        :type: bool
        """

        self._skip_validation = skip_validation

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
        if issubclass(SkipValidationRequest, dict):
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
        if not isinstance(other, SkipValidationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
