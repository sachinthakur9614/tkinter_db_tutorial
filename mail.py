from tkinter import*
import random
import time
import sqlite3
root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")
Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)
f1 = Frame(root,width = 1000,height=700,relief=SUNKEN)

f2 = Frame(root ,width = 600,height=700,relief=SUNKEN)
# f2.pack(side=RIGHT)
menu=Menu(root)
root.config(menu=menu)

menu = Menu(root)
root.config(menu=menu)

db = sqlite3.connect('employee1.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS employee1(empid INTEGER PRIMARY KEY,name TEXT,phone TEXT,address TEXT,desig TEXT)')
db.commit()
db2 = sqlite3.connect('order_emp.db')
cursor2 = db2.cursor()
cursor2.execute('CREATE TABLE IF NOT EXISTS order_emp(id TEXT,fires TEXT,largefries TEXT,burger TEXT,Filet TEXT,subtotal TEXT,total TEXT,service_charge TEXT,drinks TEXT,tax TEXT,cost TEXT,cheese_burger TEXT)')
db2.commit()
#------------------TIME--------------

localtime=time.asctime(time.localtime(time.time()))

#-----------------INFO TOP------------

lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg="steel blue",bd=10,anchor='w')

lblinfo.grid(row=0,column=0)

lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)

lblinfo.grid(row=1,column=0)

empid =  StringVar()
name = StringVar()
desig = StringVar()
address = StringVar()
phone = StringVar()

def display():
	connt = sqlite3.connect('employee1.db')
	cursor = connt.cursor()
	cursor.execute('SELECT * FROM employee1')
	print("*************************EMPLOYEE DETAILS************************* ")
	for row in cursor.fetchall():
		
		print("Employee Id:",row[0])
		print("Employee Name:",row[1])
		print("Employee Phone:",row[2])
		print("Employee Address:",row[3])
		print("Employee Designation:",row[4])
		print("************************************************** ")
	



def remove_emp():
   empId = empid.get()
   connnt = sqlite3.connect('employee1.db')
   cursor = connnt.cursor()
   cursor.execute("DELETE FROM employee1 WHERE empid = ?",(empId,))
   connnt.commit()
   print("EMPLOYEE ID " + empId + " is successfully DELETED")




def edit_emp():

	empId= empid.get()
	name1  = name.get()
	phone1 = phone.get()
	address1 = address.get()
	desig1 = desig.get()
	connnt=sqlite3.connect('employee1.db')
	cursor = connnt.cursor()
	cursor.execute("UPDATE employee1 SET name=?,phone=?,address=?,desig=? WHERE empid = ?",(name1,phone1,address1,desig1,empId))
	connnt.commit()
	connnt.close()

	connt = sqlite3.connect('employee1.db')
	cursor = connt.cursor()
	cursor.execute('SELECT * FROM employee1 WHERE empid=?',(empId))
	print("*************************EMPLOYEE EDITED DETAILS************************* ")
	for row in cursor.fetchall():
		print("Employee Id:",row[0])
		print("Employee Name:",row[1])
		print("Employee Phone:",row[2])
		print("Employee Address:",row[3])
		print("Employee Designation:",row[4])
		print("************************************************** ")
		# print("EMPLOYEE ID " + empId + " is successfully EDITED",row)
	connt.close()


def insert_emp():
	# empId= empid.get()
	name1  = name.get()
	phone1 = phone.get()
	address1 = address.get()
	desig1 = desig.get()
	conn = sqlite3.connect('employee1.db')
	with conn:
		cursor = conn.cursor()
		cursor.execute('INSERT INTO employee1(name,phone,address,desig ) VALUES(?,?,?,?)',(name1,phone1,address1,desig1,))
		db.close()

	connt = sqlite3.connect('employee1.db')
	cursor = connt.cursor()
	# cursor.execute('SELECT * FROM employee1 WHERE empid=?',(empId))
	print("************************* NEW EMPLOYEE DETAILS************************* ")
	for row in cursor.fetchall():
		print("Employee Id:",row[0])
		print("Employee Name:",name1)
		print("Employee Phone:",phone1)
		print("Employee Address:",address1)
		print("Employee Designation:",desig1)
		print("************************************************** ")
		# print("New Employee Details Inserted ",row)
	connt.close()


