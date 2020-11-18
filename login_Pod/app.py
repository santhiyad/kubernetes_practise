from flask import Flask, render_template, request, redirect
import dbconnect


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            print(request)
            userDetails = request.form
            name = userDetails['name']
            print(name)
            passwd = userDetails['passwd']
            print(passwd)
            dbconnect.database_creation()
            dbconnect.table_creation()
            print("database and table creation done")
            status = dbconnect.submit(name,passwd)
            print(status)
            return "login Successful"
    except Exception as e:
        print(e)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)