# -*- coding: utf-8 -*-

"""
    mundiapi.models.create_seller_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""
import mundiapi.models.create_card_request

class CreateSellerRequest(object):

    """Implementation of the 'CreateSellerRequest' model.

    TODO: type model description here.

    Attributes:
        name (string): Name
        code (string): Seller's code identification
        description (string): Description
        document (string): Document number (individual / company)
        address (string): Address
        mtype (string): Person type (individual / company)
        metadata (CreateCardRequest): Metadata

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name" : "name",
        "code" : "code",
        "description" : "description",
        "document" : "document",
        "address" : "address",
        "mtype" : "type",
        "metadata" : "metadata"
    }

    def __init__(self,
                 name=None,
                 code=None,
                 description=None,
                 document=None,
                 address=None,
                 mtype=None,
                 metadata=None):
        """Constructor for the CreateSellerRequest class"""

        # Initialize members of the class
        self.name = name
        self.code = code
        self.description = description
        self.document = document
        self.address = address
        self.mtype = mtype
        self.metadata = metadata


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get("name")
        code = dictionary.get("code")
        description = dictionary.get("description")
        document = dictionary.get("document")
        address = dictionary.get("address")
        mtype = dictionary.get("type")
        metadata = mundiapi.models.create_card_request.CreateCardRequest.from_dictionary(dictionary.get("metadata")) if dictionary.get("metadata") else None

        # Return an object of this model
        return cls(name,
                   code,
                   description,
                   document,
                   address,
                   mtype,
                   metadata)