def insert_order():
	x=random.randint(12980, 50876)
	randomRef = str(x)
	rand.set(randomRef)
	cof =int(Fries.get())
	colfries= float(Largefries.get())
	cob= float(Burger.get())
	cofi= float(Filet.get())
	cochee= float(Cheese_burger.get())
	codr= float(Drinks.get())
	costoffries = cof*25
	costoflargefries = colfries*40
	costofburger = cob*35
	costoffilet = cofi*50
	costofcheeseburger = cochee*50
	costofdrinks = codr*35
	costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
	PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
	Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
	Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
	Service="Rs.",str('%.2f'% Ser_Charge)
	OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
	PaidTax="Rs.",str('%.2f'% PayTax)
	Service_Charge.set(Service)
	cost.set(costofmeal)
	Tax.set(PaidTax)
	Subtotal.set(costofmeal)
	Total.set(OverAllCost)

	conn = sqlite3.connect('order_emp.db')
	with conn:
		cursor = conn.cursor()
		cursor.execute('INSERT INTO order_emp(id,fires,largefries,burger,Filet,subtotal,total,service_charge,drinks,tax,cost,cheese_burger ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(str(randomRef),str(cof),str(colfries),str(cob),str(cofi),str(cochee),str(codr),str(costofmeal),str(Service),str(PaidTax),str(costofmeal),str(OverAllCost),))
		db.close()

	roo = Tk()
	roo.geometry("600x220+0+0")
	roo.title("RECEIPT LIST")

	lblinfo = Label(roo, font=('aria', 15,'bold'), text="________________________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=0, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="BILL RECEIPT", fg="black", bd=5)

	lblinfo.grid(row=0, column=1)


	lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=0, column=2)

	lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=0, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ORDER ID", fg="black", anchor=W)

	lblinfo.grid(row=2, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=randomRef, fg="steel blue", anchor=W)

	lblinfo.grid(row=2, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="FIRES MEAL", fg="steel blue", anchor=W)

	lblinfo.grid(row=3, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=cof, fg="steel blue", anchor=W)

	lblinfo.grid(row=3, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="LUNCH MEAL", fg="steel blue", anchor=W)

	lblinfo.grid(row=4, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=colfries, fg="steel blue", anchor=W)

	lblinfo.grid(row=4, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="BURGER MEAL", fg="steel blue", anchor=W)

	lblinfo.grid(row=5, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=cob, fg="steel blue", anchor=W)

	lblinfo.grid(row=5, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PIZZA MEAL", fg="steel blue", anchor=W)

	lblinfo.grid(row=6, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=cofi, fg="steel blue", anchor=W)

	lblinfo.grid(row=6, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="CHEESE BURGER", fg="steel blue", anchor=W)

	lblinfo.grid(row=7, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=cochee, fg="steel blue", anchor=W)

	lblinfo.grid(row=7, column=3)

# str(cob),str(cofi),str(cochee),str(codr),str(costofmeal),str(Service),str(PaidTax),str(costofmeal),str(OverAllCost
	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="CHEESE BURGER", fg="steel blue", anchor=W)

	lblinfo.grid(row=8, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=codr, fg="steel blue", anchor=W)

	lblinfo.grid(row=8, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="DRINKS", fg="steel blue", anchor=W)

	lblinfo.grid(row=9, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=codr, fg="steel blue", anchor=W)

	lblinfo.grid(row=9, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="COST (Rs.)", fg="steel blue", anchor=W)

	lblinfo.grid(row=10, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=costofmeal, fg="steel blue", anchor=W)

	lblinfo.grid(row=10, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SERVICE CHARGE", fg="steel blue", anchor=W)

	lblinfo.grid(row=11, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=Service, fg="steel blue", anchor=W)

	lblinfo.grid(row=11, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="TAX", fg="steel blue", anchor=W)

	lblinfo.grid(row=12, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=PaidTax, fg="steel blue", anchor=W)

	lblinfo.grid(row=12, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SUB TOTAL", fg="steel blue", anchor=W)

	lblinfo.grid(row=13, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=costofmeal, fg="steel blue", anchor=W)

	lblinfo.grid(row=13, column=3)

	# lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SUB TOTAL", fg="steel blue", anchor=W)

	# lblinfo.grid(row=14, column=0)


	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_______________________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=14, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="______________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=14, column=1)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=14, column=2)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="___________________________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=14, column=3)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="TOTAL", fg="steel blue", anchor=W)

	lblinfo.grid(row=15, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text=OverAllCost, fg="steel blue", anchor=W)

	lblinfo.grid(row=15, column=3)



	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_______________________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=16, column=0)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="______________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=16, column=1)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=16, column=2)

	lblinfo = Label(roo, font=('aria', 15, 'bold'), text="___________________________________", fg="steel blue", anchor=W)

	lblinfo.grid(row=16	, column=3)




	roo.mainloop()




