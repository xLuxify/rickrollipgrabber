from tkinter import *
import webbrowser

root = Tk()
root.geometry("450x250")
root.configure(bg="white")
root.title("LiteBolt IP Grabber v1")

new = 1
url = "http://bit.ly/liteboltus"

def openweb():
    webbrowser.open(url,new=new)

greeting = Label(text="LiteBolt IP Grabber v1")
greeting.pack()

Username = Label(text="Enter TikTok Username Below")
Username.pack()

text = Entry()
text.pack()


Btn = Button(root, text = "Grab IP Address",command=openweb)
Btn.pack()

CopyrightText = Label(text="All rights reserved. Use without permission will not go unnoticed.") 
CopyrightText.pack()

CopyrightPanel = Label(text="The credits of our product can be produced from our social medias.") 
CopyrightPanel.pack()

Copyright = Label(text="Any parts of our services are not allowed to be reproduced in any form.")
Copyright.pack()

Copyright = Label(text="For business inquiries, or other questions, please contact us below.")
Copyright.pack()

Copyright = Label(text="Contact us - liteboltus@yahoo.com")
Copyright.pack()

Copyright = Label(text="Copyright LiteBolt 2020 ©")
Copyright.pack()
 
root.mainloop()
