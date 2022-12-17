from flask import Flask, request
app = Flask(__name__)

# create a route for the API at /hello
@app.route('/hello', methods=['GET'])
def hello():
    # get the value of the "name" query parameter
    name = request.args.get('name')
    # return a greeting as a string
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
