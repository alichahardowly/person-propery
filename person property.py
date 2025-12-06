people = []

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

def add_person():
    person = {}
    while True:
        name = input("enter name: ")
        if name_exists(name):
            print("Error: this name already exists!")
        else:
            person['name'] = name
            break
    for prop, p_type in properties[1:]:
        while True:
            try:
                value = input(f"enter {prop}: ")
                person[prop] = p_type(value)
                break
            except ValueError:
                print("Invalid value, try again.")

    people.append(person)
    print("Person added successfully!\n")

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
        add_person()

    elif cmd == 's':
        search_person()

    elif cmd == 'k':
        print_all()

    elif cmd == 'e':
        print("Exiting program...")
        break

    else:
        print("Unknown command. Type 'h' for help.")
