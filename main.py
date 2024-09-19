import pandas as pd
import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter import ttk

contacts_path = "/Users/appletrh/PycharmProjects/ENS/contacts.csv"

def users_upload(path):
    df = pd.read_csv(path)
    return df

def choose_services():
    """
    Create a window to choose services from checkboxes.
    """
    services = ['SMS', 'Telegram', 'Email']
    selected_services = []

    def on_submit():
        nonlocal selected_services
        selected_services = [service for var, service in zip(service_vars, services) if var.get()]
        services_window.destroy()

    # Create a new Tk window for selecting services.
    services_window = tk.Toplevel()
    services_window.title("Select Services")

    # Create a frame for the checkboxes and title
    frame = tk.Frame(services_window)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Choose Services:", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=len(services), pady=5)

    # Create a list of checkboxes for services.
    service_vars = []
    for index, service in enumerate(services):
        var = tk.BooleanVar()
        service_vars.append(var)
        cb = tk.Checkbutton(frame, text=service, variable=var)
        cb.grid(row=1, column=index, padx=5, pady=5)

    tk.Button(services_window, text="Submit", command=on_submit).pack(pady=5)

    services_window.wait_window()

    return selected_services

def get_alert():
    """
    Gather the emergency alert and service information from the user.
    """
    # Initialize the main tkinter window.
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Step 1: Ask for the emergency alert.
    alert = askstring('Emergency Notification System', 'What is your emergency alert?')

    if not alert:
        showinfo('No Alert', 'No alert was provided.')
        root.destroy()
        return

    # Step 2: Choose services.
    services = choose_services()

    # Debugging output to check services
    print(f"Selected services: {services}")

    if services:
        # Display an information box with the provided alert and selected services.
        services_list = ', '.join(services)
        showinfo('Alert Sent', f'Your alert "{alert}" has been successfully sent via: {services_list}')
    else:
        showinfo('No Services', 'No services were selected.')

    root.destroy()

get_alert()