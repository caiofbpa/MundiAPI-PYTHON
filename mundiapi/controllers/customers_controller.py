# -*- coding: utf-8 -*-

"""
    mundiapi.controllers.customers_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.list_addresses_response import ListAddressesResponse
from ..models.list_cards_response import ListCardsResponse
from ..models.get_customer_response import GetCustomerResponse
from ..models.get_address_response import GetAddressResponse
from ..models.get_card_response import GetCardResponse
from ..models.list_access_tokens_response import ListAccessTokensResponse
from ..models.list_customers_response import ListCustomersResponse
from ..models.get_access_token_response import GetAccessTokenResponse

class CustomersController(BaseController):

    """A Controller to access Endpoints in the mundiapi API."""


    def get_addresses(self,
                      customer_id):
        """Does a GET request to /customers/{customer_id}/addresses.

        Gets all adressess from a customer

        Args:
            customer_id (string): Customer id

        Returns:
            ListAddressesResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/addresses'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListAddressesResponse.from_dictionary)

    def get_cards(self,
                  customer_id):
        """Does a GET request to /customers/{customer_id}/cards.

        Get all cards from a customer

        Args:
            customer_id (string): Customer Id

        Returns:
            ListCardsResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/cards'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListCardsResponse.from_dictionary)

    def create_customer(self,
                        request):
        """Does a POST request to /customers.

        Creates a new customer

        Args:
            request (CreateCustomerRequest): Request for creating a customer

        Returns:
            GetCustomerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCustomerResponse.from_dictionary)

    def get_customer(self,
                     customer_id):
        """Does a GET request to /customers/{customer_id}.

        Get a customer

        Args:
            customer_id (string): Customer Id

        Returns:
            GetCustomerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCustomerResponse.from_dictionary)

    def update_address(self,
                       customer_id,
                       address_id,
                       request):
        """Does a PUT request to /customers/{customer_id}/addresses/{address_id}.

        Updates an address

        Args:
            customer_id (string): Customer Id
            address_id (string): Address Id
            request (UpdateAddressRequest): Request for updating an address

        Returns:
            GetAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/addresses/{address_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'address_id': address_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAddressResponse.from_dictionary)

    def update_card(self,
                    customer_id,
                    card_id,
                    request):
        """Does a PUT request to /customers/{customer_id}/cards/{card_id}.

        Updates a card

        Args:
            customer_id (string): Customer Id
            card_id (string): Card id
            request (UpdateCardRequest): Request for updating a card

        Returns:
            GetCardResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/cards/{card_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'card_id': card_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCardResponse.from_dictionary)

    def get_address(self,
                    customer_id,
                    address_id):
        """Does a GET request to /customers/{customer_id}/addresses/{address_id}.

        Get a customer's address

        Args:
            customer_id (string): Customer id
            address_id (string): Address Id

        Returns:
            GetAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/addresses/{address_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'address_id': address_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAddressResponse.from_dictionary)

    def delete_address(self,
                       customer_id,
                       address_id):
        """Does a DELETE request to /customers/{customer_id}/addresses/{address_id}.

        Delete a Customer's address

        Args:
            customer_id (string): Customer Id
            address_id (string): Address Id

        Returns:
            GetAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/addresses/{address_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'address_id': address_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAddressResponse.from_dictionary)

    def delete_card(self,
                    customer_id,
                    card_id):
        """Does a DELETE request to /customers/{customer_id}/cards/{card_id}.

        Delete a customer's card

        Args:
            customer_id (string): Customer Id
            card_id (string): Card Id

        Returns:
            GetCardResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/cards/{card_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'card_id': card_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCardResponse.from_dictionary)

    def create_address(self,
                       customer_id,
                       request):
        """Does a POST request to /customers/{customer_id}/addresses.

        Creates a new address for a customer

        Args:
            customer_id (string): Customer Id
            request (CreateAddressRequest): Request for creating an address

        Returns:
            GetAddressResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/addresses'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAddressResponse.from_dictionary)

    def get_card(self,
                 customer_id,
                 card_id):
        """Does a GET request to /customers/{customer_id}/cards/{card_id}.

        Get a customer's card

        Args:
            customer_id (string): Customer id
            card_id (string): Card id

        Returns:
            GetCardResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/cards/{card_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'card_id': card_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCardResponse.from_dictionary)

    def create_card(self,
                    customer_id,
                    request):
        """Does a POST request to /customers/{customer_id}/cards.

        Creates a new card for a customer

        Args:
            customer_id (string): Customer id
            request (CreateCardRequest): Request for creating a card

        Returns:
            GetCardResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/cards'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCardResponse.from_dictionary)

    def update_customer(self,
                        customer_id,
                        request):
        """Does a PUT request to /customers/{customer_id}.

        Updates a customer

        Args:
            customer_id (string): Customer id
            request (UpdateCustomerRequest): Request for updating a customer

        Returns:
            GetCustomerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCustomerResponse.from_dictionary)

    def delete_access_tokens(self,
                             customer_id):
        """Does a GET request to /customers/{customer_id}/access-tokens/.

        Delete a Customer's access tokens

        Args:
            customer_id (string): Customer Id

        Returns:
            ListAccessTokensResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/access-tokens/'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListAccessTokensResponse.from_dictionary)

    def get_access_tokens(self,
                          customer_id):
        """Does a GET request to /customers/{customer_id}/access-tokens.

        Get all access tokens from a customer

        Args:
            customer_id (string): Customer Id

        Returns:
            ListAccessTokensResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/access-tokens'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListAccessTokensResponse.from_dictionary)

    def get_customers(self,
                      name=None,
                      document=None,
                      page=1,
                      size=10):
        """Does a GET request to /customers.

        Get all Customers

        Args:
            name (string, optional): Name of the Customer
            document (string, optional): Document of the Customer
            page (int, optional): Current page the the search
            size (int, optional): Quantity pages of the search

        Returns:
            ListCustomersResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers'
        _query_parameters = {
            'name': name,
            'document': document,
            'page': page,
            'size': size
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListCustomersResponse.from_dictionary)

    def delete_access_token(self,
                            customer_id,
                            token_id):
        """Does a DELETE request to /customers/{customer_id}/access-tokens/{token_id}.

        Delete a customer's access token

        Args:
            customer_id (string): Customer Id
            token_id (string): Token Id

        Returns:
            GetAccessTokenResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/access-tokens/{token_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'token_id': token_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAccessTokenResponse.from_dictionary)

    def create_access_token(self,
                            customer_id,
                            request):
        """Does a POST request to /customers/{customer_id}/access-tokens.

        Creates a access token for a customer

        Args:
            customer_id (string): Customer Id
            request (CreateAccessTokenRequest): Request for creating a access
                token

        Returns:
            GetAccessTokenResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/access-tokens'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAccessTokenResponse.from_dictionary)

    def get_access_token(self,
                         customer_id,
                         token_id):
        """Does a GET request to /customers/{customer_id}/access-tokens/{token_id}.

        Get a Customer's access token

        Args:
            customer_id (string): Customer Id
            token_id (string): Token Id

        Returns:
            GetAccessTokenResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/customers/{customer_id}/access-tokens/{token_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id,
            'token_id': token_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetAccessTokenResponse.from_dictionary)

    def update_customer_metadata(self,
                                 customer_id,
                                 request):
        """Does a PATCH request to /Customers/{customer_id}/metadata.

        Updates the metadata a customer

        Args:
            customer_id (string): The customer id
            request (UpdateMetadataRequest): Request for updating the customer
                metadata

        Returns:
            GetCustomerResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/Customers/{customer_id}/metadata'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'customer_id': customer_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetCustomerResponse.from_dictionary)
