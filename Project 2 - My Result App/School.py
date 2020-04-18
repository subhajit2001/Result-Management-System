# Python program to create a 
# GUI mark sheet using tkinter 


# Import tkinter as tk 
import tkinter as tk 


# creating a new tkinter window 
master = tk.Tk() 

# assigning a title 
master.title("My School Result - Class 10")

tabcontrol = ttk.Notebook(master)
Inventory = ttk.Frame(tabcontrol)
labelFrame = ttk.LabelFrame(Inventory,text="Inventory Management")
labelFrame.grid(column=0,row=0,padx=8,pady=4,sticky="N")

# specifying geomtery for window size 
master.geometry("1000x500") 


# declaring objects for entering data 
ename = tk.Entry(master,bd=2,width=18) 
estream = tk.Entry(master,bd=2,width=18) 
eroll = tk.Entry(master,bd=2,width=18)
eclass=tk.Entry(master,bd=2,width=18)

e_englang_80=tk.Entry(master,bd=2,width=18)
e_englit_80=tk.Entry(master,bd=2,width=18)
e_2langb_80=tk.Entry(master,bd=2,width=18) 
e_2langh_80=tk.Entry(master,bd=2,width=18)
e_hist_80=tk.Entry(master,bd=2,width=18)
e_geo_80=tk.Entry(master,bd=2,width=18)
e_maths_80=tk.Entry(master,bd=2,width=18)
e_com_80=tk.Entry(master,bd=2,width=18)
e_eco_80=tk.Entry(master,bd=2,width=18)
e_phy_80=tk.Entry(master,bd=2,width=18)
e_chem_80=tk.Entry(master,bd=2,width=18)
e_bio_80=tk.Entry(master,bd=2,width=18)
e_comp_80=tk.Entry(master,bd=2,width=18)

e_englang_20=tk.Entry(master,bd=2,width=18)
e_englit_20=tk.Entry(master,bd=2,width=18)
e_2langb_20=tk.Entry(master,bd=2,width=18) 
e_2langh_20=tk.Entry(master,bd=2,width=18)
e_hist_20=tk.Entry(master,bd=2,width=18)
e_geo_20=tk.Entry(master,bd=2,width=18)
e_maths_20=tk.Entry(master,bd=2,width=18)
e_com_20=tk.Entry(master,bd=2,width=18)
e_eco_20=tk.Entry(master,bd=2,width=18)
e_phy_20=tk.Entry(master,bd=2,width=18)
e_chem_20=tk.Entry(master,bd=2,width=18)
e_bio_20=tk.Entry(master,bd=2,width=18)
e_comp_20=tk.Entry(master,bd=2,width=18)

e_supw=tk.Entry(master,bd=2,width=18)
e_games=tk.Entry(master,bd=2,width=18)
e_con=tk.Entry(master,bd=2,width=18)
e_att=tk.Entry(master,bd=2,width=18)
e_resp=tk.Entry(master,bd=2,width=18)
e_uni=tk.Entry(master,bd=2,width=18)
e_part=tk.Entry(master,bd=2,width=18)
e_attendance=tk.Entry(master,bd=2,width=18)

