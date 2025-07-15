from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/square')
def square():
    num = request.args.get('n', default=1, type=int)
    return jsonify({"number": num, "square": num*num})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
