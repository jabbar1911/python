#!/usr/bin/env python3
"""To-Do List - Task Management App"""

import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, task_description):
        task = {
            "id": len(self.tasks) + 1,
            "description": task_description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"\n✅ Task added! (ID: {task['id']})")

    def view_tasks(self):
        if not self.tasks:
            print("\n📭 No tasks found!")
            return

        print("\n" + "=" * 70)
        print("YOUR TO-DO LIST".center(70))
        print("=" * 70)

        for task in self.tasks:
            status = "✓" if task["completed"] else "○"
            print(f"\n[{status}] ID: {task['id']}")
            print(f"    Task: {task['description']}")
            print(f"    Created: {task['created_at']}")

    def delete_task(self, task_id):
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]

        if len(self.tasks) < initial_length:
            self.save_tasks()
            print(f"\n🗑️  Task {task_id} deleted!")
        else:
            print(f"\n❌ Task not found!")

def main():
    todo = TodoList()

    print("\n🎯 Welcome to To-Do List!")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("\nChoice (1-4): ").strip()

        if choice == "1":
            task = input("\nEnter task: ").strip()
            if task:
                todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("\nTask ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("❌ Invalid ID!")
        elif choice == "4":
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
