import json
import tkinter as tk
from tkinter import Tk, Button,Label,Scrollbar,Listbox,StringVar,Entry,W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox
import sys
import datetime

'''
Designed a software to access an external serialized Cars database with a single table stored in JSON file
[RegNo][Make][EngineSize],DateRegistered,[RentalPerDay][Available]
'''

root = Tk()
today = datetime.date.today().strftime('%B %d,%Y')
root.title('Vehicle Details - Date: '+ today)


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

def cal_total_records():

        #read the json file in python datastructure that is list
        with open('datafile3.json', 'r') as file3:
            expected_data1 = json.load(file3)


        #then chcek length of the list that is total number of items in list
        total_records = len(expected_data1)


        return total_records




def current_records(current_record_ind):


    Record_label = Button(root,text=f"{current_record_ind}   of   {cal_total_records()} ",bg='white',font=("TkDefaultFont", 10),width=20,command='')
    Record_label.grid(row=8,column=1,sticky= W)

    return current_record_ind

#side buttons
def update():#worked
    #fetch updated curent values in the entry widgets
    #new_data = [RegNo_text.get(),Make_text.get(),Engine_text.get(),Date_text.get(),Rental_text.get(),Avaiable_text.get()]

    try:

       new_data = {'RegNo':RegNo_text.get(),'Make':Make_text.get(),'EngineSize':Engine_text.get(),'DateRegistered':Date_text.get(),'RentalPerDay':Rental_text.get(),'Available':Avaiable_text.get() }

       if RegNo_text.get() == '' :
               raise Exception('zero-length entry is not allowed')

       elif Make_text.get()=='':
               raise Exception('zero-length entry is not allowed')

       elif Engine_text.get()=='':
               raise Exception('zero-length entry is not allowed')

       elif Date_text.get()=='':
                raise Exception('zero-length entry is not allowed')
       elif Rental_text.get()=='':
                raise Exception('zero-length entry is not allowed')

       elif Avaiable_text.get()=='':
                raise Exception('zero-length entry is not allowed')




       #read the file in python datastructure
       with open('datafile3.json', 'r') as file3:
           expected_data1 = json.load(file3)

       #print(expected_data1)


       for row in expected_data1:
             index_num = expected_data1.index((row))
             for m in row:
                 row[m] = str(row[m])


       #print(expected_data1)

       #this function avoids updating registration number
       count = 0
       for m in expected_data1:
            if m['RegNo'] == new_data['RegNo']:
                ind = expected_data1.index((m))
                print(ind)
                count = count + 1
                print('count',count)

       if count == 0:

                 messagebox.showinfo(title = 'Car Database',message='RegNo information cannot be updated')
                 Cancel()

                 ''' L = [RegNo_entry,Make_entry,Engine_entry,Date_entry,Rental_entry,Avaiable_entry]
                 #read the file in python datastructure
                 with open('datafile3.json', 'r') as file3:
                      expected_data1 = json.load(file3)

                 #now insering orignal values in entry widgets
                 q = 0
                 for t in expected_data1:
                     for g in t:
                         L[q].delete(0,'end')
                         L[q].insert('end',t[g] )
                         q = q + 1'''

                 return



       r = 0
       for j in expected_data1:

            for k in j:
                if j[k] == new_data[k]:
                    print('yes')
                    print(j)
                    print()

                    for i in j:
                       if j[i] == new_data[i]:

                          continue


                       else:
                          print(i)
                          print(r)
                          j[i] = new_data[i]


                          del expected_data1[r]
                          #expected_data1.append(j)
                          expected_data1.insert(r,j)

                          print(expected_data1)

                          #open the JSON file for writing
                          with open('datafile3.json','w') as file2:
                             json.dump(expected_data1,file2)


                          messagebox.showinfo(title = 'Car Database',message='information has been updated')
                          return

                else:

                   r = r + 1
                   break

    except Exception as e:
                         messagebox.showinfo(title= 'Car Database' ,message=str(e))





#open existing JSON file for reading
def Add(new_data): #inpiut new_data as dictionary


    with open('datafile3.json', 'r') as file3:
          expected_data1 = json.load(file3)


    #print(expected_data1)
    #print(type(expected_data1))

   #Modify existing_data object by adding required fields
    #new_data = {'RegNo':23,'Make':'fg','EngineSize':76,'DateRegistered':'20223-01-01','Rental':10,'Available':1 }

    expected_data1.append(new_data)
    #print(expected_data1)

    #open the JSON file for writing
    with open('datafile3.json','w') as file2:
          json.dump(expected_data1,file2)

    messagebox.showinfo(title = 'Car Database',message='new car has been added')


