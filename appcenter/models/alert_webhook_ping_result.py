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
from appcenter.models.alert_operation_result import AlertOperationResult  # noqa: F401,E501


class AlertWebhookPingResult(AlertOperationResult):
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
        'response_status_code': 'int',
        'response_reason': 'str'
    }
    if hasattr(AlertOperationResult, "swagger_types"):
        swagger_types.update(AlertOperationResult.swagger_types)

    attribute_map = {
        'response_status_code': 'response_status_code',
        'response_reason': 'response_reason'
    }
    if hasattr(AlertOperationResult, "attribute_map"):
        attribute_map.update(AlertOperationResult.attribute_map)

    def __init__(self, response_status_code=None, response_reason=None, *args, **kwargs):  # noqa: E501
        """AlertWebhookPingResult - a model defined in Swagger"""  # noqa: E501
        self._response_status_code = None
        self._response_reason = None
        self.discriminator = None
        self.response_status_code = response_status_code
        if response_reason is not None:
            self.response_reason = response_reason
        AlertOperationResult.__init__(self, *args, **kwargs)

    @property
    def response_status_code(self):
        """Gets the response_status_code of this AlertWebhookPingResult.  # noqa: E501

        HTTP status code returned in response from calling webhook  # noqa: E501

        :return: The response_status_code of this AlertWebhookPingResult.  # noqa: E501
        :rtype: int
        """
        return self._response_status_code

    @response_status_code.setter
    def response_status_code(self, response_status_code):
        """Sets the response_status_code of this AlertWebhookPingResult.

        HTTP status code returned in response from calling webhook  # noqa: E501

        :param response_status_code: The response_status_code of this AlertWebhookPingResult.  # noqa: E501
        :type: int
        """
        if response_status_code is None:
            raise ValueError("Invalid value for `response_status_code`, must not be `None`")  # noqa: E501

        self._response_status_code = response_status_code

    @property
    def response_reason(self):
        """Gets the response_reason of this AlertWebhookPingResult.  # noqa: E501

        Reason returned in response from calling webhook  # noqa: E501

        :return: The response_reason of this AlertWebhookPingResult.  # noqa: E501
        :rtype: str
        """
        return self._response_reason

    @response_reason.setter
    def response_reason(self, response_reason):
        """Sets the response_reason of this AlertWebhookPingResult.

        Reason returned in response from calling webhook  # noqa: E501

        :param response_reason: The response_reason of this AlertWebhookPingResult.  # noqa: E501
        :type: str
        """

        self._response_reason = response_reason

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
        if issubclass(AlertWebhookPingResult, dict):
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
        if not isinstance(other, AlertWebhookPingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
