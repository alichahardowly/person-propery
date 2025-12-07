import os
import json
people = []
if os.path.exists("people.json"):
    with open("people.json", "r") as f:
        people = json.load(f)
properties = [
    ('name', str),
    ('family name', str),
    ('age', int)
]

def name_exists(name):
    for person in people:
        if person['name'].lower() == name.lower():
            return True
    return False

def show_help():
    print("""
Available Commands:
  h  : show help
  d  : add new person
  s  : search a person by name
  k  : show all people
  e  : exit program
""")
def add_person(name):
    person = {}
    person['name'] = name 
    for prop, p_type in properties[1:]:
        while True:
            try:
                value = input(f"enter {prop}: ")
                person[prop] = p_type(value)
                break
            except ValueError:
                print("Invalid value, try again.")

    people.append(person)
    print("Person added successfully!")
    print("you %s person aded\n" %len(people))
    return person

def search_person():
    text = input("enter name or family name to search: ").strip().lower()
    found_any = False

    for person in people:
        if (person['name'].lower() == text) or (person['family name'].lower() == text):
            print("\nPerson found:")
            for key, value in person.items():
                print(f"{key}: {value}")
            found_any = True

    if not found_any:
        print("No person found with that name or family name.")

def print_all():
    if not people:
        print("No people added yet.")
        return

    print("\nAll people:")
    for i, person in enumerate(people, 1):
        print(f"\nPerson {i}:")
        for key, value in person.items():
            print(f"  {key}: {value}")

print("Welcome! Type 'h' for help.\n")

while True:
    cmd = input("> ").strip().lower()

    if cmd == 'h':
        show_help()

    elif cmd == 'd':
        while True:
            print("type  quit to quit adding")
            name = input("enter name: ").strip()

            if name == "quit":
                break
            person = add_person(name)
        

    elif cmd == 's':
        search_person()

    elif cmd == 'k':
        while True:
            print_all()
            subcmd=input("type d for delete or q for quit:\n")
            if subcmd == 'd':
                try:
                    num = int(input("Enter the number of the person to delete: "))
                    if num < 1 or num > len(people):
                        print("Invalid number!")
                        continue
                except ValueError:
                    print("Please enter a valid number!")
                    continue

                selected = people[num - 1]
                print(f"Do you want to delete '{selected['name']}'? (yes/no)")
                confirm = input("> ").strip().lower()

                if confirm == "yes":
                    del people[num - 1]
                    print("Person deleted.")

                else:
                    print("Canceled.")
            elif subcmd == 'q':
                break

        

    elif cmd == 'e':
        print("Exiting program...")
        with open("people.json", "w") as f:
            json.dump(people, f)
        break

    else:
        print("Unknown command. Type 'h' for help.")
