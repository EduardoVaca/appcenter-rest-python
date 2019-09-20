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


class Build(object):
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
        'id': 'int',
        'build_number': 'str',
        'queue_time': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'last_changed_date': 'str',
        'status': 'str',
        'result': 'str',
        'source_branch': 'str',
        'source_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'build_number': 'buildNumber',
        'queue_time': 'queueTime',
        'start_time': 'startTime',
        'finish_time': 'finishTime',
        'last_changed_date': 'lastChangedDate',
        'status': 'status',
        'result': 'result',
        'source_branch': 'sourceBranch',
        'source_version': 'sourceVersion'
    }

    def __init__(self, id=None, build_number=None, queue_time=None, start_time=None, finish_time=None, last_changed_date=None, status=None, result=None, source_branch=None, source_version=None):  # noqa: E501
        """Build - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._build_number = None
        self._queue_time = None
        self._start_time = None
        self._finish_time = None
        self._last_changed_date = None
        self._status = None
        self._result = None
        self._source_branch = None
        self._source_version = None
        self.discriminator = None
        self.id = id
        self.build_number = build_number
        self.queue_time = queue_time
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if last_changed_date is not None:
            self.last_changed_date = last_changed_date
        self.status = status
        self.result = result
        self.source_branch = source_branch
        self.source_version = source_version

    @property
    def id(self):
        """Gets the id of this Build.  # noqa: E501

        The build ID  # noqa: E501

        :return: The id of this Build.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Build.

        The build ID  # noqa: E501

        :param id: The id of this Build.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def build_number(self):
        """Gets the build_number of this Build.  # noqa: E501

        The build number  # noqa: E501

        :return: The build_number of this Build.  # noqa: E501
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this Build.

        The build number  # noqa: E501

        :param build_number: The build_number of this Build.  # noqa: E501
        :type: str
        """
        if build_number is None:
            raise ValueError("Invalid value for `build_number`, must not be `None`")  # noqa: E501

        self._build_number = build_number

    @property
    def queue_time(self):
        """Gets the queue_time of this Build.  # noqa: E501

        The time the build was queued  # noqa: E501

        :return: The queue_time of this Build.  # noqa: E501
        :rtype: str
        """
        return self._queue_time

    @queue_time.setter
    def queue_time(self, queue_time):
        """Sets the queue_time of this Build.

        The time the build was queued  # noqa: E501

        :param queue_time: The queue_time of this Build.  # noqa: E501
        :type: str
        """
        if queue_time is None:
            raise ValueError("Invalid value for `queue_time`, must not be `None`")  # noqa: E501

        self._queue_time = queue_time

    @property
    def start_time(self):
        """Gets the start_time of this Build.  # noqa: E501

        The time the build was started  # noqa: E501

        :return: The start_time of this Build.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Build.

        The time the build was started  # noqa: E501

        :param start_time: The start_time of this Build.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def finish_time(self):
        """Gets the finish_time of this Build.  # noqa: E501

        The time the build was finished  # noqa: E501

        :return: The finish_time of this Build.  # noqa: E501
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this Build.

        The time the build was finished  # noqa: E501

        :param finish_time: The finish_time of this Build.  # noqa: E501
        :type: str
        """

        self._finish_time = finish_time

    @property
    def last_changed_date(self):
        """Gets the last_changed_date of this Build.  # noqa: E501

        The time the build status was last changed  # noqa: E501

        :return: The last_changed_date of this Build.  # noqa: E501
        :rtype: str
        """
        return self._last_changed_date

    @last_changed_date.setter
    def last_changed_date(self, last_changed_date):
        """Sets the last_changed_date of this Build.

        The time the build status was last changed  # noqa: E501

        :param last_changed_date: The last_changed_date of this Build.  # noqa: E501
        :type: str
        """

        self._last_changed_date = last_changed_date

    @property
    def status(self):
        """Gets the status of this Build.  # noqa: E501

        The build status  # noqa: E501

        :return: The status of this Build.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Build.

        The build status  # noqa: E501

        :param status: The status of this Build.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def result(self):
        """Gets the result of this Build.  # noqa: E501

        The build result  # noqa: E501

        :return: The result of this Build.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Build.

        The build result  # noqa: E501

        :param result: The result of this Build.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    @property
    def source_branch(self):
        """Gets the source_branch of this Build.  # noqa: E501

        The source branch name  # noqa: E501

        :return: The source_branch of this Build.  # noqa: E501
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        """Sets the source_branch of this Build.

        The source branch name  # noqa: E501

        :param source_branch: The source_branch of this Build.  # noqa: E501
        :type: str
        """
        if source_branch is None:
            raise ValueError("Invalid value for `source_branch`, must not be `None`")  # noqa: E501

        self._source_branch = source_branch

    @property
    def source_version(self):
        """Gets the source_version of this Build.  # noqa: E501

        The source SHA  # noqa: E501

        :return: The source_version of this Build.  # noqa: E501
        :rtype: str
        """
        return self._source_version

    @source_version.setter
    def source_version(self, source_version):
        """Sets the source_version of this Build.

        The source SHA  # noqa: E501

        :param source_version: The source_version of this Build.  # noqa: E501
        :type: str
        """
        if source_version is None:
            raise ValueError("Invalid value for `source_version`, must not be `None`")  # noqa: E501

        self._source_version = source_version

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
        if issubclass(Build, dict):
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
        if not isinstance(other, Build):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
