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
from appcenter.models.team_response import TeamResponse  # noqa: F401,E501


class TeamAppResponse(TeamResponse):
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
        'permissions': 'list[str]'
    }
    if hasattr(TeamResponse, "swagger_types"):
        swagger_types.update(TeamResponse.swagger_types)

    attribute_map = {
        'permissions': 'permissions'
    }
    if hasattr(TeamResponse, "attribute_map"):
        attribute_map.update(TeamResponse.attribute_map)

    def __init__(self, permissions=None, *args, **kwargs):  # noqa: E501
        """TeamAppResponse - a model defined in Swagger"""  # noqa: E501
        self._permissions = None
        self.discriminator = None
        if permissions is not None:
            self.permissions = permissions
        TeamResponse.__init__(self, *args, **kwargs)

    @property
    def permissions(self):
        """Gets the permissions of this TeamAppResponse.  # noqa: E501

        The permissions the team has for the app  # noqa: E501

        :return: The permissions of this TeamAppResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this TeamAppResponse.

        The permissions the team has for the app  # noqa: E501

        :param permissions: The permissions of this TeamAppResponse.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["manager", "developer", "viewer", "tester"]  # noqa: E501
        if not set(permissions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(permissions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._permissions = permissions

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
        if issubclass(TeamAppResponse, dict):
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
        if not isinstance(other, TeamAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other