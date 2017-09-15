# -*- coding: utf-8 -*-

"""
    mundiapi.models.update_metadata_request

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class UpdateMetadataRequest(object):

    """Implementation of the 'UpdateMetadataRequest' model.

    Request for updating an metadata

    Attributes:
        metadata (dict<object, string>): Metadata

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metadata" : "metadata"
    }

    def __init__(self,
                 metadata=None):
        """Constructor for the UpdateMetadataRequest class"""

        # Initialize members of the class
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
        metadata = dictionary.get("metadata")

        # Return an object of this model
        return cls(metadata)

