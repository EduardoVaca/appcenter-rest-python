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
from appcenter.models.legacy_code_push_release import LegacyCodePushRelease  # noqa: F401,E501


class LegacyPatchDeploymentResponse(object):
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
        'key': 'str',
        'name': 'str',
        'package': 'LegacyCodePushRelease'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'package': 'package'
    }

    def __init__(self, key=None, name=None, package=None):  # noqa: E501
        """LegacyPatchDeploymentResponse - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._name = None
        self._package = None
        self.discriminator = None
        if key is not None:
            self.key = key
        self.name = name
        if package is not None:
            self.package = package

    @property
    def key(self):
        """Gets the key of this LegacyPatchDeploymentResponse.  # noqa: E501

        Deployment key (aka Deployment Id)  # noqa: E501

        :return: The key of this LegacyPatchDeploymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LegacyPatchDeploymentResponse.

        Deployment key (aka Deployment Id)  # noqa: E501

        :param key: The key of this LegacyPatchDeploymentResponse.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this LegacyPatchDeploymentResponse.  # noqa: E501

        Updated deployment name  # noqa: E501

        :return: The name of this LegacyPatchDeploymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LegacyPatchDeploymentResponse.

        Updated deployment name  # noqa: E501

        :param name: The name of this LegacyPatchDeploymentResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def package(self):
        """Gets the package of this LegacyPatchDeploymentResponse.  # noqa: E501


        :return: The package of this LegacyPatchDeploymentResponse.  # noqa: E501
        :rtype: LegacyCodePushRelease
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this LegacyPatchDeploymentResponse.


        :param package: The package of this LegacyPatchDeploymentResponse.  # noqa: E501
        :type: LegacyCodePushRelease
        """

        self._package = package

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
        if issubclass(LegacyPatchDeploymentResponse, dict):
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
        if not isinstance(other, LegacyPatchDeploymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other