# TRIPEX - Travel and  expense Management Application
# Tkinter is used for creating Graphical user interface (GUI).
#JSON file is used to store username, passowrd, trip details and expenses.
#PIL is used for dispaying the Truipex image

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json
import os
import heapq
from tkinter import messagebox

window = tk.Tk()
dir = os.path.dirname(os.path.abspath(__file__))
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.title("TRIPEX")


frame = tk.Frame(window)
frame.pack(fill="both", expand=True)

def clear_screen():
    for widgit in frame.winfo_children():
        widgit.destroy()

def title_page():
    clear_screen()
    frame.configure(bg="white")
    tk.Label(
    frame,
    text="TRIPEX",
    fg="Dark Blue",
    bg="white",
    font=("impact", 200, "italic" ),
    ).pack(expand=True, anchor="c")

def click(username):
    new_page = tk.Toplevel()
    # replace either screen_width and screen_height to change the appropriate dimension
    new_page.geometry(f"{screen_width}x{screen_height}")
    new_page.configure(bg="white")

    tk.Label(
        new_page,
        text="TRIP NAME",
        font=("Arial", 15)
    ).grid(row=0, column=0, padx=20, pady=20, sticky="e")

    trip_entry = tk.Entry(new_page, width=40)
    trip_entry.grid(row=0, column=1, padx=20, pady=20)

    tk.Label(
        new_page,
        text="DESTINATION",
        font=("Arial", 15)
    ).grid(row=1, column=0, padx=20, pady=20, sticky="e")

    Destination_entry = tk.Entry(new_page, width=40)
    Destination_entry.grid(row=1, column=1, padx=20, pady=20)

    tk.Label(
        new_page,
        text="PARTICIPANT",
        font = ("Arial", 15),
    ).grid(row=2, column=0, padx=20, pady=20, sticky="e")

    Participant_entry = tk.Spinbox(
        new_page,
        from_=1,
        to=100,
        width=38
    )
    Participant_entry.grid(row=2, column=1, padx=20, pady=20)

    tk.Label(
        new_page,
        text="BUDGET",
        font = ("Arial", 15),
        ).grid(row=3, column=0, padx=20, pady=20, sticky="e")

    budget_entry = tk.Spinbox(
            new_page,
            from_=1,
            to=100,
            width=38
        )
    budget_entry.grid(row=3, column=1, padx=20, pady=20)

    tk.Label(
        new_page,
        text="START DATE",
        font=("Arial", 15)
    ).grid(row=4, column=0, padx=20, pady=20, sticky="e")

    Startdate_entry = tk.Entry(new_page, width=20)
    Startdate_entry.grid(row=4, column=1, padx=5, pady=20)


    tk.Label(
        new_page,
        text="END DATE",
        font=("Arial", 15)
    ).grid(row=4, column=2, padx=20, pady=20, sticky="e")

    Enddate_entry = tk.Entry(new_page, width=20)
    Enddate_entry.grid(row=4, column=3, padx=5, pady=20)

    Startdate_entry.insert(0, "DD/MM/YYYY")
    Enddate_entry.insert(0, "DD/MM/YYYY")

    def save_trip():

        if (trip_entry.get().strip() == "" or
            Destination_entry.get().strip()==""or
            Participant_entry.get().strip()=="" or
            budget_entry.get().strip() == "" or
            Startdate_entry.get().strip() == "" or
            Enddate_entry.get().strip() == ""
        ):
   
            messagebox.showerror("Error", "Please fill in all the details that are required.")
            return

        budget = budget_entry.get()

        if not budget.startswith("$"):
            budget = "$" + budget
           
        trip = {
            "username": username,
            "Trip_name": trip_entry.get(),
            "destination":Destination_entry.get(),
            "participants": Participant_entry.get(),
            "budget": budget,
            "start_date":Startdate_entry.get(),
            "end_date":Enddate_entry.get(),
        }

        if os.path.exists("trips.json"):
            try:
                with open("trips.json", "r") as file:
                    trips = json.load(file)
            except json.JSONDecodeError:
                trips = []
        else:
            trips = []

        trips.append(trip)

        with open("trips.json", "w") as file:
            json.dump(trips, file, indent=4)

        messagebox.showinfo("Success", "Trip saved successfully!")

        new_page.destroy()
        dashboard(username)

    button= tk.Button(
        new_page,
        command=save_trip,
        text="Save Trip",
        background="grey",
        fg="Black",
        height=5,
        width=20,
    )
    button.grid(row=6, column=2, padx=5, pady=20)

