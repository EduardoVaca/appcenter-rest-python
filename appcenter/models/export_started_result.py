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


class ExportStartedResult(object):
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
        'export_id': 'str'
    }

    attribute_map = {
        'export_id': 'export_id'
    }

    def __init__(self, export_id=None):  # noqa: E501
        """ExportStartedResult - a model defined in Swagger"""  # noqa: E501
        self._export_id = None
        self.discriminator = None
        self.export_id = export_id

    @property
    def export_id(self):
        """Gets the export_id of this ExportStartedResult.  # noqa: E501

        The unique export identifier.  # noqa: E501

        :return: The export_id of this ExportStartedResult.  # noqa: E501
        :rtype: str
        """
        return self._export_id

    @export_id.setter
    def export_id(self, export_id):
        """Sets the export_id of this ExportStartedResult.

        The unique export identifier.  # noqa: E501

        :param export_id: The export_id of this ExportStartedResult.  # noqa: E501
        :type: str
        """
        if export_id is None:
            raise ValueError("Invalid value for `export_id`, must not be `None`")  # noqa: E501

        self._export_id = export_id

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
        if issubclass(ExportStartedResult, dict):
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
        if not isinstance(other, ExportStartedResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
