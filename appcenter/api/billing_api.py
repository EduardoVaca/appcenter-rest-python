# coding: utf-8

"""
    App Center Client

    Microsoft Visual Studio App Center API  # noqa: E501

    OpenAPI spec version: preview
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from appcenter.api_client import ApiClient


class BillingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def billing_aggregated_information_get_all(self, **kwargs):  # noqa: E501
        """billing_aggregated_information_get_all  # noqa: E501

        Aggregated Billing Information for the requesting user and the organizations in which the user is an admin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_aggregated_information_get_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service: Type of service that should be included in the Billing Information
        :param str period: Type of period that should be included in the Billing Information
        :param bool show_original_plans: Controls whether the API should show the original plan when Azure Subscription is not enabled
        :return: AllAccountsAggregatedBillingInformation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.billing_aggregated_information_get_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.billing_aggregated_information_get_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def billing_aggregated_information_get_all_with_http_info(self, **kwargs):  # noqa: E501
        """billing_aggregated_information_get_all  # noqa: E501

        Aggregated Billing Information for the requesting user and the organizations in which the user is an admin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_aggregated_information_get_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service: Type of service that should be included in the Billing Information
        :param str period: Type of period that should be included in the Billing Information
        :param bool show_original_plans: Controls whether the API should show the original plan when Azure Subscription is not enabled
        :return: AllAccountsAggregatedBillingInformation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service', 'period', 'show_original_plans']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billing_aggregated_information_get_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'service' in params:
            query_params.append(('service', params['service']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'show_original_plans' in params:
            query_params.append(('showOriginalPlans', params['show_original_plans']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/billing/allAccountsAggregated', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AllAccountsAggregatedBillingInformation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def billing_aggregated_information_get_by_app(self, owner_name, app_name, **kwargs):  # noqa: E501
        """billing_aggregated_information_get_by_app  # noqa: E501

        Aggregated Billing Information for owner of a given app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_aggregated_information_get_by_app(owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :param str service: Type of service that should be included in the Billing Information
        :param str period: Type of period that should be included in the Billing Information
        :param bool show_original_plans: Controls whether the API should show the original plan when Azure Subscription is not enabled
        :return: AggregatedBillingInformation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.billing_aggregated_information_get_by_app_with_http_info(owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.billing_aggregated_information_get_by_app_with_http_info(owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def billing_aggregated_information_get_by_app_with_http_info(self, owner_name, app_name, **kwargs):  # noqa: E501
        """billing_aggregated_information_get_by_app  # noqa: E501

        Aggregated Billing Information for owner of a given app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_aggregated_information_get_by_app_with_http_info(owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :param str service: Type of service that should be included in the Billing Information
        :param str period: Type of period that should be included in the Billing Information
        :param bool show_original_plans: Controls whether the API should show the original plan when Azure Subscription is not enabled
        :return: AggregatedBillingInformation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_name', 'app_name', 'service', 'period', 'show_original_plans']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billing_aggregated_information_get_by_app" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `billing_aggregated_information_get_by_app`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `billing_aggregated_information_get_by_app`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []
        if 'service' in params:
            query_params.append(('service', params['service']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'show_original_plans' in params:
            query_params.append(('showOriginalPlans', params['show_original_plans']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/billing/aggregated', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AggregatedBillingInformation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def billing_aggregated_information_get_for_org(self, org_name, **kwargs):  # noqa: E501
        """billing_aggregated_information_get_for_org  # noqa: E501

        Aggregated Billing Information for a given Organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_aggregated_information_get_for_org(org_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_name: The name of the Organization (required)
        :param str service: Type of service that should be included in the Billing Information
        :param str period: Type of period that should be included in the Billing Information
        :param bool show_original_plans: Controls whether the API should show the original plan when Azure Subscription is not enabled
        :return: AggregatedBillingInformation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.billing_aggregated_information_get_for_org_with_http_info(org_name, **kwargs)  # noqa: E501
        else:
            (data) = self.billing_aggregated_information_get_for_org_with_http_info(org_name, **kwargs)  # noqa: E501
            return data

    def billing_aggregated_information_get_for_org_with_http_info(self, org_name, **kwargs):  # noqa: E501
        """billing_aggregated_information_get_for_org  # noqa: E501

        Aggregated Billing Information for a given Organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_aggregated_information_get_for_org_with_http_info(org_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_name: The name of the Organization (required)
        :param str service: Type of service that should be included in the Billing Information
        :param str period: Type of period that should be included in the Billing Information
        :param bool show_original_plans: Controls whether the API should show the original plan when Azure Subscription is not enabled
        :return: AggregatedBillingInformation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org_name', 'service', 'period', 'show_original_plans']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billing_aggregated_information_get_for_org" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org_name' is set
        if ('org_name' not in params or
                params['org_name'] is None):
            raise ValueError("Missing the required parameter `org_name` when calling `billing_aggregated_information_get_for_org`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org_name' in params:
            path_params['orgName'] = params['org_name']  # noqa: E501

        query_params = []
        if 'service' in params:
            query_params.append(('service', params['service']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501
        if 'show_original_plans' in params:
            query_params.append(('showOriginalPlans', params['show_original_plans']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/orgs/{orgName}/billing/aggregated', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AggregatedBillingInformation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)