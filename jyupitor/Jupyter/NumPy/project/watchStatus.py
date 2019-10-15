import requests
import time
import rap2constants as Prop
from baseLogging import logger as logger
from utility import Utility as Util
from rap2Utility import Rap2Utility as rap2Util
import sys

logger.info("job started")
# disable ssl certificate
requests.packages.urllib3.disable_warnings()

ln = len(sys.argv)
args = sys.argv
paramStr = ''.join(args)
url = Prop.batchStatusApiUrl

# Validate parameter if it contains batchType
if Prop.batchType not in paramStr or Prop.env not in paramStr:
    logger.error("Invalid Usage:<env=?> <batchType=?> optional <batchId=?><submittedStartDate=?><submittedEndDate=?><status=?>")
    exit(1)
# extract envirorment from system args
env = rap2Util.extract_param_value(args, Prop.env)
param = args[2:]

try:
    batch_id = ""
    rap2Util.set_usr_pass()
    # get access token
    access_token = Util.get_token(env, Prop.tokenApiUrl, Prop.usr, Prop.pwd)

    # Validate and format api url based on batch id
    if Prop.batchId in paramStr:
        url = Util.format_base_url(param, url, env)
    else:
        url = Util.format_base_url(param, url, env)
        # extract batch_type from param
        batch_type = rap2Util.extract_param_value(args, Prop.batchType)

        # get batch id
        batch_id = rap2Util.get_batch_id(batch_type, env, access_token)

        url += Prop.urlParamStr.format(Prop.batchId, str(batch_id))

    logger.info("batch status url : " + url)
    batchStatus = ""
    while batchStatus not in ["FAILED", "COMPLETED"]:
        logger.info("before status check batchStatus : " + batchStatus)
        time.sleep(20)
        # api call
        data = Util.call_api(url, None, "GET", access_token)
        logger.info("api returned : " + str(data))
        data = data.json()
        if data:
            batchStatus = data[0]["status"]
            logger.info("after status check batchStatus : "+batchStatus)
        else:
            raise ValueError("No data found for batch id ", batch_id)
    else:
        logger.info("batch completed successfully ")

except requests.exceptions.RequestException:
        logger.exception("Error occurred while calling batch status  : ")
        exit(1)
except Exception:
        logger.exception("Error occurred while calling batch batch:")
        exit(1)


