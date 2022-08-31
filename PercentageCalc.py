# import tkinter
# tkinter is the standard Python interface and GUI library
from calendar import month
import tkinter as tk

# import messagebox module from tkinter library
from tkinter import messagebox

# impirt datetime to utilize for time stamps
from datetime import datetime

# Declare a new object and assign as a tk() object
frmPercentage = tk.Tk()

#
#	Create Window
#

# Adjust the display settings of the main window
frmPercentage.geometry("800x500")
frmPercentage.title("Academy IT Consulting Services - Case Percentage Calculator")
frmPercentage.configure(background="#002060")

#
#	Create labels for fields
#

# Create label for user name
lblUserName = tk.Label(frmPercentage, text="User Name:", width=20, height=2, bg="#FFC000")
lblUserName.place(x=175, y=60)
# Create label for total cases assigned
lblTtlCases = tk.Label(frmPercentage, text="Total Cases:", width=20, height=2, bg="#FFC000")
lblTtlCases.place(x=175, y=130)
# Create label for finished cases
lblFinCases = tk.Label(frmPercentage, text="Cases Completed/Closed:", width=20, height=2, bg="#FFC000")
lblFinCases.place(x=175, y=200)
# Create label for calculated percentage
lblPercentage = tk.Label(frmPercentage, text="Completion:", width=20, height=2, bg="#FFC000")
lblPercentage.place(x=175, y=270)

#
#	Text Entry Fields
#

# function to validate entry input is numerical characters only
def CheckInt(input):
	if input.isdigit():
		return True
	elif input == "":
		return True
	else:
		return False

# Load the validate number function into the tk instance
validnum = frmPercentage.register(CheckInt)

# Create a text entry box for entering user name
tbxUserName = tk.Entry(frmPercentage, bg="white")
tbxUserName.place(x=375, y=60, width=250, height=35)
# Create a text entry box for entering total cases
tbxTtlCases = tk.Entry(frmPercentage, bg="white")
tbxTtlCases.place(x=375, y=130, width=250, height=35)
# Hook the validate number function to the entry text field
tbxTtlCases.config(validate = "key", validatecommand = (validnum, '%P'))
# Create a text entry box for entering the finished cases
tbxFinCases = tk.Entry(frmPercentage, bg="white")
tbxFinCases.place(x=375, y=200, width=250, height=35)
# Hook the validate number function to the entry text field
tbxFinCases.config(validate = "key", validatecommand = (validnum, '%P'))
# Create label for the Percentage calculation and position on form
lblPercentage2 = tk.Label(frmPercentage, text="", width=35, height=2, bg="white")
lblPercentage2.place(x=375, y=270)


#
#	Buttons
#

# Declare float for percentage calculation
fltPercentage = float
fltPercentageStr = ""


# General function to check if all fields contain data
def CheckData():
	if tbxUserName.get() == "":
		messagebox.showinfo("Missing Information", "User name must be entered")
		return False
	elif tbxTtlCases.get() == "":
		messagebox.showinfo("Missing Information", "Total number of cases must be entered")
		return False
	elif tbxFinCases.get() == "":
		messagebox.showinfo("Missing Information", "Number of finished cases must be entered")
		return False
	else:
		return True

def GetPercentage():
	global fltPercentageStr
	# Check that all entry boxes have a value, if blank inform user entry box is blank
	if CheckData() == True:
		# Get the percentage of total cases vs. finished cases
		intMaxNum = (tbxTtlCases.get())
		intNumAch = (tbxFinCases.get())
		fltPercentage = int(intNumAch)/int(intMaxNum)*100
		fltPercentageStr = "{:0.2f}%".format(fltPercentage)
		# display in label percentage
		# String converts fltPercentage to use a float with precision of two decimal places
		lblPercentage2 = tk.Label(frmPercentage, text=fltPercentageStr, width=35, height=2, bg="white")
		lblPercentage2.place(x=375, y=270)

# Add a button to perform the calculate function to display the percentage of completion 
cmdCalculate = tk.Button(frmPercentage, text="Calculate", width=8, bg="light grey", fg="black", command=GetPercentage)
# Place command button using x, y plotter
cmdCalculate.place(x=375, y=325)

def SaveToTxt():
	global fltPercentageStr
	print(fltPercentageStr)
	if CheckData() == True:
		if fltPercentageStr == "":
			messagebox.showinfo("Missing Information", "Percentage must be calculated first")
		else:
			ts = datetime.now()
			targetFileName = tbxUserName.get() + ".txt"
			outputfile = open(targetFileName, 'a')
			outputfile.write("%s/%s/%s : %s.%s - User: %s, Total Cases: %s, Finished Cases: %s, Completion Percentage: %s \n" % (ts.year, ts.month, ts.day, ts.hour, ts.minute, tbxUserName.get(), tbxTtlCases.get(), tbxFinCases.get(), fltPercentageStr))
			outputfile.close()

SaveTxt = tk.Button(frmPercentage, text="Save to File", width=8, bg="light grey", fg="black", command=SaveToTxt)
SaveTxt.place(x=375, y=365)

# Function to clear all existing data in text entry fields
def ClearForm():
	global fltPercentageStr
	tbxUserName.delete(0, 'end')
	tbxTtlCases.delete(0, 'end')
	tbxFinCases.delete(0, 'end')
	lblPercentage2 = tk.Label(frmPercentage, text="", width=35, height=2, bg="white")
	fltPercentageStr = ""
	lblPercentage2.place(x=375, y=270)
# Add a calculate pecentage command button, background colour light grey, foreground colour black
cmdClear = tk.Button(frmPercentage, text="Clear", width=8, bg="light grey", fg="black", command=ClearForm)
# Place command button using x, y plotter
cmdClear.place(x=375, y=450)

#
#	Main Program loop
#

# mainloop runs the event for the graphical user interface
frmPercentage.mainloop()
