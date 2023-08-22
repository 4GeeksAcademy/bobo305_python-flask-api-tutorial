from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "Me first task", "done": False },
    { "label": "Me second task", "done": False },
    
]

@app.route('/')
def type():
    return 'Type in /todos to get transfered to the url'

@app.route('/todos', methods=['GET'])
def set_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    return jsonify(todos), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port =3245, debug = True)