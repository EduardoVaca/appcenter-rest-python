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


class TransferAppAdminRequest(object):
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
        'new_owner_id': 'str'
    }

    attribute_map = {
        'new_owner_id': 'new_owner_id'
    }

    def __init__(self, new_owner_id=None):  # noqa: E501
        """TransferAppAdminRequest - a model defined in Swagger"""  # noqa: E501
        self._new_owner_id = None
        self.discriminator = None
        self.new_owner_id = new_owner_id

    @property
    def new_owner_id(self):
        """Gets the new_owner_id of this TransferAppAdminRequest.  # noqa: E501

        The internal unique id (UUID) of the user/org.  # noqa: E501

        :return: The new_owner_id of this TransferAppAdminRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_owner_id

    @new_owner_id.setter
    def new_owner_id(self, new_owner_id):
        """Sets the new_owner_id of this TransferAppAdminRequest.

        The internal unique id (UUID) of the user/org.  # noqa: E501

        :param new_owner_id: The new_owner_id of this TransferAppAdminRequest.  # noqa: E501
        :type: str
        """
        if new_owner_id is None:
            raise ValueError("Invalid value for `new_owner_id`, must not be `None`")  # noqa: E501

        self._new_owner_id = new_owner_id

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
        if issubclass(TransferAppAdminRequest, dict):
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
        if not isinstance(other, TransferAppAdminRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other