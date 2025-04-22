from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/greet')

def greet():
   a = request.args.get('a', default=1, type=int)
   b = request.args.get('b', default=2, type=int)
   response = requests.get(f"http://addition_service:5001/add?{a}&b={b}")
   sum_result = response.text
   return "Hello,world! Sum is:{sum_result}"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