def log_page():
    log_page = tk.Toplevel()
    log_page.geometry(f"{screen_width}x{screen_height}")
    log_page.configure(bg="black")
    log_page.title("SIGN IN")

    filename = "users.json"

    tk.Label(
        log_page,
        text="TRIPEX",
        font=("calligraffitti", 40, "bold", "italic"),
        fg="blue",
        bg="black",
    ).pack(anchor="nw", side="top", padx=20, pady=20)


    tk.Label(
        log_page,
        text = "Enter your info to sign in",
        font=("Times New Roman", 45, "bold"),
        fg="Dark Blue",
        background="White"
    ).pack(pady=(0, 40))

    login_form = tk.Frame(log_page, bg="black")
    login_form.pack(pady=10)

    tk.Label(
        login_form,
        text="Username",
        font=("Arial", 16),
        fg="Dark Blue",
        bg="White",
        width=15,
        anchor="e"
    ).grid(row=0, column=0, padx=10, pady=10, sticky="e")

    userID_entry = tk.Entry(login_form, width=40)
    userID_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(
        login_form,
        text="Password",
        font=("Arial", 16),
        fg="Dark blue",
        bg="White",
        width=15,
        anchor="e"
    ).grid(row=1, column=0, padx=10, pady=10, sticky="e")

    password_entry = tk.Entry(login_form, width=40, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    def register():
        register_page = tk.Toplevel()
        register_page.geometry(f"{screen_width}x{screen_height}")
        register_page.configure(bg="#1F5E79")
        register_page.title("REGISTER")

        tk.Label(
            register_page,
            text="CREATE ACCOUNT",
            font=("Arial", 40, "bold"),
            fg="Dark blue",
            bg="white",
        ).pack(pady=40)

        register_form = tk.Frame(register_page, bg="#1F5E79")
        register_form.pack(pady=10)

        tk.Label(
            register_form,
            text="Username",
            font=("Arial", 16, "bold"),
            fg="Dark Blue",
            bg="White",
            width=18,
            anchor="e"
        ).grid(row=0, column=0, padx=10, pady=15, sticky="e")

        register_user = tk.Entry(register_form, width=40)
        register_user.grid(row=0, column=1, padx=10, pady=15)

        tk.Label(
            register_form,
            text="Password",
            font=("Arial", 16),
            fg="Dark Blue",
            bg="White",
            width=18,
            anchor="e"
        ).grid(row=1, column=0, padx=10, pady=15, sticky="e")

        register_password = tk.Entry(register_form, width=40, show="*")
        register_password.grid(row=1, column=1, padx=10, pady=15)

        tk.Label(
            register_form,
            text="Confirm Password",
            font=("Arial", 16),
            fg="Dark Blue",
            bg="white",
            width=18,
            anchor="e"
        ).grid(row=2, column=0, padx=10, pady=15, sticky="e")

        confirm_password = tk.Entry(register_form, width=40, show="*")
        confirm_password.grid(row=2, column=1, padx=10, pady=15)

   
        def save_account():
            userID = register_user.get().strip()
            password = register_password.get().strip()
            confirm = confirm_password.get().strip()

            if userID == "" or password == "" or confirm == "":
                messagebox.showerror( "Error", "Please fill all fields")
                return

            if password != confirm:
                messagebox.showerror("Error", "Passwords do not match")
                return

            filename = "users.json"
               
            if os.path.exists (filename):
                try:
                    with open(filename, "r") as file:
                        users = json.load(file)
                except json.JSONDecodeError:
                    users = {}
            else:
                users  = {}

                   
            if userID in users:
                messagebox.showerror( "Error", "Username already exists")
                return
                   
            users[userID]={
                "password": password,
                "role": "user",
             }


            with open (filename, "w") as file :
                json.dump(users, file,  indent=4)

            messagebox.showinfo("Success", "Account created!")
            register_page.destroy()

        tk.Button(
            register_page,
            text="Create Account",
            command=save_account,
            bg="white",
            fg="Dark blue",
            width=20,
            height=2,
        ).pack(pady=20)
       
       
    def sign_in():
       
        userID = userID_entry.get().strip()
        password = password_entry.get().strip()
        filename = "users.json"

        print("Entered username:", userID)
        print("Entered password:", password)

        if userID == "" or password == "":
            messagebox.showerror("Error", "Please enter username and password")
            return

        if not os.path.exists(filename):
            messagebox.showerror("Error", "No users have registerd yet.")
            return

        try:                                          
            with open(filename, "r") as file:
             users = json.load(file)

        except json.JSONDecodeError:
            messagebox.showerror("Error", "User file is empty or corrupted")
            return

        if userID not in users:
            messagebox.showerror("Error", "Username not found")
            return

        if userID in users:
            if users [userID]["password"] != password:
                messagebox.showerror("Error", "wrong Password")
                return
           
            role = users[userID]["role"]

            messagebox.showinfo("Success", f"Welcome {userID}!")
            log_page.destroy()

            window.withdraw()

            if role =="admin":
                dashboard(userID)
            else:
                open_user_expense(userID)
      
                                           
    button_frame = tk.Frame(log_page, bg="black")
    button_frame.pack(pady=20)


    tk.Button(
        button_frame,
        text="Sign In",
        command=sign_in,
        bg="green",
        fg="Black",
        width=18,
        height=2,
    ).pack(side="left", padx=10)
           
    tk.Label(
        button_frame,
        text="or",
        bg="black",
        fg="white",
        font=("Arial", 14, "bold"),
    ).pack(side="left", padx=10)

    tk.Button(
        button_frame,
        text="Create New Account",
        command=register,
        bg="Blue",
        fg="black",
        width=18,
        height=2,
    ).pack(side="left", padx=10)
          

 
   

def dashboard(username):
    dash = tk.Toplevel()
    dash.geometry(f"{screen_width}x{screen_height}")
    dash.configure(bg="white")
    dash.title("Dashboard")

    if os.path.exists("trips.json"):
        try:
            with open("trips.json", "r") as file:
                trips = json.load(file)
        except json.JSONDecodeError:
            trips = []
    else:
        trips = []

    user_trips = []
    for trip in trips:
        if trip["username"] == username:
            user_trips.append(trip)

    print("All trips", trips)
    print("User trips:", user_trips)
   
    tk.Label(
        dash,
         text=f"Welcome {username}",
        font=("Arial", 30, "bold"),
        bg="White",
        fg="Dark Blue",
    ).pack(pady=30)

    tk.Label(
        dash,
        text=f"Total Trips: {len(user_trips)}",
        font=("Arial", 20, "bold"),
        bg="White",
        fg="Dark Blue",
    ).pack(pady=10)

    tk.Label(
        dash,
        text="Your Trip",
        font=("Times New Roman", 35),
        anchor="c",
        bg="White",
        fg="Dark Blue",
    ).pack(pady=30)

    #create a frame for the grid (columns for trip and buttons)
    #pack frame
    trip_frame = tk.Frame(
        dash,
        bg="light Grey",
        bd=5,
        relief="solid",
        width=800,
        height=300
    )
   

    trip_frame.pack(
        fill="both",
        padx=3,
        pady=20
    )
   
    if len(user_trips) == 0:
        tk.Label(
            trip_frame,
            text="You have not created any trips yet.",
            font=("Arial", 16),
            bg="White",
            fg="Dark Blue",
        ).pack(pady=10) #grid label to first column
        print("test")

    else:

        for trip in user_trips:
            trip_text = (
                f"{trip['Trip_name']} | "
                f"{trip['destination']} | "
                f"participants:{trip['participants']} |"
                f"Budget:{trip['budget']} |"
                f"{trip['start_date']} -> {trip['end_date']} "
            )
                
            tk.Button(
                trip_frame,
                text=trip_text,
                font=("Arial", 16),
                bg="white",
                fg="Dark Blue",
                relief="flat",
                anchor="w",
                command=lambda t=trip: open_trip(t, dash)
            ).pack(fill=tk.X, padx=10, pady=5) #grid label to first column
            #create buttons for each trip (this is already in the loop)
            #grid buttons to next column

            #create function for each button to create a window to show trip details and expenses (not here)

    create_button = tk.Button(
        trip_frame,
        text="+ Create Trip",
        command=lambda:click(username),
        font=("Arial", 20, "bold"),
        width=10,
        height=2,
        anchor="c",
        bg="White",
        fg="Dark Blue",
    )
    create_button.pack(
        side="bottom",
        pady=30
    )
 


def delete_trip(trip, trip_window, dash):
    answer = messagebox.askyesno(
        "Delete Trip",
        f"Are you sure you want to delete '{trip['Trip_name']}'?"
    )

    if not answer:
        return
    #Read the trips from trips.json
    try:
        with open ("trips.json","r" ) as file:
            trips = json.load(file)
              
    except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Coloud not read trips.json")
            return
    new_trips = []

    for t in trips:
        if not (
            t["username"] == trip["username"]
            and t ["Trip_name"] == trip["Trip_name"]
            and t["destination"] == trip["destination"]
        ):
            continue

        new_trips.append(t)

    if len(new_trips) == len(trips):
        messagebox.showerror("Error", "The trip could not be found."
        )
        return

    with open("trips.json", "w") as file:
            json.dump(new_trips, file, indent=4)
    messagebox.showinfo("Success", "Trips deleted successfully!")

    trip_window.destroy()

    dash.destroy()

    dashboard(trip["username"])



def compute_settlement(people, expenses):

    total = sum(float(e["amount"]) for e in expenses)

    if len(people) == 0:
        return None
    #Calculates how much each person should pay
    share = total / len(people)
    #Store how muc each person has actually paid.
    paid = {}

    for person in people:
        paid[person] = 0.0

    for expense in expenses:
        person = expense["paid_by"]
        amount = float(expense["amount"])

        paid[person] = paid.get(person, 0.0) + amount

    balances = {}

    for person in people:
        balances [person] = round(paid[person]- share, 2 )

    creditors = []
    debtors = []

    for person, balance in balances.items():

        if balance > 0:
            creditors.append([person, balance])

        elif balance < 0:
            debtors.append([person, abs(balance)])

    transactions = []

    while creditors and debtors:

        creditor = creditors[0]
        debtor = debtors[0]

        creditor_name = creditor[0]
        creditor_amount = creditor[1]

        debator_name = debtor [0]
        debtor_amount = debtor[1]

        amount = min(creditor_amount, debtor_amount)
        amount = round(amount, 2 )

        transactions.append({
            "from": debator_name,
            "to": creditor_name,
            "amount": amount
        })

        creditor[1] = round (creditor_amount - amount, 2)
        debtor[1] = round(debtor_amount - amount, 2)
       
        if creditor[1] <=0.01:
            creditors.pop(0)

        if debtor[1] <= 0.01:
            debtors.pop(0)

    return {
        "total": round(total, 2),
        "share_per_person":round(share, 2 ),
        "balances": balances,
        "transactions": transactions

    }       

   
def settle_trip(trip):
           
    try:
        with open("expenses.json", "r") as file:
            all_expenses = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(
            "Error",
            "Could not read expenses.json"
        )
        return

    trip_expenses = []

    for expense in all_expenses:
        if expense["Trip_name"] == trip["Trip_name"]:
            trip_expenses.append(expense)

    if not trip_expenses:
        messagebox.showinfo(
        "settlement",
        "there are no expenses for this trip."
        )
        return
    people = trip["participants"]

    if isinstance(people, str):
        try:
            people = int(people)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Invalid number of participants"
            )
            return
    if (people) <= 0:
        messagebox.showerror(
            "Error",
            "There are no participants."
        )
        return

    participant_names = []

    for expense in trip_expenses:
        person = expense["paid_by"]

        if person not in participant_names:
            participant_names.append(person)

    if len(participant_names) ==0:
        messagebox.showerror(
            "Error",
            "no participants could be found"
        )
        return

    result = compute_settlement(
        participant_names,
        trip_expenses
    )

    settlement_window = tk.Toplevel()
    settlement_window.title(
        "Settlement - " + trip ["Trip_name"]
    )

    settlement_window.geometry("650x650")
    settlement_window.minsize(500, 500)

    settlement_window.configure(
        bg="white"
                )
    tk.Label(
        settlement_window,
        text=trip['Trip_name'],
        font=("Arial", 18, "bold"),
        fg="Dark Blue",
        bg="white"
    ).pack(pady=(15, 10))

    tk.Label(
        settlement_window,
        text=f"Total spent: ${result['total']:.2f}",
        font=("Arial", 16),
        bg="white"
    ).pack(pady=2)

    tk.Label(
        settlement_window,
        text=f"Each person pays: ${result['share_per_person']:.2f}",
        font=("Arial", 16),
        bg="white"
     ).pack(pady=2)

    ttk.Separator(settlement_window, orient="horizontal").pack(fill="x", padx=30, pady=15)

    tk.Label(
        settlement_window,
        text="BALANCES",
        font=("Arial", 20, "bold"),
        fg="Dark Blue",
        bg="white"
    ).pack(pady=(20, 10))

    for person, balance in result['balances'].items():

        if balance > 0:
            text = f"{person} receives ${balance:.2f}"
            colour = "green"

        elif balance < 0 :

            text = f"{person} owes ${abs(balance):.2f}"
            colour = "red"

        else:
            text = f"{person} is settled"
            colour = "black"

        tk.Label(
            settlement_window,
            text=text,
            font=("Arial", 15, "bold"),
            fg=colour,
            bg="white"
        ).pack(pady=3)

    ttk.Separator(settlement_window, orient="horizontal").pack(fill="x", padx=30, pady=15)

    tk.Label(
        settlement_window,
        text="WHO PAYS WHOM",
        font=("Arial", 20, "bold"),
        fg="Dark Blue",
        bg="white"
    ).pack(pady=(0, 10))

    if result["transactions"]:
        for transaction in result["transactions"]:
            text = (
                f"{transaction['from']} → {transaction['to']}: "
                f"${transaction['amount']:.2f}"
            )

            tk.Label(
                settlement_window,
                text=text,
                font=("Arial", 15),
                fg="Dark Blue",
                bg="white"
            ).pack(pady=3)

    else:

        tk.Label(
            settlement_window,
            text="Everyone is already settled",
            font=("Arial", 15),
            bg="white"
        ).pack(pady=3)