# function to display the total subject 
# credits total credits and SGPA according 
# to grades entered 
def display(): 
	
	# Varibale to store total marks 
	tot=0
	
	# 10*number of subject credits 
	# give total credits for grade A 
	if e4.get() == "A": 
		
		# grid method is used for placing 
		# the widgets at respective positions 
		# in table like structure . 
		tk.Label(master, text ="40").grid(row=3, column=4) 
		tot += 40
		
	# 9*number of subject credits give 
	# total credits for grade B 
	if e4.get() == "B": 
		tk.Label(master, text ="36").grid(row=3, column=4) 
		tot += 36
		
	# 8*number of subject credits give 
	# total credits for grade C 
	if e4.get() == "C": 
		tk.Label(master, text ="32").grid(row=3, column=4) 
		tot += 32
		
	# 7*number of subject credits 
	# give total credits for grade D	 
	if e4.get() == "D": 
		tk.Label(master, text ="28").grid(row=3, column=4) 
		tot += 28
		
	# 6*number of subject credits give 
	# total credits for grade P	 
	if e4.get() == "P": 
		tk.Label(master, text ="24").grid(row=3, column=4) 
		tot += 24
		
	# 0*number of subject credits give 
	# total credits for grade F	 
	if e4.get() == "F": 
		tk.Label(master, text ="0").grid(row=3, column=4) 
		tot += 0


	# Similarly doing with other objects 
	if e5.get() == "A": 
		tk.Label(master, text ="40").grid(row=4, column=4) 
		tot += 40
	if e5.get() == "B": 
		tk.Label(master, text ="36").grid(row=4, column=4) 
		tot += 36
	if e5.get() == "C": 
		tk.Label(master, text ="32").grid(row=4, column=4) 
		tot += 32
	if e5.get() == "D": 
		tk.Label(master, text ="28").grid(row=4, column=4) 
		tot += 28
	if e5.get() == "P": 
		tk.Label(master, text ="28").grid(row=4, column=4) 
		tot += 24
	if e5.get() == "F": 
		tk.Label(master, text ="0").grid(row=4, column=4) 
		tot += 0
	
	

	if e6.get() == "A": 
		tk.Label(master, text ="30").grid(row=5, column=4) 
		tot += 30
	if e6.get() == "B": 
		tk.Label(master, text ="27").grid(row=5, column=4) 
		tot += 27
	if e6.get() == "C": 
		tk.Label(master, text ="24").grid(row=5, column=4) 
		tot += 24
	if e6.get() == "D": 
		tk.Label(master, text ="21").grid(row=5, column=4) 
		tot += 21
	if e6.get() == "P": 
		tk.Label(master, text ="28").grid(row=5, column=4) 
		tot += 24
	if e6.get() == "F": 
		tk.Label(master, text ="0").grid(row=5, column=4) 
		tot += 0




	if e7.get() == "A": 
		tk.Label(master, text ="40").grid(row=6, column=4) 
		tot += 40
	if e7.get() == "B": 
		tk.Label(master, text ="36").grid(row=6, column=4) 
		tot += 36
	if e7.get() == "C": 
		tk.Label(master, text ="32").grid(row=6, column=4) 
		tot += 32
	if e7.get() == "D": 
		tk.Label(master, text ="28").grid(row=6, column=4) 
		tot += 28
	if e7.get() == "P": 
		tk.Label(master, text ="28").grid(row=6, column=4) 
		tot += 24
	if e7.get() == "F": 
		tk.Label(master, text ="0").grid(row=6, column=4) 
		tot += 0


	# to display total credits 
	tk.Label(master, text=str(tot)).grid(row=7, column=4) 
	
	# to display SGPA 
	tk.Label(master, text=str(tot/15)).grid(row=8, column=4)

