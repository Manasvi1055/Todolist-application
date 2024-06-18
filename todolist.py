import tkinter as tk
from tkinter import messagebox

class ToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("400x400")

        self.tasks = []

        self.label = tk.Label(self, text="To-Do List", font=('Arial', 16))
        self.label.pack(pady=10)

        self.frame = tk.Frame(self)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=25, font=('Arial', 14))
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, font=('Arial', 14))
        self.add_button.pack(side=tk.LEFT)

        self.listbox = tk.Listbox(self, font=('Arial', 14), width=30, height=10)
        self.listbox.pack(pady=20)

        self.delete_button = tk.Button(self, text="Delete Task", command=self.delete_task, font=('Arial', 14))
        self.delete_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    app = ToDoListApp()
    app.mainloop()
