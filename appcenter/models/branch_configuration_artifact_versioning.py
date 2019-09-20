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


class BranchConfigurationArtifactVersioning(object):
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
        'build_number_format': 'str'
    }

    attribute_map = {
        'build_number_format': 'buildNumberFormat'
    }

    def __init__(self, build_number_format=None):  # noqa: E501
        """BranchConfigurationArtifactVersioning - a model defined in Swagger"""  # noqa: E501
        self._build_number_format = None
        self.discriminator = None
        if build_number_format is not None:
            self.build_number_format = build_number_format

    @property
    def build_number_format(self):
        """Gets the build_number_format of this BranchConfigurationArtifactVersioning.  # noqa: E501


        :return: The build_number_format of this BranchConfigurationArtifactVersioning.  # noqa: E501
        :rtype: str
        """
        return self._build_number_format

    @build_number_format.setter
    def build_number_format(self, build_number_format):
        """Sets the build_number_format of this BranchConfigurationArtifactVersioning.


        :param build_number_format: The build_number_format of this BranchConfigurationArtifactVersioning.  # noqa: E501
        :type: str
        """
        allowed_values = ["buildId", "timestamp"]  # noqa: E501
        if build_number_format not in allowed_values:
            raise ValueError(
                "Invalid value for `build_number_format` ({0}), must be one of {1}"  # noqa: E501
                .format(build_number_format, allowed_values)
            )

        self._build_number_format = build_number_format

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
        if issubclass(BranchConfigurationArtifactVersioning, dict):
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
        if not isinstance(other, BranchConfigurationArtifactVersioning):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
