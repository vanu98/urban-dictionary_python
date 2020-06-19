import requests
from tkinter import *

HEIGHT = 1000
WIDTH = 1000

def formatting(slang):
	meaning = slang['list'][0]['definition']
	examp= slang['list'][0]['example']
	
	output = '%s \n %s ' % (meaning, examp)
	return output
def get_slang():
	url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

	querystring = {"term":entry.get()}

	headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "05f972929bmshb7a19c5df621e95p14b3d1jsnb983f39d4b82"
    }


	response = requests.request("GET", url, headers=headers, params=querystring)
	slang = response.json()
	label['text'] = formatting(slang)


root = Tk()

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = PhotoImage(file='urban.png')
background_label = Label(root, image=background_image)
background_label.place(relx=0, rely=0)

frame = Frame(root, bg='#0066ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Meaning?", font=40, command=get_slang)
button.place(relx=0.7,relheight=1, relwidth=0.3)

lower_frame = Frame(root, bg='#0066ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame,font=("arial", 10))
label.place(relwidth=1, relheight=1)

root.mainloop()