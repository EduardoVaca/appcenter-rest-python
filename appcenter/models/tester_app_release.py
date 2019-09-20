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
from appcenter.models.distribution_group_release import DistributionGroupRelease  # noqa: F401,E501


class TesterAppRelease(DistributionGroupRelease):
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
        'size': 'int',
        'install_url': 'str',
        'release_notes': 'str'
    }
    if hasattr(DistributionGroupRelease, "swagger_types"):
        swagger_types.update(DistributionGroupRelease.swagger_types)

    attribute_map = {
        'size': 'size',
        'install_url': 'install_url',
        'release_notes': 'release_notes'
    }
    if hasattr(DistributionGroupRelease, "attribute_map"):
        attribute_map.update(DistributionGroupRelease.attribute_map)

    def __init__(self, size=None, install_url=None, release_notes=None, *args, **kwargs):  # noqa: E501
        """TesterAppRelease - a model defined in Swagger"""  # noqa: E501
        self._size = None
        self._install_url = None
        self._release_notes = None
        self.discriminator = None
        self.size = size
        if install_url is not None:
            self.install_url = install_url
        if release_notes is not None:
            self.release_notes = release_notes
        DistributionGroupRelease.__init__(self, *args, **kwargs)

    @property
    def size(self):
        """Gets the size of this TesterAppRelease.  # noqa: E501

        The release's size in bytes.  # noqa: E501

        :return: The size of this TesterAppRelease.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TesterAppRelease.

        The release's size in bytes.  # noqa: E501

        :param size: The size of this TesterAppRelease.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def install_url(self):
        """Gets the install_url of this TesterAppRelease.  # noqa: E501

        The href required to install a release on a mobile device. On iOS devices will be prefixed with `itms-services://?action=download-manifest&url=`  # noqa: E501

        :return: The install_url of this TesterAppRelease.  # noqa: E501
        :rtype: str
        """
        return self._install_url

    @install_url.setter
    def install_url(self, install_url):
        """Sets the install_url of this TesterAppRelease.

        The href required to install a release on a mobile device. On iOS devices will be prefixed with `itms-services://?action=download-manifest&url=`  # noqa: E501

        :param install_url: The install_url of this TesterAppRelease.  # noqa: E501
        :type: str
        """

        self._install_url = install_url

    @property
    def release_notes(self):
        """Gets the release_notes of this TesterAppRelease.  # noqa: E501

        The release's release notes.  # noqa: E501

        :return: The release_notes of this TesterAppRelease.  # noqa: E501
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this TesterAppRelease.

        The release's release notes.  # noqa: E501

        :param release_notes: The release_notes of this TesterAppRelease.  # noqa: E501
        :type: str
        """

        self._release_notes = release_notes

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
        if issubclass(TesterAppRelease, dict):
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
        if not isinstance(other, TesterAppRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
