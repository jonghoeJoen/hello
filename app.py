from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("page/sigin-in.html")

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        num = request.args["num"]
        name = request.args.get("name")
        return "GET으로 전달된 데이터({}, {})".format(num, name)
    else:
        num = request.form["num"]
        name = request.form["name"]
        return "POST로 전달된 데이터({}, {})".format(num, name)

@app.route('/sigin-in')
def hellohtml():
    return render_template("page/sigin-in.html")

if __name__ == '__main__':
    app.run(debug=True)