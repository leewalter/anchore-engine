# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class PolicyEvaluationProblem(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, severity=None, problem_type=None, details=None):
        """
        PolicyEvaluationProblem - a model defined in Swagger

        :param severity: The severity of this PolicyEvaluationProblem.
        :type severity: str
        :param problem_type: The problem_type of this PolicyEvaluationProblem.
        :type problem_type: str
        :param details: The details of this PolicyEvaluationProblem.
        :type details: str
        """
        self.swagger_types = {
            'severity': str,
            'problem_type': str,
            'details': str
        }

        self.attribute_map = {
            'severity': 'severity',
            'problem_type': 'problem_type',
            'details': 'details'
        }

        self._severity = severity
        self._problem_type = problem_type
        self._details = details

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PolicyEvaluationProblem of this PolicyEvaluationProblem.
        :rtype: PolicyEvaluationProblem
        """
        return deserialize_model(dikt, cls)

    @property
    def severity(self):
        """
        Gets the severity of this PolicyEvaluationProblem.
        severity string such as \"warn\", \"error\", \"fatal\"

        :return: The severity of this PolicyEvaluationProblem.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this PolicyEvaluationProblem.
        severity string such as \"warn\", \"error\", \"fatal\"

        :param severity: The severity of this PolicyEvaluationProblem.
        :type severity: str
        """
        if severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")

        self._severity = severity

    @property
    def problem_type(self):
        """
        Gets the problem_type of this PolicyEvaluationProblem.
        the type of problem encountered, such as a misconfiguration or unavailable data

        :return: The problem_type of this PolicyEvaluationProblem.
        :rtype: str
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """
        Sets the problem_type of this PolicyEvaluationProblem.
        the type of problem encountered, such as a misconfiguration or unavailable data

        :param problem_type: The problem_type of this PolicyEvaluationProblem.
        :type problem_type: str
        """
        if problem_type is None:
            raise ValueError("Invalid value for `problem_type`, must not be `None`")

        self._problem_type = problem_type

    @property
    def details(self):
        """
        Gets the details of this PolicyEvaluationProblem.
        Details about the problem itself and how to fix it

        :return: The details of this PolicyEvaluationProblem.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this PolicyEvaluationProblem.
        Details about the problem itself and how to fix it

        :param details: The details of this PolicyEvaluationProblem.
        :type details: str
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")

        self._details = details
