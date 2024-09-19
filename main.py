import pandas as pd
import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

contacts_path = "/Users/appletrh/PycharmProjects/ENS/contacts.csv"

def users_upload(path):
    df = pd.read_csv(path)
    return df

#print(users_upload(contacts_path))

def get_alert():
    """
    """
    # Initialize the main tkinter window.
    root = tk.Tk()

    # Hide the main tkinter window as we only want to show the message box.
    # root.withdraw()

    # Display a pop-up message box with the task's name.
    alert = askstring('Emergency Notification System', 'What is your emergency alert?')
    showinfo('Hello!', 'Your alert have been successfully send: {}'.format(alert))

    win.mainloop()
    root.destroy()

get_alert("dada")