def open_trip(trip, dash):

    trip_window = tk.Toplevel()
    trip_window.title(trip["Trip_name"])
    trip_window.geometry("600x500")
    trip_window.configure(bg="white")
       

    tk.Label(
        trip_window,
        text=trip["Trip_name"],
        font=("Arial", 24, "bold"),
        bg="White",
        fg="Dark Blue",
    ).pack(pady=20)

    tk.Label(
        trip_window,
        text=f"Destination:{trip['destination']}",
        font=("Arial", 16),
        bg="white",
        fg="Dark Blue",
    ).pack(anchor="w", padx=30)

    tk.Label(
        trip_window,
        text=f"Participant:{trip['participants']}",
        font=("Arial", 16),
        bg="white",
        fg="Dark Blue"
    ).pack(anchor="w", padx=30)

    tk.Label(
        trip_window,
        text=f"Budget:{trip['budget']}",
        font=("Arial", 16),
        bg="white",
    ).pack(anchor="w", padx=30)

    tk.Label(
        trip_window,
        text=f"Start Date:{trip['start_date']}",
        font=("Arial", 16),
        bg="white",
    ).pack(anchor="w", padx=30)


    tk.Label(
        trip_window,
        text=f"End Date:{trip['end_date']}",
        font=("Arial", 16),
        bg="white",
        fg="Dark Blue"
    ).pack(anchor="w", padx=30)

    tk.Button(
        trip_window,
        text="Settle",
        font=("Arial", 16, "bold"),
        bg="white",
        fg="dark Blue",
        command= lambda: settle_trip(trip),
    ).pack(pady=30)


    tk.Button(
        trip_window,
        text="Delete",
        font=("Arial", 16, "bold"),
        bg="white",
        fg="Dark Blue",
        command=lambda:delete_trip(trip, trip_window, dash)
    ).pack(pady=30)

   

