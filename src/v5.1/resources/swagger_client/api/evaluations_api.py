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


class EvaluationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_evaluation_by_id(self, id, **kwargs):  # noqa: E501
        """Deletes an existing resource using the resource identifier.  # noqa: E501

        The DELETE operation is used to delete an existing resource by identifier. If the resource doesn't exist, an error will result (the resource will not be found).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_evaluation_by_id(id, async_req=True)
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
            return self.delete_evaluation_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_evaluation_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_evaluation_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes an existing resource using the resource identifier.  # noqa: E501

        The DELETE operation is used to delete an existing resource by identifier. If the resource doesn't exist, an error will result (the resource will not be found).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_evaluation_by_id_with_http_info(id, async_req=True)
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
                    " to method delete_evaluation_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `delete_evaluation_by_id`")  # noqa: E501

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
            '/tpdm/evaluations/{id}', 'DELETE',
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

    def deletes_evaluations(self, **kwargs):  # noqa: E501
        """Retrieves deleted resources based on change version.  # noqa: E501

        The DELETES operation is used to retrieve deleted resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletes_evaluations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :return: list[TpdmEvaluation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletes_evaluations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.deletes_evaluations_with_http_info(**kwargs)  # noqa: E501
            return data

    def deletes_evaluations_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves deleted resources based on change version.  # noqa: E501

        The DELETES operation is used to retrieve deleted resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletes_evaluations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :return: list[TpdmEvaluation]
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
                    " to method deletes_evaluations" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('limit' in params and params['limit'] > 500):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `deletes_evaluations`, must be a value less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 0):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `deletes_evaluations`, must be a value greater than or equal to `0`")  # noqa: E501
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
            '/tpdm/evaluations/deletes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TpdmEvaluation]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_evaluations(self, **kwargs):  # noqa: E501
        """Retrieves specific resources using the resource's property values (using the \"Get\" pattern).  # noqa: E501

        This GET operation provides access to resources using the \"Get\" search pattern.  The values of any properties of the resource that are specified will be used to return all matching results (if it exists).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_evaluations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :param bool total_count: Indicates if the total number of items available should be returned in the 'Total-Count' header of the response.  If set to false, 'Total-Count' header will not be provided.
        :param str evaluation_title: The name or title of the evaluation.
        :param int education_organization_id: The identifier assigned to an education organization.
        :param str evaluation_period_descriptor: The period for the evaluation (e.g., BOY, MOY, EOY, Summer).
        :param str performance_evaluation_title: An assigned unique identifier for the performance evaluation.
        :param str performance_evaluation_type_descriptor: The type (e.g., walkthrough, summative) of performance evaluation conducted.
        :param int school_year: The identifier for the school year.
        :param str term_descriptor: The term for the session during the school year.
        :param str evaluation_type_descriptor: The type of the evaluation (e.g., observation, principal, peer, student survey, student growth).
        :param str id: 
        :param int inter_rater_reliability_score: A score indicating how much homogeneity, or consensus, there is in the ratings given by judges.
        :param float max_rating: The maximum summary numerical rating or score for the evaluation.
        :param float min_rating: The minimum summary numerical rating or score for the evaluation. If omitted, assumed to be 0.0.
        :return: list[TpdmEvaluation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_evaluations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_evaluations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_evaluations_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves specific resources using the resource's property values (using the \"Get\" pattern).  # noqa: E501

        This GET operation provides access to resources using the \"Get\" search pattern.  The values of any properties of the resource that are specified will be used to return all matching results (if it exists).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_evaluations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset: Indicates how many items should be skipped before returning results.
        :param int limit: Indicates the maximum number of items that should be returned in the results.
        :param int min_change_version: Used in synchronization to set sequence minimum ChangeVersion
        :param int max_change_version: Used in synchronization to set sequence maximum ChangeVersion
        :param bool total_count: Indicates if the total number of items available should be returned in the 'Total-Count' header of the response.  If set to false, 'Total-Count' header will not be provided.
        :param str evaluation_title: The name or title of the evaluation.
        :param int education_organization_id: The identifier assigned to an education organization.
        :param str evaluation_period_descriptor: The period for the evaluation (e.g., BOY, MOY, EOY, Summer).
        :param str performance_evaluation_title: An assigned unique identifier for the performance evaluation.
        :param str performance_evaluation_type_descriptor: The type (e.g., walkthrough, summative) of performance evaluation conducted.
        :param int school_year: The identifier for the school year.
        :param str term_descriptor: The term for the session during the school year.
        :param str evaluation_type_descriptor: The type of the evaluation (e.g., observation, principal, peer, student survey, student growth).
        :param str id: 
        :param int inter_rater_reliability_score: A score indicating how much homogeneity, or consensus, there is in the ratings given by judges.
        :param float max_rating: The maximum summary numerical rating or score for the evaluation.
        :param float min_rating: The minimum summary numerical rating or score for the evaluation. If omitted, assumed to be 0.0.
        :return: list[TpdmEvaluation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'min_change_version', 'max_change_version', 'total_count', 'evaluation_title', 'education_organization_id', 'evaluation_period_descriptor', 'performance_evaluation_title', 'performance_evaluation_type_descriptor', 'school_year', 'term_descriptor', 'evaluation_type_descriptor', 'id', 'inter_rater_reliability_score', 'max_rating', 'min_rating']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_evaluations" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('limit' in params and params['limit'] > 500):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_evaluations`, must be a value less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 0):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_evaluations`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and ('evaluation_title' in params and
                                                       len(params['evaluation_title']) > 50):
            raise ValueError("Invalid value for parameter `evaluation_title` when calling `get_evaluations`, length must be less than or equal to `50`")  # noqa: E501
        if self.api_client.client_side_validation and ('evaluation_period_descriptor' in params and
                                                       len(params['evaluation_period_descriptor']) > 306):
            raise ValueError("Invalid value for parameter `evaluation_period_descriptor` when calling `get_evaluations`, length must be less than or equal to `306`")  # noqa: E501
        if self.api_client.client_side_validation and ('performance_evaluation_title' in params and
                                                       len(params['performance_evaluation_title']) > 50):
            raise ValueError("Invalid value for parameter `performance_evaluation_title` when calling `get_evaluations`, length must be less than or equal to `50`")  # noqa: E501
        if self.api_client.client_side_validation and ('performance_evaluation_type_descriptor' in params and
                                                       len(params['performance_evaluation_type_descriptor']) > 306):
            raise ValueError("Invalid value for parameter `performance_evaluation_type_descriptor` when calling `get_evaluations`, length must be less than or equal to `306`")  # noqa: E501
        if self.api_client.client_side_validation and ('term_descriptor' in params and
                                                       len(params['term_descriptor']) > 306):
            raise ValueError("Invalid value for parameter `term_descriptor` when calling `get_evaluations`, length must be less than or equal to `306`")  # noqa: E501
        if self.api_client.client_side_validation and ('evaluation_type_descriptor' in params and
                                                       len(params['evaluation_type_descriptor']) > 306):
            raise ValueError("Invalid value for parameter `evaluation_type_descriptor` when calling `get_evaluations`, length must be less than or equal to `306`")  # noqa: E501
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
        if 'evaluation_title' in params:
            query_params.append(('evaluationTitle', params['evaluation_title']))  # noqa: E501
        if 'education_organization_id' in params:
            query_params.append(('educationOrganizationId', params['education_organization_id']))  # noqa: E501
        if 'evaluation_period_descriptor' in params:
            query_params.append(('evaluationPeriodDescriptor', params['evaluation_period_descriptor']))  # noqa: E501
        if 'performance_evaluation_title' in params:
            query_params.append(('performanceEvaluationTitle', params['performance_evaluation_title']))  # noqa: E501
        if 'performance_evaluation_type_descriptor' in params:
            query_params.append(('performanceEvaluationTypeDescriptor', params['performance_evaluation_type_descriptor']))  # noqa: E501
        if 'school_year' in params:
            query_params.append(('schoolYear', params['school_year']))  # noqa: E501
        if 'term_descriptor' in params:
            query_params.append(('termDescriptor', params['term_descriptor']))  # noqa: E501
        if 'evaluation_type_descriptor' in params:
            query_params.append(('evaluationTypeDescriptor', params['evaluation_type_descriptor']))  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'inter_rater_reliability_score' in params:
            query_params.append(('interRaterReliabilityScore', params['inter_rater_reliability_score']))  # noqa: E501
        if 'max_rating' in params:
            query_params.append(('maxRating', params['max_rating']))  # noqa: E501
        if 'min_rating' in params:
            query_params.append(('minRating', params['min_rating']))  # noqa: E501

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
            '/tpdm/evaluations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TpdmEvaluation]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_evaluations_by_id(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific resource using the resource's identifier (using the \"Get By Id\" pattern).  # noqa: E501

        This GET operation retrieves a resource by the specified resource identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_evaluations_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param str if_none_match: The previously returned ETag header value, used here to prevent the unnecessary data transfer of an unchanged resource.
        :return: TpdmEvaluation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_evaluations_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_evaluations_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_evaluations_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a specific resource using the resource's identifier (using the \"Get By Id\" pattern).  # noqa: E501

        This GET operation retrieves a resource by the specified resource identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_evaluations_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param str if_none_match: The previously returned ETag header value, used here to prevent the unnecessary data transfer of an unchanged resource.
        :return: TpdmEvaluation
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
                    " to method get_evaluations_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_evaluations_by_id`")  # noqa: E501

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
            '/tpdm/evaluations/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TpdmEvaluation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_evaluation(self, evaluation, **kwargs):  # noqa: E501
        """Creates or updates resources based on the natural key values of the supplied resource.  # noqa: E501

        The POST operation can be used to create or update resources. In database terms, this is often referred to as an \"upsert\" operation (insert + update). Clients should NOT include the resource \"id\" in the JSON body because it will result in an error (you must use a PUT operation to update a resource by \"id\"). The web service will identify whether the resource already exists based on the natural key values provided, and update or create the resource appropriately.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_evaluation(evaluation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TpdmEvaluation evaluation: The JSON representation of the \"evaluation\" resource to be created or updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_evaluation_with_http_info(evaluation, **kwargs)  # noqa: E501
        else:
            (data) = self.post_evaluation_with_http_info(evaluation, **kwargs)  # noqa: E501
            return data

    def post_evaluation_with_http_info(self, evaluation, **kwargs):  # noqa: E501
        """Creates or updates resources based on the natural key values of the supplied resource.  # noqa: E501

        The POST operation can be used to create or update resources. In database terms, this is often referred to as an \"upsert\" operation (insert + update). Clients should NOT include the resource \"id\" in the JSON body because it will result in an error (you must use a PUT operation to update a resource by \"id\"). The web service will identify whether the resource already exists based on the natural key values provided, and update or create the resource appropriately.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_evaluation_with_http_info(evaluation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TpdmEvaluation evaluation: The JSON representation of the \"evaluation\" resource to be created or updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['evaluation']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_evaluation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'evaluation' is set
        if self.api_client.client_side_validation and ('evaluation' not in params or
                                                       params['evaluation'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `evaluation` when calling `post_evaluation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'evaluation' in params:
            body_params = params['evaluation']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/tpdm/evaluations', 'POST',
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

    def put_evaluation(self, id, evaluation, **kwargs):  # noqa: E501
        """Updates or creates a resource based on the resource identifier.  # noqa: E501

        The PUT operation is used to update or create a resource by identifier. If the resource doesn't exist, the resource will be created using that identifier. Additionally, natural key values cannot be changed using this operation, and will not be modified in the database.  If the resource \"id\" is provided in the JSON body, it will be ignored as well.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_evaluation(id, evaluation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param TpdmEvaluation evaluation: The JSON representation of the \"evaluation\" resource to be created or updated. (required)
        :param str if_match: The ETag header value used to prevent the PUT from updating a resource modified by another consumer.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_evaluation_with_http_info(id, evaluation, **kwargs)  # noqa: E501
        else:
            (data) = self.put_evaluation_with_http_info(id, evaluation, **kwargs)  # noqa: E501
            return data

    def put_evaluation_with_http_info(self, id, evaluation, **kwargs):  # noqa: E501
        """Updates or creates a resource based on the resource identifier.  # noqa: E501

        The PUT operation is used to update or create a resource by identifier. If the resource doesn't exist, the resource will be created using that identifier. Additionally, natural key values cannot be changed using this operation, and will not be modified in the database.  If the resource \"id\" is provided in the JSON body, it will be ignored as well.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_evaluation_with_http_info(id, evaluation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: A resource identifier that uniquely identifies the resource. (required)
        :param TpdmEvaluation evaluation: The JSON representation of the \"evaluation\" resource to be created or updated. (required)
        :param str if_match: The ETag header value used to prevent the PUT from updating a resource modified by another consumer.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'evaluation', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_evaluation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `put_evaluation`")  # noqa: E501
        # verify the required parameter 'evaluation' is set
        if self.api_client.client_side_validation and ('evaluation' not in params or
                                                       params['evaluation'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `evaluation` when calling `put_evaluation`")  # noqa: E501

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
        if 'evaluation' in params:
            body_params = params['evaluation']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2_client_credentials']  # noqa: E501

        return self.api_client.call_api(
            '/tpdm/evaluations/{id}', 'PUT',
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
