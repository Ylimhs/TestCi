import datetime
from flask import Flask, request
from flask_apscheduler import APScheduler

import logging
# 配置日志显示
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log.txt',
                    filemode='a')


app = Flask(__name__)

class Config(object):
    SCHEDULER_API_ENABLED = True

def add(a, b):
    print(a + b)

def date_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)
    # 故意抛出异常
    print (1/0)


def strToTime(timeStr):
    try:
        return datetime.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
    except Exception as e: 
        print(e)
    return None


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        # 处理GitHub Webhooks数据
        user_name = data.get('user_name')
        draft_id =  data.get('draft_id')
        publishTime = data.get('time')
        publishTime = strToTime(publishTime)
        logging.info("user is : %s arct_id is %s  pulishTime is  %s " % (user_name, draft_id, publishTime))
        scheduler.add_job(func=date_test, args=('一次性任务,会出错',), next_run_time=publishTime, id='date_task')

        return 'Webhook received successfully!', 200
    else:
        return 'Invalid request method', 400



if __name__ == '__main__':
    scheduler = APScheduler()
    app.config.from_object(Config())
    scheduler.init_app(app)
    # scheduler.add_job(func=date_test, args=('一次性任务,会出错',), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=15), id='date_task')
    scheduler.start()



    app.run(debug=True, port=8001)