def calculate():
        tot=0
        sci_tot=0
        sc_avg=0
        eng_avg=0
        number1=tk.Entry.get(e_englang_80)
        number2=tk.Entry.get(e_englang_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        eng_avg+=answer
        tk.Label(master, text=(str)(answer)).grid(row=3, column=4)
        number1=tk.Entry.get(e_englit_80)
        number2=tk.Entry.get(e_englit_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        eng_avg+=answer
        tk.Label(master, text=(str)(answer)).grid(row=4, column=4)
        number1=tk.Entry.get(e_2langb_80)
        number2=tk.Entry.get(e_2langb_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        tk.Label(master, text=(str)(answer)).grid(row=5, column=4) 
        number1=tk.Entry.get(e_2langh_80)
        number2=tk.Entry.get(e_2langh_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        tk.Label(master, text=(str)(answer)).grid(row=6, column=4) 
        number1=tk.Entry.get(e_hist_80)
        number2=tk.Entry.get(e_hist_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        sc_avg+=answer
        tk.Label(master, text=(str)(answer)).grid(row=7, column=4)
        number1=tk.Entry.get(e_geo_80)
        number2=tk.Entry.get(e_geo_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        sc_avg+=answer
        tk.Label(master, text=(str)(answer)).grid(row=8, column=4)
        number1=tk.Entry.get(e_maths_80)
        number2=tk.Entry.get(e_maths_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        tk.Label(master, text=(str)(answer)).grid(row=9, column=4)
        number1=tk.Entry.get(e_com_80)
        number2=tk.Entry.get(e_com_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        tk.Label(master, text=(str)(answer)).grid(row=10, column=4)
        number1=tk.Entry.get(e_eco_80)
        number2=tk.Entry.get(e_eco_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        tk.Label(master, text=(str)(answer)).grid(row=11, column=4)
        number1=tk.Entry.get(e_phy_80)
        number2=tk.Entry.get(e_phy_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        sci_tot+=answer
        tk.Label(master, text=(str)(answer)).grid(row=12, column=4)
        number1=tk.Entry.get(e_chem_80)
        number2=tk.Entry.get(e_chem_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        sci_tot+=answer
        tk.Label(master, text=(str)(answer)).grid(row=13, column=4)
        number1=tk.Entry.get(e_bio_80)
        number2=tk.Entry.get(e_bio_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        sci_tot+=answer
        tk.Label(master, text=(str)(answer)).grid(row=14, column=4)
        number1=tk.Entry.get(e_comp_80)
        number2=tk.Entry.get(e_comp_20)
        number1=int(number1)
        number2=int(number2)
        answer=number1+number2
        tot=tot+answer
        tk.Label(master, text=(str)(answer)).grid(row=15, column=4)
        tk.Label(master, text=(str)(eng_avg/2)).grid(row=18, column=6) 
        tk.Label(master, text=(str)(sc_avg/2)).grid(row=19, column=6) 
        tk.Label(master, text=(str)(sci_tot/3)).grid(row=20, column=6) 
        tk.Label(master, text=(str)(tot)).grid(row=21, column=6) 
        tk.Label(master, text=(str)(tot/10)).grid(row=22, column=6)

def clear():
        e_englang_80.delete(0,last=10)
        e_englang_80.insert(0,0)
        e_englit_80.delete(0,last=10)
        e_englit_80.insert(0,0)
        e_2langb_80.delete(0,last=10)
        e_2langb_80.insert(0,0)
        e_2langh_80.delete(0,last=10)
        e_2langh_80.insert(0,0)
        e_hist_80.delete(0,last=10)
        e_hist_80.insert(0,0)
        e_geo_80.delete(0,last=10)
        e_geo_80.insert(0,0)
        e_maths_80.delete(0,last=10)
        e_maths_80.insert(0,0)
        e_com_80.delete(0,last=10)
        e_com_80.insert(0,0)
        e_eco_80.delete(0,last=10)
        e_eco_80.insert(0,0)
        e_phy_80.delete(0,last=10)
        e_phy_80.insert(0,0)
        e_chem_80.delete(0,last=10)
        e_chem_80.insert(0,0)
        e_bio_80.delete(0,last=10)
        e_bio_80.insert(0,0)
        e_comp_80.delete(0,last=10)
        e_comp_80.insert(0,0)

        e_englang_20.delete(0,last=10)
        e_englang_20.insert(0,0)
        e_englit_20.delete(0,last=10)
        e_englit_20.insert(0,0)
        e_2langb_20.delete(0,last=10)
        e_2langb_20.insert(0,0)
        e_2langh_20.delete(0,last=10)
        e_2langh_20.insert(0,0)
        e_hist_20.delete(0,last=10)
        e_hist_20.insert(0,0)
        e_geo_20.delete(0,last=10)
        e_geo_20.insert(0,0)
        e_maths_20.delete(0,last=10)
        e_maths_20.insert(0,0)
        e_com_20.delete(0,last=10)
        e_com_20.insert(0,0)
        e_eco_20.delete(0,last=10)
        e_eco_20.insert(0,0)
        e_phy_20.delete(0,last=10)
        e_phy_20.insert(0,0)
        e_chem_20.delete(0,last=10)
        e_chem_20.insert(0,0)
        e_bio_20.delete(0,last=10)
        e_bio_20.insert(0,0)
        e_comp_20.delete(0,last=10)
        e_comp_20.insert(0,0)
        
        
        
	
# end of display function

# labels for subject credits
tk.Label(master, text="Total Marks").grid(row=2, column=4) 

# label to enter name 
tk.Label(master, text="Name").grid(row=0, column=2) 

# label for Stream
tk.Label(master, text="Stream").grid(row=0, column=4) 

# label for roll Number 
tk.Label(master, text="Roll.No").grid(row=1, column=2)

# label for Class
tk.Label(master, text="Class").grid(row=1, column=4) 

# labels for serial numbers 
tk.Label(master, text="Srl.No",underline=5).grid(row=2, column=0) 
tk.Label(master, text="1").grid(row=3, column=0) 
tk.Label(master, text="2").grid(row=4, column=0) 
tk.Label(master, text="3").grid(row=5, column=0) 
tk.Label(master, text="4").grid(row=6, column=0)
tk.Label(master, text="5").grid(row=7, column=0)
tk.Label(master, text="6").grid(row=8, column=0)
tk.Label(master, text="7").grid(row=9, column=0)
tk.Label(master, text="8").grid(row=10, column=0)
tk.Label(master, text="9").grid(row=11, column=0)
tk.Label(master, text="10").grid(row=12, column=0)
tk.Label(master, text="11").grid(row=13, column=0)
tk.Label(master, text="12").grid(row=14, column=0)
tk.Label(master, text="13").grid(row=15, column=0)


# labels for subject codes 
tk.Label(master, text="Subject").grid(row=2, column=1) 
tk.Label(master, text="English Language").grid(row=3, column=1) 
tk.Label(master, text="English Literature").grid(row=4, column=1) 
tk.Label(master, text="2nd Language(B)").grid(row=5, column=1)
tk.Label(master, text="2nd Language(H)").grid(row=6, column=1)
tk.Label(master, text="History/Civics").grid(row=7, column=1)
tk.Label(master, text="Geography").grid(row=8, column=1)
tk.Label(master, text="Mathematics").grid(row=9, column=1)
tk.Label(master, text="Commercial Studies").grid(row=10, column=1)
tk.Label(master, text="Economics Application").grid(row=11, column=1)
tk.Label(master, text="Physics").grid(row=12, column=1)
tk.Label(master, text="Chemistry").grid(row=13, column=1)
tk.Label(master, text="Biology").grid(row=14, column=1)
tk.Label(master, text="Computer Applications").grid(row=15, column=1)


	
# label for grades 
tk.Label(master, text="Marks(out of 20)").grid(row=2, column=2) 
e_englang_20.grid(row=3, column=2) 
e_englit_20.grid(row=4, column=2) 
e_2langb_20.grid(row=5, column=2) 
e_2langh_20.grid(row=6, column=2)
e_hist_20.grid(row=7, column=2)
e_geo_20.grid(row=8, column=2)
e_maths_20.grid(row=9, column=2)
e_com_20.grid(row=10, column=2)
e_eco_20.grid(row=11, column=2)
e_phy_20.grid(row=12, column=2)
e_chem_20.grid(row=13, column=2)
e_bio_20.grid(row=14, column=2)
e_comp_20.grid(row=15,column=2)

# label for grades 
tk.Label(master, text="Marks(out of 80)").grid(row=2, column=3) 
e_englang_80.grid(row=3, column=3) 
e_englit_80.grid(row=4, column=3) 
e_2langb_80.grid(row=5, column=3) 
e_2langh_80.grid(row=6, column=3)
e_hist_80.grid(row=7, column=3)
e_geo_80.grid(row=8, column=3)
e_maths_80.grid(row=9, column=3)
e_com_80.grid(row=10, column=3)
e_eco_80.grid(row=11, column=3)
e_phy_80.grid(row=12, column=3)
e_chem_80.grid(row=13, column=3)
e_bio_80.grid(row=14, column=3)
e_comp_80.grid(row=15,column=3)

#label for total marks
tk.Label(master, text="Passing Marks").grid(row=2, column=5) 
tk.Label(master, text="35%").grid(row=3, column=5) 
tk.Label(master, text="35%").grid(row=4, column=5) 
tk.Label(master, text="35%").grid(row=5, column=5) 
tk.Label(master, text="35%").grid(row=6, column=5)
tk.Label(master, text="35%").grid(row=7, column=5)
tk.Label(master, text="35%").grid(row=8, column=5)
tk.Label(master, text="35%").grid(row=9, column=5)
tk.Label(master, text="35%").grid(row=10, column=5)
tk.Label(master, text="35%").grid(row=11, column=5)
tk.Label(master, text="35%").grid(row=12, column=5)
tk.Label(master, text="35%").grid(row=13, column=5)
tk.Label(master, text="35%").grid(row=14, column=5)
tk.Label(master, text="35%").grid(row=15, column=5)

# labels for all round development
tk.Label(master, text="All Round Development").grid(row=2, column=6) 
tk.Label(master, text="SUPW").grid(row=3, column=6) 
tk.Label(master, text="Games").grid(row=4, column=6) 
tk.Label(master, text="Conduct").grid(row=5, column=6)
tk.Label(master, text="Attentive)").grid(row=6, column=6)
tk.Label(master, text="Responsibility").grid(row=7, column=6)
tk.Label(master, text="Uniform & Personal Appearance").grid(row=8, column=6)
tk.Label(master, text="Participation").grid(row=9, column=6)
tk.Label(master, text="Attendance").grid(row=10, column=6)

# labels for entry
tk.Label(master, text="Grades - A/B/C/D").grid(row=2, column=7)
e_supw.grid(row=3, column=7)
e_games.grid(row=4, column=7)
e_con.grid(row=5, column=7)
e_att.grid(row=6, column=7)
e_resp.grid(row=7, column=7)
e_uni.grid(row=8, column=7)
e_part.grid(row=9, column=7)
e_attendance.grid(row=10, column=7)


# taking entries of name, reg, roll number respectively 
ename=tk.Entry(master) 
estream=tk.Entry(master) 
eroll=tk.Entry(master)
eclass=tk.Entry(master)

# organizing them in th e grid 
ename.grid(row=0, column=3) 
estream.grid(row=0, column=5) 
eroll.grid(row=1, column=3)
eclass.grid(row=1, column=5)

# button to display all the calculated credit scores and sgpa 
button1=tk.Button(master, text="Submit", bg="yellow", command=calculate,bd=3,width=10) 
button1.grid(row=35, column=12)

button1=tk.Button(master, text="Clear", bg="yellow", command=clear,bd=3,width=10) 
button1.grid(row=35, column=7)

button1=tk.Button(master, text="Save as PDF", bg="yellow", command=clear,bd=3,width=10) 
button1.grid(row=35, column=6,padx=(120,0)) 

tk.Label(master, text="English Average").grid(row=18, column=5) 
tk.Label(master, text="Social Studies Average").grid(row=19, column=5) 
tk.Label(master, text="Science Average").grid(row=20, column=5) 
tk.Label(master, text="Total").grid(row=21, column=5) 
tk.Label(master, text="Percentage").grid(row=22, column=5) 


	
master.mainloop() 



#This Marksheet can be snapshotted and printed out 
# as a report card for the semester 
