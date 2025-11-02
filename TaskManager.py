import Task


class TaskManager:

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description):
        task = Task.Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self):
        return [task.to_dict() for task in self.tasks]

    # Returns the first task after matching the id
    def get_task(self, id):
        return next((task for task in self.tasks if task.id == id), None)

    def update_task(self, id, data):
        task = self.get_task(id)
        if task:
            task.update(**data)
            return task
        return None

    def delete_task(self):
        task = self.get_task(id)
        if task:
            self.tasks.remove(task)
            return True

        return False





