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


class PrivateBasicReleaseDetailsResponse(object):
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
        'id': 'int',
        'version': 'str',
        'origin': 'str',
        'short_version': 'str',
        'uploaded_at': 'str',
        'distribution_group_id': 'str',
        'destination_type': 'str',
        'is_latest': 'bool',
        'mandatory_update': 'bool',
        'publishing_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'origin': 'origin',
        'short_version': 'short_version',
        'uploaded_at': 'uploaded_at',
        'distribution_group_id': 'distribution_group_id',
        'destination_type': 'destination_type',
        'is_latest': 'is_latest',
        'mandatory_update': 'mandatory_update',
        'publishing_status': 'publishing_status'
    }

    def __init__(self, id=None, version=None, origin=None, short_version=None, uploaded_at=None, distribution_group_id=None, destination_type=None, is_latest=None, mandatory_update=None, publishing_status=None):  # noqa: E501
        """PrivateBasicReleaseDetailsResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version = None
        self._origin = None
        self._short_version = None
        self._uploaded_at = None
        self._distribution_group_id = None
        self._destination_type = None
        self._is_latest = None
        self._mandatory_update = None
        self._publishing_status = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if origin is not None:
            self.origin = origin
        if short_version is not None:
            self.short_version = short_version
        if uploaded_at is not None:
            self.uploaded_at = uploaded_at
        if distribution_group_id is not None:
            self.distribution_group_id = distribution_group_id
        if destination_type is not None:
            self.destination_type = destination_type
        if is_latest is not None:
            self.is_latest = is_latest
        if mandatory_update is not None:
            self.mandatory_update = mandatory_update
        if publishing_status is not None:
            self.publishing_status = publishing_status

    @property
    def id(self):
        """Gets the id of this PrivateBasicReleaseDetailsResponse.  # noqa: E501

        ID identifying this unique release.  # noqa: E501

        :return: The id of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivateBasicReleaseDetailsResponse.

        ID identifying this unique release.  # noqa: E501

        :param id: The id of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this PrivateBasicReleaseDetailsResponse.  # noqa: E501

        The release's version.<br> For iOS: CFBundleVersion from info.plist.<br> For Android: android:versionCode from AppManifest.xml.   # noqa: E501

        :return: The version of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PrivateBasicReleaseDetailsResponse.

        The release's version.<br> For iOS: CFBundleVersion from info.plist.<br> For Android: android:versionCode from AppManifest.xml.   # noqa: E501

        :param version: The version of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def origin(self):
        """Gets the origin of this PrivateBasicReleaseDetailsResponse.  # noqa: E501

        The release's origin  # noqa: E501

        :return: The origin of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this PrivateBasicReleaseDetailsResponse.

        The release's origin  # noqa: E501

        :param origin: The origin of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["hockeyapp", "appcenter"]  # noqa: E501
        if origin not in allowed_values:
            raise ValueError(
                "Invalid value for `origin` ({0}), must be one of {1}"  # noqa: E501
                .format(origin, allowed_values)
            )

        self._origin = origin

    @property
    def short_version(self):
        """Gets the short_version of this PrivateBasicReleaseDetailsResponse.  # noqa: E501

        The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist.<br> For Android: android:versionName from AppManifest.xml.   # noqa: E501

        :return: The short_version of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._short_version

    @short_version.setter
    def short_version(self, short_version):
        """Sets the short_version of this PrivateBasicReleaseDetailsResponse.

        The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist.<br> For Android: android:versionName from AppManifest.xml.   # noqa: E501

        :param short_version: The short_version of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :type: str
        """

        self._short_version = short_version

    @property
    def uploaded_at(self):
        """Gets the uploaded_at of this PrivateBasicReleaseDetailsResponse.  # noqa: E501

        UTC time in ISO 8601 format of the uploaded time.  # noqa: E501

        :return: The uploaded_at of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_at

    @uploaded_at.setter
    def uploaded_at(self, uploaded_at):
        """Sets the uploaded_at of this PrivateBasicReleaseDetailsResponse.

        UTC time in ISO 8601 format of the uploaded time.  # noqa: E501

        :param uploaded_at: The uploaded_at of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :type: str
        """

        self._uploaded_at = uploaded_at

    @property
    def distribution_group_id(self):
        """Gets the distribution_group_id of this PrivateBasicReleaseDetailsResponse.  # noqa: E501

        the destination id of release where it is distributed.  # noqa: E501

        :return: The distribution_group_id of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._distribution_group_id

    @distribution_group_id.setter
    def distribution_group_id(self, distribution_group_id):
        """Sets the distribution_group_id of this PrivateBasicReleaseDetailsResponse.

        the destination id of release where it is distributed.  # noqa: E501

        :param distribution_group_id: The distribution_group_id of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :type: str
        """

        self._distribution_group_id = distribution_group_id

    @property
    def destination_type(self):
        """Gets the destination_type of this PrivateBasicReleaseDetailsResponse.  # noqa: E501

        The destination type.<br> <b>group</b>: The release distributed to internal groups and distribution_groups details will be returned.<br> <b>store</b>: The release distributed to external stores and distribution_stores details will be returned. <br>   # noqa: E501

        :return: The destination_type of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this PrivateBasicReleaseDetailsResponse.

        The destination type.<br> <b>group</b>: The release distributed to internal groups and distribution_groups details will be returned.<br> <b>store</b>: The release distributed to external stores and distribution_stores details will be returned. <br>   # noqa: E501

        :param destination_type: The destination_type of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["group", "store", "tester"]  # noqa: E501
        if destination_type not in allowed_values:
            raise ValueError(
                "Invalid value for `destination_type` ({0}), must be one of {1}"  # noqa: E501
                .format(destination_type, allowed_values)
            )

        self._destination_type = destination_type

    @property
    def is_latest(self):
        """Gets the is_latest of this PrivateBasicReleaseDetailsResponse.  # noqa: E501

        Indicates if this is the latest release in the group.  # noqa: E501

        :return: The is_latest of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """Sets the is_latest of this PrivateBasicReleaseDetailsResponse.

        Indicates if this is the latest release in the group.  # noqa: E501

        :param is_latest: The is_latest of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :type: bool
        """

        self._is_latest = is_latest

    @property
    def mandatory_update(self):
        """Gets the mandatory_update of this PrivateBasicReleaseDetailsResponse.  # noqa: E501

        A boolean which determines whether the release is a mandatory update or not.  # noqa: E501

        :return: The mandatory_update of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory_update

    @mandatory_update.setter
    def mandatory_update(self, mandatory_update):
        """Sets the mandatory_update of this PrivateBasicReleaseDetailsResponse.

        A boolean which determines whether the release is a mandatory update or not.  # noqa: E501

        :param mandatory_update: The mandatory_update of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :type: bool
        """

        self._mandatory_update = mandatory_update

    @property
    def publishing_status(self):
        """Gets the publishing_status of this PrivateBasicReleaseDetailsResponse.  # noqa: E501

        the publishing status of the distributed release  # noqa: E501

        :return: The publishing_status of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._publishing_status

    @publishing_status.setter
    def publishing_status(self, publishing_status):
        """Sets the publishing_status of this PrivateBasicReleaseDetailsResponse.

        the publishing status of the distributed release  # noqa: E501

        :param publishing_status: The publishing_status of this PrivateBasicReleaseDetailsResponse.  # noqa: E501
        :type: str
        """

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
        if issubclass(PrivateBasicReleaseDetailsResponse, dict):
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
        if not isinstance(other, PrivateBasicReleaseDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
