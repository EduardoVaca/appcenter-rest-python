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


class AppUserPermissionResponse(object):
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
        'app_id': 'str',
        'permissions': 'list[str]',
        'user_email': 'str',
        'user_id': 'str',
        'app_origin': 'str',
        'app_secret': 'str',
        'is_cutover_from_hockeyapp': 'bool'
    }

    attribute_map = {
        'app_id': 'app_id',
        'permissions': 'permissions',
        'user_email': 'user_email',
        'user_id': 'user_id',
        'app_origin': 'app_origin',
        'app_secret': 'app_secret',
        'is_cutover_from_hockeyapp': 'is_cutover_from_hockeyapp'
    }

    def __init__(self, app_id=None, permissions=None, user_email=None, user_id=None, app_origin=None, app_secret=None, is_cutover_from_hockeyapp=None):  # noqa: E501
        """AppUserPermissionResponse - a model defined in Swagger"""  # noqa: E501
        self._app_id = None
        self._permissions = None
        self._user_email = None
        self._user_id = None
        self._app_origin = None
        self._app_secret = None
        self._is_cutover_from_hockeyapp = None
        self.discriminator = None
        self.app_id = app_id
        self.permissions = permissions
        self.user_email = user_email
        self.user_id = user_id
        self.app_origin = app_origin
        self.app_secret = app_secret
        self.is_cutover_from_hockeyapp = is_cutover_from_hockeyapp

    @property
    def app_id(self):
        """Gets the app_id of this AppUserPermissionResponse.  # noqa: E501

        The unique id (UUID) of the app  # noqa: E501

        :return: The app_id of this AppUserPermissionResponse.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AppUserPermissionResponse.

        The unique id (UUID) of the app  # noqa: E501

        :param app_id: The app_id of this AppUserPermissionResponse.  # noqa: E501
        :type: str
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def permissions(self):
        """Gets the permissions of this AppUserPermissionResponse.  # noqa: E501

        The permissions the user has for the app  # noqa: E501

        :return: The permissions of this AppUserPermissionResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this AppUserPermissionResponse.

        The permissions the user has for the app  # noqa: E501

        :param permissions: The permissions of this AppUserPermissionResponse.  # noqa: E501
        :type: list[str]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501
        allowed_values = ["manager", "developer", "viewer", "tester"]  # noqa: E501
        if not set(permissions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(permissions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._permissions = permissions

    @property
    def user_email(self):
        """Gets the user_email of this AppUserPermissionResponse.  # noqa: E501

        The email of the user  # noqa: E501

        :return: The user_email of this AppUserPermissionResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this AppUserPermissionResponse.

        The email of the user  # noqa: E501

        :param user_email: The user_email of this AppUserPermissionResponse.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

    @property
    def user_id(self):
        """Gets the user_id of this AppUserPermissionResponse.  # noqa: E501

        The unique id (UUID) of the user  # noqa: E501

        :return: The user_id of this AppUserPermissionResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AppUserPermissionResponse.

        The unique id (UUID) of the user  # noqa: E501

        :param user_id: The user_id of this AppUserPermissionResponse.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def app_origin(self):
        """Gets the app_origin of this AppUserPermissionResponse.  # noqa: E501

        The creation origin of this app  # noqa: E501

        :return: The app_origin of this AppUserPermissionResponse.  # noqa: E501
        :rtype: str
        """
        return self._app_origin

    @app_origin.setter
    def app_origin(self, app_origin):
        """Sets the app_origin of this AppUserPermissionResponse.

        The creation origin of this app  # noqa: E501

        :param app_origin: The app_origin of this AppUserPermissionResponse.  # noqa: E501
        :type: str
        """
        if app_origin is None:
            raise ValueError("Invalid value for `app_origin`, must not be `None`")  # noqa: E501
        allowed_values = ["appcenter", "hockeyapp", "codepush"]  # noqa: E501
        if app_origin not in allowed_values:
            raise ValueError(
                "Invalid value for `app_origin` ({0}), must be one of {1}"  # noqa: E501
                .format(app_origin, allowed_values)
            )

        self._app_origin = app_origin

    @property
    def app_secret(self):
        """Gets the app_secret of this AppUserPermissionResponse.  # noqa: E501

        A unique and secret key used to identify the app in communication with the ingestion endpoint for crash reporting and analytics  # noqa: E501

        :return: The app_secret of this AppUserPermissionResponse.  # noqa: E501
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this AppUserPermissionResponse.

        A unique and secret key used to identify the app in communication with the ingestion endpoint for crash reporting and analytics  # noqa: E501

        :param app_secret: The app_secret of this AppUserPermissionResponse.  # noqa: E501
        :type: str
        """
        if app_secret is None:
            raise ValueError("Invalid value for `app_secret`, must not be `None`")  # noqa: E501

        self._app_secret = app_secret

    @property
    def is_cutover_from_hockeyapp(self):
        """Gets the is_cutover_from_hockeyapp of this AppUserPermissionResponse.  # noqa: E501

        Whether the app had a 'hockeyapp' origin before being \"cut over\" to App Center  # noqa: E501

        :return: The is_cutover_from_hockeyapp of this AppUserPermissionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_cutover_from_hockeyapp

    @is_cutover_from_hockeyapp.setter
    def is_cutover_from_hockeyapp(self, is_cutover_from_hockeyapp):
        """Sets the is_cutover_from_hockeyapp of this AppUserPermissionResponse.

        Whether the app had a 'hockeyapp' origin before being \"cut over\" to App Center  # noqa: E501

        :param is_cutover_from_hockeyapp: The is_cutover_from_hockeyapp of this AppUserPermissionResponse.  # noqa: E501
        :type: bool
        """
        if is_cutover_from_hockeyapp is None:
            raise ValueError("Invalid value for `is_cutover_from_hockeyapp`, must not be `None`")  # noqa: E501

        self._is_cutover_from_hockeyapp = is_cutover_from_hockeyapp

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
        if issubclass(AppUserPermissionResponse, dict):
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
        if not isinstance(other, AppUserPermissionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
