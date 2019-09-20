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


class GrantAdminRoleRequest(object):
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
        'admin_role': 'str'
    }

    attribute_map = {
        'admin_role': 'admin_role'
    }

    def __init__(self, admin_role=None):  # noqa: E501
        """GrantAdminRoleRequest - a model defined in Swagger"""  # noqa: E501
        self._admin_role = None
        self.discriminator = None
        self.admin_role = admin_role

    @property
    def admin_role(self):
        """Gets the admin_role of this GrantAdminRoleRequest.  # noqa: E501

        The new admin_role  # noqa: E501

        :return: The admin_role of this GrantAdminRoleRequest.  # noqa: E501
        :rtype: str
        """
        return self._admin_role

    @admin_role.setter
    def admin_role(self, admin_role):
        """Sets the admin_role of this GrantAdminRoleRequest.

        The new admin_role  # noqa: E501

        :param admin_role: The admin_role of this GrantAdminRoleRequest.  # noqa: E501
        :type: str
        """
        if admin_role is None:
            raise ValueError("Invalid value for `admin_role`, must not be `None`")  # noqa: E501
        allowed_values = ["superAdmin", "admin", "devOps", "customerSupport", "notAdmin"]  # noqa: E501
        if admin_role not in allowed_values:
            raise ValueError(
                "Invalid value for `admin_role` ({0}), must be one of {1}"  # noqa: E501
                .format(admin_role, allowed_values)
            )

        self._admin_role = admin_role

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
        if issubclass(GrantAdminRoleRequest, dict):
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
        if not isinstance(other, GrantAdminRoleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
