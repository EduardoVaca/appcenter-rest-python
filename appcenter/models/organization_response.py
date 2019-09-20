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


class OrganizationResponse(object):
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
        'display_name': 'str',
        'name': 'str',
        'avatar_url': 'str',
        'origin': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name',
        'name': 'name',
        'avatar_url': 'avatar_url',
        'origin': 'origin',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, display_name=None, name=None, avatar_url=None, origin=None, created_at=None, updated_at=None):  # noqa: E501
        """OrganizationResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._display_name = None
        self._name = None
        self._avatar_url = None
        self._origin = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.id = id
        self.display_name = display_name
        self.name = name
        if avatar_url is not None:
            self.avatar_url = avatar_url
        self.origin = origin
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this OrganizationResponse.  # noqa: E501

        The internal unique id (UUID) of the organization.  # noqa: E501

        :return: The id of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationResponse.

        The internal unique id (UUID) of the organization.  # noqa: E501

        :param id: The id of this OrganizationResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this OrganizationResponse.  # noqa: E501

        The display name of the organization  # noqa: E501

        :return: The display_name of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this OrganizationResponse.

        The display name of the organization  # noqa: E501

        :param display_name: The display_name of this OrganizationResponse.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def name(self):
        """Gets the name of this OrganizationResponse.  # noqa: E501

        The slug name of the organization  # noqa: E501

        :return: The name of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationResponse.

        The slug name of the organization  # noqa: E501

        :param name: The name of this OrganizationResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def avatar_url(self):
        """Gets the avatar_url of this OrganizationResponse.  # noqa: E501

        The URL to a user-uploaded Avatar image  # noqa: E501

        :return: The avatar_url of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this OrganizationResponse.

        The URL to a user-uploaded Avatar image  # noqa: E501

        :param avatar_url: The avatar_url of this OrganizationResponse.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def origin(self):
        """Gets the origin of this OrganizationResponse.  # noqa: E501

        The creation origin of this organization  # noqa: E501

        :return: The origin of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this OrganizationResponse.

        The creation origin of this organization  # noqa: E501

        :param origin: The origin of this OrganizationResponse.  # noqa: E501
        :type: str
        """
        if origin is None:
            raise ValueError("Invalid value for `origin`, must not be `None`")  # noqa: E501
        allowed_values = ["appcenter", "hockeyapp"]  # noqa: E501
        if origin not in allowed_values:
            raise ValueError(
                "Invalid value for `origin` ({0}), must be one of {1}"  # noqa: E501
                .format(origin, allowed_values)
            )

        self._origin = origin

    @property
    def created_at(self):
        """Gets the created_at of this OrganizationResponse.  # noqa: E501

        The creation date of this organization  # noqa: E501

        :return: The created_at of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OrganizationResponse.

        The creation date of this organization  # noqa: E501

        :param created_at: The created_at of this OrganizationResponse.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this OrganizationResponse.  # noqa: E501

        The date the organization was last updated at  # noqa: E501

        :return: The updated_at of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OrganizationResponse.

        The date the organization was last updated at  # noqa: E501

        :param updated_at: The updated_at of this OrganizationResponse.  # noqa: E501
        :type: str
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if issubclass(OrganizationResponse, dict):
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
        if not isinstance(other, OrganizationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
