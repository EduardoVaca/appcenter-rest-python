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


class PrivateReleaseUpdateRequest(object):
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
        'publishing_status': 'str'
    }

    attribute_map = {
        'publishing_status': 'publishing_status'
    }

    def __init__(self, publishing_status=None):  # noqa: E501
        """PrivateReleaseUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._publishing_status = None
        self.discriminator = None
        if publishing_status is not None:
            self.publishing_status = publishing_status

    @property
    def publishing_status(self):
        """Gets the publishing_status of this PrivateReleaseUpdateRequest.  # noqa: E501

        The store publishing status.  # noqa: E501

        :return: The publishing_status of this PrivateReleaseUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._publishing_status

    @publishing_status.setter
    def publishing_status(self, publishing_status):
        """Sets the publishing_status of this PrivateReleaseUpdateRequest.

        The store publishing status.  # noqa: E501

        :param publishing_status: The publishing_status of this PrivateReleaseUpdateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["failed", "processing", "submitted", "timeout"]  # noqa: E501
        if publishing_status not in allowed_values:
            raise ValueError(
                "Invalid value for `publishing_status` ({0}), must be one of {1}"  # noqa: E501
                .format(publishing_status, allowed_values)
            )

        self._publishing_status = publishing_status

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
        if issubclass(PrivateReleaseUpdateRequest, dict):
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
        if not isinstance(other, PrivateReleaseUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other