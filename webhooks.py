from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        # 处理GitHub Webhooks数据
        return 'Webhook received successfully!', 200
    else:
        return 'Invalid request method', 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
