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


class StorePatchRequest(object):
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
        'service_connection_id': 'str'
    }

    attribute_map = {
        'service_connection_id': 'service_connection_id'
    }

    def __init__(self, service_connection_id=None):  # noqa: E501
        """StorePatchRequest - a model defined in Swagger"""  # noqa: E501
        self._service_connection_id = None
        self.discriminator = None
        self.service_connection_id = service_connection_id

    @property
    def service_connection_id(self):
        """Gets the service_connection_id of this StorePatchRequest.  # noqa: E501

        Service connection id to updated.  # noqa: E501

        :return: The service_connection_id of this StorePatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_connection_id

    @service_connection_id.setter
    def service_connection_id(self, service_connection_id):
        """Sets the service_connection_id of this StorePatchRequest.

        Service connection id to updated.  # noqa: E501

        :param service_connection_id: The service_connection_id of this StorePatchRequest.  # noqa: E501
        :type: str
        """
        if service_connection_id is None:
            raise ValueError("Invalid value for `service_connection_id`, must not be `None`")  # noqa: E501

        self._service_connection_id = service_connection_id

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
        if issubclass(StorePatchRequest, dict):
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
        if not isinstance(other, StorePatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
