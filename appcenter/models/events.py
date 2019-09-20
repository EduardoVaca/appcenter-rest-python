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
from appcenter.models.event import Event  # noqa: F401,E501


class Events(object):
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
        'events': 'list[Event]',
        'total': 'int',
        'total_devices': 'int'
    }

    attribute_map = {
        'events': 'events',
        'total': 'total',
        'total_devices': 'total_devices'
    }

    def __init__(self, events=None, total=None, total_devices=None):  # noqa: E501
        """Events - a model defined in Swagger"""  # noqa: E501
        self._events = None
        self._total = None
        self._total_devices = None
        self.discriminator = None
        if events is not None:
            self.events = events
        if total is not None:
            self.total = total
        if total_devices is not None:
            self.total_devices = total_devices

    @property
    def events(self):
        """Gets the events of this Events.  # noqa: E501


        :return: The events of this Events.  # noqa: E501
        :rtype: list[Event]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this Events.


        :param events: The events of this Events.  # noqa: E501
        :type: list[Event]
        """

        self._events = events

    @property
    def total(self):
        """Gets the total of this Events.  # noqa: E501

        The total count of events.  # noqa: E501

        :return: The total of this Events.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Events.

        The total count of events.  # noqa: E501

        :param total: The total of this Events.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def total_devices(self):
        """Gets the total_devices of this Events.  # noqa: E501

        The active device over this period.  # noqa: E501

        :return: The total_devices of this Events.  # noqa: E501
        :rtype: int
        """
        return self._total_devices

    @total_devices.setter
    def total_devices(self, total_devices):
        """Sets the total_devices of this Events.

        The active device over this period.  # noqa: E501

        :param total_devices: The total_devices of this Events.  # noqa: E501
        :type: int
        """

        self._total_devices = total_devices

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
        if issubclass(Events, dict):
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
        if not isinstance(other, Events):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
