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
from appcenter.models.date_time_percentages import DateTimePercentages  # noqa: F401,E501


class CrashFreeDevicePercentages(object):
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
        'average_percentage': 'float',
        'daily_percentages': 'list[DateTimePercentages]'
    }

    attribute_map = {
        'average_percentage': 'average_percentage',
        'daily_percentages': 'daily_percentages'
    }

    def __init__(self, average_percentage=None, daily_percentages=None):  # noqa: E501
        """CrashFreeDevicePercentages - a model defined in Swagger"""  # noqa: E501
        self._average_percentage = None
        self._daily_percentages = None
        self.discriminator = None
        if average_percentage is not None:
            self.average_percentage = average_percentage
        if daily_percentages is not None:
            self.daily_percentages = daily_percentages

    @property
    def average_percentage(self):
        """Gets the average_percentage of this CrashFreeDevicePercentages.  # noqa: E501

        Average percentage.  # noqa: E501

        :return: The average_percentage of this CrashFreeDevicePercentages.  # noqa: E501
        :rtype: float
        """
        return self._average_percentage

    @average_percentage.setter
    def average_percentage(self, average_percentage):
        """Sets the average_percentage of this CrashFreeDevicePercentages.

        Average percentage.  # noqa: E501

        :param average_percentage: The average_percentage of this CrashFreeDevicePercentages.  # noqa: E501
        :type: float
        """

        self._average_percentage = average_percentage

    @property
    def daily_percentages(self):
        """Gets the daily_percentages of this CrashFreeDevicePercentages.  # noqa: E501

        The crash-free percentage per day.  # noqa: E501

        :return: The daily_percentages of this CrashFreeDevicePercentages.  # noqa: E501
        :rtype: list[DateTimePercentages]
        """
        return self._daily_percentages

    @daily_percentages.setter
    def daily_percentages(self, daily_percentages):
        """Sets the daily_percentages of this CrashFreeDevicePercentages.

        The crash-free percentage per day.  # noqa: E501

        :param daily_percentages: The daily_percentages of this CrashFreeDevicePercentages.  # noqa: E501
        :type: list[DateTimePercentages]
        """

        self._daily_percentages = daily_percentages

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
        if issubclass(CrashFreeDevicePercentages, dict):
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
        if not isinstance(other, CrashFreeDevicePercentages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
