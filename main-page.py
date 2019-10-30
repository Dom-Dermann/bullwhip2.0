from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    author = "Dom"
    name = "User"
    return render_template("home.html", author=author, name=name)

@app.route("/company_data", methods=['POST'])
def company_data():
    company_short = request.form['company_symbol']
    
    return render_template("company_data.html", name=company_short)
    
if __name__ == "__main__":
    app.run(debug=True)