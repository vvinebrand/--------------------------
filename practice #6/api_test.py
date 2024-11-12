from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_test():
    name = request.args.get('name')
    lastname = request.args.get('lastname')

    arg = {
        'message': 'hello world',
        'name': name,
        'lastname': lastname
    }

    return jsonify(arg)

if __name__ == '__main__':
    app.run(debug=True)