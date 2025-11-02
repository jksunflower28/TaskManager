

class Task:

    # constructor
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.status = "Pending"

    # Method to update the instance variables
    def update(self, title=None, description=None, status=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if status:
            self.status = status

    def to_dict(self):
        return {"id": self.id,
                "title":self.title,
                "description": self.description,
                "status": self.status}





    #Method to return the values as dictionary



