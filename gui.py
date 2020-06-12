from tkinter import Tk, Label,CENTER,Entry,Button
import LUCIFER

class Gui:
 
   
   def __init__(self,master):
      self.master = master
      #Configuring the gui Window
      
      self.master.resizable(0,0)
      self.master.geometry("700x450")
      self.master.configure(bg="White")

      #Adding the titile
      self.title =  self.master.title("LUCIFER")

      #Adding the header text
      self.lable =  Label(self.master,text="LUCIFER")
      self.lable.config(anchor=CENTER,fg="White",bg="turquoise2",padx=700,pady=20,font=("",25))
      self.lable.pack()
      self.lable =  Label(self.master,text="")
      self.lable.config(anchor=CENTER,fg="White",bg="turquoise2",padx=700,pady=20,font=("",12))
      self.lable.pack()
      

      self.message= Entry(self.master,width=80)
      self.message.pack()
      self.lable =  Label(self.master,text="")
      self.lable.config(anchor=CENTER,fg="White",bg="White",padx=700,pady=30,font=("",12))
      self.lable.pack()

   

      #Adding the button
      self.Order= Button(self.master,text="COMMAND",command=self.send)
      self.Order.pack()

      LUCIFER.wishMe()

      
   #Calling the lucifer program
   def send(self):
      text = self.message.get()
      
      LUCIFER.takeCommand(text)
      
      
 #main function for      
if __name__=='__main__':

      window = Tk()
      Gui(window)
      
      window.mainloop()