def show_home():

    clear_screen()
    frame.configure(bg="White")
   

    log_in = tk.Button(
        frame,
        command=log_page,
        text="Sign in",
        height=3,
        width=16,
        bg="White",
        fg="Dark Blue",
        )
    log_in.pack(anchor="ne", side="top", padx=20, pady=20)

    tk.Label(
        frame,
        text="TRIPEX",
        font=("Acme", 100, "bold"),
        fg="Dark blue",
        bg="White",
    ).pack(anchor="nw", side="top", padx=20, pady=20)
   
    photo = Image.open(dir + "/TRIPEX.png")
    photo = photo.resize((1000, 550))

    photo = ImageTk.PhotoImage(photo)

    image_label = tk.Label(
        frame,
        image=photo,
        bg="white",
    )

    image_label.image = photo
    image_label.pack(pady=20)


class Tripex:
    def __init__(self, Trip, Name_particpants, Total, Expenses, Estimate_budget):
        self.Trip = Trip
        self.Name_particpants = Name_particpants
        self.Total = Total
        self.Expenses = Expenses
        self.Estimate_budget = Estimate_budget

def open_user_expense(username):

    if os.path.exists("trips.json"):
        try:
            with open("trips.json", "r") as file:
                trips = json.load(file)
        except json.JSONDecodeError:
            trips = []
    else:
        trips = []

    if os.path.exists("users.json"):
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except json.JSONDecodeError:
            users = {}
    else:
            users = {}

    admin_users =  []

    for user, information in users.items():
        if information.get("role") == "admin":
            admin_users.append(user)


    print("Logged in user:", username)
    print("Admin users:", admin_users)
    print("All Trips:", trips)
   

    admin_trips = []

    for trip in trips:
        if trip.get("username") in admin_users:
            admin_trips.append(trip)

    print("Admin Trips:", admin_trips)

    if len(admin_trips) == 0:
        messagebox.showinfo(
            "No Trips",
            "The admin has not created any trips yet."
        )

        window.deiconify()
        show_home()
        return

    User_expense_screen(admin_trips, username)

