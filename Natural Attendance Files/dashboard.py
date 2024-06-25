import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import subprocess
import os

def run_file(filename):
    try:
        subprocess.run([f'./{filename}'], check=True)
    except Exception as e:
        print(f"Error: {str(e)}")

def change_color(button):
    button.config(bg='dark orange', fg='black')
    button.after(0, lambda: button.config(bg='orange', fg='black'))

def show_buttons():
    # Create frames for departments
    department_frame = tk.Frame(button_frame, bg='#333333')
    department_frame.pack(pady=50, padx=20)

    # Create buttons for Reception
    reception_frame = tk.Frame(department_frame, bg='#444444')
    reception_frame.pack(side=tk.LEFT, padx=20, pady=20)

    tk.Label(reception_frame, text="ADMIN BLOCK", font=("Roboto Mono", 22, "bold"), fg='white', bg='#444444').pack(pady=20)

    reception_checkin_button = tk.Button(reception_frame, text="Check-in Cam", command=lambda: [run_file('SeedoAdminBlockCheckinCam'), change_color(reception_checkin_button)], 
                                        bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                        highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    reception_checkin_button.pack(pady=10)
    tk.Label(reception_frame, text="[IP Address: 10.253.0.72]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

    reception_checkout_button = tk.Button(reception_frame, text="Check-out Cam", command=lambda: [run_file('SeedoAdminBlockCheckoutCam'), change_color(reception_checkout_button)], 
                                          bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                          highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    reception_checkout_button.pack(pady=10)
    tk.Label(reception_frame, text="[IP Address: 10.253.0.72]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

    reception_training_button = tk.Button(reception_frame, text="Training Cam", command=lambda: [run_file('SeedoAdminBlockTraining'), change_color(reception_training_button)], 
                                          bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                          highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    reception_training_button.pack(pady=10)
    tk.Label(reception_frame, text="[IP Address: 10.253.0.72]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

    # Create buttons for Civil
    civil_frame = tk.Frame(department_frame, bg='#444444')
    civil_frame.pack(side=tk.LEFT, padx=20, pady=20)

    tk.Label(civil_frame, text="B-BLOCK", font=("Roboto Mono", 22, "bold"), fg='white', bg='#444444').pack(pady=20)

    civil_checkin_button = tk.Button(civil_frame, text="Check-in Cam", command=lambda: [run_file('SeedoBBlockCheckinCam'), change_color(civil_checkin_button)], 
                                    bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                    highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    civil_checkin_button.pack(pady=10)
    tk.Label(civil_frame, text="[IP Address: 10.253.0.74]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

    civil_checkout_button = tk.Button(civil_frame, text="Check-out Cam", command=lambda: [run_file('SeedoBBlockCheckoutCam'), change_color(civil_checkout_button)], 
                                     bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                     highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    civil_checkout_button.pack(pady=10)
    tk.Label(civil_frame, text="[IP Address: 10.253.0.74]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

    civil_training_button= tk.Button(civil_frame, text="Training Cam", command=lambda: [run_file('SeedoBblockTraining'), change_color(civil_training_button)], 
                                     bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                     highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    civil_training_button.pack(pady=10)
    tk.Label(civil_frame, text="[IP Address: 10.253.0.74]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

    # Create buttons for Applied Science
    applied_science_frame = tk.Frame(department_frame, bg='#444444')
    applied_science_frame.pack(side=tk.LEFT, padx=20, pady=20)

    tk.Label(applied_science_frame, text="C-BLOCK", font=("Roboto Mono", 22, "bold"), fg='white', bg='#444444').pack(pady=20)

    applied_science_checkin_button = tk.Button(applied_science_frame, text="Check-in Cam", command=lambda: [run_file('SeedoCBlockCheckinCam'), change_color(applied_science_checkin_button)], 
                                              bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                              highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    applied_science_checkin_button.pack(pady=10)
    tk.Label(applied_science_frame, text="[IP Address: 10.253.0.73]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

    applied_science_checkout_button = tk.Button(applied_science_frame, text="Check-out Cam", command=lambda: [run_file('SeedoCBlockCheckoutCam'), change_color(applied_science_checkout_button)], 
                                               bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                               highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    applied_science_checkout_button.pack(pady=10)
    tk.Label(applied_science_frame, text="[IP Address: 10.253.0.73]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

    applied_science_training_button = tk.Button(applied_science_frame, text="Training Cam", command=lambda: [run_file('SeedoCblockTraining'), change_color(applied_science_training_button)], 
                                               bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                               highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    applied_science_training_button.pack(pady=10)
    tk.Label(applied_science_frame, text="[IP Address: 10.253.0.73]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

    # Create buttons for CSE
    cse_frame = tk.Frame(department_frame, bg='#444444')
    cse_frame.pack(side=tk.LEFT, padx=20, pady=20)

    tk.Label(cse_frame, text="D-BLOCK", font=("Roboto Mono", 22, "bold"), fg='white', bg='#444444').pack(pady=20)

    cse_checkin_button = tk.Button(cse_frame, text="Check-in Cam", command=lambda: [run_file('SeedoDBlockCheckinCam'), change_color(cse_checkin_button)], 
                                  bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                  highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    cse_checkin_button.pack(pady=10)
    tk.Label(cse_frame, text="[IP Address: 10.253.0.75]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

    cse_checkout_button = tk.Button(cse_frame, text="Check-out Cam", command=lambda: [run_file('SeedoDBlockCheckoutCam'), change_color(cse_checkout_button)], 
                                   bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                   highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    cse_checkout_button.pack(pady=10)
    tk.Label(cse_frame, text="[IP Address: 10.253.0.75]", font=("RobotoMono", 10), fg='white', bg='#444444').pack(pady=5)

    cse_training_button = tk.Button(cse_frame, text="Training Cam", command=lambda: [run_file('SeedoDblockTraining'), change_color(cse_training_button)], 
                                   bg='orange', fg='black', font=("Roboto Mono", 16, "bold"), width=20, height=2, 
                                   highlightthickness=0, highlightbackground="orange", bd=0, relief="ridge")
    cse_training_button.pack(pady=10)
    tk.Label(cse_frame, text="[IP Address: 10.253.0.75]", font=("Roboto Mono", 10), fg='white', bg='#444444').pack(pady=5)

# Create the main window
root = tk.Tk()
root.title("C++ Application Dashboard")
root.configure(bg='#333333')  # Set the background color of the root window

# Set the initial window size
root.geometry("1000x800")

# Create a frame for the logo
logo_frame = tk.Frame(root, bg='#333333')
logo_frame.pack(side=tk.TOP, anchor=tk.NE)

# Create a logo label
image = Image.open("logomietnewwhite.png")
image = image.resize((250, 80), Image.ANTIALIAS)  # resize the image to 50x50 pixels
photo = ImageTk.PhotoImage(image)
logo_label = tk.Label(logo_frame, image=photo, bg='#333333')
logo_label.image = photo  # keep a reference to the image
logo_label.pack()

# Create a frame for title
title_frame = tk.Frame(root, bg='#333333')
title_frame.pack(pady=20)

# Create a title label
title_label = tk.Label(title_frame, text="SEEDO.AI", font=("Roboto Mono", 48, "bold"), fg='white', bg='#333333')
title_label.pack(pady=80)

# Create a frame for buttons
button_frame = tk.Frame(root, bg='#333333')
button_frame.pack(pady=20)

# Show the initial buttons to run files
show_buttons()

# Start the Tkinter main loop
root.mainloop()
