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


class GitHubAccountLite(object):
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
        'id': 'str',
        'login': 'str',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'login': 'login',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, id=None, login=None, type=None, url=None):  # noqa: E501
        """GitHubAccountLite - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._login = None
        self._type = None
        self._url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if login is not None:
            self.login = login
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this GitHubAccountLite.  # noqa: E501

        GitHub Account Id  # noqa: E501

        :return: The id of this GitHubAccountLite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GitHubAccountLite.

        GitHub Account Id  # noqa: E501

        :param id: The id of this GitHubAccountLite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this GitHubAccountLite.  # noqa: E501

        GitHub Account Login Name  # noqa: E501

        :return: The login of this GitHubAccountLite.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this GitHubAccountLite.

        GitHub Account Login Name  # noqa: E501

        :param login: The login of this GitHubAccountLite.  # noqa: E501
        :type: str
        """

        self._login = login

    @property
    def type(self):
        """Gets the type of this GitHubAccountLite.  # noqa: E501

        GitHub Account Type  # noqa: E501

        :return: The type of this GitHubAccountLite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GitHubAccountLite.

        GitHub Account Type  # noqa: E501

        :param type: The type of this GitHubAccountLite.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this GitHubAccountLite.  # noqa: E501

        GitHub Account Url  # noqa: E501

        :return: The url of this GitHubAccountLite.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GitHubAccountLite.

        GitHub Account Url  # noqa: E501

        :param url: The url of this GitHubAccountLite.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(GitHubAccountLite, dict):
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
        if not isinstance(other, GitHubAccountLite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
