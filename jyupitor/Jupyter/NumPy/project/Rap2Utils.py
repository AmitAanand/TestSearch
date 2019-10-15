from datetime import date
from utility import Utility as Util
import rap2constants as Prop
from baseLogging import  logger as logger


class Rap2Utility:

    @staticmethod
    def get_batch_id(batch_type, env, access_token):
        date_today = date.today()
        url = Util.format_url(Prop.batchStatusByDateUrl, env, date_today, date_today)
        logger.info("batchDetailsApiUrl : "+url)
        # api call
        data = Util.call_api(url, None, 'GET', access_token).json()
        # filter the max batch id based on user id and batch type
        batch_id_set = set(map(Rap2Utility.filter_response(batch_type), data))
        return max(batch_id_set) if batch_id_set else ""

    @staticmethod
    def filter_response(batch_type):
        return lambda ob: ob['batchId'] if ob["batchType"] == batch_type and ob["submitterId"] == Prop.usr else 0

    @staticmethod
    def extract_param_value(args, param_type):
        for i in args:
            if param_type in i:
                return i.split("=")[1]
    @staticmethod
    def set_usr_pass():
        usepasslst= [x.split("=")[1].strip("\n") for x in Util.read_file(".env")]
        Prop.usr = usepasslst[0]
        Prop.pwd = usepasslst[1]