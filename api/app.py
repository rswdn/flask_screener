from flask import Flask,request,jsonify
from getstock import stock

app = Flask(__name__)

#App route for the getstock function
@app.route('/getstock', methods=['POST'])
def getStock():
    result = stock().get_stock() #Setting results to the getstock function
    return result #Returning the result


if __name__ == '__main__':
    app.run(debug=True)


