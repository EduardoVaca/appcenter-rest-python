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
from appcenter.models.metrics_values import MetricsValues  # noqa: F401,E501
from appcenter.models.metrics_values_by_app import MetricsValuesByApp  # noqa: F401,E501


class UsagePeriod(object):
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
        'start_time': 'str',
        'end_time': 'str',
        'by_account': 'MetricsValues',
        'by_app': 'MetricsValuesByApp'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime',
        'by_account': 'byAccount',
        'by_app': 'byApp'
    }

    def __init__(self, start_time=None, end_time=None, by_account=None, by_app=None):  # noqa: E501
        """UsagePeriod - a model defined in Swagger"""  # noqa: E501
        self._start_time = None
        self._end_time = None
        self._by_account = None
        self._by_app = None
        self.discriminator = None
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if by_account is not None:
            self.by_account = by_account
        if by_app is not None:
            self.by_app = by_app

    @property
    def start_time(self):
        """Gets the start_time of this UsagePeriod.  # noqa: E501

        Inclusive start time of the usage period  # noqa: E501

        :return: The start_time of this UsagePeriod.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this UsagePeriod.

        Inclusive start time of the usage period  # noqa: E501

        :param start_time: The start_time of this UsagePeriod.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this UsagePeriod.  # noqa: E501

        Exclusive end time of the usage period.  # noqa: E501

        :return: The end_time of this UsagePeriod.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this UsagePeriod.

        Exclusive end time of the usage period.  # noqa: E501

        :param end_time: The end_time of this UsagePeriod.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def by_account(self):
        """Gets the by_account of this UsagePeriod.  # noqa: E501


        :return: The by_account of this UsagePeriod.  # noqa: E501
        :rtype: MetricsValues
        """
        return self._by_account

    @by_account.setter
    def by_account(self, by_account):
        """Sets the by_account of this UsagePeriod.


        :param by_account: The by_account of this UsagePeriod.  # noqa: E501
        :type: MetricsValues
        """

        self._by_account = by_account

    @property
    def by_app(self):
        """Gets the by_app of this UsagePeriod.  # noqa: E501


        :return: The by_app of this UsagePeriod.  # noqa: E501
        :rtype: MetricsValuesByApp
        """
        return self._by_app

    @by_app.setter
    def by_app(self, by_app):
        """Sets the by_app of this UsagePeriod.


        :param by_app: The by_app of this UsagePeriod.  # noqa: E501
        :type: MetricsValuesByApp
        """

        self._by_app = by_app

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
        if issubclass(UsagePeriod, dict):
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
        if not isinstance(other, UsagePeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other