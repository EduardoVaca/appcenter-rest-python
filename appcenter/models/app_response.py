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
from appcenter.models.azure_subscription_response import AzureSubscriptionResponse  # noqa: F401,E501
from appcenter.models.basic_app_response import BasicAppResponse  # noqa: F401,E501
from appcenter.models.owner import Owner  # noqa: F401,E501


class AppResponse(BasicAppResponse):
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
        'app_secret': 'str',
        'azure_subscription': 'AzureSubscriptionResponse',
        'platform': 'str',
        'origin': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'member_permissions': 'list[str]'
    }
    if hasattr(BasicAppResponse, "swagger_types"):
        swagger_types.update(BasicAppResponse.swagger_types)

    attribute_map = {
        'app_secret': 'app_secret',
        'azure_subscription': 'azure_subscription',
        'platform': 'platform',
        'origin': 'origin',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'member_permissions': 'member_permissions'
    }
    if hasattr(BasicAppResponse, "attribute_map"):
        attribute_map.update(BasicAppResponse.attribute_map)

    def __init__(self, app_secret=None, azure_subscription=None, platform=None, origin=None, created_at=None, updated_at=None, member_permissions=None, *args, **kwargs):  # noqa: E501
        """AppResponse - a model defined in Swagger"""  # noqa: E501
        self._app_secret = None
        self._azure_subscription = None
        self._platform = None
        self._origin = None
        self._created_at = None
        self._updated_at = None
        self._member_permissions = None
        self.discriminator = None
        if app_secret is not None:
            self.app_secret = app_secret
        if azure_subscription is not None:
            self.azure_subscription = azure_subscription
        if platform is not None:
            self.platform = platform
        if origin is not None:
            self.origin = origin
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if member_permissions is not None:
            self.member_permissions = member_permissions
        BasicAppResponse.__init__(self, *args, **kwargs)

    @property
    def app_secret(self):
        """Gets the app_secret of this AppResponse.  # noqa: E501

        A unique and secret key used to identify the app in communication with the ingestion endpoint for crash reporting and analytics  # noqa: E501

        :return: The app_secret of this AppResponse.  # noqa: E501
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this AppResponse.

        A unique and secret key used to identify the app in communication with the ingestion endpoint for crash reporting and analytics  # noqa: E501

        :param app_secret: The app_secret of this AppResponse.  # noqa: E501
        :type: str
        """

        self._app_secret = app_secret

    @property
    def azure_subscription(self):
        """Gets the azure_subscription of this AppResponse.  # noqa: E501


        :return: The azure_subscription of this AppResponse.  # noqa: E501
        :rtype: AzureSubscriptionResponse
        """
        return self._azure_subscription

    @azure_subscription.setter
    def azure_subscription(self, azure_subscription):
        """Sets the azure_subscription of this AppResponse.


        :param azure_subscription: The azure_subscription of this AppResponse.  # noqa: E501
        :type: AzureSubscriptionResponse
        """

        self._azure_subscription = azure_subscription

    @property
    def platform(self):
        """Gets the platform of this AppResponse.  # noqa: E501

        The platform of the app  # noqa: E501

        :return: The platform of this AppResponse.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this AppResponse.

        The platform of the app  # noqa: E501

        :param platform: The platform of this AppResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Java", "Objective-C-Swift", "UWP", "Cordova", "React-Native", "Unity", "Electron", "Xamarin", "WPF", "WinForms", "Unknown"]  # noqa: E501
        if platform not in allowed_values:
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"  # noqa: E501
                .format(platform, allowed_values)
            )

        self._platform = platform

    @property
    def origin(self):
        """Gets the origin of this AppResponse.  # noqa: E501

        The creation origin of this app  # noqa: E501

        :return: The origin of this AppResponse.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this AppResponse.

        The creation origin of this app  # noqa: E501

        :param origin: The origin of this AppResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["appcenter", "hockeyapp", "codepush"]  # noqa: E501
        if origin not in allowed_values:
            raise ValueError(
                "Invalid value for `origin` ({0}), must be one of {1}"  # noqa: E501
                .format(origin, allowed_values)
            )

        self._origin = origin

    @property
    def created_at(self):
        """Gets the created_at of this AppResponse.  # noqa: E501

        The created date of this app  # noqa: E501

        :return: The created_at of this AppResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AppResponse.

        The created date of this app  # noqa: E501

        :param created_at: The created_at of this AppResponse.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this AppResponse.  # noqa: E501

        The last updated date of this app  # noqa: E501

        :return: The updated_at of this AppResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AppResponse.

        The last updated date of this app  # noqa: E501

        :param updated_at: The updated_at of this AppResponse.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def member_permissions(self):
        """Gets the member_permissions of this AppResponse.  # noqa: E501

        The permissions of the calling user  # noqa: E501

        :return: The member_permissions of this AppResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_permissions

    @member_permissions.setter
    def member_permissions(self, member_permissions):
        """Sets the member_permissions of this AppResponse.

        The permissions of the calling user  # noqa: E501

        :param member_permissions: The member_permissions of this AppResponse.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["manager", "developer", "viewer", "tester"]  # noqa: E501
        if not set(member_permissions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `member_permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(member_permissions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._member_permissions = member_permissions

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
        if issubclass(AppResponse, dict):
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
        if not isinstance(other, AppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other