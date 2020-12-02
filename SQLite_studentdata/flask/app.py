from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/compute')
def compute():
    a = 4
    b = 3
    return str(a * b)

@app.route('/result')
def name_result():
    name = {
        "first" : "Josiah",
        "last"  : "Oborekanhwo",
        "course"    : "Data Science"
    }
    return jsonify(name)

@app.route('/score', methods=["GET", "POST"])
def score_val():
    dataDict = request.get_json()
    return jsonify(dataDict)

# """
# Use this in postman
# {
#   "course": "Data Science",
#   "first": "Josiah",
#   "last": "Oborekanhwo"
# }
# """


if __name__=="__main__":
    app.run(port=1752, debug=True)