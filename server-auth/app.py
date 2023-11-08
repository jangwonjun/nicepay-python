from flask import Flask, render_template, request, make_response
from requests.auth import HTTPBasicAuth
import requests
import uuid
import json

clientId = 'S2_a10b2371c44945bfa5ec028a37d197ce'
secretKey = '29bab677827348f19ba70e11e9026eb7'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        orderId = uuid.uuid4(),
        clientId = clientId
    )
    
    
@app.route('/cancel', methods=['GET'])
def cancel():
    return render_template(
        'cancel.html'
    )      


@app.route('/serverAuth', methods=['POST'])
def clientAuth():
    try:
        response = requests.post('https://sandbox-api.nicepay.co.kr/v1/payments/' + request.form['tid'], 
            json={
                'amount': request.form['amount']
            },
            headers={
                'Content-type' : 'application/json'
            },
            auth=HTTPBasicAuth(clientId, secretKey)
        )
        
        resDict = json.loads(response.text)
        print(resDict)
        
        # 결제 비즈니스 로직 구현
        
        return render_template(
            'response.html',
            resultMsg = resDict['resultMsg']
        )
        
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


@app.route('/cancel', methods=['POST'])
def cancelAuth():
    try:
        response = requests.post('https://sandbox-api.nicepay.co.kr/v1/payments/'+ request.form['tid'] + '/cancel', 
            json={
                'amount': request.form['amount'],
                'reason' : 'test',
                'orderId' : str(uuid.uuid4())
            },
            headers={
                'Content-type' : 'application/json'
            },
            auth=HTTPBasicAuth(clientId, secretKey)
        )
        
        resDict = json.loads(response.text)
        print(resDict)
        
        # 결제 비즈니스 로직 구현
        
        return render_template(
            'response.html',
            resultMsg = resDict['resultMsg']
        )
        
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


@app.route('/hook', methods=['POST'])
def hook():
    print(request.json)
    return make_response("ok", 200)

if __name__ == '__main__':
    app.run(debug=True)