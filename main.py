from flask import Flask, request, redirect, render_template, url_for
from env import FLASK_ENUM
from modules.database import get_db_direct

app = Flask(__name__, static_url_path='/static')

final_menu = []
menu_count = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_quantity_1', methods=['POST'])
def submit_quantity_1():
    quantity_1 = request.form.get('quantity_1')
    print(f"카라멜 팝콘 수량: {quantity_1}")
    menu_count_order_1 = '카라멜 팝콘' + quantity_1 + '개'
    quantity_1 = 'K' + quantity_1
    menu_count.append(menu_count_order_1)
    final_menu.append(quantity_1)
    return "수량이 전송되었습니다."

@app.route('/submit_quantity_2', methods=['POST'])
def submit_quantity_2():
    quantity_2 = request.form.get('quantity_2')
    print(f"치즈 팝콘 수량: {quantity_2}")
    menu_count_order_2 = '치즈 팝콘' + quantity_2 + '개'
    quantity_2 = 'C' + quantity_2
    final_menu.append(quantity_2)
    menu_count.append(menu_count_order_2)
    return "수량이 전송되었습니다."

@app.route('/submit_quantity_3', methods=['POST'])
def submit_quantity_3():
    quantity_3 = request.form.get('quantity_3')
    print(f"에이드 수량: {quantity_3}")
    menu_count_order_3 = '에이드' + quantity_3 + '개'
    quantity_3 = 'A' + quantity_3
    final_menu.append(quantity_3)
    menu_count.append(menu_count_order_3)
    
    return "수량이 전송되었습니다."


@app.route('/order',methods=['POST'])
def order():
    final_menu_text = ''.join(final_menu)
    return final_menu_text


@app.route('/final_pay',methods=['POST'])
def final_order():
    print(final_menu)
    print(menu_count)
    return render_template('index.html', final_menu=menu_count)

@app.route('/now_order')
def now_order():
    return render_template('index.html', now_order=final_menu)

@app.route('/discard',methods=['POST'])
def discard_order():
    print("메뉴를 전부 삭제합니다.")
    final_menu.clear()
    menu_count.clear()
    discard_message = '메뉴가 초기화 되었습니다.'
    return render_template('index.html', discard_message=discard_message)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=FLASK_ENUM.PORT)