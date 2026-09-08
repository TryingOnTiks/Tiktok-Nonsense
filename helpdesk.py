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
        return
    
    for ticket in tickets:
        print(f"Ticket #{ticket['id']}")
        print(f"Name: {ticket['name']}")
        print(f"Problem: {ticket['problem']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}\n")

def delete_ticket():
    print("\n======Delete Ticket=====")
    if len(tickets) == 0:
        print("No tickets")
        return

    print("Available Tickets:")

    for ticket in tickets:
        print(f"Ticket #{ticket['id']} - {ticket['name']}")

    try:
        ticket_id = int(input("Enter ticket number to delete: "))

        for i, ticket in enumerate(tickets):
            if ticket["id"] == ticket_id:
                del tickets[i]
                print(f"Ticket #{ticket_id} deleted.")
                return

        print("Ticket not found.")

    except ValueError:
        print("Enter VALID ticket number!")

while True:
    print("=====IT HELP DESK=====")
    print("1. Create ticket")
    print("2. View Tickets")
    print("3. Ticket Delete")
    print("4. Exit\n")
    choice = input("Option: (1-3): ")

    if choice == "1":
        create_ticket()
    elif choice == "2":
        view_tickets()
    elif choice == "3":
        delete_ticket()
    elif choice == "4":
        print("Exiting....")
        time.sleep(1)
        break
    else:
        print("Invalid Input!")