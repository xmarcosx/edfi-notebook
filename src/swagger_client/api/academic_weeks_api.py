# coding: utf-8

"""
    Ed-Fi Operational Data Store API

    The Ed-Fi ODS / API enables applications to read and write education data stored in an Ed-Fi ODS through a secure REST interface.  ***  > *Note: Consumers of ODS / API information should sanitize all data for display and storage. The ODS / API provides reasonable safeguards against cross-site scripting attacks and other malicious content, but the platform does not and cannot guarantee that the data it contains is free of all potentially harmful content.*  ***   # noqa: E501

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AcademicWeeksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_academic_week_by_id(self, id, **kwargs):  # noqa: E501
        """Deletes an existing resource using the resource identifier.  # noqa: E501

        The DELETE operation is used to delete an existing resource by identifier. If the resource doesn't exist, an error will result (the resource will not be found).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_academic_week_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param str if_match: The ETag header value used to prevent the DELETE from removing a resource modified by another consumer.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_academic_week_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_academic_week_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_academic_week_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes an existing resource using the resource identifier.  # noqa: E501

        The DELETE operation is used to delete an existing resource by identifier. If the resource doesn't exist, an error will result (the resource will not be found).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_academic_week_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param str if_match: The ETag header value used to prevent the DELETE from removing a resource modified by another consumer.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_academic_week_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_academic_week_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/academicWeeks/{id}', 'DELETE',
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

    def deletes_academic_weeks(self, **kwargs):  # noqa: E501
        """Retrieves deleted resources based on change version.  # noqa: E501

        The DELETES operation is used to retrieve deleted resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletes_academic_weeks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :return: list[EdFiAcademicWeek]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletes_academic_weeks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.deletes_academic_weeks_with_http_info(**kwargs)  # noqa: E501
            return data

    def deletes_academic_weeks_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves deleted resources based on change version.  # noqa: E501

        The DELETES operation is used to retrieve deleted resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletes_academic_weeks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :return: list[EdFiAcademicWeek]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'min_change_version', 'max_change_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletes_academic_weeks" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 500:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `deletes_academic_weeks`, must be a value less than or equal to `500`")  # noqa: E501
        if 'limit' in params and params['limit'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `deletes_academic_weeks`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'min_change_version' in params:
            query_params.append(('minChangeVersion', params['min_change_version']))  # noqa: E501
        if 'max_change_version' in params:
            query_params.append(('maxChangeVersion', params['max_change_version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/academicWeeks/deletes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EdFiAcademicWeek]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_academic_weeks(self, **kwargs):  # noqa: E501
        """Retrieves specific resources using the resource's property values (using the \"Get\" pattern).  # noqa: E501

        This GET operation provides access to resources using the \"Get\" search pattern.  The values of any properties of the resource that are specified will be used to return all matching results (if it exists).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_academic_weeks(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :param bool total_count: Indicates if the total number of items available should be returned in the 'Total-Count' header of the response.  If set to false, 'Total-Count' header will not be provided.
        :param str week_identifier: The school label for the week.
        :param int school_id: The identifier assigned to a school.
        :param date begin_date: The start date for the academic week.
        :param date end_date: The end date for the academic week.
        :param str id: 
        :param int total_instructional_days: The total instructional days during the academic week.
        :return: list[EdFiAcademicWeek]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_academic_weeks_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_academic_weeks_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_academic_weeks_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves specific resources using the resource's property values (using the \"Get\" pattern).  # noqa: E501

        This GET operation provides access to resources using the \"Get\" search pattern.  The values of any properties of the resource that are specified will be used to return all matching results (if it exists).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_academic_weeks_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :param bool total_count: Indicates if the total number of items available should be returned in the 'Total-Count' header of the response.  If set to false, 'Total-Count' header will not be provided.
        :param str week_identifier: The school label for the week.
        :param int school_id: The identifier assigned to a school.
        :param date begin_date: The start date for the academic week.
        :param date end_date: The end date for the academic week.
        :param str id: 
        :param int total_instructional_days: The total instructional days during the academic week.
        :return: list[EdFiAcademicWeek]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'min_change_version', 'max_change_version', 'total_count', 'week_identifier', 'school_id', 'begin_date', 'end_date', 'id', 'total_instructional_days']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_academic_weeks" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 500:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_academic_weeks`, must be a value less than or equal to `500`")  # noqa: E501
        if 'limit' in params and params['limit'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_academic_weeks`, must be a value greater than or equal to `0`")  # noqa: E501
        if ('week_identifier' in params and
                len(params['week_identifier']) > 80):
            raise ValueError("Invalid value for parameter `week_identifier` when calling `get_academic_weeks`, length must be less than or equal to `80`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'min_change_version' in params:
            query_params.append(('minChangeVersion', params['min_change_version']))  # noqa: E501
        if 'max_change_version' in params:
            query_params.append(('maxChangeVersion', params['max_change_version']))  # noqa: E501
        if 'total_count' in params:
            query_params.append(('totalCount', params['total_count']))  # noqa: E501
        if 'week_identifier' in params:
            query_params.append(('weekIdentifier', params['week_identifier']))  # noqa: E501
        if 'school_id' in params:
            query_params.append(('schoolId', params['school_id']))  # noqa: E501
        if 'begin_date' in params:
            query_params.append(('beginDate', params['begin_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'total_instructional_days' in params:
            query_params.append(('totalInstructionalDays', params['total_instructional_days']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/academicWeeks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EdFiAcademicWeek]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_academic_weeks_by_id(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific resource using the resource's identifier (using the \"Get By Id\" pattern).  # noqa: E501

        This GET operation retrieves a resource by the specified resource identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_academic_weeks_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param str if_none_match: The previously returned ETag header value, used here to prevent the unnecessary data transfer of an unchanged resource.
        :return: EdFiAcademicWeek
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_academic_weeks_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_academic_weeks_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_academic_weeks_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific resource using the resource's identifier (using the \"Get By Id\" pattern).  # noqa: E501

        This GET operation retrieves a resource by the specified resource identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_academic_weeks_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param str if_none_match: The previously returned ETag header value, used here to prevent the unnecessary data transfer of an unchanged resource.
        :return: EdFiAcademicWeek
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_academic_weeks_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_academic_weeks_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/academicWeeks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EdFiAcademicWeek',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_academic_week(self, academic_week, **kwargs):  # noqa: E501
        """Creates or updates resources based on the natural key values of the supplied resource.  # noqa: E501

        The POST operation can be used to create or update resources. In database terms, this is often referred to as an \"upsert\" operation (insert + update). Clients should NOT include the resource \"id\" in the JSON body because it will result in an error (you must use a PUT operation to update a resource by \"id\"). The web service will identify whether the resource already exists based on the natural key values provided, and update or create the resource appropriately.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_academic_week(academic_week, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EdFiAcademicWeek academic_week: The JSON representation of the \"academicWeek\" resource to be created or updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_academic_week_with_http_info(academic_week, **kwargs)  # noqa: E501
        else:
            (data) = self.post_academic_week_with_http_info(academic_week, **kwargs)  # noqa: E501
            return data

    def post_academic_week_with_http_info(self, academic_week, **kwargs):  # noqa: E501
        """Creates or updates resources based on the natural key values of the supplied resource.  # noqa: E501

        The POST operation can be used to create or update resources. In database terms, this is often referred to as an \"upsert\" operation (insert + update). Clients should NOT include the resource \"id\" in the JSON body because it will result in an error (you must use a PUT operation to update a resource by \"id\"). The web service will identify whether the resource already exists based on the natural key values provided, and update or create the resource appropriately.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_academic_week_with_http_info(academic_week, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EdFiAcademicWeek academic_week: The JSON representation of the \"academicWeek\" resource to be created or updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['academic_week']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_academic_week" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'academic_week' is set
        if ('academic_week' not in params or
                params['academic_week'] is None):
            raise ValueError("Missing the required parameter `academic_week` when calling `post_academic_week`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'academic_week' in params:
            body_params = params['academic_week']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/academicWeeks', 'POST',
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

    def put_academic_week(self, id, academic_week, **kwargs):  # noqa: E501
        """Updates or creates a resource based on the resource identifier.  # noqa: E501

        The PUT operation is used to update or create a resource by identifier. If the resource doesn't exist, the resource will be created using that identifier. Additionally, natural key values cannot be changed using this operation, and will not be modified in the database.  If the resource \"id\" is provided in the JSON body, it will be ignored as well.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_academic_week(id, academic_week, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param EdFiAcademicWeek academic_week: The JSON representation of the \"academicWeek\" resource to be created or updated. (required)
        :param str if_match: The ETag header value used to prevent the PUT from updating a resource modified by another consumer.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_academic_week_with_http_info(id, academic_week, **kwargs)  # noqa: E501
        else:
            (data) = self.put_academic_week_with_http_info(id, academic_week, **kwargs)  # noqa: E501
            return data

    def put_academic_week_with_http_info(self, id, academic_week, **kwargs):  # noqa: E501
        """Updates or creates a resource based on the resource identifier.  # noqa: E501

        The PUT operation is used to update or create a resource by identifier. If the resource doesn't exist, the resource will be created using that identifier. Additionally, natural key values cannot be changed using this operation, and will not be modified in the database.  If the resource \"id\" is provided in the JSON body, it will be ignored as well.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_academic_week_with_http_info(id, academic_week, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param EdFiAcademicWeek academic_week: The JSON representation of the \"academicWeek\" resource to be created or updated. (required)
        :param str if_match: The ETag header value used to prevent the PUT from updating a resource modified by another consumer.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'academic_week', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_academic_week" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `put_academic_week`")  # noqa: E501
        # verify the required parameter 'academic_week' is set
        if ('academic_week' not in params or
                params['academic_week'] is None):
            raise ValueError("Missing the required parameter `academic_week` when calling `put_academic_week`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'academic_week' in params:
            body_params = params['academic_week']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/ed-fi/academicWeeks/{id}', 'PUT',
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
