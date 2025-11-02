import TaskManager
from flask import Flask, jsonify, request

app = Flask(__name__)

taskManager = TaskManager.TaskManager()
@app.route("/tasks", methods = ["GET"])
def get_tasks():
    return jsonify(taskManager.get_all_tasks())

@app.route("/tasks", methods = ["POST"])
def add_task():
    data = request.json
    task = taskManager.create_task(data["title"], data.get("description"))
    return jsonify(task.to_dict(), 201)

@app.route("/tasks/<int:id>", methods = ["PUT"])
def update_task(id):
    data = request.json
    task = taskManager.update_task(id, data)
    if task:
        return jsonify(task.to_dict())
    return jsonify({"error": "Task not found"}, 404)

@app.route("/tasks/<int:id>", methods = ["DELETE"])
def delete_task(id):
    data = request.json
    task = taskManager.delete_task(id)
    if task:
        return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Task not found"}, 404)

if __name__ == "__main__":
    app.run(debug=True)