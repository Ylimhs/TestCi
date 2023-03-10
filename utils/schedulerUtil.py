
from app import scheduler
from utils.Clinet.JJClient import publish_article
from utils.utils import is_past_date, logging, strToTime
from flask_apscheduler import APScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

def add_article_publish_job(task_id, draft_id, time):
    logging.debug(task_id)
    logging.debug(draft_id)
    if is_past_date(time):
        return -1;
    else:
        time = strToTime(time)
    logging.debug(time)
    try:
        if time is not None:
            scheduler.add_job(func=publish_article, args=[draft_id], next_run_time=time, id=str(task_id))
        else:
            return -1
    except Exception as e:
        logging.error("add_article_publish_job failed with err " + str(e))
        return -2
    return 0