#Function to be called when click add button
def add_record():  #worked

    global current_record_ind
    #RegNo_text.get(), Make_text.get(), Engine_text.get(), Date_text.get(), Rental_text.get(),Avaiable_text.get()

    if RegNo_text.get() == '':
        return messagebox.showinfo(title = 'Car Database',message='entry cannot be empty')

    elif Make_text.get()== '':
         return messagebox.showinfo(title = 'Car Database',message='entry cannot be empty')


    elif Engine_text.get() == '':
         return messagebox.showinfo(title = 'Car Database',message='entry cannot be empty')

    elif Date_text.get() == '':
         return messagebox.showinfo(title = 'Car Database',message='entry cannot be empty')

    elif Rental_text.get() == '':
         return messagebox.showinfo(title = 'Car Database',message='entry cannot be empty')

    elif Avaiable_text.get() == '':

         return messagebox.showinfo(title = 'Car Database',message='entry cannot be empty')



    new_data = {}
    l = ['RegNo','Make','EngineSize','DateRegistered','RentalPerDay','Available']
    m = [RegNo_text.get(),Make_text.get(),Engine_text.get(),Date_text.get(),Rental_text.get(),Avaiable_text.get()]
    for i in range (6):
         new_data[l[i]] = m[i]


    print(new_data)
    Add(new_data)
    Cancel()

    RegNo_entry.delete(0,"end") #clear input after inserting
    Make_entry.delete(0,"end")
    Engine_entry.delete(0,"end")
    Date_entry.delete(0,"end")
    Rental_entry.delete(0,"end")
    Avaiable_entry.delete(0,"end")

    Last()


def Delete():#worked
    #read file and change into python list
    with open('datafile3.json', 'r') as file3:
          expected_data1 = json.load(file3)
          #print(expected_data1)


    #read all current values from entry widgets
    k = {'RegNo':RegNo_entry.get(),'Make':Make_entry.get(),'EngineSize':Engine_entry.get(),'DateRegistered':Date_entry.get(),
    'RentalPerDay':Rental_entry.get(),'Available':Avaiable_entry.get()}
    #print(k)

    L = [RegNo_entry,Make_entry,Engine_entry,Date_entry,Rental_entry,Avaiable_entry]

    for row in expected_data1:
        index_num = expected_data1.index((row))
        for m in row:
            row[m] = str(row[m])

        expected_data1[index_num] = row
        #print(row)

        if k == row:
             #remove row from list
             expected_data1.remove(row)
             #print(expected_data1)

             r = 0
             for a in row:
                 L[r].delete(0,'end')

                 r = r + 1

             #open the JSON file for writing
             with open('datafile3.json','w') as file2:
                   json.dump(expected_data1,file2)

             Cancel()
             break





def Cancel():

    global current_record_ind


    #RegNo_text.get()
    RegNo_entry.delete(0,"end") #clear input after inserting
    #Make_text.get()
    Make_entry.delete(0,"end")
    #Engine_text.get()
    Engine_entry.delete(0,"end")
    #Date_text.get()
    Date_entry.delete(0,"end")
    #Rental_text.get()
    Rental_entry.delete(0,"end")
    #Avaiable_text.get()
    Avaiable_entry.delete(0,"end")

    current_record_ind = 0
    current_records(current_record_ind)


def Exit():
    root.destroy()



#Bottom buttons
def First(): #worked
    global current_record_ind
    current_record_ind = 1
    current_records(current_record_ind)


    #RegNo_text.get()
    RegNo_entry.delete(0,"end") #clear input after inserting
    #Make_text.get()
    Make_entry.delete(0,"end")
    #Engine_text.get()
    Engine_entry.delete(0,"end")
    #Date_text.get()
    Date_entry.delete(0,"end")
    #Rental_text.get()
    Rental_entry.delete(0,"end")
    #Avaiable_text.get()
    Avaiable_entry.delete(0,"end")


    i = 0
    #read existing json file and load in python datastructure
    with open('datafile3.json', 'r') as file3:
          expected_data1 = json.load(file3)

    #print(expected_data1)
    #output is list

    L = [RegNo_entry,Make_entry,Engine_entry,Date_entry,Rental_entry,Avaiable_entry]
    l = ['RegNo','Make','EngineSize','DateRegistered','RentalPerDay','Available']

    for j in expected_data1: #j is dictionary
        if i < 1:
           for i in range(len(L)):
              L[i].delete(0,'end')
              L[i].insert('end',j[l[i]] )


           i = i + 1

        else:
            break




