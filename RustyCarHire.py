import tkinter as tk
from tkinter import Tk, Button,Label,Scrollbar,Listbox,StringVar,Entry,W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox
from SQLserverconfig import dbconfig
import datetime
import pypyodbc as py
from SQLserverconfig import dbconfig

'''
[RegNo][Make][EngineSize],DateRegistered,[RentalPerDay][Available]'''

con = py.connect(**dbconfig)

#print(con)

cursor = con.cursor()



class rustycarhiredb:
      def __init__(self):
         self.con = py.connect(**dbconfig)
         self.cursor = con.cursor()
         print('you have connected to the database')
         print(con)

      def __del__(self):
            self.con.close()
            print('Database connection closed')

      def insert(self,RegNo,Make,EngineSize,DateRegistered,RentalPerDay,Available):#worked
         try:
            sql = "INSERT INTO Cars (RegNo,Make,EngineSize,DateRegistered,RentalPerDay,Available)VALUES (?,?,?,?,?,?)"
            values = [RegNo,Make,EngineSize,DateRegistered,RentalPerDay,Available]
            self.cursor.execute(sql,values)
            self.con.commit()
            messagebox.showinfo(title = 'Car Database',message='new car has been added')

            #if messagebox.askokcancel("Quit","Do you want to quit"):


         except Exception as e:

                     messagebox.showinfo(title = 'Car Database',message=str(e))


      def update(self,Make,EngineSize,DateRegistered,RentalPerDay,Available,RegNo):#worked
         tsql = 'UPDATE Cars SET Make=?,EngineSize=?,DateRegistered=?,RentalPerDay=?,Available=? WHERE RegNo=?'
         self.cursor.execute(tsql,[Make,EngineSize,DateRegistered,RentalPerDay,Available,RegNo])
         self.con.commit()
         messagebox.showinfo(title='show car database',message='Car Database Updated')

      def delete (self,RegNo):#worked

        try:
            if RegNo == '':
               messagebox.showinfo(title='Car Database',message='RegNo cannot be empty')

            else:
               delquery= 'DELETE FROM Cars WHERE RegNo=?'
               self.cursor.execute(delquery,[RegNo])
               self.con.commit()
               messagebox.showinfo(title='Car Database',message='car entry has been deleted')

        except Exception as e:
                             messagebox.showinfo(title = 'Car Database',message=str(e))


      def view (self):
        sql = "SELECT * FROM Cars"
        self.cursor.execute(sql)
        rows=self.cursor.fetchall()
        return rows

      def cal_total_records(self):

         sql_query = 'SELECT COUNT(*) FROM Cars'
         self.cursor.execute(sql_query)
         total_records = self.cursor.fetchone()[0]


         return total_records



db = rustycarhiredb()
#print(db.view())

def current_records(current_record_ind):


    Record_label = Button(root,text=f"{current_record_ind}   of   {db.cal_total_records()} ",bg='white',font=("TkDefaultFont", 10),width=20,command='')
    Record_label.grid(row=8,column=1,sticky= W)

    return current_record_ind




def add_btn():#worked
    global current_record_ind

    db.insert(RegNo_text.get(), Make_text.get(), Engine_text.get(), Date_text.get(), Rental_text.get(),Avaiable_text.get())

    db.cal_total_records()
    RegNo_entry.delete(0,"end") #clear input after inserting
    Make_entry.delete(0,"end")
    Engine_entry.delete(0,"end")
    Date_entry.delete(0,"end")
    Rental_entry.delete(0,"end")
    Avaiable_entry.delete(0,"end")

    Last()

    con.commit()


def update_records():#worked

    db.update( Make_text.get(), Engine_text.get(), Date_text.get(), Rental_text.get(),Avaiable_text.get(),RegNo_text.get())

    #RegNo_entry.delete(0,"end") #clear input after inserting
    #Make_entry.delete(0,"end")
    #Engine_entry.delete(0,"end")
    #Date_entry.delete(0,"end")
    #Rental_entry.delete(0,"end")
    #Avaiable_entry.delete(0,"end")
    #RegNo_text.get(), Make_text.get(), Engine_text.get(), Date_text.get(), Rental_text.get(),Avaiable_text.get()
    #RegNo_text.insert('end', RegNo_text.get())

    con.commit()




