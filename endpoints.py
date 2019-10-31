from flask import Flask, render_template, request
import db_handler


app = Flask(__name__)

@app.route("/")
def home():
    author = "Dom"
    name = "User"
    return render_template("home.html", author=author, name=name)

@app.route("/company_data", methods=['POST'])
def company_data():
    company_short = request.form['company_symbol']
    conn = db_handler.create_connection('./stock_db.db')
    key_information = db_handler.get_key_information(conn, company_short)

    return render_template("company_data.html", name=company_short, data=key_information)
    db_handler.close_connection(conn)

if __name__ == "__main__":
    app.run(debug=True)