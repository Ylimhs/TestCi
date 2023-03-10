from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from flask import Flask, request
from flask_apscheduler import APScheduler

from utils.utils import logging


class Config(object):
    # 设置时区
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    # 开启API
    SCHEDULER_API_ENABLED = True
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url='sqlite:///utils/jobstores.db')
    }


app = Flask(__name__)
scheduler = APScheduler()
app.config.from_object(Config())
scheduler.init_app(app)
scheduler.start()


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        logging.debug("request headers is: ")
        logging.debug(request.headers)
        data = request.json
        # 处理GitHub Webhooks数据
        # 验证处理
        # 处理events
        from utils.handler import handlerRequest
        ret = handlerRequest(data, request.headers)
        logging.debug("handlerRequest return is %s " % str(ret))
        return 'Webhook received successfully!', 200
    else:
        return 'Invalid request method', 400


if __name__ == '__main__':
    app.run(debug=True, port=8000)
