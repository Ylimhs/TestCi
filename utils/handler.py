import json

from utils.schedulerUtil import add_article_publish_job
from utils.utils import logging


def handlerRequest(data, headers):
    logging.debug("-------------  begin handlerRequest -----------------")
    event = headers.get('X-Github-Event')
    logging.info("handlerRequest the event is %s" % event)
    if event == "issues":
        handler_issues(data)


def handler_issues(json_data):
    action = json_data.get("action")
    issue = json_data.get("issue")

    if action == "opened":
        logging.info("handler_issues the action is opened.")
        try:
            number = issue.get("number")
            body = issue.get("body")
            body = json.loads(body)
            time = body.get("time")
            draft_id = body.get("draft_id")

            logging.info("issue number is {} body is :{}".format(number, body))
            ret = add_article_publish_job(number, draft_id, time)
            if ret == 0:
                logging.info("add the issue %s draft_id %s publish at %s  success." % (number, draft_id, time))
            elif ret == -1 or ret == -2:
                logging.error("add_article_publish_job failed with  this time is missing or format error.")
            else:
                logging.error("add the issue %s draft_id %s publish at %s  failed." % (number, draft_id, time))
                # 发送信息 改变issues 状态。
        except Exception as e:
            logging.error("handler_issues opened fail with err " + str(e))


if __name__ == '__main__':
    pass
