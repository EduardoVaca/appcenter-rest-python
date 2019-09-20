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


class AlertingError(AlertOperationResult):
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
        'code': 'int',
        'message': 'str'
    }
    if hasattr(AlertOperationResult, "swagger_types"):
        swagger_types.update(AlertOperationResult.swagger_types)

    attribute_map = {
        'code': 'code',
        'message': 'message'
    }
    if hasattr(AlertOperationResult, "attribute_map"):
        attribute_map.update(AlertOperationResult.attribute_map)

    def __init__(self, code=None, message=None, *args, **kwargs):  # noqa: E501
        """AlertingError - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self.discriminator = None
        self.code = code
        if message is not None:
            self.message = message
        AlertOperationResult.__init__(self, *args, **kwargs)

    @property
    def code(self):
        """Gets the code of this AlertingError.  # noqa: E501

        The status code return by the API. It can be 400 or 404 or 409 or 500.  # noqa: E501

        :return: The code of this AlertingError.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AlertingError.

        The status code return by the API. It can be 400 or 404 or 409 or 500.  # noqa: E501

        :param code: The code of this AlertingError.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self):
        """Gets the message of this AlertingError.  # noqa: E501

        The reason for the request failed  # noqa: E501

        :return: The message of this AlertingError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AlertingError.

        The reason for the request failed  # noqa: E501

        :param message: The message of this AlertingError.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(AlertingError, dict):
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
        if not isinstance(other, AlertingError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