def Delete_records():#worked
    #global current_record_ind #add this line to access the global variable
    db.delete(RegNo_text.get())

    RegNo_entry.delete(0,"end")#clear the input
    Make_entry.delete(0,"end")
    Engine_entry.delete(0,"end")
    Date_entry.delete(0,"end")
    Rental_entry.delete(0,"end")
    Avaiable_entry.delete(0,"end")
    First_btn()
    con.commit()




def Cancel():
    RegNo_text.get()
    RegNo_entry.delete(0,"end") #clear input after inserting
    Make_text.get()
    Make_entry.delete(0,"end")
    Engine_text.get()
    Engine_entry.delete(0,"end")
    Date_text.get()
    Date_entry.delete(0,"end")
    Rental_text.get()
    Rental_entry.delete(0,"end")
    Avaiable_text.get()
    Avaiable_entry.delete(0,"end")

    current_record_ind = 0
    current_records(current_record_ind)




def Exit():#worked
    dd = db
    if messagebox.askokcancel("Quit","Do you want to quit"):
        root.destroy()
        del dd

def search():
    messagebox.showinfo(title = 'Car Database',message='work in progress')

#Write code for the controls to move to the first, previous, next and last records.

def First_btn(): #worked
    global current_record_ind
    current_record_ind = 1
    current_records(current_record_ind)


    i = 0

    for row in db.view():
         if i < 1:

             L = [RegNo_entry,Make_entry,Engine_entry,Date_entry,Rental_entry,Avaiable_entry]
             r = 0
             for a in row:

                  L[r].delete(0,'end')
                  L[r].insert('end',a)
                  r = r + 1


             i = i + 1

         else:
            break



def Previous_btn():
    global current_record_ind
    try:

      k = []
      l = 0
      L = [RegNo_entry,Make_entry,Engine_entry,Date_entry,Rental_entry,Avaiable_entry]
      while l< len(L):

           k.append(L[l].get())

           l = l + 1


      all_records = db.view()
      for row in all_records:
          rowlist = list(row)

          index_num = all_records.index((row))


          newrowlist = []
          for m in rowlist:
              newrowlist.append(str(m))


          if k == newrowlist:
             if index_num == 0:
                break
             else:
                 row = all_records[index_num - 1]
                 r = 0
                 for a in row:
                    L[r].delete(0,'end')
                    L[r].insert('end', a)
                    r = r + 1

                 #print(current_record_ind)
                 current_record_ind = current_record_ind -1
                 current_records(current_record_ind)

                 break

    except Exception as e:

        messagebox.showinfo(title = 'Car Database',message=str(e))


def Next_btn():
    global current_record_ind
    try:

      k = []
      l = 0
      L = [RegNo_entry,Make_entry,Engine_entry,Date_entry,Rental_entry,Avaiable_entry]
      while l< len(L):

           k.append(L[l].get())

           l = l + 1


      all_records = db.view()
      for row in all_records:
          rowlist = list(row)

          index_num = all_records.index((row))


          newrowlist = []
          for m in rowlist:
              newrowlist.append(str(m))


          if k == newrowlist:
             row = all_records[index_num + 1]
             r = 0
             for a in row:
                 L[r].delete(0,'end')
                 L[r].insert('end', a)
                 r = r + 1

             current_record_ind = current_record_ind + 1
             current_records(current_record_ind)



             break
    except Exception as e:

        messagebox.showinfo(title = 'Car Database',message= str(e))



def Last():
    global current_record_ind
    all_records = db.view()
    all_records.reverse()

    L = [RegNo_entry,Make_entry,Engine_entry,Date_entry,Rental_entry,Avaiable_entry]
    r = 0
    for row in all_records:
         for a in row:
             L[r].delete(0,'end')
             L[r].insert('end', a)
             r = r + 1
         current_record_ind = db.cal_total_records()
         current_records(current_record_ind)
         #print(current_record_ind)
         break




root = Tk()
today = datetime.date.today().strftime('%B %d,%Y')
root.title('Vechile Details - Date: '+ today)


