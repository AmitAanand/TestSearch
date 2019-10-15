import requests
import sys
from utility import Utility as Util
import rap2constants as Prop
from datetime import date
from baseLogging import logger as logger
from rap2Utility import Rap2Utility as rap2Util

# disable ssl certificate
requests.packages.urllib3.disable_warnings()

logger.info("job started")
ln = len(sys.argv)
args = sys.argv
paramStr = ''.join(args)
url = Prop.batchSubmitApiUrl

# extract envirorment from system args
env = rap2Util.extract_param_value(args, "env")
param = args[2:]

# Validate parameter if it contains batchType
if Prop.batchType not in paramStr or Prop.env not in paramStr:
    logger.error("Invalid Usage: <env=?> <batchTyp=?>  optional <asOfStartDate=?> <asOfEndDate=?> <accountCodes=?> <priority=?>")
    exit(1)

try:
    # get access token
    tokenEnv = "" if env == "" else env
    rap2Util.set_usr_pass()
    access_token = Util.get_token(tokenEnv, Prop.tokenApiUrl, Prop.usr, Prop.pwd)

    # Validate and format api url based on asOfStartDate and asOfStartEnd
    if Prop.asOfStartDate in paramStr and Prop.asOfEndDate in paramStr:
        url = Util.format_base_url(param, url, env)
    else:
        # if dates are not present get it suing calc engine api
        url = Util.format_base_url(param, url, env)
        as_of_start_date = Util.get_pre_business_day(date.today(),access_token)
        url += Prop.urlParamStr.format(Prop.asOfStartDate, as_of_start_date)
        url += Prop.urlParamStr.format(Prop.asOfEndDate, as_of_start_date)

    # format the create batch api url
    logger.info("batchSubmitApiUrl :  " + url)

    # api call to create the batch
    data = Util.call_api(url, None, 'PUT', access_token)
    logger.info("api returned : " + str(data))
    data = data.json()
    if ("status" in data) and data['status'] != 200:
        raise requests.exceptions.RequestException(data)
    logger.info(data)
    logger.info("job completed sucessfully")

except requests.exceptions.RequestException:
    logger.exception("Error occurred while calling create batch:")
    exit(1)
except Exception:
    logger.exception("Error occurred while calling create batch:")
    exit(1)