def Previous():#worked
     global current_record_ind

     #read current values from entry widgets
     k = {'RegNo':RegNo_entry.get(),'Make':Make_entry.get(),'EngineSize':Engine_entry.get(),'DateRegistered':Date_entry.get(),
     'RentalPerDay':Rental_entry.get(),'Available':Avaiable_entry.get()}

     #if values are empty then no action

     L = [RegNo_entry,Make_entry,Engine_entry,Date_entry,Rental_entry,Avaiable_entry]

     #read existing json file and load in python datastructure list
     with open('datafile3.json', 'r') as file3:
           expected_data1 = json.load(file3)

     #loop to check if entry read rom widgets is equal to entry in given list

     for row in expected_data1:
         index_num = expected_data1.index((row))

         #change all values in string
         for m in row:
            row[m] = str(row[m])

         if k == row:
            if index_num == 0:

                messagebox.showinfo(title='Car Database', message='This is first record')
                break

            row = expected_data1[index_num -1]

            r = 0
            for a in row:
                 L[r].delete(0,'end')
                 L[r].insert('end', row[a])

                 r = r + 1

                #print(current_record_ind)
            current_record_ind = current_record_ind -1
            current_records(current_record_ind)
            break




def Next(): #worked

    global current_record_ind
    #read current record in entry widgets

    k = {'RegNo':RegNo_entry.get(),'Make':Make_entry.get(),'EngineSize':Engine_entry.get(),'DateRegistered':Date_entry.get(),
    'RentalPerDay':Rental_entry.get(),'Available':Avaiable_entry.get()}

    L = [RegNo_entry,Make_entry,Engine_entry,Date_entry,Rental_entry,Avaiable_entry]

    #print('value of k',k)
    #print(type(k))


    #read existing json file and load in python datastructure list
    with open('datafile3.json', 'r') as file3:
          expected_data1 = json.load(file3)

    #print(expected_data1)
    #output is list

    #print(type(expected_data1))

    for row in expected_data1:

        '''row = {'RegNo': '871D12345', 'Make': 'Hypo Car', 'EngineSize': '16000', 'DateRegistered': '1970-02-24', 'RentalPerDay': 20.5, 'Available': 1}'''
        index_num = expected_data1.index((row))
        #print(index_num)

        for m in row:
            row[m] = str(row[m])



        #print('row value',row)
        #print(type(row))

        #updating entry widgets by taking values of next record in list expected_data1

        if k == row:

             if index_num == (len(expected_data1)-1):

                messagebox.showinfo(title='Car Database', message='This is last record')
                break

             row = expected_data1[index_num + 1]

             r = 0
             for a in row:
                 L[r].delete(0,'end')
                 L[r].insert('end', row[a])

                 r = r + 1

             current_record_ind = current_record_ind + 1
             current_records(current_record_ind)

             break







def Last():#worked

    global current_record_ind



    #read existing json file and load in python datastructure list
    with open('datafile3.json', 'r') as file3:
          expected_data1 = json.load(file3)

    #print(expected_data1)
    #print(type(expected_data1))

    expected_data1.reverse()
    #print('reverse',expected_data1)

    L = [RegNo_entry,Make_entry,Engine_entry,Date_entry,Rental_entry,Avaiable_entry]
    r = 0
    for row in expected_data1:
         for a in row:
             L[r].delete(0,'end')
             L[r].insert('end', row[a])
             r = r + 1

         current_record_ind = cal_total_records()
         current_records(current_record_ind)

         break




