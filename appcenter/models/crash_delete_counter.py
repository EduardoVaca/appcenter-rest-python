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


class CrashDeleteCounter(object):
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
        'app_id': 'str',
        'crash_group_id': 'str',
        'crash_id': 'str',
        'crashes_deleted': 'int',
        'attachments_deleted': 'int',
        'blobs_succeeded': 'int',
        'blobs_failed': 'int'
    }

    attribute_map = {
        'app_id': 'app_id',
        'crash_group_id': 'crash_group_id',
        'crash_id': 'crash_id',
        'crashes_deleted': 'crashes_deleted',
        'attachments_deleted': 'attachments_deleted',
        'blobs_succeeded': 'blobs_succeeded',
        'blobs_failed': 'blobs_failed'
    }

    def __init__(self, app_id=None, crash_group_id=None, crash_id=None, crashes_deleted=None, attachments_deleted=None, blobs_succeeded=None, blobs_failed=None):  # noqa: E501
        """CrashDeleteCounter - a model defined in Swagger"""  # noqa: E501
        self._app_id = None
        self._crash_group_id = None
        self._crash_id = None
        self._crashes_deleted = None
        self._attachments_deleted = None
        self._blobs_succeeded = None
        self._blobs_failed = None
        self.discriminator = None
        if app_id is not None:
            self.app_id = app_id
        if crash_group_id is not None:
            self.crash_group_id = crash_group_id
        if crash_id is not None:
            self.crash_id = crash_id
        if crashes_deleted is not None:
            self.crashes_deleted = crashes_deleted
        if attachments_deleted is not None:
            self.attachments_deleted = attachments_deleted
        if blobs_succeeded is not None:
            self.blobs_succeeded = blobs_succeeded
        if blobs_failed is not None:
            self.blobs_failed = blobs_failed

    @property
    def app_id(self):
        """Gets the app_id of this CrashDeleteCounter.  # noqa: E501


        :return: The app_id of this CrashDeleteCounter.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CrashDeleteCounter.


        :param app_id: The app_id of this CrashDeleteCounter.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def crash_group_id(self):
        """Gets the crash_group_id of this CrashDeleteCounter.  # noqa: E501


        :return: The crash_group_id of this CrashDeleteCounter.  # noqa: E501
        :rtype: str
        """
        return self._crash_group_id

    @crash_group_id.setter
    def crash_group_id(self, crash_group_id):
        """Sets the crash_group_id of this CrashDeleteCounter.


        :param crash_group_id: The crash_group_id of this CrashDeleteCounter.  # noqa: E501
        :type: str
        """

        self._crash_group_id = crash_group_id

    @property
    def crash_id(self):
        """Gets the crash_id of this CrashDeleteCounter.  # noqa: E501


        :return: The crash_id of this CrashDeleteCounter.  # noqa: E501
        :rtype: str
        """
        return self._crash_id

    @crash_id.setter
    def crash_id(self, crash_id):
        """Sets the crash_id of this CrashDeleteCounter.


        :param crash_id: The crash_id of this CrashDeleteCounter.  # noqa: E501
        :type: str
        """

        self._crash_id = crash_id

    @property
    def crashes_deleted(self):
        """Gets the crashes_deleted of this CrashDeleteCounter.  # noqa: E501


        :return: The crashes_deleted of this CrashDeleteCounter.  # noqa: E501
        :rtype: int
        """
        return self._crashes_deleted

    @crashes_deleted.setter
    def crashes_deleted(self, crashes_deleted):
        """Sets the crashes_deleted of this CrashDeleteCounter.


        :param crashes_deleted: The crashes_deleted of this CrashDeleteCounter.  # noqa: E501
        :type: int
        """

        self._crashes_deleted = crashes_deleted

    @property
    def attachments_deleted(self):
        """Gets the attachments_deleted of this CrashDeleteCounter.  # noqa: E501


        :return: The attachments_deleted of this CrashDeleteCounter.  # noqa: E501
        :rtype: int
        """
        return self._attachments_deleted

    @attachments_deleted.setter
    def attachments_deleted(self, attachments_deleted):
        """Sets the attachments_deleted of this CrashDeleteCounter.


        :param attachments_deleted: The attachments_deleted of this CrashDeleteCounter.  # noqa: E501
        :type: int
        """

        self._attachments_deleted = attachments_deleted

    @property
    def blobs_succeeded(self):
        """Gets the blobs_succeeded of this CrashDeleteCounter.  # noqa: E501


        :return: The blobs_succeeded of this CrashDeleteCounter.  # noqa: E501
        :rtype: int
        """
        return self._blobs_succeeded

    @blobs_succeeded.setter
    def blobs_succeeded(self, blobs_succeeded):
        """Sets the blobs_succeeded of this CrashDeleteCounter.


        :param blobs_succeeded: The blobs_succeeded of this CrashDeleteCounter.  # noqa: E501
        :type: int
        """

        self._blobs_succeeded = blobs_succeeded

    @property
    def blobs_failed(self):
        """Gets the blobs_failed of this CrashDeleteCounter.  # noqa: E501


        :return: The blobs_failed of this CrashDeleteCounter.  # noqa: E501
        :rtype: int
        """
        return self._blobs_failed

    @blobs_failed.setter
    def blobs_failed(self, blobs_failed):
        """Sets the blobs_failed of this CrashDeleteCounter.


        :param blobs_failed: The blobs_failed of this CrashDeleteCounter.  # noqa: E501
        :type: int
        """

        self._blobs_failed = blobs_failed

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
        if issubclass(CrashDeleteCounter, dict):
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
        if not isinstance(other, CrashDeleteCounter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
