# -*- coding: utf-8 -*-

"""
    mundiapi.models.get_device_response

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io )
"""


class GetDeviceResponse(object):

    """Implementation of the 'GetDeviceResponse' model.

    Response object for geetting an order device

    Attributes:
        platform (string): Device's platform name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "platform":'platform'
    }

    def __init__(self,
                 platform=None):
        """Constructor for the GetDeviceResponse class"""

        # Initialize members of the class
        self.platform = platform


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
        platform = dictionary.get('platform')

        # Return an object of this model
        return cls(platform)