#root.configure(background = 'sky blue')
root.geometry("900x400")
root.resizable(width=False,height=False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_rowconfigure(8, weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_columnconfigure(3,weight=1)


title_label =ttk.Label(root,text="Speedy Car Hire",background="",font=("TkDefaultFont", 22, "bold italic"))
title_label.grid(row=0, column=0, columnspan=3)

RegNo_label = ttk.Label(root,text='Vehicle Registration Number',background='',font=("TkDefaultFont", 16))
RegNo_label.grid(row= 1,column=0,sticky=W,padx=20)
RegNo_text = StringVar()
RegNo_entry = ttk.Entry(root,width=24,textvariable=RegNo_text)
RegNo_entry.grid(row=1,column=1,sticky=W)


Make_label = ttk.Label(root,text='Make',background='',font=("TkDefaultFont", 16))
Make_label.grid(row=2,column=0,sticky=W,padx=20)
Make_text = StringVar()
Make_entry = ttk.Entry(root,width=24,textvariable=Make_text)
Make_entry.grid(row=2,column=1,sticky=W)


Engine_label = ttk.Label(root,text='Engine Size',background='',font=("TkDefaultFont", 16))
Engine_label.grid(row=3,column=0,sticky=W,padx=20)
Engine_text = StringVar()
Engine_entry = ttk.Entry(root,width=24,textvariable=Engine_text)
Engine_entry.grid(row=3,column=1,sticky=W)


Date_label = ttk.Label(root,text='Date Registered',background='',font=("TkDefaultFont", 16))
Date_label.grid(row=4,column=0,sticky=W,padx=20)
Date_text = StringVar()
Date_entry = ttk.Entry(root,width=24,textvariable=Date_text)
Date_entry.grid(row=4,column=1,sticky=W)


Rental_label = ttk.Label(root,text='Rental Per Day',background='',font=("TkDefaultFont", 16))
Rental_label.grid(row=5,column=0,sticky=W,padx=20)
Rental_text = StringVar()
Rental_entry = ttk.Entry(root,width=24,textvariable=Rental_text )
Rental_entry.grid(row=5,column=1,sticky=W)


Avaiable_label = ttk.Label(root,text='Available',background='',font=("TkDefaultFont", 16))
Avaiable_label.grid(row=6,column=0,sticky=W,padx=20)
Avaiable_text = StringVar()
Avaiable_entry = ttk.Entry(root,width=4,textvariable=Avaiable_text)
Avaiable_entry.grid(row=6,column=1,sticky=W)


# Add buttons
View_First_btn = Button(root, text="First",bg='light grey',font=("TkDefaultFont", 10),width=10,command=First_btn)
View_First_btn.grid(row=8, column=0,padx=20,sticky=W)

Previous_View_First_btn = Button(root, text="Previous",bg='light grey',font=("TkDefaultFont", 10),width=10,command=Previous_btn)
Previous_View_First_btn.grid(row=8,column=0,padx=100,sticky=E)

#current_record = 1 #current record is always 1

#Record_label = Button(root,text=f"{current_record}   of   {db.cal_total_records()} ",bg='white',font=("TkDefaultFont", 10),width=20,command='')
#Record_label.grid(row=8,column=1,sticky= W)

Next_View_btn = Button(root, text="Next",bg='light grey',font=("TkDefaultFont", 10),width=10,command=Next_btn)
Next_View_btn.grid(row=8, column=2,sticky= W)

Later_View_btn = Button(root, text="Last",bg='light grey',font=("TkDefaultFont", 10),width=10,command=Last)
Later_View_btn.grid(row=8, column=2,padx=50,sticky= E)

#SIDE buttons
update_btn = Button(root, text="Update",bg='light grey',font=("TkDefaultFont", 10),width=24,command=update_records)
update_btn.grid(row=1, column=2,sticky=W)

Add_btn = Button(root, text="Add",bg="light grey",font=("TkDefaultFont", 10),width=24,command=add_btn)
Add_btn.grid(row=2, column=2,sticky=W)

Delete_btn = Button(root, text="Delete",bg="light grey",font=("TkDefaultFont", 10),width=24,command=Delete_records)
Delete_btn.grid(row=3, column=2,sticky=W)

Search_btn = Button(root, text="Search",bg="light grey",font=("TkDefaultFont", 10),width=24,command=search)
Search_btn.grid(row=4, column=2,sticky=W)

Cancel_btn = Button(root, text="Cancel",bg="light grey",font=("TkDefaultFont", 10),width=24,command=Cancel)
Cancel_btn.grid(row=5, column=2,sticky=W)

Exit_btn = Button(root, text="Exit",bg="light grey",font=("TkDefaultFont", 10),width=24,command=Exit)
Exit_btn.grid(row=6, column=2,sticky=W)

First_btn() #worked


root.mainloop()