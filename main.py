import TaskManager
from flask import Flask
app = Flask(__name__)

taskManager = TaskManager.TaskManager()



if __name__ == "__main__":
    app.run(debug=True)