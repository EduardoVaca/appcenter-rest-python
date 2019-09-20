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


class XamarinSDKBundle(object):
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
        'mono_version': 'str',
        'sdk_bundle': 'str',
        'current': 'bool',
        'stable': 'bool',
        'xcode_versions': 'list[str]'
    }

    attribute_map = {
        'mono_version': 'monoVersion',
        'sdk_bundle': 'sdkBundle',
        'current': 'current',
        'stable': 'stable',
        'xcode_versions': 'xcodeVersions'
    }

    def __init__(self, mono_version=None, sdk_bundle=None, current=None, stable=None, xcode_versions=None):  # noqa: E501
        """XamarinSDKBundle - a model defined in Swagger"""  # noqa: E501
        self._mono_version = None
        self._sdk_bundle = None
        self._current = None
        self._stable = None
        self._xcode_versions = None
        self.discriminator = None
        if mono_version is not None:
            self.mono_version = mono_version
        if sdk_bundle is not None:
            self.sdk_bundle = sdk_bundle
        if current is not None:
            self.current = current
        if stable is not None:
            self.stable = stable
        if xcode_versions is not None:
            self.xcode_versions = xcode_versions

    @property
    def mono_version(self):
        """Gets the mono_version of this XamarinSDKBundle.  # noqa: E501

        The Mono version  # noqa: E501

        :return: The mono_version of this XamarinSDKBundle.  # noqa: E501
        :rtype: str
        """
        return self._mono_version

    @mono_version.setter
    def mono_version(self, mono_version):
        """Sets the mono_version of this XamarinSDKBundle.

        The Mono version  # noqa: E501

        :param mono_version: The mono_version of this XamarinSDKBundle.  # noqa: E501
        :type: str
        """

        self._mono_version = mono_version

    @property
    def sdk_bundle(self):
        """Gets the sdk_bundle of this XamarinSDKBundle.  # noqa: E501

        The Xamarin SDK version  # noqa: E501

        :return: The sdk_bundle of this XamarinSDKBundle.  # noqa: E501
        :rtype: str
        """
        return self._sdk_bundle

    @sdk_bundle.setter
    def sdk_bundle(self, sdk_bundle):
        """Sets the sdk_bundle of this XamarinSDKBundle.

        The Xamarin SDK version  # noqa: E501

        :param sdk_bundle: The sdk_bundle of this XamarinSDKBundle.  # noqa: E501
        :type: str
        """

        self._sdk_bundle = sdk_bundle

    @property
    def current(self):
        """Gets the current of this XamarinSDKBundle.  # noqa: E501

        If the SDK is latest stable  # noqa: E501

        :return: The current of this XamarinSDKBundle.  # noqa: E501
        :rtype: bool
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this XamarinSDKBundle.

        If the SDK is latest stable  # noqa: E501

        :param current: The current of this XamarinSDKBundle.  # noqa: E501
        :type: bool
        """

        self._current = current

    @property
    def stable(self):
        """Gets the stable of this XamarinSDKBundle.  # noqa: E501

        If the SDK is stable  # noqa: E501

        :return: The stable of this XamarinSDKBundle.  # noqa: E501
        :rtype: bool
        """
        return self._stable

    @stable.setter
    def stable(self, stable):
        """Sets the stable of this XamarinSDKBundle.

        If the SDK is stable  # noqa: E501

        :param stable: The stable of this XamarinSDKBundle.  # noqa: E501
        :type: bool
        """

        self._stable = stable

    @property
    def xcode_versions(self):
        """Gets the xcode_versions of this XamarinSDKBundle.  # noqa: E501

        Specific for iOS SDK. A list of Xcode versions supported by current SDK version  # noqa: E501

        :return: The xcode_versions of this XamarinSDKBundle.  # noqa: E501
        :rtype: list[str]
        """
        return self._xcode_versions

    @xcode_versions.setter
    def xcode_versions(self, xcode_versions):
        """Sets the xcode_versions of this XamarinSDKBundle.

        Specific for iOS SDK. A list of Xcode versions supported by current SDK version  # noqa: E501

        :param xcode_versions: The xcode_versions of this XamarinSDKBundle.  # noqa: E501
        :type: list[str]
        """

        self._xcode_versions = xcode_versions

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
        if issubclass(XamarinSDKBundle, dict):
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
        if not isinstance(other, XamarinSDKBundle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
