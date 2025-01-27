import time
# Global Data Structure
data = {
   "employees": ["Marco"],
   "managers": ["Laura"],
   "clients": ["Coca-cola"],
   "active_projects": {},
   "inactive_projects": {},
   "active_tickets": {},
   "inactive_tickets": {}
}

def sleep_timer():
   time.sleep(3)

def clear_screen():
   print("\n" * 40)

def banner_print():
   print(r"""
   #########################################################################
   ╔═╗┬─┐┌─┐ ┬┌─┐┌─┐┌┬┐  ┌┬┐┌─┐┌┐┌┌─┐┌─┐┌─┐┌┬┐┌─┐┌┐┌┌┬┐  ┌─┐┬ ┬┌─┐┌┬┐┌─┐┌┬┐
   ╠═╝├┬┘│ │ │├┤ │   │   │││├─┤│││├─┤│ ┬├┤ │││├┤ │││ │   └─┐└┬┘└─┐ │ ├┤ │││
   ╩  ┴└─└─┘└┘└─┘└─┘ ┴   ┴ ┴┴ ┴┘└┘┴ ┴└─┘└─┘┴ ┴└─┘┘└┘ ┴   └─┘ ┴ └─┘ ┴ └─┘┴ ┴
   #########################################################################
   """)
   
def input_validation_static_dict(options, previous_menu, location=None):
   clear_screen()
   if location:
       print(location)
   for idx, option in enumerate(options, start=1):
       print(f"{idx}. {option}")
   print("0. Go back")
   while True:
       try:
           choice = int(input("Choose an option: "))
           if choice == 0:
               previous_menu()
               break
           elif 1 <= choice <= len(options):
               return options[choice - 1]
           else:
               print("Invalid choice. Try again.")
       except ValueError:
           print("Invalid input. Enter a number.")

def initial_menu():
   banner_print()
   options = {
       "Projects": project_menu,
       "Personnel": personnel_menu,
       "Clients": client_menu,
       "Exit": exit_program
   }
   choice = input_validation_static_dict(list(options.keys()), exit_program, "Main Menu")
   if choice:
       options[choice]()

def project_menu():
   options = {
       "Show Projects": show_projects,
       "Add Project": add_project,
       "Back": initial_menu
   }
   choice = input_validation_static_dict(list(options.keys()), initial_menu, "Projects Menu")
   if choice and choice != "Back":
       options[choice]()

def personnel_menu():
   options = {
       "Show Personnel": show_personnel,
       "Add Personnel": add_personnel,
       "Back": initial_menu
   }
   choice = input_validation_static_dict(list(options.keys()), initial_menu, "Personnel Menu")
   if choice and choice != "Back":
       options[choice]()

def client_menu():
   options = {
       "Show Clients": show_clients,
       "Add Client": add_client,
       "Back": initial_menu
   }
   choice = input_validation_static_dict(list(options.keys()), initial_menu, "Client Menu")
   if choice and choice != "Back":
       options[choice]()

def show_projects():
   if data["active_projects"]:
       for project_name, details in data["active_projects"].items():
           print(f"Project: {project_name}, Manager: {details['manager']}, Client: {details['client']}")
   else:
       print("No active projects found.")
   input("\nPress Enter to go back...")
   project_menu()

def add_project():
   client = input_validation_static_dict(data["clients"], project_menu, "Select a client:")
   manager = input_validation_static_dict(data["managers"], project_menu, "Select a manager:")
   project_name = input("Enter the project name: ").strip()
   if project_name not in data["active_projects"]:
       data["active_projects"][project_name] = {
           "client": client,
           "manager": manager,
           "tickets": []
       }
       print(f"Project '{project_name}' added successfully!")
   else:
       print("Project already exists!")
   sleep_timer()
   project_menu()

def show_personnel():
   print("Managers:")
   for manager in data["managers"]:
       print(f"- {manager}")
   print("\nEmployees:")
   for employee in data["employees"]:
       print(f"- {employee}")
   input("\nPress Enter to go back...")
   personnel_menu()

def add_personnel():
   person_type = input_validation_static_dict(["Manager", "Employee"], personnel_menu, "Select personnel type:")
   person_name = input("Enter the person's name: ").strip()
   if person_type == "Manager":
       if person_name not in data["managers"]:
           data["managers"].append(person_name)
           print(f"Manager '{person_name}' added successfully!")
       else:
           print("Manager already exists!")
   elif person_type == "Employee":
       if person_name not in data["employees"]:
           data["employees"].append(person_name)
           print(f"Employee '{person_name}' added successfully!")
       else:
           print("Employee already exists!")
   sleep_timer()
   personnel_menu()

def show_clients():
   print("Clients:")
   for client in data["clients"]:
       print(f"- {client}")
   input("\nPress Enter to go back...")
   client_menu()

def add_client():
   client_name = input("Enter the client name: ").strip()
   if client_name not in data["clients"]:
       data["clients"].append(client_name)
       print(f"Client '{client_name}' added successfully!")
   else:
       print("Client already exists!")
   sleep_timer()
   client_menu()

def exit_program():
   print("Thank you for using the system. Goodbye!")
   sleep_timer()
   exit()

if __name__ == "__main__":
   initial_menu()