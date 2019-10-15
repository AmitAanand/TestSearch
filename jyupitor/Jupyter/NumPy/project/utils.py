import requests
import sys
import xml.etree.ElementTree as ET
import rap2constants as Prop
from baseLogging import logger as logger

# disable ssl certificate
requests.packages.urllib3.disable_warnings()


class Utility:

    # call rest api based on method type
    @classmethod
    def call_api(cls, url, payload, method, access_token):
        headers = {"Content-Type": "application/json", Prop.apiKey: Prop.userAPIKey, "authorization": "Bearer " +access_token}

        # api call
        try:
            if method == 'PUT':
                return requests.put(url=url, headers=headers, verify=False, timeout=600)
            elif method == 'POST':
                return requests.post(url=url, data=payload)
            elif method == 'GET':
                return requests.get(url=url, headers=headers, verify=False, timeout=600)

        except requests.exceptions.RequestException:
            logger.exception("Error occurred while calling call api utility method:")
            sys.exit(1)

    # get oauth token
    @classmethod
    def get_token(cls, evn, url, usr, pwd):
        # get access token from property file
        access_token = Prop.access_token
        if access_token != "":
            return access_token

        url = Utility.format_url(url, evn)
        logger.info("tokenUrl : " + url)
        payload = {"username": usr, "password": pwd}

        data = cls.call_api(url, payload, 'POST', "").json()
        # extracting data in json format
        oauth_token = data["access_token"]
        Prop.access_token = oauth_token
        return oauth_token

    @staticmethod
    def write_file(path, data):
        with open(path, 'w') as wf:
            wf.writelines(data)

    @staticmethod
    def read_file(path):
        global file_data
        with open(path, 'r') as rf:
            file_data = rf.readlines()
        return file_data

    @classmethod
    def get_pre_business_day(cls, current_date, access_token):

        # format url
        url = Utility.format_url(Prop.prevBusinessDayApiUrl, current_date)

        logger.info("prevBusinessDayApiUrl : "+url)
        data = cls.call_api(url, None, "GET", access_token)
        data = data.content.decode('utf8')
        for elt in ET.ElementTree(ET.fromstring(data)).iter():
            if "CalendarDate" == elt.tag:
                Prop.business_day = elt.text
                break

        return Prop.business_day

    @staticmethod
    def format_url(url, *values):
        return url.format(*values)

    @staticmethod
    def format_base_url(vals, url, env):

        for idx, val in enumerate(vals):
            if idx == 0:
                url += val
            else:
                url += "&" + val
        return url.format(env) + Prop.urlParamStr.format(Prop.apiKey,  Prop.userAPIKey)


