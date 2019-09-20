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


class MbaasApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def data_check_name_exists(self, ac_authorization_arm, account_name, owner_name, app_name, **kwargs):  # noqa: E501
        """Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the '-' character, and must be between 3 and 31 characters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_check_name_exists(ac_authorization_arm, account_name, owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ac_authorization_arm: ARM token (required)
        :param str account_name: Account Name (required)
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_check_name_exists_with_http_info(ac_authorization_arm, account_name, owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_check_name_exists_with_http_info(ac_authorization_arm, account_name, owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def data_check_name_exists_with_http_info(self, ac_authorization_arm, account_name, owner_name, app_name, **kwargs):  # noqa: E501
        """Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the '-' character, and must be between 3 and 31 characters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_check_name_exists_with_http_info(ac_authorization_arm, account_name, owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ac_authorization_arm: ARM token (required)
        :param str account_name: Account Name (required)
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ac_authorization_arm', 'account_name', 'owner_name', 'app_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_check_name_exists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ac_authorization_arm' is set
        if ('ac_authorization_arm' not in params or
                params['ac_authorization_arm'] is None):
            raise ValueError("Missing the required parameter `ac_authorization_arm` when calling `data_check_name_exists`")  # noqa: E501
        # verify the required parameter 'account_name' is set
        if ('account_name' not in params or
                params['account_name'] is None):
            raise ValueError("Missing the required parameter `account_name` when calling `data_check_name_exists`")  # noqa: E501
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `data_check_name_exists`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `data_check_name_exists`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_name' in params:
            path_params['accountName'] = params['account_name']  # noqa: E501
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'ac_authorization_arm' in params:
            header_params['AC-Authorization-ARM'] = params['ac_authorization_arm']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/data/database_account_names/{accountName}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_get_overview(self, ac_authorization_arm, owner_name, app_name, **kwargs):  # noqa: E501
        """Gets general data about the provisioned database  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_get_overview(ac_authorization_arm, owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ac_authorization_arm: ARM access token. (required)
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :return: OverviewResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_get_overview_with_http_info(ac_authorization_arm, owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_get_overview_with_http_info(ac_authorization_arm, owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def data_get_overview_with_http_info(self, ac_authorization_arm, owner_name, app_name, **kwargs):  # noqa: E501
        """Gets general data about the provisioned database  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_get_overview_with_http_info(ac_authorization_arm, owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ac_authorization_arm: ARM access token. (required)
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :return: OverviewResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ac_authorization_arm', 'owner_name', 'app_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_get_overview" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ac_authorization_arm' is set
        if ('ac_authorization_arm' not in params or
                params['ac_authorization_arm'] is None):
            raise ValueError("Missing the required parameter `ac_authorization_arm` when calling `data_get_overview`")  # noqa: E501
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `data_get_overview`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `data_get_overview`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'ac_authorization_arm' in params:
            header_params['AC-Authorization-ARM'] = params['ac_authorization_arm']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/data/overview', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OverviewResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_get_resource_provisioning(self, owner_name, app_name, **kwargs):  # noqa: E501
        """data_get_resource_provisioning  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_get_resource_provisioning(owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :return: ProvisionStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_get_resource_provisioning_with_http_info(owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_get_resource_provisioning_with_http_info(owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def data_get_resource_provisioning_with_http_info(self, owner_name, app_name, **kwargs):  # noqa: E501
        """data_get_resource_provisioning  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_get_resource_provisioning_with_http_info(owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :return: ProvisionStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_name', 'app_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_get_resource_provisioning" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `data_get_resource_provisioning`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `data_get_resource_provisioning`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/data/resource_provisioning', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProvisionStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_post_resource_provisioning(self, ac_authorization_arm, owner_name, app_name, **kwargs):  # noqa: E501
        """Creates Cosmos DB or attaches an existing one  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_post_resource_provisioning(ac_authorization_arm, owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ac_authorization_arm: (required)
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :param DataProvisioningParameters body:
        :return: ProvisionStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_post_resource_provisioning_with_http_info(ac_authorization_arm, owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.data_post_resource_provisioning_with_http_info(ac_authorization_arm, owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def data_post_resource_provisioning_with_http_info(self, ac_authorization_arm, owner_name, app_name, **kwargs):  # noqa: E501
        """Creates Cosmos DB or attaches an existing one  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_post_resource_provisioning_with_http_info(ac_authorization_arm, owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ac_authorization_arm: (required)
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :param DataProvisioningParameters body:
        :return: ProvisionStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ac_authorization_arm', 'owner_name', 'app_name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_post_resource_provisioning" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ac_authorization_arm' is set
        if ('ac_authorization_arm' not in params or
                params['ac_authorization_arm'] is None):
            raise ValueError("Missing the required parameter `ac_authorization_arm` when calling `data_post_resource_provisioning`")  # noqa: E501
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `data_post_resource_provisioning`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `data_post_resource_provisioning`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'ac_authorization_arm' in params:
            header_params['AC-Authorization-ARM'] = params['ac_authorization_arm']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/data/resource_provisioning', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProvisionStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def identity_get_users(self, owner_name, app_name, **kwargs):  # noqa: E501
        """Returns users of a tenant. Returns all users if no searchTerm param is specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.identity_get_users(owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :param str ac_authorization_aad_graph: MSGraph Auth Token
        :param str search_term: User search term
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.identity_get_users_with_http_info(owner_name, app_name, **kwargs)  # noqa: E501
        else:
            (data) = self.identity_get_users_with_http_info(owner_name, app_name, **kwargs)  # noqa: E501
            return data

    def identity_get_users_with_http_info(self, owner_name, app_name, **kwargs):  # noqa: E501
        """Returns users of a tenant. Returns all users if no searchTerm param is specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.identity_get_users_with_http_info(owner_name, app_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_name: The name of the owner (required)
        :param str app_name: The name of the application (required)
        :param str ac_authorization_aad_graph: MSGraph Auth Token
        :param str search_term: User search term
        :return: UsersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_name', 'app_name', 'ac_authorization_aad_graph', 'search_term']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method identity_get_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_name' is set
        if ('owner_name' not in params or
                params['owner_name'] is None):
            raise ValueError("Missing the required parameter `owner_name` when calling `identity_get_users`")  # noqa: E501
        # verify the required parameter 'app_name' is set
        if ('app_name' not in params or
                params['app_name'] is None):
            raise ValueError("Missing the required parameter `app_name` when calling `identity_get_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_name' in params:
            path_params['owner_name'] = params['owner_name']  # noqa: E501
        if 'app_name' in params:
            path_params['app_name'] = params['app_name']  # noqa: E501

        query_params = []
        if 'search_term' in params:
            query_params.append(('searchTerm', params['search_term']))  # noqa: E501

        header_params = {}
        if 'ac_authorization_aad_graph' in params:
            header_params['AC-Authorization-AAD-Graph'] = params['ac_authorization_aad_graph']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/apps/{owner_name}/{app_name}/auth/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UsersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