def search():
    N = cal_total_records()



    def run():
            if ((combobox1.get()== 'Available' or 'RegNo' or 'Make' or 'EngineSize' or 'DateRegistered' or 'RentalPerDay')
               and combobox2.get()== '=' and combobox3.get()== 'Yes') :

               #read existing json file and load in python datastructure list
               with open('datafile3.json', 'r') as file3:
                   expected_data1 = json.load(file3)
                   print(expected_data1)

               r = 1
               c = 0

               for i in expected_data1:
                    c = 0
                    print(i)
                    print()

                    for j in i:
                       if j != 'Available':
                          continue

                       else:

                              if i[j] == '0':
                                 r = 0
                                 break


                              else:
                                   for j in i:
                                       print(i)
                                       print(j)

                                       label = ttk.Label(table, text=i[j], style="Table.TLabel", borderwidth=1, relief="solid", width=15)
                                       label.grid(row= r  , column=c)#, padx=1, pady=1)

                                       c = c + 1
                                       print(c)

                    r = r + 1



    def close():
        window.destroy()


    # Create the main window
    window = tk.Tk()
    window.title("Search Form")
    window.geometry("800x400")
    window.resizable(width=False,height=False)

    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=1)
    window.grid_rowconfigure(5, weight=1)

    window.grid_columnconfigure(0,weight=1)
    window.grid_columnconfigure(1,weight=1)
    window.grid_columnconfigure(2,weight=1)
    window.grid_columnconfigure(3,weight=1)
    window.grid_columnconfigure(4,weight=1)
    window.grid_columnconfigure(5,weight=1)
    window.grid_columnconfigure(6,weight=1)
    window.grid_columnconfigure(7,weight=1)
    window.grid_columnconfigure(8,weight=1)

    # Create labels
    Field_label = ttk.Label(window,text='Field',background='',font=("TkDefaultFont", 12))
    Field_label.grid(row=0,column=1,sticky=W,padx=20)

    option1 = ['Available']
    option4= ['VechicleRegNo']
    option5=['Make']
    option6=['EngineSize']
    option7=['DateRegistered']
    option8=['RentalPerDay']


    options = [option1,option4,option5,option6,option7,option8]


    #selected_value1 = tk.StringVar()
    combobox1 = ttk.Combobox(window,values=options)#,option4,option5,option6,option7,option8)
    combobox1.config(width=15)
    combobox1.grid(row=1,column=1,sticky=W,padx=20)
    combobox1.set('Select an option')

    operator_label = ttk.Label(window,text='Operator',background='',font=("TkDefaultFont", 12))
    operator_label.grid(row=0,column=2,sticky=W,padx=20)

    option2 = ['=']

    #selected_value2 = tk.StringVar()
    combobox2 = ttk.Combobox(window,values=option2)
    combobox2.config(width=15)
    combobox2.grid(row=1,column=2,sticky=W,padx=20)
    combobox2.set('Select an option')

    Value_label = ttk.Label(window,text='Value',background='',font=("TkDefaultFont", 12))
    Value_label.grid(row=0,column=3,sticky=W,padx=20)

    option3 = ['Yes']

    #selected_value3 = tk.StringVar()
    combobox3 = ttk.Combobox(window,values=option3)
    combobox3.config(width=15)
    combobox3.grid(row=1,column=3,sticky=W,padx=20)
    combobox3.set('Select an option')

    # Create buttons
    Run_btn = Button(window, text="Run",bg='light grey',font=("TkDefaultFont", 10),width=10,command = run)
    Run_btn.grid(row=0, column=4)

    Close_btn = Button(window, text="Close",bg='light grey',font=("TkDefaultFont", 10),width=10,command=close)
    Close_btn.grid(row=1, column=4)

    # Create a frame for the table
    table_frame = ttk.Frame(window)
    table_frame.grid(row=4, column=1, columnspan=6,sticky=W,padx=20)

    # Create a canvas widget
    canvas = tk.Canvas(table_frame, background="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    desired_table_width = 550
    canvas.config(width=desired_table_width)

    # Create a scrollbar for the vertical direction
    y_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=canvas.yview)
    y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a scrollbar for the horizontal direction
    x_scrollbar = ttk.Scrollbar(window, orient=tk.HORIZONTAL, command=canvas.xview)
    x_scrollbar.grid(row=5, column=1, columnspan=3 ,sticky="we")

    # Configure the canvas to use the scrollbars
    canvas.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

    # Create a frame within the canvas to hold the table
    table = ttk.Frame(canvas, style="Table.TFrame", borderwidth=0)

    # Add content to the table
    for i in range(N+20):
        for j in range(6):

           if  i ==0 and j==0:
               label = ttk.Label(table, text=f"VechicleRegNo", style="Table.TLabel", borderwidth=1, relief="solid", width=15)
               label.grid(row=i, column=j)#, padx=1, pady=1)

           elif i==0 and j==1:
               label = ttk.Label(table, text=f"Make", borderwidth=1, relief="solid", width=15)
               label.grid(row=i, column=j)#, padx=1, pady=1)

           elif i==0 and j==2:
               label = ttk.Label(table, text=f"Engine Size", style="Table.TLabel", borderwidth=1, relief="solid", width=15)
               label.grid(row=i, column=j)#, padx=1, pady=1)


           elif i==0 and j==3:
               label = ttk.Label(table, text=f"Date Registered", style="Table.TLabel", borderwidth=1, relief="solid", width=15)
               label.grid(row=i, column=j)#, padx=1, pady=1)


           elif i==0 and j==4:
               label = ttk.Label(table, text=f"Rental Per Day", style="Table.TLabel", borderwidth=1, relief="solid", width=15)
               label.grid(row=i, column=j)#, padx=1, pady=1)

           elif i==0 and j==5:
               label = ttk.Label(table, text=f"Available", style="Table.TLabel", borderwidth=1, relief="solid", width=15)
               label.grid(row=i, column=j)#, padx=1, pady=1)



           else:
               #if combobox1.get()== 'Available'and combobox2.get()== '=' and combobox3.get()== '1' :

               label = ttk.Label(table, text=f"", style="Table.TLabel", borderwidth=1, relief="solid", width=15)
               label.grid(row=i, column=j)#, padx=1, pady=1)



    # Add the table to the canvas
    canvas.create_window((0, 0), window=table, anchor=tk.NW)

    # Update the scrollable region of the canvas
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    # Configure the scrollable region of the canvas
    canvas.bind("<Configure>", update_scroll_region)

    # Update the canvas view when the scrollbars are moved
    def update_scrollbars(*args):
       canvas.xview_moveto(x_scrollbar.get()[0])
       canvas.yview_moveto(y_scrollbar.get()[0])

    x_scrollbar.config(command=canvas.xview)
    y_scrollbar.config(command=canvas.yview)

    # Start the Tkinter event loop
    window.mainloop()



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
View_First_btn = Button(root, text="First",bg='light grey',font=("TkDefaultFont", 10),width=10,command=First)
View_First_btn.grid(row=8, column=0,padx=20,sticky=W)

