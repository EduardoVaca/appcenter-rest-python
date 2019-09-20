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


class Event(object):
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
        'name': 'str',
        'device_count': 'int',
        'previous_device_count': 'int',
        'count': 'int',
        'previous_count': 'int',
        'count_per_device': 'float',
        'count_per_session': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'device_count': 'device_count',
        'previous_device_count': 'previous_device_count',
        'count': 'count',
        'previous_count': 'previous_count',
        'count_per_device': 'count_per_device',
        'count_per_session': 'count_per_session'
    }

    def __init__(self, id=None, name=None, device_count=None, previous_device_count=None, count=None, previous_count=None, count_per_device=None, count_per_session=None):  # noqa: E501
        """Event - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._device_count = None
        self._previous_device_count = None
        self._count = None
        self._previous_count = None
        self._count_per_device = None
        self._count_per_session = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if device_count is not None:
            self.device_count = device_count
        if previous_device_count is not None:
            self.previous_device_count = previous_device_count
        if count is not None:
            self.count = count
        if previous_count is not None:
            self.previous_count = previous_count
        if count_per_device is not None:
            self.count_per_device = count_per_device
        if count_per_session is not None:
            self.count_per_session = count_per_session

    @property
    def id(self):
        """Gets the id of this Event.  # noqa: E501


        :return: The id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Event.


        :param id: The id of this Event.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Event.  # noqa: E501


        :return: The name of this Event.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Event.


        :param name: The name of this Event.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def device_count(self):
        """Gets the device_count of this Event.  # noqa: E501


        :return: The device_count of this Event.  # noqa: E501
        :rtype: int
        """
        return self._device_count

    @device_count.setter
    def device_count(self, device_count):
        """Sets the device_count of this Event.


        :param device_count: The device_count of this Event.  # noqa: E501
        :type: int
        """

        self._device_count = device_count

    @property
    def previous_device_count(self):
        """Gets the previous_device_count of this Event.  # noqa: E501

        The device count of previous time range of the event.  # noqa: E501

        :return: The previous_device_count of this Event.  # noqa: E501
        :rtype: int
        """
        return self._previous_device_count

    @previous_device_count.setter
    def previous_device_count(self, previous_device_count):
        """Sets the previous_device_count of this Event.

        The device count of previous time range of the event.  # noqa: E501

        :param previous_device_count: The previous_device_count of this Event.  # noqa: E501
        :type: int
        """

        self._previous_device_count = previous_device_count

    @property
    def count(self):
        """Gets the count of this Event.  # noqa: E501


        :return: The count of this Event.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Event.


        :param count: The count of this Event.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def previous_count(self):
        """Gets the previous_count of this Event.  # noqa: E501

        The event count of previous time range of the event.  # noqa: E501

        :return: The previous_count of this Event.  # noqa: E501
        :rtype: int
        """
        return self._previous_count

    @previous_count.setter
    def previous_count(self, previous_count):
        """Sets the previous_count of this Event.

        The event count of previous time range of the event.  # noqa: E501

        :param previous_count: The previous_count of this Event.  # noqa: E501
        :type: int
        """

        self._previous_count = previous_count

    @property
    def count_per_device(self):
        """Gets the count_per_device of this Event.  # noqa: E501


        :return: The count_per_device of this Event.  # noqa: E501
        :rtype: float
        """
        return self._count_per_device

    @count_per_device.setter
    def count_per_device(self, count_per_device):
        """Sets the count_per_device of this Event.


        :param count_per_device: The count_per_device of this Event.  # noqa: E501
        :type: float
        """

        self._count_per_device = count_per_device

    @property
    def count_per_session(self):
        """Gets the count_per_session of this Event.  # noqa: E501


        :return: The count_per_session of this Event.  # noqa: E501
        :rtype: float
        """
        return self._count_per_session

    @count_per_session.setter
    def count_per_session(self, count_per_session):
        """Sets the count_per_session of this Event.


        :param count_per_session: The count_per_session of this Event.  # noqa: E501
        :type: float
        """

        self._count_per_session = count_per_session

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
