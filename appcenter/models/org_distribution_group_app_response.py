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
from appcenter.models.basic_app_response import BasicAppResponse  # noqa: F401,E501
from appcenter.models.owner import Owner  # noqa: F401,E501


class OrgDistributionGroupAppResponse(BasicAppResponse):
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
        'platform': 'str',
        'origin': 'str'
    }
    if hasattr(BasicAppResponse, "swagger_types"):
        swagger_types.update(BasicAppResponse.swagger_types)

    attribute_map = {
        'platform': 'platform',
        'origin': 'origin'
    }
    if hasattr(BasicAppResponse, "attribute_map"):
        attribute_map.update(BasicAppResponse.attribute_map)

    def __init__(self, platform=None, origin=None, *args, **kwargs):  # noqa: E501
        """OrgDistributionGroupAppResponse - a model defined in Swagger"""  # noqa: E501
        self._platform = None
        self._origin = None
        self.discriminator = None
        if platform is not None:
            self.platform = platform
        if origin is not None:
            self.origin = origin
        BasicAppResponse.__init__(self, *args, **kwargs)

    @property
    def platform(self):
        """Gets the platform of this OrgDistributionGroupAppResponse.  # noqa: E501

        The platform of the app  # noqa: E501

        :return: The platform of this OrgDistributionGroupAppResponse.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this OrgDistributionGroupAppResponse.

        The platform of the app  # noqa: E501

        :param platform: The platform of this OrgDistributionGroupAppResponse.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def origin(self):
        """Gets the origin of this OrgDistributionGroupAppResponse.  # noqa: E501

        The creation origin of this app  # noqa: E501

        :return: The origin of this OrgDistributionGroupAppResponse.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this OrgDistributionGroupAppResponse.

        The creation origin of this app  # noqa: E501

        :param origin: The origin of this OrgDistributionGroupAppResponse.  # noqa: E501
        :type: str
        """

        self._origin = origin

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
        if issubclass(OrgDistributionGroupAppResponse, dict):
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
        if not isinstance(other, OrgDistributionGroupAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
