#Building helpdesk sim idea only XD
import time
tickets = []
ticket_number = 101

def create_ticket():
    global ticket_number

    name = input("Name: ")
    problem = input("Problem: ")
    priority = input("Priority: ")

    ticket = {
        "id": ticket_number,
        "name": name,
        "problem": problem,
        "priority": priority,
        "status": "Open"
    }
    tickets.append(ticket)

    print(f"Ticket #{ticket_number} created.")
    ticket_number += 1

def view_tickets():
    print("=======View Tickets======")
    if len(tickets) == 0:
        print("No tickets")

    for ticket in tickets:
        print(f"Ticket #{ticket['id']}")
        print(f"Name: {ticket['name']}")
        print(f"Problem: {ticket['problem']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}\n")

while True:
    print("=====IT HELP DESK=====")
    print("1. Create ticket")
    print("2. View Tickets")
    print("3. Exit\n")
    choice = input("Option: (1-3): ")

    if choice == "1":
        create_ticket()
    elif choice == "2":
        view_tickets()
    elif choice == "3":
        print("Exiting....")
        time.sleep(1)
        break
    else:
        print("Invalid Input!")