from flask import Flask, request, redirect, render_template, url_for
from env import FLASK_ENUM
from modules.database import get_db_direct

app = Flask(__name__, static_url_path='/static')

final_menu = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_quantity_1', methods=['POST'])
def submit_quantity_1():
    quantity_1 = request.form.get('quantity_1')
    # 여기에서 수량을 사용하여 원하는 작업을 수행합니다.
    print(f"카라멜 팝콘 수량: {quantity_1}")
    quantity_1 = 'K' + quantity_1
    final_menu.append(quantity_1)
    return "수량이 전송되었습니다."

@app.route('/submit_quantity_2', methods=['POST'])
def submit_quantity_2():
    quantity_2 = request.form.get('quantity_2')
    # 여기에서 수량을 사용하여 원하는 작업을 수행합니다.
    print(f"치즈 팝콘 수량: {quantity_2}")
    quantity_2 = 'C' + quantity_2
    final_menu.append(quantity_2)
    return "수량이 전송되었습니다."

@app.route('/submit_quantity_3', methods=['POST'])
def submit_quantity_3():
    quantity_3 = request.form.get('quantity_3')
    # 여기에서 수량을 사용하여 원하는 작업을 수행합니다.
    print(f"에이드 수량: {quantity_3}")
    quantity_3 = 'A' + quantity_3
    final_menu.append(quantity_3)
    return "수량이 전송되었습니다."

@app.route('/final_pay')
def final_order():
    print(final_menu)
    return render_template('index.html', final_menu=final_menu)

@app.route('/discard')
def discard_order():
    print("메뉴를 전부 삭제합니다.")
    final_menu.clear()
    discard_message = '메뉴가 초기화 되었습니다.'
    return render_template('index.html', discard_message=discard_message)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=FLASK_ENUM.PORT)