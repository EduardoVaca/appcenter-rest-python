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


class FileValidationDetails(object):
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
        'p12password': 'str',
        'certificate_upload_id': 'str'
    }

    attribute_map = {
        'p12password': 'p12password',
        'certificate_upload_id': 'certificateUploadId'
    }

    def __init__(self, p12password=None, certificate_upload_id=None):  # noqa: E501
        """FileValidationDetails - a model defined in Swagger"""  # noqa: E501
        self._p12password = None
        self._certificate_upload_id = None
        self.discriminator = None
        self.p12password = p12password
        if certificate_upload_id is not None:
            self.certificate_upload_id = certificate_upload_id

    @property
    def p12password(self):
        """Gets the p12password of this FileValidationDetails.  # noqa: E501


        :return: The p12password of this FileValidationDetails.  # noqa: E501
        :rtype: str
        """
        return self._p12password

    @p12password.setter
    def p12password(self, p12password):
        """Sets the p12password of this FileValidationDetails.


        :param p12password: The p12password of this FileValidationDetails.  # noqa: E501
        :type: str
        """
        if p12password is None:
            raise ValueError("Invalid value for `p12password`, must not be `None`")  # noqa: E501

        self._p12password = p12password

    @property
    def certificate_upload_id(self):
        """Gets the certificate_upload_id of this FileValidationDetails.  # noqa: E501


        :return: The certificate_upload_id of this FileValidationDetails.  # noqa: E501
        :rtype: str
        """
        return self._certificate_upload_id

    @certificate_upload_id.setter
    def certificate_upload_id(self, certificate_upload_id):
        """Sets the certificate_upload_id of this FileValidationDetails.


        :param certificate_upload_id: The certificate_upload_id of this FileValidationDetails.  # noqa: E501
        :type: str
        """

        self._certificate_upload_id = certificate_upload_id

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
        if issubclass(FileValidationDetails, dict):
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
        if not isinstance(other, FileValidationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
