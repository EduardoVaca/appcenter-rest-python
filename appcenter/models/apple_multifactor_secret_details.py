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


class AppleMultifactorSecretDetails(object):
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
        'username': 'str',
        'password': 'str',
        'auth_code': 'str',
        'app_specific_password': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'auth_code': 'authCode',
        'app_specific_password': 'appSpecificPassword'
    }

    def __init__(self, username=None, password=None, auth_code=None, app_specific_password=None):  # noqa: E501
        """AppleMultifactorSecretDetails - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._password = None
        self._auth_code = None
        self._app_specific_password = None
        self.discriminator = None
        self.username = username
        self.password = password
        self.auth_code = auth_code
        if app_specific_password is not None:
            self.app_specific_password = app_specific_password

    @property
    def username(self):
        """Gets the username of this AppleMultifactorSecretDetails.  # noqa: E501

        username to connect to apple store.  # noqa: E501

        :return: The username of this AppleMultifactorSecretDetails.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AppleMultifactorSecretDetails.

        username to connect to apple store.  # noqa: E501

        :param username: The username of this AppleMultifactorSecretDetails.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this AppleMultifactorSecretDetails.  # noqa: E501

        password to connect to apple store.  # noqa: E501

        :return: The password of this AppleMultifactorSecretDetails.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AppleMultifactorSecretDetails.

        password to connect to apple store.  # noqa: E501

        :param password: The password of this AppleMultifactorSecretDetails.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def auth_code(self):
        """Gets the auth_code of this AppleMultifactorSecretDetails.  # noqa: E501

        The 6 digit Apple OTP for Multifactor accounts  # noqa: E501

        :return: The auth_code of this AppleMultifactorSecretDetails.  # noqa: E501
        :rtype: str
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """Sets the auth_code of this AppleMultifactorSecretDetails.

        The 6 digit Apple OTP for Multifactor accounts  # noqa: E501

        :param auth_code: The auth_code of this AppleMultifactorSecretDetails.  # noqa: E501
        :type: str
        """
        if auth_code is None:
            raise ValueError("Invalid value for `auth_code`, must not be `None`")  # noqa: E501

        self._auth_code = auth_code

    @property
    def app_specific_password(self):
        """Gets the app_specific_password of this AppleMultifactorSecretDetails.  # noqa: E501

        The app specific password required for app publishing for 2FA accounts  # noqa: E501

        :return: The app_specific_password of this AppleMultifactorSecretDetails.  # noqa: E501
        :rtype: str
        """
        return self._app_specific_password

    @app_specific_password.setter
    def app_specific_password(self, app_specific_password):
        """Sets the app_specific_password of this AppleMultifactorSecretDetails.

        The app specific password required for app publishing for 2FA accounts  # noqa: E501

        :param app_specific_password: The app_specific_password of this AppleMultifactorSecretDetails.  # noqa: E501
        :type: str
        """

        self._app_specific_password = app_specific_password

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
        if issubclass(AppleMultifactorSecretDetails, dict):
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
        if not isinstance(other, AppleMultifactorSecretDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