def receipt_order():


	order_id =rand.get()

	connt = sqlite3.connect('order_emp.db')
	cursor = connt.cursor()
	cursor.execute('SELECT * FROM order_emp WHERE id=?',(order_id,))
	roo = Tk()
	roo.geometry("600x220+0+0")
	roo.title("RECEIPT LIST")
	for row in cursor:
		print("data is ",row)


		lblinfo = Label(roo, font=('aria', 15,'bold'), text="________________________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=0, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="BILL RECEIPT", fg="black", bd=5)

		lblinfo.grid(row=0, column=1)


		lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=0, column=2)

		lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=0, column=3)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ORDER ID", fg="black", anchor=W)

		lblinfo.grid(row=2, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[0], fg="steel blue", anchor=W)

		lblinfo.grid(row=2, column=3)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="FIRES MEAL", fg="steel blue", anchor=W)

		lblinfo.grid(row=3, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[1], fg="steel blue", anchor=W)

		lblinfo.grid(row=3, column=3)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="LUNCH MEAL", fg="steel blue", anchor=W)

		lblinfo.grid(row=4, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[2], fg="steel blue", anchor=W)

		lblinfo.grid(row=4, column=3)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="BURGER MEAL", fg="steel blue", anchor=W)

		lblinfo.grid(row=5, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[3], fg="steel blue", anchor=W)

		lblinfo.grid(row=5, column=3)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PIZZA MEAL", fg="steel blue", anchor=W)

		lblinfo.grid(row=6, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[4], fg="steel blue", anchor=W)

		lblinfo.grid(row=6, column=3)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="CHEESE BURGER", fg="steel blue", anchor=W)

		lblinfo.grid(row=7, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[5], fg="steel blue", anchor=W)

		lblinfo.grid(row=7, column=3)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="CHEESE BURGER", fg="steel blue", anchor=W)

		lblinfo.grid(row=8, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[5], fg="steel blue", anchor=W)

		lblinfo.grid(row=8, column=3)
		
		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="DRINKS", fg="steel blue", anchor=W)

		lblinfo.grid(row=9, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[6], fg="steel blue", anchor=W)

		lblinfo.grid(row=9, column=3)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="COST (Rs.)", fg="steel blue", anchor=W)

		lblinfo.grid(row=10, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[7], fg="steel blue", anchor=W)

		lblinfo.grid(row=10, column=3)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SERVICE CHARGE", fg="steel blue", anchor=W)

		lblinfo.grid(row=11, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[8], fg="steel blue", anchor=W)

		lblinfo.grid(row=11, column=3)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="TAX", fg="steel blue", anchor=W)

		lblinfo.grid(row=12, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[9], fg="steel blue", anchor=W)

		lblinfo.grid(row=12, column=3)
		
		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SUB TOTAL", fg="steel blue", anchor=W)

		lblinfo.grid(row=13, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[10], fg="steel blue", anchor=W)

		lblinfo.grid(row=13, column=3)

		# lblinfo = Label(roo, font=('aria', 15, 'bold'), text="SUB TOTAL", fg="steel blue", anchor=W)

		# lblinfo.grid(row=14, column=0)


		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_______________________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=14, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="______________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=14, column=1)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=14, column=2)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="___________________________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=14, column=3)
		
		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="TOTAL", fg="steel blue", anchor=W)

		lblinfo.grid(row=15, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text=row[11], fg="steel blue", anchor=W)

		lblinfo.grid(row=15, column=3)



		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_______________________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=16, column=0)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="______________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=16, column=1)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=16, column=2)

		lblinfo = Label(roo, font=('aria', 15, 'bold'), text="___________________________________", fg="steel blue", anchor=W)

		lblinfo.grid(row=16	, column=3)




	roo.mainloop()




