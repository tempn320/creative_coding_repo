import tkinter as tk
import random

### GRID ###

root = tk.Tk()
root.title("laptop home")
root.geometry("2500x1500")

# menus

menu_1 = tk.Button(root, text="apple")
menu_1.grid(row=0, column=0, sticky ="nsew")

menu_2 = tk.Button(root, text="finder")
menu_2.grid(row=0, column=1, sticky ="nsew")

menu_3 = tk.Button(root, text="file")
menu_3.grid(row=0, column=2, sticky ="nsew")

menu_4 = tk.Button(root, text="edit")
menu_4.grid(row=0, column=3, sticky ="nsew")

menu_5 = tk.Button(root, text="view")
menu_5.grid(row=0, column=4, sticky ="nsew")

menu_6 = tk.Button(root, text="go")
menu_6.grid(row=0, column=5, sticky ="nsew")

menu_7 = tk.Button(root, text="window")
menu_7.grid(row=0, column=6, sticky ="nsew")

menu_8 = tk.Button(root, text="help")
menu_8.grid(row=0, column=7, sticky ="nsew")

# sticky notes

sticky_1 = tk.Button(root, text="sticky note 1")
sticky_1.grid(row=1, column=0, columnspan=3, rowspan=2, sticky ="nsew")

sticky_2 = tk.Button(root, text="sticky note 2")
sticky_2.grid(row=3, column=0, columnspan=3, rowspan=2, sticky="nsew")

sticky_3 = tk.Button(root, text="sticky note 3")
sticky_3.grid(row=1, column=13, sticky="nsew")

sticky_4 = tk.Button(root, text="sticky note 4")
sticky_4.grid(row=2, column=13, sticky="nsew")

sticky_5 = tk.Button(root, text="sticky note 5")
sticky_5.grid(row=3, column=13, sticky="nsew")

# folders

folder_05 = tk.Button(root, text="methods1 folder")
folder_05.grid(row=4, column=13, sticky ="nsew")

folder_15 = tk.Button(root, text="parsons yr1 folder")
folder_15.grid(row=5, column=13, sticky="nsew")

folder_25 = tk.Button(root, text="parsons yr2 folder")
folder_25.grid(row=6, column=13, sticky="nsew")

folder_35 = tk.Button(root, text="parsons sem4 folder")
folder_35.grid(row=7, column=13, sticky="nsew")

folder_45 = tk.Button(root, text="past academics folder")
folder_45.grid(row=8, column=13, sticky="nsew")

folder_55 = tk.Button(root, text="media folder")
folder_55.grid(row=9, column=13, sticky="nsew")

folder_65 = tk.Button(root, text="projects folder")
folder_65.grid(row=10, column=13, sticky="nsew")

# apps

app_0 = tk.Button(root, text="finder")
app_0.grid(row=13, column=0, sticky="nsew")

app_1 = tk.Button(root, text="launchpad")
app_1.grid(row=13, column=1, sticky="nsew")

app_2 = tk.Button(root, text="safari")
app_2.grid(row=13, column=2, sticky="nsew")

app_3 = tk.Button(root, text="chrome")
app_3.grid(row=13, column=3, sticky="nsew")

app_4 = tk.Button(root, text="ical")
app_4.grid(row=13, column=4, sticky="nsew")

app_5 = tk.Button(root, text="notes")
app_5.grid(row=13, column=5, sticky="nsew")

app_6 = tk.Button(root, text="photos")
app_6.grid(row=13, column=6, sticky="nsew")

app_7 = tk.Button(root, text="facetime")
app_7.grid(row=13, column=7, sticky="nsew")

app_8 = tk.Button(root, text="messages")
app_8.grid(row=13, column=8, sticky="nsew")

app_9 = tk.Button(root, text="news")
app_9.grid(row=13, column=9, sticky="nsew")

app_10 = tk.Button(root, text="app store")
app_10.grid(row=13, column=10, sticky="nsew")

app_11 = tk.Button(root, text="settings")
app_11.grid(row=13, column=11, sticky="nsew")

# icons

icon_1 = tk.Button(root, text="downloads")
icon_1.grid(row=13, column=12, sticky="nsew")

icon_2 = tk.Button(root, text="trash")
icon_2.grid(row=13, column=13, sticky="nsew")





for i in range(13):
    root.rowconfigure(i, weight=1) # weight=1 lets the cells stretch if the window resizes
    root.columnconfigure(i, weight=1)

root.mainloop()