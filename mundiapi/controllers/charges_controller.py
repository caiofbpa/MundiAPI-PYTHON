# -*- coding: utf-8 -*-

"""
    mundiapi.controllers.charges_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth
from ..models.get_charge_response import GetChargeResponse
from ..models.list_charges_response import ListChargesResponse

class ChargesController(BaseController):

    """A Controller to access Endpoints in the mundiapi API."""


    def get_charge(self,
                   charge_id):
        """Does a GET request to /charges/{charge_id}.

        Get a charge from its id

        Args:
            charge_id (string): Charge id

        Returns:
            GetChargeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/charges/{charge_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'charge_id': charge_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetChargeResponse.from_dictionary)

    def retry_charge(self,
                     charge_id):
        """Does a POST request to /charges/{charge_id}/retry.

        Retries a charge

        Args:
            charge_id (string): Charge id

        Returns:
            GetChargeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/charges/{charge_id}/retry'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'charge_id': charge_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetChargeResponse.from_dictionary)

    def create_charge(self,
                      request):
        """Does a POST request to /Charges.

        Creates a new charge

        Args:
            request (CreateChargeRequest): Request for creating a charge

        Returns:
            GetChargeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/Charges'
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetChargeResponse.from_dictionary)

    def update_charge_card(self,
                           charge_id,
                           request):
        """Does a PATCH request to /charges/{charge_id}/card.

        Updates the card from a charge

        Args:
            charge_id (string): Charge id
            request (UpdateChargeCardRequest): Request for updating a charge's
                card

        Returns:
            GetChargeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/charges/{charge_id}/card'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'charge_id': charge_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetChargeResponse.from_dictionary)

    def update_charge_payment_method(self,
                                     charge_id,
                                     request):
        """Does a PATCH request to /charges/{charge_id}/payment-method.

        Updates a charge's payment method

        Args:
            charge_id (string): Charge id
            request (UpdateChargePaymentMethodRequest): Request for updating
                the payment method from a charge

        Returns:
            GetChargeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/charges/{charge_id}/payment-method'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'charge_id': charge_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetChargeResponse.from_dictionary)

    def cancel_charge(self,
                      charge_id,
                      request=None):
        """Does a DELETE request to /charges/{charge_id}.

        Cancel a charge

        Args:
            charge_id (string): Charge id
            request (CreateCancelChargeRequest, optional): Request for
                cancelling a charge

        Returns:
            GetChargeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/charges/{charge_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'charge_id': charge_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers, parameters=APIHelper.json_serialize(request))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetChargeResponse.from_dictionary)

    def capture_charge(self,
                       charge_id,
                       request=None):
        """Does a POST request to /charges/{charge_id}/capture.

        Captures a charge

        Args:
            charge_id (string): Charge id
            request (CreateCaptureChargeRequest, optional): Request for
                capturing a charge

        Returns:
            GetChargeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/charges/{charge_id}/capture'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'charge_id': charge_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetChargeResponse.from_dictionary)

    def update_charge_metadata(self,
                               charge_id,
                               request):
        """Does a PATCH request to /Charges/{charge_id}/metadata.

        Updates the metadata from a charge

        Args:
            charge_id (string): The charge id
            request (UpdateMetadataRequest): Request for updating the charge
                metadata

        Returns:
            GetChargeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/Charges/{charge_id}/metadata'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'charge_id': charge_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetChargeResponse.from_dictionary)

    def get_charges(self,
                    page=None,
                    size=None,
                    code=None,
                    status=None,
                    payment_method=None,
                    customer_id=None,
                    order_id=None,
                    created_since=None,
                    created_until=None):
        """Does a GET request to /charges.

        Lists all charges

        Args:
            page (int, optional): Page number
            size (int, optional): Page size
            code (string, optional): Filter for charge's code
            status (string, optional): Filter for charge's status
            payment_method (string, optional): Filter for charge's payment
                method
            customer_id (string, optional): Filter for charge's customer id
            order_id (string, optional): Filter for charge's order id
            created_since (datetime, optional): Filter for the beginning of
                the range for charge's creation
            created_until (datetime, optional): Filter for the end of the
                range for charge's creation

        Returns:
            ListChargesResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/charges'
        _query_parameters = {
            'page': page,
            'size': size,
            'code': code,
            'status': status,
            'payment_method': payment_method,
            'customer_id': customer_id,
            'order_id': order_id,
            'created_since': APIHelper.RFC3339DateTime(created_since),
            'created_until': APIHelper.RFC3339DateTime(created_until)
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
        return APIHelper.json_deserialize(_context.response.raw_body, ListChargesResponse.from_dictionary)

    def update_charge_due_date(self,
                               charge_id,
                               request):
        """Does a PATCH request to /Charges/{charge_id}/due-date.

        Updates the due date from a charge

        Args:
            charge_id (string): Charge Id
            request (UpdateChargeDueDateRequest): Request for updating the due
                date

        Returns:
            GetChargeResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/Charges/{charge_id}/due-date'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'charge_id': charge_id
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
        return APIHelper.json_deserialize(_context.response.raw_body, GetChargeResponse.from_dictionary)