def User_expense_screen(trips, username):
   
    expense_page = tk.Toplevel()
    expense_page.geometry(f"{screen_width}x{screen_height}")
    expense_page.configure(bg="white")
    expense_page.title("Expense Table")

    tk.Label(
        expense_page,
        text="Expense Tracker",
        font=("Arial", 20, "bold"),
        fg="dark blue",
        bg="white",
    ).pack(pady=20)

    tk.Label(
        expense_page,
        text="Enter your Expenses",
        font=("Arial", 35, "bold"),
        fg="Dark Blue",
        bg="white",
    ).pack(pady=30)

    expense_frame = tk.Frame(
        expense_page,
        bg="#F5F7FA",
        bd=3,
        relief="solid",
        width=700,
        height=450
    )
    expense_frame.pack(
        pady=20,
        padx=20
    )

    expense_frame.pack_propagate(False)

    tk.Label(
        expense_frame,
        text="Add Expense",
        font=("Arial", 25, "bold"),
        fg="Dark Blue",
        bg="#F5F7FA"
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        pady=20
    )


    tk.Label(
            expense_frame,
            text="Description",
            font=("Arial", 15, "bold"),
            fg="Dark Blue",
            bg="#F5F7FA"
        ).grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="e"
        )

    description_entry = tk.Entry(
        expense_frame,
        width=35,
        font=("Arial", 14)
    )

    description_entry.grid(
        row=2,
        column=1,
        padx=20,
        pady=10
    )

    tk.Label(
        expense_frame,
        text="cost($)",
        font=("Arial", 15, "bold"),
        fg="Dark Blue",
        bg="#F5F7FA"
    ).grid(
        row=3,
        column=0,
        padx=20,
        pady=10,
        sticky="e"
    )

    cost_entry = tk.Entry(
        expense_frame,
        width=35,
        font=("Arial", 14)
    )

    cost_entry.grid(
            row=3,
            column=1,
            padx=20,
            pady=10
    )
    tk.Label(
        expense_frame,
        text="Date",
        font=("Arial", 15, "bold"),
        fg="Dark Blue",
        bg="#F5F7FA",

        ).grid(
            row=4,
            column=0,
            padx=20,
            pady=10,
            sticky="e"
        )


    date_entry = tk.Entry(
        expense_frame,
        width=35,
        font=("Arial", 14)
    )

    date_entry.grid(
        row=4,
        column=1,
        padx=20,
        pady=10
    )

    date_entry.insert(
        0,
        "DD/MM/YYYY"
    )
    tk.Label(
        expense_frame,
        text="Trip",
        font=("Arial", 15, "bold"),
        fg="Dark Blue",
        bg="#F5F7FA",
    ).grid(
        row=1,
        column=0,
        padx=20,
        pady=10,
        sticky="e"
    )

    trip_names = [
        trip["Trip_name"]
        for trip in trips
    ]
    selected_trip = tk.StringVar()

    trip_box = ttk.Combobox(
        expense_frame,
        textvariable=selected_trip,
        values=trip_names,
        state="readonly",
        width=33,
        font=("Arial", 14)
    )

    if trip_names:
        trip_box.current(0)

    trip_box.grid(
        row=1,
        column=1,
        padx=20,
        pady=10
    )

    if trip_names:
        trip_box.current(0)

    def save_expense():
        trip_name = selected_trip.get()
        description = description_entry.get().strip()
        cost = cost_entry.get().strip()
        date = date_entry.get().strip()

        if trip_name =="":
            messagebox.showerror("Error", "Please select a trip.")
            return
        if description =="":
            messagebox.showerror("Error", "Please enter a description.")
            return
        if cost == "":
            messagebox.showerror("Error", "Please enter the cost.")
            return
        if date =="" or date == "DD/MM/YYYY":
            messagebox.showerror("Error", "Please enter the date.")
            return
        try:
            cost=float(cost)
        except ValueError:
            messagebox.showerror("Error","Cost must be a number.")
            return
        cost = f"{cost}"

        expense = {
            "Trip_name":trip_name,
            "description": description,
            "amount": cost,
            "paid_by": username,
            "date":date,
        }

        if os.path.exists("expenses.json"):
            try:
                with open ("expenses.json", "r") as file:
                    expenses = json.load(file)
            except json.JSONDecodeError:
                expenses = []
        else:
            expenses= []

        expenses.append(expense)

        with open ("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        messagebox.showinfo("Success", "Expense saved successfully!")

        description_entry.delete(0, tk.END)
        cost_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        date_entry.insert(0, "DD/MM/YYYY")

    tk.Button(
        expense_frame,
        text="Save Expense",
        command=save_expense,
        font=("Arial", 15, "bold"),
        bg="White",
        fg="Dark Blue",
        width=18,
        height=2
    ).grid(
        row=5,
        column=0,
        columnspan=2,
        pady=20
    )

       
#------------------------------------
#SAVE EXPENSE
#---------------------------------------

title_page()


window.after(3000,show_home)

window.mainloop()
