import requests
import sys
import rap2constants as Prop
from utility import Utility as Util
from rap2Utility import Rap2Utility as rap2Util
from baseLogging import logger as logger

# disable ssl certificate
requests.packages.urllib3.disable_warnings()

logger.info("job started")

ln = len(sys.argv)
args = sys.argv
paramStr = ''.join(args)
url = Prop.batchPublishApiUrl

# Validate parameter if it contains batchType
if Prop.batchType not in paramStr or Prop.env not in paramStr:
    logger.error("Invalid Usage: <env=?> <batchType=?>  optional <batchId=?>")
    exit(1)

# extract envirorment from system args
env = rap2Util.extract_param_value(args, Prop.env)
param = args[2:]
try:
    rap2Util.set_usr_pass()
    # get access token
    access_token = Util.get_token(env, Prop.tokenApiUrl, Prop.usr, Prop.pwd)

    # Validate and format api url based on batchId
    if Prop.batchId in paramStr:
        url = Util.format_base_url(param, url, env)
    else:
        url = Util.format_base_url(param, url, env)

        # extract batch_type from param
        batch_type = rap2Util.extract_param_value(args, Prop.batchType)

        # get batch id
        batchId = rap2Util.get_batch_id(batch_type, env, access_token)
        url += Prop.urlParamStr.format(Prop.batchId, str(batchId))

    logger.info("batchPublishApiUrl : "+url)
    # api call
    data = Util.call_api(url, None, 'PUT', access_token)
    logger.info("api returned : " + str(data))
    data = data.json()

    if ("status" in data) and data['status'] != 200:
        raise requests.exceptions.RequestException(data)
    logger.info(data)
    logger.info("job completed sucessfully")

except requests.exceptions.RequestException:
    logger.exception("Error occurred while publish  batch :")
    exit(1)
except Exception:
    logger.exception("Error occurred while publish  batch :")
    exit(1)
