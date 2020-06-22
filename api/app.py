from flask import Flask,request,jsonify
from getstock import stock

app = Flask(__name__)

@app.route('/getstock', methods=['GET'])
def getStock():
    result = stock().get_stock()
    return result


if __name__ == '__main__':
    app.run()