Previous_View_First_btn = Button(root, text="Previous",bg='light grey',font=("TkDefaultFont", 10),width=10,command=Previous)
Previous_View_First_btn.grid(row=8,column=0,padx=100,sticky=E)

#current_record = 1 #current record is always 1

#Record_label = Button(root,text=f"{current_record}   of   {db.cal_total_records()} ",bg='white',font=("TkDefaultFont", 10),width=20,command='')
#Record_label.grid(row=8,column=1,sticky= W)

Next_View_btn = Button(root, text="Next",bg='light grey',font=("TkDefaultFont", 10),width=10,command=Next)
Next_View_btn.grid(row=8, column=2,sticky= W)

Later_View_btn = Button(root, text="Last",bg='light grey',font=("TkDefaultFont", 10),width=10,command=Last)
Later_View_btn.grid(row=8, column=2,padx=50,sticky= E)

#SIDE buttons
update_btn = Button(root, text="Update",bg='light grey',font=("TkDefaultFont", 10),width=24,command=update)
update_btn.grid(row=1, column=2,sticky=W)

Add_btn = Button(root, text="Add",bg="light grey",font=("TkDefaultFont", 10),width=24,command=add_record)
Add_btn.grid(row=2, column=2,sticky=W)

Delete_btn = Button(root, text="Delete",bg="light grey",font=("TkDefaultFont", 10),width=24,command=Delete)
Delete_btn.grid(row=3, column=2,sticky=W)

Search_btn = Button(root, text="Search",bg="light grey",font=("TkDefaultFont", 10),width=24,command=search)
Search_btn.grid(row=4, column=2,sticky=W)

Cancel_btn = Button(root, text="Cancel",bg="light grey",font=("TkDefaultFont", 10),width=24,command=Cancel)
Cancel_btn.grid(row=5, column=2,sticky=W)

Exit_btn = Button(root, text="Exit",bg="light grey",font=("TkDefaultFont", 10),width=24,command=Exit)
Exit_btn.grid(row=6, column=2,sticky=W)

First()

root.mainloop()













