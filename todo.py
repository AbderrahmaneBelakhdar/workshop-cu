import json

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    task = input("Nouvelle tâche: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def show_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def delete_task():
    show_tasks()
    tasks = load_tasks()
    index = int(input("Numéro à supprimer: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

while True:
    print("\n1. Ajouter\n2. Afficher\n3. Supprimer\n4. Quitter")
    choice = input("Choix: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break