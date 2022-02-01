from lib2to3.pgen2 import token
import logging
from urllib.parse import urljoin
import requests
from datetime import datetime
from pprint import pprint


class ResultApi:
    def __init__(
        self,
        token,
        log_level="INFO",
        version="0.1.0",
        host="results.us.securityeducation.com",
    ):
        """Python class to interrogate the Proofpoint result REST API.
        Each call to the API is returned as a Python dict.

        Args:
            token (str): Proofpoint reporting API key.
            log_level (str, optional): Log level. Defaults is "INFO".
            version (str, optional): Version of the API to use. Defaults is 0.1.0.
            host (str, optional): Proofpoint API host. Defaults is results.us.securityeducation.com.
        """
        self.headers = {"Content-type": "application/json", "x-apikey-token": token}
        self.base_url = f"https://{host}/api/reporting/v{version}"
        self.page_size = 20

        self.logger = logging.getLogger("default")
        self.logger.setLevel(logging.getLevelName(log_level))
        formatter = logging.Formatter(
            "%(asctime)s - %(funcName)s - %(levelname)s - %(message)s"
        )
        ch = logging.StreamHandler()

        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def set_page_size(self, size):
        """Change the page size.

        Args:
            size (int): The new page size.
        """
        self.page_size = size

    def make_request(self, method, path, parameters):
        """Function to standardize requests made to the API.

        Args:
            method (str): Method to use. GET, POST, etc.
            path (str): API path to query.
            parameters (dict, optional): Parameters to pass the queried path. See the official API documentation here: https://proofpoint.securityeducation.com/api/reporting/documentation/#api-Introduction
        """
        url = self.base_url + path
        params = {"page[size]": self.page_size}

        self.logger.debug(f"{method}\t{url}")

        s = requests.Session()
        if parameters:
            params.update(parameters)
            response = s.request(method, url, headers=self.headers, params=params)
        else:
            response = s.request(method, url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(
                str(response.status_code)
                + ": "
                + response.reason
                + ": "
                + str(response.content)
            )
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    def get_users(self, params=""):
        """Query the Users endpoint.

        Args:
            params (dict): Parameters to pass the queried path. See the official API documentation here: https://proofpoint.securityeducation.com/api/reporting/documentation/#api-API_Endpoints-UsersFunction
        """
        return self.make_request("GET", "/users", params)["data"]

    def get_cyberstrength(self, params=""):
        """Query the Cyberstrength endpoint.

        Args:
            params (dict): Parameters to pass the queried path. See the official API documentation here: https://proofpoint.securityeducation.com/api/reporting/documentation/#api-API_Endpoints-CyberStrengthFunction
        """
        return self.make_request("GET", "/cyberstrength", params)["data"]

    def get_phishalarm(self, params=""):
        """Query the PhishAlarm endpoint.

        Args:
            params (dict): Parameters to pass the queried path. See the official API documentation here: https://proofpoint.securityeducation.com/api/reporting/documentation/#api-API_Endpoints-PhishAlarmFunction
        """
        return self.make_request("GET", "/phishalarm", params)["data"]

    def get_phishing(self, params=""):
        """Query the Phishing endpoint.

        Args:
            params (dict): Parameters to pass the queried path. See the official API documentation here: https://proofpoint.securityeducation.com/api/reporting/documentation/#api-API_Endpoints-PhishingEventFunction
        """
        return self.make_request("GET", "/phishing", params)["data"]

    def get_training(self, params=""):
        """Query the Training endpoint.

        Args:
            params (dict): Parameters to pass the queried path. See the official API documentation here: https://proofpoint.securityeducation.com/api/reporting/documentation/#api-API_Endpoints-TrainingFunction
        """
        return self.make_request("GET", "/training", params)["data"]

    def get_trainingenrollments(self, params=""):
        """Query the TrainingEnrollments endpoint.

        Args:
            params (dict): Parameters to pass the queried path. See the official API documentation here: https://proofpoint.securityeducation.com/api/reporting/documentation/#api-API_Endpoints-TrainingEnrollmentsFunction
        """
        return self.make_request("GET", "/trainingenrollments", params)["data"]
