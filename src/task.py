class Task:
    def __init__(self, task: str, completed: bool = False):
        self.task = task
        self.completed = completed

    def __repr__(self):
        return f"Task: {self.task}, Completed: {self.completed}"

    def convert_to_dict(self):
        return {"task": self.task, "completed": self.completed}
