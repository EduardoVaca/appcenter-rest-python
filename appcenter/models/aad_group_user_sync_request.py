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


class AADGroupUserSyncRequest(object):
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
        'user_id': 'str',
        'aad_group_id': 'str',
        'role': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'aad_group_id': 'aad_group_id',
        'role': 'role'
    }

    def __init__(self, user_id=None, aad_group_id=None, role=None):  # noqa: E501
        """AADGroupUserSyncRequest - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._aad_group_id = None
        self._role = None
        self.discriminator = None
        self.user_id = user_id
        self.aad_group_id = aad_group_id
        self.role = role

    @property
    def user_id(self):
        """Gets the user_id of this AADGroupUserSyncRequest.  # noqa: E501

        user id  # noqa: E501

        :return: The user_id of this AADGroupUserSyncRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AADGroupUserSyncRequest.

        user id  # noqa: E501

        :param user_id: The user_id of this AADGroupUserSyncRequest.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def aad_group_id(self):
        """Gets the aad_group_id of this AADGroupUserSyncRequest.  # noqa: E501

        The appcenter AAD group id  # noqa: E501

        :return: The aad_group_id of this AADGroupUserSyncRequest.  # noqa: E501
        :rtype: str
        """
        return self._aad_group_id

    @aad_group_id.setter
    def aad_group_id(self, aad_group_id):
        """Sets the aad_group_id of this AADGroupUserSyncRequest.

        The appcenter AAD group id  # noqa: E501

        :param aad_group_id: The aad_group_id of this AADGroupUserSyncRequest.  # noqa: E501
        :type: str
        """
        if aad_group_id is None:
            raise ValueError("Invalid value for `aad_group_id`, must not be `None`")  # noqa: E501

        self._aad_group_id = aad_group_id

    @property
    def role(self):
        """Gets the role of this AADGroupUserSyncRequest.  # noqa: E501

        role  # noqa: E501

        :return: The role of this AADGroupUserSyncRequest.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AADGroupUserSyncRequest.

        role  # noqa: E501

        :param role: The role of this AADGroupUserSyncRequest.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["admin", "collaborator", "member"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

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
        if issubclass(AADGroupUserSyncRequest, dict):
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
        if not isinstance(other, AADGroupUserSyncRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
