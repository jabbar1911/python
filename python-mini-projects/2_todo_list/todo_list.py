#!/usr/bin/env python3
"""To-Do List - Task Management App"""

import json
import os
from datetime import datetime

class Todo:
    def __init__(self, file="tasks.json"):
        self.file = file
        self.tasks = self.load()

    def load(self):
        if os.path.exists(self.file):
            try:
                with open(self.file, "r") as f:
                    return json.load(f)
            except:
                return []
        return []

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add(self, desc):
        t = {
            "id": len(self.tasks) + 1,
            "description": desc,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(t)
        self.save()
        print(f"\n✅ Task added! (ID: {t['id']})")

    def view(self):
        if not self.tasks:
            print("\n📭 No tasks found!")
            return

        print("\n" + "=" * 60)
        print("YOUR TO-DO LIST".center(60))
        print("=" * 60)

        for t in self.tasks:
            s = "✓" if t["completed"] else "○"
            print(f"\n[{s}] ID: {t['id']}")
            print(f"    Task: {t['description']}")
            print(f"    Created: {t['created_at']}")

    def delete(self, tid):
        ln = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != tid]

        if len(self.tasks) < ln:
            self.save()
            print(f"\n🗑️  Task {tid} deleted!")
        else:
            print("\n❌ Task not found!")

def main():
    todo = Todo()
    print("\n🎯 Welcome to To-Do List!")

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        ch = input("\nChoice (1-4): ").strip()

        if ch == "1":
            d = input("\nEnter task: ").strip()
            if d:
                todo.add(d)
        elif ch == "2":
            todo.view()
        elif ch == "3":
            try:
                tid = int(input("\nTask ID to delete: "))
                todo.delete(tid)
            except ValueError:
                print("\n❌ Invalid ID!")
        elif ch == "4":
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
