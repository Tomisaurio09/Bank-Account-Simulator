class Task:
    def __init__(self,name,description,due_date,priority,status):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def mark_complete(self):
        if self.status:
            print("The task was already completed.")
        self.status = True
    
    def reschedule(self, new_date):
        self.due_date = new_date
        