from flask import Flask, request, redirect, render_template, url_for, session
from env import FLASK_ENUM, SQL
from modules.database import get_db_direct
import random
import string
import pymysql

app = Flask(__name__, static_url_path='/static')
app.secret_key = FLASK_ENUM.SECRET_KEY

final_menu = []
menu_count = []
coupon_result = []

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

@app.route('/coupon_making')
def coupon_making():
    #쿠폰 발생기
    for i in range(8):
        coupon_result.append(str(random.randint(0, 9)))
    
    certification_code = ''.join(coupon_result)
    certification_code = certification_code + 'ddbk'
        
    return certification_code

@app.route('/information',methods=['GET','POST'])
def information():
    #사용자의 결제 정보를 위한 정보를 입력받습니다. 
    #이메일과 카카오톡 알람톡을 전송할 전화번호를 수집합니다. 
    #이메일은 unique 값으로 처리를 하였기 때문에, 중복을 예방합니다. 
    
    conn, cursor = get_db_direct()
    email = request.form.get('email')
    phone_number = request.form.get('tel')
    print(email,phone_number)
    session['email'] = email
    session['phone_number'] = phone_number
    
    try : 
        cursor.execute(f"USE {SQL.DB_NAME}")
        sql_query = "INSERT INTO login (name, phone_number) VALUES (%s, %s)"
        cursor.execute(sql_query, (email,phone_number))
        conn.commit()
        cursor.close()
        conn.close()
        print("사용자의 정보가 입력되었습니다.")
    except pymysql.Error as e :
        print(f"SQL 구문 오류가 발생하였습니다. {e}")
    
    return render_template('login.html')
'''
@app.route('/registration_auto',methods=['POST','GET'])
def registration_auto():
   #결제 완료전의 주문한 쿠폰을 서버에 저장합니다. 
   #결제가 완료 되지 않은 쿠폰의 state는 0입니다. 결제가 완료된 쿠폰의 state는 1입니다. 
   conn, cursor = get_db_direct()
   email = session.get('email')
   phone_number = session.get('phone_number')
   
   try : 
        cursor.execute(f"USE {SQL.DB_NAME}")
        sql_query = "INSERT INTO pay (pay_num, pay_state) VALUES (%s, %s)"
        cursor.execute(sql_query, (email,'0'))
        conn.commit()
        cursor.close()
        conn.close()
        print("사용자의 정보가 입력되었습니다.")
        
    except pymysql.Error as e :
        print(f"SQL 구문 오류가 발생하였습니다. {e}")
    
    return render_template('login.html')
'''

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=FLASK_ENUM.PORT)