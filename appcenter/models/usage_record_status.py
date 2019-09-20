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


class UsageRecordStatus(object):
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
        'expected_latest_build_exists': 'bool',
        'expected_latest_test_exists': 'bool',
        'latest_build_usage_record_time': 'str',
        'latest_test_usage_record_time': 'str'
    }

    attribute_map = {
        'expected_latest_build_exists': 'expectedLatestBuildExists',
        'expected_latest_test_exists': 'expectedLatestTestExists',
        'latest_build_usage_record_time': 'latestBuildUsageRecordTime',
        'latest_test_usage_record_time': 'latestTestUsageRecordTime'
    }

    def __init__(self, expected_latest_build_exists=None, expected_latest_test_exists=None, latest_build_usage_record_time=None, latest_test_usage_record_time=None):  # noqa: E501
        """UsageRecordStatus - a model defined in Swagger"""  # noqa: E501
        self._expected_latest_build_exists = None
        self._expected_latest_test_exists = None
        self._latest_build_usage_record_time = None
        self._latest_test_usage_record_time = None
        self.discriminator = None
        if expected_latest_build_exists is not None:
            self.expected_latest_build_exists = expected_latest_build_exists
        if expected_latest_test_exists is not None:
            self.expected_latest_test_exists = expected_latest_test_exists
        if latest_build_usage_record_time is not None:
            self.latest_build_usage_record_time = latest_build_usage_record_time
        if latest_test_usage_record_time is not None:
            self.latest_test_usage_record_time = latest_test_usage_record_time

    @property
    def expected_latest_build_exists(self):
        """Gets the expected_latest_build_exists of this UsageRecordStatus.  # noqa: E501

        Is the age of the most recent Build service usage record within expected limits  # noqa: E501

        :return: The expected_latest_build_exists of this UsageRecordStatus.  # noqa: E501
        :rtype: bool
        """
        return self._expected_latest_build_exists

    @expected_latest_build_exists.setter
    def expected_latest_build_exists(self, expected_latest_build_exists):
        """Sets the expected_latest_build_exists of this UsageRecordStatus.

        Is the age of the most recent Build service usage record within expected limits  # noqa: E501

        :param expected_latest_build_exists: The expected_latest_build_exists of this UsageRecordStatus.  # noqa: E501
        :type: bool
        """

        self._expected_latest_build_exists = expected_latest_build_exists

    @property
    def expected_latest_test_exists(self):
        """Gets the expected_latest_test_exists of this UsageRecordStatus.  # noqa: E501

        Is the age of the most recent Test service usage record within expected limits  # noqa: E501

        :return: The expected_latest_test_exists of this UsageRecordStatus.  # noqa: E501
        :rtype: bool
        """
        return self._expected_latest_test_exists

    @expected_latest_test_exists.setter
    def expected_latest_test_exists(self, expected_latest_test_exists):
        """Sets the expected_latest_test_exists of this UsageRecordStatus.

        Is the age of the most recent Test service usage record within expected limits  # noqa: E501

        :param expected_latest_test_exists: The expected_latest_test_exists of this UsageRecordStatus.  # noqa: E501
        :type: bool
        """

        self._expected_latest_test_exists = expected_latest_test_exists

    @property
    def latest_build_usage_record_time(self):
        """Gets the latest_build_usage_record_time of this UsageRecordStatus.  # noqa: E501

        The time of the most recent Build service usage record  # noqa: E501

        :return: The latest_build_usage_record_time of this UsageRecordStatus.  # noqa: E501
        :rtype: str
        """
        return self._latest_build_usage_record_time

    @latest_build_usage_record_time.setter
    def latest_build_usage_record_time(self, latest_build_usage_record_time):
        """Sets the latest_build_usage_record_time of this UsageRecordStatus.

        The time of the most recent Build service usage record  # noqa: E501

        :param latest_build_usage_record_time: The latest_build_usage_record_time of this UsageRecordStatus.  # noqa: E501
        :type: str
        """

        self._latest_build_usage_record_time = latest_build_usage_record_time

    @property
    def latest_test_usage_record_time(self):
        """Gets the latest_test_usage_record_time of this UsageRecordStatus.  # noqa: E501

        The time of the most recent Test service usage record  # noqa: E501

        :return: The latest_test_usage_record_time of this UsageRecordStatus.  # noqa: E501
        :rtype: str
        """
        return self._latest_test_usage_record_time

    @latest_test_usage_record_time.setter
    def latest_test_usage_record_time(self, latest_test_usage_record_time):
        """Sets the latest_test_usage_record_time of this UsageRecordStatus.

        The time of the most recent Test service usage record  # noqa: E501

        :param latest_test_usage_record_time: The latest_test_usage_record_time of this UsageRecordStatus.  # noqa: E501
        :type: str
        """

        self._latest_test_usage_record_time = latest_test_usage_record_time

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
        if issubclass(UsageRecordStatus, dict):
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
        if not isinstance(other, UsageRecordStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