def display_order():

	connt = sqlite3.connect('order_emp.db')
	cursor = connt.cursor()
	cursor.execute('SELECT * FROM order_emp')
	print("*********************************RESTAURANTS ORDERS*********************************")
	# fires,largefries,burger,Filet,subtotal,total,service_charge,drinks,tax,cost,cheese_burger )
	for row in cursor.fetchall():
		# print("RESTAURANTS ORDERS:",row)
		print("Order Id:",row[0])
		print("Fries:",row[1])
		print("Lunch Meal:",row[2])
		print("Burger:",row[3])
		print("Pizza:",row[4])
		print("Drinks:",row[6])
		print("Chees Burger:",row[5])
		print("Service Charge:",row[8])
		print("Tax:",row[9])
		print("Cost:",row[10])
		print("Sub Total:",row[7])
		print("Total:",row[11])

	
		print("******************************************************************")
		

rand = StringVar()
Fries = IntVar()
Largefries = IntVar()
Burger = IntVar()
Filet = IntVar()
Subtotal = IntVar()
Total = IntVar()
Service_Charge = IntVar()
Drinks = IntVar()
Tax = IntVar()
cost = IntVar()
Cheese_burger = IntVar()

def qexit():
    root.destroy()

def reset():
    rand.set(0)
    Fries.set(0)
    Largefries.set(0)
    Burger.set(0)
    Filet.set(0)
    Subtotal.set(0)
    Total.set(0)
    Service_Charge.set(0)
    Drinks.set(0)
    Tax.set(0)
    cost.set(0)
    Cheese_burger.set(0)

def reset_emp():
    empid.set("")
    name.set("")
    phone.set("")
    address.set("")
    desig.set("")

def add():
	empId= int(empid.get())
	name  = str(name.get())
	phone = int(phone.get())
	address = str(address.get())
	desig = str(desig.get())


def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)
    cof =int(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())
    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35
    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="Rs.",str('%.2f'% PayTax)
    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)

def emp2():

	f2.pack()

	f1.pack_forget()
	
	lblempid = Label(f2, font=( 'aria' ,16, 'bold' ),text="Employee Id",fg="steel blue",bd=10,anchor='w')

	lblempid.grid(row=0,column=0)

	txtempid = Entry(f2,font=('ariel' ,16,'bold'), textvariable=empid, bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtempid.grid(row=0,column=1)

	lblname = Label(f2, font=( 'aria' ,16, 'bold' ),text="Employee Name",fg="steel blue",bd=10,anchor='w')

	lblname.grid(row=1,column=0)

	txtname = Entry(f2,font=('ariel' ,16,'bold'), textvariable=name, bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtname.grid(row=1,column=1)



	lblphone = Label(f2, font=( 'aria' ,16, 'bold' ),text="Mobile Number",fg="steel blue",bd=10,anchor='w')

	lblphone.grid(row=2,column=0)

	txtphone = Entry(f2,font=('ariel' ,16,'bold'), textvariable=phone, bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtphone.grid(row=2,column=1)





	lbldesig = Label(f2, font=( 'aria' ,16, 'bold' ),text="Designation",fg="steel blue",bd=10,anchor='w')

	lbldesig.grid(row=3,column=0)

	txtdesig = Entry(f2,font=('ariel' ,16,'bold'), textvariable=desig, bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtdesig.grid(row=3,column=1)



	lbladdress = Label(f2, font=( 'aria' ,16, 'bold' ),text="Address",fg="steel blue",bd=10,anchor='w')

	lbladdress.grid(row=4,column=0)

	txtaddress = Entry(f2,font=('ariel' ,16,'bold'), textvariable=address, bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtaddress.grid(row=4,column=1)



	# lbladd = Label(f1,text="---------------------",fg="white")

	# lbladd.grid(row=6,columnspan=3)



	btnadd=Button(f2,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="ADD", bg="powder blue",command=insert_emp)

	btnadd.grid(row=7, column=2)



	btndisplay=Button(f2,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="DISPLAY", bg="powder blue",command=display)

	btndisplay.grid(row=7, column=1)



	btnReset=Button(f2,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset_emp)

	btnReset.grid(row=7, column=3)


	btnRemove=Button(f2,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="REMOVE", bg="powder blue",command=remove_emp)

	btnRemove.grid(row=7, column=5)


	btnEdit=Button(f2,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EDIT", bg="powder blue",command=edit_emp)

	btnEdit.grid(row=7, column=7)
	




	# emp_root.main	loop()
	# 








def q_order_exit():

    root.destroy()









def price():

    roo = Tk()

    roo.geometry("600x220+0+0")

    roo.title("Price List")

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)

    lblinfo.grid(row=0, column=0)

    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)

    lblinfo.grid(row=0, column=2)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)

    lblinfo.grid(row=0, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)

    lblinfo.grid(row=1, column=0)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)

    lblinfo.grid(row=1, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)

    lblinfo.grid(row=2, column=0)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)

    lblinfo.grid(row=2, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)

    lblinfo.grid(row=3, column=0)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)

    lblinfo.grid(row=3, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)

    lblinfo.grid(row=4, column=0)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)

    lblinfo.grid(row=4, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)

    lblinfo.grid(row=5, column=0)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)

    lblinfo.grid(row=5, column=3)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)

    lblinfo.grid(row=6, column=0)

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)

    lblinfo.grid(row=6, column=3)



    roo.mainloop()



