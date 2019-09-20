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


class DistributionGroupAADGroupsDeleteRequest(object):
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
        'aad_group_ids': 'list[str]'
    }

    attribute_map = {
        'aad_group_ids': 'aad_group_ids'
    }

    def __init__(self, aad_group_ids=None):  # noqa: E501
        """DistributionGroupAADGroupsDeleteRequest - a model defined in Swagger"""  # noqa: E501
        self._aad_group_ids = None
        self.discriminator = None
        if aad_group_ids is not None:
            self.aad_group_ids = aad_group_ids

    @property
    def aad_group_ids(self):
        """Gets the aad_group_ids of this DistributionGroupAADGroupsDeleteRequest.  # noqa: E501

        The list of aad group ids  # noqa: E501

        :return: The aad_group_ids of this DistributionGroupAADGroupsDeleteRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._aad_group_ids

    @aad_group_ids.setter
    def aad_group_ids(self, aad_group_ids):
        """Sets the aad_group_ids of this DistributionGroupAADGroupsDeleteRequest.

        The list of aad group ids  # noqa: E501

        :param aad_group_ids: The aad_group_ids of this DistributionGroupAADGroupsDeleteRequest.  # noqa: E501
        :type: list[str]
        """

        self._aad_group_ids = aad_group_ids

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
        if issubclass(DistributionGroupAADGroupsDeleteRequest, dict):
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
        if not isinstance(other, DistributionGroupAADGroupsDeleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other