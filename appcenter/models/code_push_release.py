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
from appcenter.models.code_push_release_info import CodePushReleaseInfo  # noqa: F401,E501
from appcenter.models.package_hash_to_blob_info_map import PackageHashToBlobInfoMap  # noqa: F401,E501


class CodePushRelease(CodePushReleaseInfo):
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
        'label': 'str',
        'package_hash': 'str',
        'blob_url': 'str',
        'diff_package_map': 'PackageHashToBlobInfoMap',
        'original_deployment': 'str',
        'original_label': 'str',
        'released_by': 'str',
        'release_method': 'str',
        'size': 'float',
        'upload_time': 'int'
    }
    if hasattr(CodePushReleaseInfo, "swagger_types"):
        swagger_types.update(CodePushReleaseInfo.swagger_types)

    attribute_map = {
        'label': 'label',
        'package_hash': 'package_hash',
        'blob_url': 'blob_url',
        'diff_package_map': 'diff_package_map',
        'original_deployment': 'original_deployment',
        'original_label': 'original_label',
        'released_by': 'released_by',
        'release_method': 'release_method',
        'size': 'size',
        'upload_time': 'upload_time'
    }
    if hasattr(CodePushReleaseInfo, "attribute_map"):
        attribute_map.update(CodePushReleaseInfo.attribute_map)

    def __init__(self, label=None, package_hash=None, blob_url=None, diff_package_map=None, original_deployment=None, original_label=None, released_by=None, release_method=None, size=None, upload_time=None, *args, **kwargs):  # noqa: E501
        """CodePushRelease - a model defined in Swagger"""  # noqa: E501
        self._label = None
        self._package_hash = None
        self._blob_url = None
        self._diff_package_map = None
        self._original_deployment = None
        self._original_label = None
        self._released_by = None
        self._release_method = None
        self._size = None
        self._upload_time = None
        self.discriminator = None
        if label is not None:
            self.label = label
        if package_hash is not None:
            self.package_hash = package_hash
        if blob_url is not None:
            self.blob_url = blob_url
        if diff_package_map is not None:
            self.diff_package_map = diff_package_map
        if original_deployment is not None:
            self.original_deployment = original_deployment
        if original_label is not None:
            self.original_label = original_label
        if released_by is not None:
            self.released_by = released_by
        if release_method is not None:
            self.release_method = release_method
        if size is not None:
            self.size = size
        if upload_time is not None:
            self.upload_time = upload_time
        CodePushReleaseInfo.__init__(self, *args, **kwargs)

    @property
    def label(self):
        """Gets the label of this CodePushRelease.  # noqa: E501


        :return: The label of this CodePushRelease.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CodePushRelease.


        :param label: The label of this CodePushRelease.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def package_hash(self):
        """Gets the package_hash of this CodePushRelease.  # noqa: E501


        :return: The package_hash of this CodePushRelease.  # noqa: E501
        :rtype: str
        """
        return self._package_hash

    @package_hash.setter
    def package_hash(self, package_hash):
        """Sets the package_hash of this CodePushRelease.


        :param package_hash: The package_hash of this CodePushRelease.  # noqa: E501
        :type: str
        """

        self._package_hash = package_hash

    @property
    def blob_url(self):
        """Gets the blob_url of this CodePushRelease.  # noqa: E501


        :return: The blob_url of this CodePushRelease.  # noqa: E501
        :rtype: str
        """
        return self._blob_url

    @blob_url.setter
    def blob_url(self, blob_url):
        """Sets the blob_url of this CodePushRelease.


        :param blob_url: The blob_url of this CodePushRelease.  # noqa: E501
        :type: str
        """

        self._blob_url = blob_url

    @property
    def diff_package_map(self):
        """Gets the diff_package_map of this CodePushRelease.  # noqa: E501


        :return: The diff_package_map of this CodePushRelease.  # noqa: E501
        :rtype: PackageHashToBlobInfoMap
        """
        return self._diff_package_map

    @diff_package_map.setter
    def diff_package_map(self, diff_package_map):
        """Sets the diff_package_map of this CodePushRelease.


        :param diff_package_map: The diff_package_map of this CodePushRelease.  # noqa: E501
        :type: PackageHashToBlobInfoMap
        """

        self._diff_package_map = diff_package_map

    @property
    def original_deployment(self):
        """Gets the original_deployment of this CodePushRelease.  # noqa: E501

        Set on 'Promote'  # noqa: E501

        :return: The original_deployment of this CodePushRelease.  # noqa: E501
        :rtype: str
        """
        return self._original_deployment

    @original_deployment.setter
    def original_deployment(self, original_deployment):
        """Sets the original_deployment of this CodePushRelease.

        Set on 'Promote'  # noqa: E501

        :param original_deployment: The original_deployment of this CodePushRelease.  # noqa: E501
        :type: str
        """

        self._original_deployment = original_deployment

    @property
    def original_label(self):
        """Gets the original_label of this CodePushRelease.  # noqa: E501

        Set on 'Promote' and 'Rollback'  # noqa: E501

        :return: The original_label of this CodePushRelease.  # noqa: E501
        :rtype: str
        """
        return self._original_label

    @original_label.setter
    def original_label(self, original_label):
        """Sets the original_label of this CodePushRelease.

        Set on 'Promote' and 'Rollback'  # noqa: E501

        :param original_label: The original_label of this CodePushRelease.  # noqa: E501
        :type: str
        """

        self._original_label = original_label

    @property
    def released_by(self):
        """Gets the released_by of this CodePushRelease.  # noqa: E501


        :return: The released_by of this CodePushRelease.  # noqa: E501
        :rtype: str
        """
        return self._released_by

    @released_by.setter
    def released_by(self, released_by):
        """Sets the released_by of this CodePushRelease.


        :param released_by: The released_by of this CodePushRelease.  # noqa: E501
        :type: str
        """

        self._released_by = released_by

    @property
    def release_method(self):
        """Gets the release_method of this CodePushRelease.  # noqa: E501

        The release method is unknown if unspecified  # noqa: E501

        :return: The release_method of this CodePushRelease.  # noqa: E501
        :rtype: str
        """
        return self._release_method

    @release_method.setter
    def release_method(self, release_method):
        """Sets the release_method of this CodePushRelease.

        The release method is unknown if unspecified  # noqa: E501

        :param release_method: The release_method of this CodePushRelease.  # noqa: E501
        :type: str
        """
        allowed_values = ["Upload", "Promote", "Rollback"]  # noqa: E501
        if release_method not in allowed_values:
            raise ValueError(
                "Invalid value for `release_method` ({0}), must be one of {1}"  # noqa: E501
                .format(release_method, allowed_values)
            )

        self._release_method = release_method

    @property
    def size(self):
        """Gets the size of this CodePushRelease.  # noqa: E501


        :return: The size of this CodePushRelease.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CodePushRelease.


        :param size: The size of this CodePushRelease.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def upload_time(self):
        """Gets the upload_time of this CodePushRelease.  # noqa: E501


        :return: The upload_time of this CodePushRelease.  # noqa: E501
        :rtype: int
        """
        return self._upload_time

    @upload_time.setter
    def upload_time(self, upload_time):
        """Sets the upload_time of this CodePushRelease.


        :param upload_time: The upload_time of this CodePushRelease.  # noqa: E501
        :type: int
        """

        self._upload_time = upload_time

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
        if issubclass(CodePushRelease, dict):
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
        if not isinstance(other, CodePushRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other