def order():
	#---------------------------------------------------------------------------------------


	f1.pack()

	f2.pack_forget()




	lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')

	lblreference.grid(row=0,column=0)

	txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtreference.grid(row=0,column=1)



	lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue",bd=10,anchor='w')

	lblfries.grid(row=1,column=0)

	txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtfries.grid(row=1,column=1)



	lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue",bd=10,anchor='w')

	lblLargefries.grid(row=2,column=0)

	txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtLargefries.grid(row=2,column=1)





	lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="steel blue",bd=10,anchor='w')

	lblburger.grid(row=3,column=0)

	txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtburger.grid(row=3,column=1)



	lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="steel blue",bd=10,anchor='w')

	lblFilet.grid(row=4,column=0)

	txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtFilet.grid(row=4,column=1)



	lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="steel blue",bd=10,anchor='w')

	lblCheese_burger.grid(row=5,column=0)

	txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtCheese_burger.grid(row=5,column=1)



	#--------------------------------------------------------------------------------------

	lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')

	lblDrinks.grid(row=0,column=2)

	txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtDrinks.grid(row=0,column=3)



	lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="steel blue",bd=10,anchor='w')

	lblcost.grid(row=1,column=2)

	txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtcost.grid(row=1,column=3)



	lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w')

	lblService_Charge.grid(row=2,column=2)

	txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtService_Charge.grid(row=2,column=3)



	lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')

	lblTax.grid(row=3,column=2)

	txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtTax.grid(row=3,column=3)



	lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10,anchor='w')

	lblSubtotal.grid(row=4,column=2)

	txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtSubtotal.grid(row=4,column=3)



	lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')

	lblTotal.grid(row=5,column=2)

	txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="powder blue" ,justify='right')

	txtTotal.grid(row=5,column=3)



	#-----------------------------------------buttons------------------------------------------

	lblTotal = Label(f1,text="---------------------",fg="white")

	lblTotal.grid(row=6,columnspan=3)




	btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=insert_order)

	btnTotal.grid(row=7, column=1)

	

	btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)

	btnreset.grid(row=7, column=2)



	btnexit=Button(f1	,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=q_order_exit)

	btnexit.grid(row=7, column=3)

	btnDisplay=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="DISPLAY", bg="powder blue",command=display_order)

	btnDisplay.grid(row=7, column=4)
	
	btnprice=Button(f1	,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)

	btnprice.grid(row=7, column=5)

	btnDisplay=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RECEIPT", bg="powder blue",command=receipt_order)

	btnDisplay.grid(row=7, column=0)





employee  = Menu(menu)

menu.add_cascade(label="EMPLOYEE",menu=employee)
employee.add_command(label="EMPLOYEE",command=emp2)

order1  = Menu(menu)

menu.add_cascade(label="ORDER",menu=order1)
order1.add_command(label="ORDER",command=order)




root.mainloop()