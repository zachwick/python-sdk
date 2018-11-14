# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Marketplace, we offer a wide selection of financial data feeds sourced by our own proprietary processes as well as from many data vendors. The primary application of the Intrinio API is for use in third-party applications and integrations or for end-users utilizing the Excel add-in and Google Sheets add-on. The Intrinio API uses HTTPS verbs and a RESTful endpoint structure, which makes it easy to request data from Intrinio. Responses are delivered in JSON format. If you need additional help in using the API, go to our home page (https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SecurityScreenResultData(object):
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
        'tag': 'str',
        'number_value': 'str',
        'text_value': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'number_value': 'number_value',
        'text_value': 'text_value'
    }

    def __init__(self, tag=None, number_value=None, text_value=None):  # noqa: E501
        """SecurityScreenResultData - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._number_value = None
        self._text_value = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if number_value is not None:
            self.number_value = number_value
        if text_value is not None:
            self.text_value = text_value

    @property
    def tag(self):
        """Gets the tag of this SecurityScreenResultData.  # noqa: E501

        The data tag that was screened-for  # noqa: E501

        :return: The tag of this SecurityScreenResultData.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this SecurityScreenResultData.

        The data tag that was screened-for  # noqa: E501

        :param tag: The tag of this SecurityScreenResultData.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def number_value(self):
        """Gets the number_value of this SecurityScreenResultData.  # noqa: E501

        The numeric value for the tag  # noqa: E501

        :return: The number_value of this SecurityScreenResultData.  # noqa: E501
        :rtype: str
        """
        return self._number_value

    @number_value.setter
    def number_value(self, number_value):
        """Sets the number_value of this SecurityScreenResultData.

        The numeric value for the tag  # noqa: E501

        :param number_value: The number_value of this SecurityScreenResultData.  # noqa: E501
        :type: str
        """

        self._number_value = number_value

    @property
    def text_value(self):
        """Gets the text_value of this SecurityScreenResultData.  # noqa: E501

        The text value for the tag  # noqa: E501

        :return: The text_value of this SecurityScreenResultData.  # noqa: E501
        :rtype: str
        """
        return self._text_value

    @text_value.setter
    def text_value(self, text_value):
        """Sets the text_value of this SecurityScreenResultData.

        The text value for the tag  # noqa: E501

        :param text_value: The text_value of this SecurityScreenResultData.  # noqa: E501
        :type: str
        """

        self._text_value = text_value

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SecurityScreenResultData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
