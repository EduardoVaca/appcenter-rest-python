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


class TestReport(object):
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
        'app_upload_id': 'str',
        '_date': 'str',
        'test_type': 'str',
        'platform': 'str',
        'stats': 'object',
        'id': 'str',
        'schema_version': 'float',
        'revision': 'float',
        'features': 'list[object]',
        'finished_device_snapshots': 'list[str]',
        'device_logs': 'list[object]',
        'date_finished': 'str',
        'error_message': 'str',
        'snapshot_fatal_errors': 'list[object]'
    }

    attribute_map = {
        'app_upload_id': 'app_upload_id',
        '_date': 'date',
        'test_type': 'testType',
        'platform': 'platform',
        'stats': 'stats',
        'id': 'id',
        'schema_version': 'schema_version',
        'revision': 'revision',
        'features': 'features',
        'finished_device_snapshots': 'finished_device_snapshots',
        'device_logs': 'device_logs',
        'date_finished': 'date_finished',
        'error_message': 'errorMessage',
        'snapshot_fatal_errors': 'snapshot_fatal_errors'
    }

    def __init__(self, app_upload_id=None, _date=None, test_type=None, platform=None, stats=None, id=None, schema_version=None, revision=None, features=None, finished_device_snapshots=None, device_logs=None, date_finished=None, error_message=None, snapshot_fatal_errors=None):  # noqa: E501
        """TestReport - a model defined in Swagger"""  # noqa: E501
        self._app_upload_id = None
        self.__date = None
        self._test_type = None
        self._platform = None
        self._stats = None
        self._id = None
        self._schema_version = None
        self._revision = None
        self._features = None
        self._finished_device_snapshots = None
        self._device_logs = None
        self._date_finished = None
        self._error_message = None
        self._snapshot_fatal_errors = None
        self.discriminator = None
        self.app_upload_id = app_upload_id
        self._date = _date
        self.test_type = test_type
        self.platform = platform
        self.stats = stats
        self.id = id
        self.schema_version = schema_version
        self.revision = revision
        self.features = features
        self.finished_device_snapshots = finished_device_snapshots
        self.device_logs = device_logs
        self.date_finished = date_finished
        if error_message is not None:
            self.error_message = error_message
        if snapshot_fatal_errors is not None:
            self.snapshot_fatal_errors = snapshot_fatal_errors

    @property
    def app_upload_id(self):
        """Gets the app_upload_id of this TestReport.  # noqa: E501


        :return: The app_upload_id of this TestReport.  # noqa: E501
        :rtype: str
        """
        return self._app_upload_id

    @app_upload_id.setter
    def app_upload_id(self, app_upload_id):
        """Sets the app_upload_id of this TestReport.


        :param app_upload_id: The app_upload_id of this TestReport.  # noqa: E501
        :type: str
        """
        if app_upload_id is None:
            raise ValueError("Invalid value for `app_upload_id`, must not be `None`")  # noqa: E501

        self._app_upload_id = app_upload_id

    @property
    def _date(self):
        """Gets the _date of this TestReport.  # noqa: E501


        :return: The _date of this TestReport.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this TestReport.


        :param _date: The _date of this TestReport.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def test_type(self):
        """Gets the test_type of this TestReport.  # noqa: E501


        :return: The test_type of this TestReport.  # noqa: E501
        :rtype: str
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """Sets the test_type of this TestReport.


        :param test_type: The test_type of this TestReport.  # noqa: E501
        :type: str
        """
        if test_type is None:
            raise ValueError("Invalid value for `test_type`, must not be `None`")  # noqa: E501

        self._test_type = test_type

    @property
    def platform(self):
        """Gets the platform of this TestReport.  # noqa: E501


        :return: The platform of this TestReport.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this TestReport.


        :param platform: The platform of this TestReport.  # noqa: E501
        :type: str
        """
        if platform is None:
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501

        self._platform = platform

    @property
    def stats(self):
        """Gets the stats of this TestReport.  # noqa: E501


        :return: The stats of this TestReport.  # noqa: E501
        :rtype: object
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this TestReport.


        :param stats: The stats of this TestReport.  # noqa: E501
        :type: object
        """
        if stats is None:
            raise ValueError("Invalid value for `stats`, must not be `None`")  # noqa: E501

        self._stats = stats

    @property
    def id(self):
        """Gets the id of this TestReport.  # noqa: E501


        :return: The id of this TestReport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestReport.


        :param id: The id of this TestReport.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def schema_version(self):
        """Gets the schema_version of this TestReport.  # noqa: E501


        :return: The schema_version of this TestReport.  # noqa: E501
        :rtype: float
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this TestReport.


        :param schema_version: The schema_version of this TestReport.  # noqa: E501
        :type: float
        """
        if schema_version is None:
            raise ValueError("Invalid value for `schema_version`, must not be `None`")  # noqa: E501

        self._schema_version = schema_version

    @property
    def revision(self):
        """Gets the revision of this TestReport.  # noqa: E501


        :return: The revision of this TestReport.  # noqa: E501
        :rtype: float
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this TestReport.


        :param revision: The revision of this TestReport.  # noqa: E501
        :type: float
        """
        if revision is None:
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def features(self):
        """Gets the features of this TestReport.  # noqa: E501


        :return: The features of this TestReport.  # noqa: E501
        :rtype: list[object]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this TestReport.


        :param features: The features of this TestReport.  # noqa: E501
        :type: list[object]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def finished_device_snapshots(self):
        """Gets the finished_device_snapshots of this TestReport.  # noqa: E501


        :return: The finished_device_snapshots of this TestReport.  # noqa: E501
        :rtype: list[str]
        """
        return self._finished_device_snapshots

    @finished_device_snapshots.setter
    def finished_device_snapshots(self, finished_device_snapshots):
        """Sets the finished_device_snapshots of this TestReport.


        :param finished_device_snapshots: The finished_device_snapshots of this TestReport.  # noqa: E501
        :type: list[str]
        """
        if finished_device_snapshots is None:
            raise ValueError("Invalid value for `finished_device_snapshots`, must not be `None`")  # noqa: E501

        self._finished_device_snapshots = finished_device_snapshots

    @property
    def device_logs(self):
        """Gets the device_logs of this TestReport.  # noqa: E501


        :return: The device_logs of this TestReport.  # noqa: E501
        :rtype: list[object]
        """
        return self._device_logs

    @device_logs.setter
    def device_logs(self, device_logs):
        """Sets the device_logs of this TestReport.


        :param device_logs: The device_logs of this TestReport.  # noqa: E501
        :type: list[object]
        """
        if device_logs is None:
            raise ValueError("Invalid value for `device_logs`, must not be `None`")  # noqa: E501

        self._device_logs = device_logs

    @property
    def date_finished(self):
        """Gets the date_finished of this TestReport.  # noqa: E501


        :return: The date_finished of this TestReport.  # noqa: E501
        :rtype: str
        """
        return self._date_finished

    @date_finished.setter
    def date_finished(self, date_finished):
        """Sets the date_finished of this TestReport.


        :param date_finished: The date_finished of this TestReport.  # noqa: E501
        :type: str
        """
        if date_finished is None:
            raise ValueError("Invalid value for `date_finished`, must not be `None`")  # noqa: E501

        self._date_finished = date_finished

    @property
    def error_message(self):
        """Gets the error_message of this TestReport.  # noqa: E501


        :return: The error_message of this TestReport.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this TestReport.


        :param error_message: The error_message of this TestReport.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def snapshot_fatal_errors(self):
        """Gets the snapshot_fatal_errors of this TestReport.  # noqa: E501


        :return: The snapshot_fatal_errors of this TestReport.  # noqa: E501
        :rtype: list[object]
        """
        return self._snapshot_fatal_errors

    @snapshot_fatal_errors.setter
    def snapshot_fatal_errors(self, snapshot_fatal_errors):
        """Sets the snapshot_fatal_errors of this TestReport.


        :param snapshot_fatal_errors: The snapshot_fatal_errors of this TestReport.  # noqa: E501
        :type: list[object]
        """

        self._snapshot_fatal_errors = snapshot_fatal_errors

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
        if issubclass(TestReport, dict):
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
        if not isinstance(other, TestReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
