from tkinter import *
import random
import time
import datetime

root=Tk()                       ##ROOT WINDOW
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")    ###ROOT WINDOW WITH TITLE
root.configure(bg="black")                     ##BACKGROUNG COLOUR 

###########################FRAMES####################################################
Tops=Frame(root,width=1350,height=100,bd=14,bg="black",relief="raise")   ##FOR HEADING
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=650,bd=8,bg="black",relief="raise")  
f1.pack(side=LEFT)

f2=Frame(root,width=440,height=650,bd=8,relief="raise",bg="black")
f2.pack(side=RIGHT)

f1a=Frame(f1,width=900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)

f2a=Frame(f1,width=900,height=320,bd=6,relief="raise")
f2a.pack(side=BOTTOM)

ft2=Frame(f2,width=440,height=650,bd=12,relief="raise")
ft2.pack(side=TOP)

fb2=Frame(f2,width=440,height=50,bd=16,relief="raise")
fb2.pack(side=TOP)


f1aa=Frame(f1a,width=400,height=330,bd=16,relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a,width=400,height=330,bd=16,relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2aa.pack(side=LEFT)
f2ab=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2ab.pack(side=RIGHT)
################################HEADING############################################
lblinfo=Label(Tops,font=('arial',70,'bold italic'),text=" Restaurant Management System ",bd=10)    ##HEADING
lblinfo.grid(row=0,column=0)

######################################VARIABLES#################################
B_M =IntVar()
L_M=IntVar()
D_M=IntVar()
L_F=IntVar()
S_F=IntVar()
Bur=IntVar()
Pazz=IntVar()
Pizz=IntVar()
Filet=IntVar()
Chicken=IntVar()
Cheese=IntVar()
Dess=IntVar()
Drin=IntVar()
Gol=IntVar()
Tikki=IntVar()
Sand=IntVar()


DateofOrder=StringVar()
Receipt_Ref=StringVar()
PaidTax=StringVar()
Sub_Total=StringVar()
TotalCost=StringVar()
Costofmeal=StringVar()
Costofsnacks=StringVar()
Service_Charge=StringVar()


E_Breakfast_Meal=StringVar()
E_Lunch_Meal=StringVar()
E_Dinner_Meal=StringVar()
E_Large_Fries=StringVar()
E_Small_Fries=StringVar()
E_Burger=StringVar()
E_Pazzata=StringVar()
E_Pizza=StringVar()
E_Filet_o_Meal=StringVar()
E_Chicken_Meal=StringVar()
E_Cheese_Meal=StringVar()
E_Aloo_Tikki=StringVar()
E_Drinks=StringVar()
E_Desserts=StringVar()
E_Golgappe=StringVar()
E_Aloo_Tikki=StringVar()
E_Sandwich=StringVar()

E_Breakfast_Meal.set("0")
E_Lunch_Meal.set("0")
E_Dinner_Meal.set("0")
E_Large_Fries.set("0")
E_Small_Fries.set("0")
E_Burger.set("0")
E_Pazzata.set("0")
E_Pizza.set("0")
E_Filet_o_Meal.set("0")
E_Chicken_Meal.set("0")
E_Cheese_Meal.set("0")
E_Aloo_Tikki.set("0")
E_Drinks.set("0")
E_Desserts.set("0")
E_Golgappe.set("0")
E_Aloo_Tikki.set("0")
E_Sandwich.set("0")
##########################FUNCTIONS############################################
def Receipt():
	txtReceipt.delete("1.0",END)
	x=random.randint(10908,500876)
	randomRef=str(x)
	Receipt_Ref.set("BILL"+randomRef)


	txtReceipt.insert(END,'Receipt_Ref:\t\t\t'+ Receipt_Ref.get()
		+'\t\t'+ DateofOrder.get()+"\n")
	txtReceipt.insert(END,'items\t\t\t\t\t'+ "Cost_of_items \n\n")
	txtReceipt.insert(END,'Breakfast_Meal:\t\t\t\t\t'+ E_Breakfast_Meal.get()+"\n")
	txtReceipt.insert(END,'Lunch_Meal:\t\t\t\t\t'+ E_Lunch_Meal.get()+"\n")
	txtReceipt.insert(END,'Dinner_Meal:\t\t\t\t\t'+ E_Dinner_Meal.get()+"\n")
	txtReceipt.insert(END,'Large_Fries:\t\t\t\t\t'+ E_Large_Fries.get()+"\n")
	txtReceipt.insert(END,'Small_Fries:\t\t\t\t\t'+ E_Small_Fries.get()+"\n")
	txtReceipt.insert(END,'Burger:\t\t\t\t\t'+ E_Burger.get()+"\n")
	txtReceipt.insert(END,'Pazzata:\t\t\t\t\t'+ E_Pazzata.get()+"\n")
	txtReceipt.insert(END,'Pizza:\t\t\t\t\t'+ E_Pizza.get()+"\n")
	txtReceipt.insert(END,'Filet_o_Meal:\t\t\t\t\t'+ E_Filet_o_Meal.get()+"\n")
	txtReceipt.insert(END,'Chicken_Meal:\t\t\t\t\t'+ E_Chicken_Meal.get()+"\n")
	txtReceipt.insert(END,'Cheese_Meal:\t\t\t\t\t'+ E_Cheese_Meal.get()+"\n")
	txtReceipt.insert(END,'Drinks:\t\t\t\t\t'+ E_Drinks.get()+"\n")
	txtReceipt.insert(END,'Desserts:\t\t\t\t\t'+ E_Desserts.get()+"\n")
	txtReceipt.insert(END,'Golgappe:\t\t\t\t\t'+ E_Golgappe.get()+"\n")
	txtReceipt.insert(END,'Aloo_Tikki:\t\t\t\t\t'+ E_Aloo_Tikki.get()+"\n")
	txtReceipt.insert(END,'Sandwich:\t\t\t\t\t'+ E_Sandwich.get()+"\n")
	

	txtReceipt.insert(END,'Cost_of_Meals:\t\t'+ Costofmeal.get()+'\tTax_paid:\t\t'+PaidTax.get()+"\n")
	txtReceipt.insert(END,'Cost_of_Snacks:\t\t'+ Costofsnacks.get()+'\tSub_Total:\t\t'+Sub_Total.get()+"\n")
	txtReceipt.insert(END,'Service_Charge:\t\t'+Service_Charge.get()+'\tTotal_Cost:\t\t'+TotalCost.get()+"\n")
	
##########################FUNCTION FOR RESET BUTTON##########################################################################################################################
def Reset():
	PaidTax.set("")
	Sub_Total.set("")
	TotalCost.set("")
	Costofmeal.set("")
	Costofsnacks.set("")
	Service_Charge.set("")
	txtReceipt.delete("1.0",END)

	E_Breakfast_Meal.set("0")
	E_Lunch_Meal.set("0")
	E_Dinner_Meal.set("0")
	E_Large_Fries.set("0")
	E_Small_Fries.set("0")
	E_Burger.set("0")
	E_Pazzata.set("0")
	E_Pizza.set("0")
	E_Filet_o_Meal.set("0")
	E_Chicken_Meal.set("0")
	E_Cheese_Meal.set("0")
	E_Drinks.set("0")
	E_Desserts.set("0")
	E_Golgappe.set("0")
	E_Aloo_Tikki.set("0")
	E_Sandwich.set("0")

	B_M.set(0)
	L_M.set(0)
	D_M.set(0)
	L_F.set(0)
	S_F.set(0)
	Bur.set(0)
	Pazz.set(0)
	Pizz.set(0)
	Filet.set(0)
	Chicken.set(0)
	Cheese.set(0)
	Drin.set(0)
	Dess.set(0)
	Gol.set(0)
	Tikki.set(0)
	Sand.set(0)


	txtBreakfast_Meal.configure(state=DISABLED)
	txtLunch_Meal.configure(state=DISABLED)
	txtDinner_Meal.configure(state=DISABLED)
	txtLarge_Fries.configure(state=DISABLED)
	txtSmall_Fries.configure(state=DISABLED)
	txtBurger.configure(state=DISABLED)
	txtPazzata.configure(state=DISABLED)
	txtPizza.configure(state=DISABLED)
	txtFilet_o_Meal.configure(state=DISABLED)
	txtChicken_Meal.configure(state=DISABLED)
	txtCheese_Meal.configure(state=DISABLED)
	txtDesserts.configure(state=DISABLED)
	txtDrinks.configure(state=DISABLED)
	txtGolgappe.configure(state=DISABLED)
	txtAloo_Tikki.configure(state=DISABLED)
	txtSandwich.configure(state=DISABLED)

###########################FUNCTION FOR CHECKBUTTONS######################################################################
def chkbutton_value():
	if B_M.get()  == 1:
		txtBreakfast_Meal.configure(state=NORMAL)
	elif B_M.get()==0:
		txtBreakfast_Meal.configure(state=DISABLED)
		E_Breakfast_Meal.set("0")
	if(L_M.get()==1):
		txtLunch_Meal.configure(state=NORMAL)
	elif L_M.get()==0:
		txtLunch_Meal.configure(state=DISABLED)
		E_Lunch_Meal.set("0")

	if(D_M.get()==1):
		txtDinner_Meal.configure(state=NORMAL)
	elif D_M.get()==0:
		txtDinner_Meal.configure(state=DISABLED)
		E_Dinner_Meal.set("0")

	if(L_F.get()==1):
		txtLarge_Fries.configure(state=NORMAL)
	elif L_F.get()==0:
		txtLarge_Fries.configure(state=DISABLED)
		E_Large_Fries.set("0")

	if(S_F.get()==1):
		txtSmall_Fries.configure(state=NORMAL)
	elif S_F.get()==0:
		txtSmall_Fries.configure(state=DISABLED)
		E_Small_Fries.set("0")

	if(Bur.get()==1):
		txtBurger.configure(state=NORMAL)
	elif Bur.get()==0:
		txtBurger.configure(state=DISABLED)
		E_Burger.set("0")

	if(Pazz.get()==1):
		txtPazzata.configure(state=NORMAL)
	elif Pazz.get()==0:
		txtPazzata.configure(state=DISABLED)
		E_Pazzata.set("0")

	if(Pizz.get()==1):
		txtPizza.configure(state=NORMAL)
	elif Pizz.get()==0:
		txtPizza.configure(state=DISABLED)
		E_Pizza.set("0")

	if(Filet.get()==1):
		txtFilet_o_Meal.configure(state=NORMAL)
	elif Filet.get()==0:
		txtFilet_o_Meal.configure(state=DISABLED)
		E_Filet_o_Meal.set("0")

	if(Chicken.get()==1):
		txtChicken_Meal.configure(state=NORMAL)
	elif Chicken.get()==0:
		txtChicken_Meal.configure(state=DISABLED)
		E_Chicken_Meal.set("0")

	if(Cheese.get()==1):
		txtCheese_Meal.configure(state=NORMAL)
	elif Cheese.get()==0:
		txtCheese_Meal.configure(state=DISABLED)
		E_Cheese_Meal.set("0")

	if(Tikki.get()==1):
		txtAloo_Tikki.configure(state=NORMAL)
	elif Tikki.get()==0:
		txtAloo_Tikki.configure(state=DISABLED)
		E_Aloo_Tikki.set("0")

	if(Dess.get()==1):
		txtDesserts.configure(state=NORMAL)
	elif Dess.get()==0:
		txtDesserts.configure(state=DISABLED)
		E_Desserts.set("0")

	if(Drin.get()==1):
		txtDrinks.configure(state=NORMAL)
	elif Drin.get()==0:
		txtDrinks.configure(state=DISABLED)
		E_Drinks.set("0")

	if(Gol.get()==1):
		txtGolgappe.configure(state=NORMAL)
	elif Gol.get()==0:
		txtGolgappe.configure(state=DISABLED)
		E_Golgappe.set("0")

	if(Sand.get()==1):
		txtSandwich.configure(state=NORMAL)
	elif Sand.get()==0:
		txtSandwich.configure(state=DISABLED)
		E_Sandwich.set("0")

#############################COST OF ITEMS##############################################################################
def CostofItem():
	item1=float(E_Breakfast_Meal.get())
	item2=float(E_Lunch_Meal.get())
	item3=float(E_Dinner_Meal.get())
	item4=float(E_Large_Fries.get())
	item5=float(E_Small_Fries.get())
	item6=float(E_Burger.get())
	item7=float(E_Pazzata.get())
	item8=float(E_Pizza.get())
	item9=float(E_Filet_o_Meal.get())
	item10=float(E_Chicken_Meal.get())
	item11=float(E_Cheese_Meal.get())
	item12=float(E_Desserts.get())
	item13=float(E_Drinks.get())
	item14=float(E_Golgappe.get())
	item15=float(E_Aloo_Tikki.get())
	item16=float(E_Sandwich.get())

	PriceofMeals=((item1*200)+(item2*700)+(item3*700)+(item10*400)+(item11*350)+(item12*150)+(item13*100))

	PriceofSnacks=((item4*100)+(item5*80)+(item6*50)+(item7*100)+
		(item8*150)+(item9*300)+(item13*100)+(item14*150)+(item15*90)+(item16*100))

	MealCost="Rs",str('%.2f'%(PriceofMeals))
	SnacksCost="Rs",str('%.2f'%(PriceofSnacks))
	Costofmeal.set(MealCost)
	Costofsnacks.set(SnacksCost)
	SC="Rs",str('%2f'%20)
	Service_Charge.set(SC)

	Sub_Totalofitems="Rs",str('%.2f'%(PriceofMeals+PriceofSnacks+20))
	Sub_Total.set(Sub_Totalofitems)

	Tax="Rs",str('%.2f'%((PriceofMeals+PriceofSnacks+20)*0.15))
	PaidTax.set(Tax)
	TT=((PriceofMeals+PriceofSnacks+20)*0.15)
	TC="Rs",str('%.2f'%(PriceofMeals+PriceofSnacks+20+TT))
	TotalCost.set(TC)
##########################FUNCTION FOR EXIT BUTTON#######################################################
def qExit():
	root.destroy()

##############################VARIABLES###############################################################################################################################################################

############################FOR DATETIME################################
DateofOrder.set(time.strftime("%d/%m/%Y"))
#############################CHECKBUTTONS FOR MENU#################################################################################################

Breakfast_Meal=Checkbutton(f1aa,text="Breakfast_Meal",variable=B_M,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command= chkbutton_value)
Breakfast_Meal.grid(row=0,column=0,sticky="w")

Lunch_Meal=Checkbutton(f1aa,text="Lunch_Meal",variable=L_M,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Lunch_Meal.grid(row=1,column=0,sticky="w")

Dinner_Meal=Checkbutton(f1aa,text="Dinner_Meal",variable=D_M,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Dinner_Meal.grid(row=2,column=0,sticky="w")

Desserts=Checkbutton(f1aa,text="Desserts",variable=Dess,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Desserts.grid(row=3,column=0,sticky="w")

Drinks= Checkbutton(f1aa,text="Drinks",variable=Drin,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Drinks.grid(row=4,column=0,sticky="w")


Large_Fries= Checkbutton(f1aa,text="Large_Fries",variable=L_F,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Large_Fries.grid(row=5,column=0,sticky="w")

Small_Fries= Checkbutton(f1aa,text="Small_Fries",variable=S_F,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Small_Fries.grid(row=6,column=0,sticky="w")

Burger= Checkbutton(f1aa,text="Burger",variable=Bur,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Burger.grid(row=7,column=0,sticky="w")
#########################################################################################
Pazzata= Checkbutton(f1ab,text="Pazzata",variable=Pazz,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Pazzata.grid(row=0,column=0,sticky="w")

Pizza= Checkbutton(f1ab,text="Pizza",variable=Pizz,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Pizza.grid(row=1,column=0,sticky="w")

Filet_o_Meal= Checkbutton(f1ab,text="Filet_o_Meal",variable=Filet,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Filet_o_Meal.grid(row=2,column=0,sticky="w")

Chicken_Meal= Checkbutton(f1ab,text="Chicken_Meal",variable=Chicken,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Chicken_Meal.grid(row=3,column=0,sticky="w")

Cheese_Meal= Checkbutton(f1ab,text="Cheese_Meal",variable=Cheese,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Cheese_Meal.grid(row=4,column=0)

Sandwich=Checkbutton(f1ab,text="Sandwich",variable=Sand,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Sandwich.grid(row=5,column=0,sticky="w")

Aloo_Tikki=Checkbutton(f1ab,text="Aloo_Tikki",variable=Tikki,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Aloo_Tikki.grid(row=6,column=0,sticky="w")

Golgappe=Checkbutton(f1ab,text="Golgappe",variable=Gol,onvalue=1,offvalue=0,
	font=('arial',18,'bold'),command=chkbutton_value)
Golgappe.grid(row=7,column=0,sticky="w")
###############################WIDGETS OR TEXT BUTTONS FOR MENU########################################################################
txtBreakfast_Meal=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Breakfast_Meal,state=DISABLED)
txtBreakfast_Meal.grid(row=0,column=1)

txtLunch_Meal=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Lunch_Meal,state=DISABLED)
txtLunch_Meal.grid(row=1,column=1)

txtDinner_Meal=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Dinner_Meal,state=DISABLED)
txtDinner_Meal.grid(row=2,column=1)

txtDesserts=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Desserts,state=DISABLED)
txtDesserts.grid(row=3,column=1)

txtDrinks=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Drinks,state=DISABLED)
txtDrinks.grid(row=4,column=1)

txtLarge_Fries=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Large_Fries,state=DISABLED)
txtLarge_Fries.grid(row=5,column=1)

txtSmall_Fries=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Small_Fries,state=DISABLED)
txtSmall_Fries.grid(row=6,column=1)

txtBurger=Entry(f1aa,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Burger,state=DISABLED)
txtBurger.grid(row=7,column=1)
#################################################################################################################
txtPazzata=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Pazzata,state=DISABLED)
txtPazzata.grid(row=0,column=1)

txtPizza=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Pizza,state=DISABLED)
txtPizza.grid(row=1,column=1)

txtFilet_o_Meal=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Filet_o_Meal,state=DISABLED)
txtFilet_o_Meal.grid(row=2,column=1)

txtChicken_Meal=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Chicken_Meal,state=DISABLED)
txtChicken_Meal.grid(row=3,column=1)

txtCheese_Meal=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Cheese_Meal,state=DISABLED)
txtCheese_Meal.grid(row=4,column=1)

txtSandwich=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Sandwich,state=DISABLED)
txtSandwich.grid(row=5,column=1)

txtAloo_Tikki=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Aloo_Tikki,state=DISABLED)
txtAloo_Tikki.grid(row=6,column=1)

txtGolgappe=Entry(f1ab,font=('arial',16,'bold'),bd=8,width=6,justify="left",textvariable=E_Golgappe,state=DISABLED)
txtGolgappe.grid(row=7,column=1)


############################FOR RECEIPT################################################

lblReceipt=Label(ft2,font=('arial',12,'bold'),text="Receipt",bd=2)
lblReceipt.grid(row=0,column=0,sticky="w")
txtReceipt=Text(ft2,width=59,height=22,bg="white",bd=8,font=('arial',11,'bold') )
txtReceipt.grid(row=1,column=0)

################################FOR cost of items###############################
lblCostofmeal=Label(f2aa,font=('arial',16,'bold'),text="Cost of Meals",bd=8)
lblCostofmeal.grid(row=0,column=0,sticky='w')
txtCostofmeal=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left',textvariable=Costofmeal)
txtCostofmeal.grid(row=0,column=1,sticky="w")

lblCostofsnacks=Label(f2aa,font=('arial',16,'bold'),text="Cost of Snacks",bd=8)
lblCostofsnacks.grid(row=1,column=0,sticky='w')
txtCostofsnacks=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left',textvariable=Costofsnacks)
txtCostofsnacks.grid(row=1,column=1,sticky="w")
###########################payment mode################################################################

lblService_Charge=Label(f2aa,font=('arial',16,'bold'),text="Service_Charge",bd=8)
lblService_Charge.grid(row=2,column=0,sticky='w')
txtService_Charge=Entry(f2aa,font=('arial',16,'bold'),bd=8,justify='left',textvariable=Service_Charge)
txtService_Charge.grid(row=2,column=1,sticky="w")

lblPaid_Tax=Label(f2ab,font=('arial',16,'bold'),text="Paid_Tax",bd=8)
lblPaid_Tax.grid(row=0,column=0,sticky='w')
txtPaid_Tax=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left',textvariable=PaidTax)
txtPaid_Tax.grid(row=0,column=1,sticky="w")

lblSub_Total=Label(f2ab,font=('arial',16,'bold'),text="Sub_Total",bd=8)
lblSub_Total.grid(row=1,column=0,sticky='w')
txtSub_Total=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left',textvariable=Sub_Total)
txtSub_Total.grid(row=1,column=1,sticky="w")

lblTotal=Label(f2ab,font=('arial',16,'bold'),text="Total",bd=8)
lblTotal.grid(row=2,column=0,sticky='w')
txtTotal=Entry(f2ab,font=('arial',16,'bold'),bd=8,justify='left',textvariable=TotalCost)
txtTotal.grid(row=2,column=1,sticky="w")

############################BUTTONS#########################################################
btnTotal=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,
	text="Total",command=CostofItem).grid(row=0,column=0)

btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,
	text="Receipt",command=Receipt).grid(row=0,column=1)

btnReset=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,
	text="Reset",command=Reset).grid(row=0,column=2)

btnExit=Button(fb2,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=5,
	text="Exit",command=qExit).grid(row=0,column=3)


root.mainloop()