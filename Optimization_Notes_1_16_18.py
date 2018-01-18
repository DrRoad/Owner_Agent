from pymprog import model
import pandas as pd
import numpy as np
import sumoPython_git_A as SP
import openpyxl as OPENxlsx

def makeDataFrames_age(roads, time):
    age_i_0 = np.array(np.random.randint(1,11,(roads,1)))
    age_i_t_DF = pd.DataFrame(np.zeros((roads,time+1)))
    roadlist = list()
    timelist = list()
    for t in range(0,time+1):
        timelist.append('T_'+str(t))
    for i in range(len(age_i_0)):
        roadlist.append('Road'+str(i))
    age_i_t_DF = pd.DataFrame(np.zeros((roads,time+1)), index=roadlist, columns=timelist)
    for i in range(len(age_i_0)):
        age_i_t_DF.iloc[i,0] = age_i_0[i,0]
    return age_i_t_DF
    
def makeDataFrames_Activities(roads, time,age_i_t_DF):
    M = [(i,t) for i in range(roads) for t in range(time+1)]
    timelist = list()
    roadlist = list()
    counter = 0
    DFcolumns = ['Road_ID_t','Age_0','xl_Primal','xs_Primal','Cost_i_t','T_age']
    # for t in range(0,time):
        # timelist.append('T_'+str(t+1))
    for i in M[1::2]:
        roadlist.append('Road_'+str(counter))
        counter += 1
    XLnXS_i_t_DF = pd.DataFrame(np.zeros((roads,len(DFcolumns))), index=roadlist, columns=DFcolumns)
    counter = 0
    for i in M[1::2]:
        XLnXS_i_t_DF.iloc[counter,0] = str(i)
        XLnXS_i_t_DF.iloc[counter,1] = str(age_i_t_DF.iloc[counter,0])
        counter += 1
    return XLnXS_i_t_DF

def ageing_function(age_i_t_minus1,xl_t_minus1,xs_t_minus1):
    age_i_t = (age_i_t_minus1) - ( ((xl_t_minus1) * (age_i_t_minus1)) + ( ((xs_t_minus1) * .33) * (age_i_t_minus1) ) ) + (1 - ( (xl_t_minus1) + (xs_t_minus1) ))
    return age_i_t
    ####TEST TEST TEST FOR (agent_i_t-1,xl,xs,)
    # xls_term = PYM._math.__mul__(PYM._math.__mul__((xs[asset,1]),.33),(age_i_t[asset][0]))
    # xls_termII = PYM._math.__pow__(1,1)
    # p.st(age_i_t[asset][1].value >= ((age_i_t[asset][0]) -(PYM._math.__mul__((age_i_t[asset][1]),(xl[asset,1])) + PYM._math.__mul__(                 )))
    # age_i_t_minus1 = 4
    # var_from_above = .85
    # print(testing_function(4,1,0) == 0 , testing_function(4,0,1) == age_i_t_minus1 - var_from_above * age_i_t_minus1, testing_function(4,0,0) == age_i_t_minus1 +1,"\nxl Used:",testing_function(4,1,0) ,"\n", "xs Used: ", testing_function(4,0,1) ,"\nNothing Used:", testing_function(4,0,0))
    ###GOOD TEST BELOW###
    # age_i_t_minus1 = 4 #XLnXS_i_t_DF.loc[XLnXS_i_t_DF['Road_ID_t'].str.contains(str(i)),'Age_0'][0]
    # xl_t_minus1 = 0#xl[i].primal
    # xs_t_minus1 = 0#xs[i].primal
    ##END TEST INPUT VARIABLES##
    # age_i_t = (age_i_t_minus1) - ( ((xl_t_minus1) * (age_i_t_minus1)) + ( ((xs_t_minus1) * .33) * (age_i_t_minus1) ) ) + (1 - ( (xl_t_minus1) + (xs_t_minus1) ))
    ### old function signs on last term swapped to make easier decoding ###
    #age_i_t = ((age_i_t_minus1) - ( ((xl_t_minus1) * (age_i_t_minus1)) + ( ((xs_t_minus1) * .33) * (age_i_t_minus1)) - (1 - ( (xl_t_minus1) + (xs_t_minus1) )) ) )
    # age_i_t_1 = (age_i_t_minus1) - ( ((xl_t_minus1) * (age_i_t_minus1)) )
    # age_i_t_2 = (age_i_t_minus1) - ( ((xl_t_minus1) * (age_i_t_minus1)) + ( ((xs_t_minus1) * .33) * (age_i_t_minus1) ) ) 
    # age_i_t_3 = (age_i_t_minus1) - ( ((xl_t_minus1) * (age_i_t_minus1)) + ( ((xs_t_minus1) * .33) * (age_i_t_minus1) ) ) + (1 - ( (xl_t_minus1) + (xs_t_minus1) ))
    # print("age_i_t_minus1 = ",age_i_t_minus1,"\nxl = ",xl_t_minus1,"\nxs = ",xs_t_minus1, "\nage_i_t_1...", age_i_t_1,"\nage_i_t_2..." ,age_i_t_2,"\nage_i_t_3..." , age_i_t_3,"\nage_i_t..." , age_i_t)
    # w10 = ageing_function(7,1,0)
    # w01 = ageing_function(7,0,1)
    # w00 = ageing_function(7,0,0)
    ###END TESTING###

    
def XLnXS_i_t_DF_Maker(xl,xs,age_i_t):
    # age_i_t_DF = makeDataFrames_age(roads, time)
    # XLnXS_i_t_DF = makeDataFrames_Activities(roads, time, age_i_t_DF)
    outPut_dict = dict()
    outPut_dict_primal = dict()
    outPut_key = list()
    counter = 1
    for i in range(1,11):
        print("\n<>",p.get_col_name(i),"= Coef = ", p.get_obj_coef(i), end='\r')

    outPut_dict_primal = dict()
    counter = 1
    Total_Cost= 0
    DFrowLIST = XLnXS_i_t_DF.index.tolist()
    for i in M[1::2]:
        outPut_dict_primal.update({p.get_col_name(counter): str(xl[i].primal)})
        # XLnXS_i_t_DF.loc[counter-1,1] = str(xl[i].primal) # 1: 'xl_Primal'
        XLnXS_i_t_DF.loc[DFrowLIST[counter-1],'xs_Primal']  = str(xl[i].primal)
        XLnXS_i_t_DF.loc[DFrowLIST[counter-1],'xs_Primal'] = str(xs[i].primal)
        XLnXS_i_t_DF.loc[DFrowLIST[counter-1],'T_Final'] = ageing_function(age_i_t_minus1 = XLnXS_i_t_DF.loc[DFrowLIST[counter-1],'Age_0'],xl_t_minus1 = xl[i].primal ,xs_t_minus1 = xs[i].primal)
        # XLnXS_i_t_DF.loc[XLnXS_i_t_DF['Road_ID'].str.contains(str(i)),'xl_Primal'] = str(xl[i].primal)
        # XLnXS_i_t_DF.loc[XLnXS_i_t_DF['Road_ID'].str.contains(str(i)),'xs_Primal'] = str(xs[i].primal)
        # XLnXS_i_t_DF.loc[XLnXS_i_t_DF['Road_ID'].str.contains(str(i)),'T_Final'] = ageing_function(age_i_t_minus1 = XLnXS_i_t_DF.loc[XLnXS_i_t_DF['Road_ID'].str.contains(str(i)),'Age_0'][0],xl = xl[i].primal ,xs = xs[i].primal)
        # # XLnXS_i_t_DF.iloc[counter-1,0] = str(xl[i].primal)
        # XLnXS_i_t_DF.loc[counter-1,2 ] = str(xs[i].primal) # 'xs_Primal'
        XLnXS_i_t_DF.loc[DFrowLIST[counter-1],'Cost_i_t'] = int(xs[i].primal)*75 + int(xl[i].primal)*200 #3 : 'Cost_i_t'
        Total_Cost = Total_Cost + int(xs[i].primal)*75 + int(xl[i].primal)*200
        print("\n")
        print(XLnXS_i_t_DF.loc[DFrowLIST[counter-1],'Road_ID_t'] ," =(?)=", p.get_col_name(counter) ) #," =(?)=",
        counter += 1
    XLnXS_i_t_DF.name = ("Total Cost ="+str(Total_Cost))
    print("Total Cost = ",XLnXS_i_t_DF.name," =(?)= ",p.vobj(),"\n",XLnXS_i_t_DF)
    return XLnXS_i_t_DF
    
    
    




p = model("5 roads and 1 period")
print(p.get_prob_name())
p.verbose(True)
from __future__ import print_function

import pymprog as PYM
# from pymprog import *
np.set_printoptions(precision = 2, linewidth = 400)
from random import Random

## Model Data ##
rand = Random()
roads =5
time = 1
# initializing indices
M = [(i,t) for i in range(roads) for t in range(time+1)]
age_i_t_DF = makeDataFrames_age(roads, time)
XLnXS_i_t_DF = makeDataFrames_Activities(roads, time,age_i_t_DF)



## Beging Model ##
PYM.begin(p)
p.solver('interior', msg_lev=PYM.glpk.GLP_MSG_OFF)
p.solver(int, br_tech=PYM.glpk.GLP_BR_PCH)
# begin("5 roads and 1 period")
#action variables xl is large action, xs is small action ## Slice notation a[start_index:end_index:step]
xl = p.var('xl', M[1::2], bool)
xs = p.var('xs', M[1::2], bool)
#age variables not above 10 years old
# age_i_t = p.var('age',M, bounds = (0,10))
print("\n*Variables*\n",xl,"\n**\n",xs,"\n**\n")#,age_i_t

##Setting objective function
p.minimize(sum(xl[i]*200+xs[i]*75 for i in M[1::2]),'Cost')
print("\nprint(p.get_obj_name()) = ",p.get_obj_name(),"\n")

##FIRST Condition Set##
##Subjected to: Only one type of action can be selected
cons_list = list()
# print("Constraints: ",p.
#subject to: 
for i in M[1::2]: 
    R = xl[i] + xs[i] <=1 # Only one type of action per asset per step # Change to >= 1 if you want some results here, but it should be <=
    cons_list.append(R)
    # R1 = xl[i] + xs[i] >=0
    # cons_list.append(R1)
# p.bound_ranges(), print(cons_list), p.solve(), p.sensitivity() # print(p.status(),"Objective value ",p.get_obj_name(),": is $",p.get_obj_val())

##SECOND Condition Set###
##Subjected to: Initial conditions & maybe... age cannot be greater than 10
import pymprog as PYM
age_i_t = PYM.par('age',M[1::2])#, bounds = (0,10))
for asset in range(age_i_t_DF.shape[0]):
    R2 = p.st(age_i_t[asset][0].value == age_i_t_DF.iloc[asset,0]) # '== (?)'setting random initial conditions
    XLnXS_i_t_DF.iloc[asset,1] = age_i_t_DF.iloc[asset,0] ##Should be verified that the right age is going to the right road
    R3 = p.st(age_i_t[asset][1].value <= 10)
    # p.st(age_i_t[asset][1].value <= 10)
    cons_list.append(R2)
    cons_list.append(R3)
# p.bound_ranges(), p.solve(),# p.status_map, p.sensitivity() # print(p.status(),"Second Test ::: Objective value ",p.get_obj_name(),": is $",p.get_obj_val())



###THIRD Condition Set###
##Subjected to next time period's value must conform to age function & maybe & age cannot be greater than 10
for asset in range(len(age_i_t)): #PYM._math.__pow__(
    # R4 = p.st(((age_i_t[asset][0]) - ( ((xl[asset,1]) * (age_i_t[asset][0])) + ( ((xs[asset,1]) * .33) * (age_i_t[asset][0])) - ( 1 - ( (xl[asset,1]) + (xs[asset,1]) )) ) ) >= age_i_t[asset][1].value >= 10 )
    R4 = p.st(10 >= age_i_t[asset][1].value >= ((age_i_t[asset][0]) - ( ((xl[asset,1]) * (age_i_t[asset][0])) + ( ((xs[asset,1]) * .33) * (age_i_t[asset][0])) - ( 1 - ( (xl[asset,1]) + (xs[asset,1]) )) ) ) )
    cons_list.append(R4)
    ####TEST TEST TEST FOR (agent_i_t-1,xl,xs,)
    # print(testing_function(4,1,0) == 0 , testing_function(4,0,1) == age_i_t_minus1 - var_from_above * age_i_t_minus1, testing_function(4,0,0) == age_i_t_minus1 +1,"\nxl Used:",testing_function(4,1,0) ,"\n", "xs Used: ", testing_function(4,0,1) ,"\nNothing Used:", testing_function(4,0,0))
    ####TEST TEST TEST FOR (agent_i_t-1,xl,xs,)

     
     
p.solve()
print(p.status(),"Third Test ::: Objective value ",p.get_obj_name(),": is $",p.vobj(),"\nConstraints = (why can't I get the module to do this\n",cons_list)
# p.bound_ranges()
XLnXS_i_t_DF_Maker(xl,xs,age_i_t)
## Find the out put and change the parameters



## Now run the program again, but reset age_tminus one, have a three year forward vision... but first put in budget restrains 


    # # # XLnXS_i_t_DF.loc[XLnXS_i_t_DF['Road_ID].str.contains(str(i)),'xl_Primal'] = str(xl[i].primal)
# # print("\n")
# # counter = 6
# # for i in M[1::2]:
    # # outPut_dict_primal.update({p.get_col_name(counter): str(xs[i].primal)})
    # # XLnXS_i_t_DF.iloc[counter-1,0] = str(xs[i].primal)
    # # print(XLnXS_i_t_DF.index[counter-1]," =(?)=", p.get_col_name(counter) ) #
    # # counter += 1
    # # # XLnXS_i_t_DF.loc[XLnXS_i_t_DF['Belmont_AVEDic_ID'].str.contains(edgeLISTa[n].edgeID),'Total_Trucks']
# # print("\n")






p.write_prob(0,'/Users/Biko/Dropbox/PhD/Research/Python Code/Sumo_Python_Code_DB/Basic_Trial_Opti_Solver.txt')



for i in M[1::2]:
    print("xl[",i,"].dual = ",xl[i].dual,"\nxs[",i,"].dual = ",xs[i].dual)






p.sensitivity()
print(p.status(),"THIRD TEST ###  Objective value ",p.get_obj_name(),": is $",p.get_obj_val())
print("\nInital Age = \n",age_i_0,"\nNew ages = \n", age_i_t[::])















 
######################## Just one period first age is a variable not a parameter##############################
from pymprog import model

p = model("5 roads and 1 period")
print(p.get_prob_name())
p.verbose(True)
from __future__ import print_function
import numpy as np
import pymprog as PYM
# from pymprog import *
np.set_printoptions(precision = 2, linewidth = 400)
from random import Random

rand = Random()
roads =5
time = 1
# initializing indices
M = [(i,t) for i in range(roads) for t in range(time+1)]
age_i_0 = np.array(np.random.randint(1,11,(5,1)))

PYM.begin(p)
# p.solver(int, br_tech=PYM.glpk.GLP_BR_PCH)
# begin("5 roads and 1 period")
#action variables xl is large action, xs is small action ## Slice notation a[start_index:end_index:step]
xl = p.var('xl', M[1::2], bool)
xs = p.var('xs', M[1::2], bool)
#age variables not above 10 years old
# age_i_t = p.var('age',M, bounds = (0,10))
print("\n*Variables*\n"),xl, print("\n**\n"),xs, print("\n**\n")#,age_i_t

#Setting objective function
p.minimize(sum(xl[i]*200+xs[i]*75 for i in M[1::2]),'Cost')
print("\nprint(p.get_obj_name()) = ",p.get_obj_name(),"\n")

cons_list = list()
# print("Constraints: ",p.
#subject to: Only one type of action per asset per step
for i in M[1::2]:
    R = xl[i] + xs[i] <=1
    R1 = xl[i] + xs[i] >=0
    cons_list.append(R)
    cons_list.append(R1)
p.bound_ranges()
# print(cons_list)

p.solve()
p.sensitivity()
print(p.status(),"Objective value ",p.get_obj_name(),": is $",p.get_obj_val())

for asset in range(age_i_0.shape[0]):
    R2 = age_i_t[asset,0] = age_i_0[asset,0] # '== (?)'setting random initial conditions
    R4 = age_i_t[asset,1] <= 10
    cons_list.append(R2)
    cons_list.append(R4)
p.bound_ranges()
# cons_list
####TEST TEST TES NOT TESTED YET
p.solve()
p.sensitivity()
print(p.status(),"Objective value ",p.get_obj_name(),": is $",p.get_obj_val())
# p.status_map
##This fails
import pymprog as PYM
for asset in range(age_i_0.shape[0]):
    p.st(age_i_t[asset,1] >= ((age_i_t[asset,0]) -((xl[asset,1])*(age_i_t[asset,1])+((xs[asset,1])*.33)*(age_i_t[asset,0])-(((xl[asset,1])+(xs[asset,1]))))))
p.solve()

for asset in range(age_i_0.shape[0]):
    p.st(age_i_t[asset,1].value >= ((age_i_t[asset,0]) -((xl[asset,1])*(age_i_t[asset,1])+((xs[asset,1])*.33)*(age_i_t[asset,0])-(((xl[asset,1])+(xs[asset,1]))))))
p.solve()

    
    
    
    
    
    PYM.solver(int,MIP_presolver='glpk.GLP_ON')
p.solve()
p.sensitivity()
print(p.status(),"Objective value ",p.get_obj_name(),": is $",p.get_obj_val())
## PYM.p.std_basis() #NOT USED
###FAILES ABOVE
import pymprog as PYM
age_i_t = PYM.par('age',M[1::2])#, bounds = (0,10))
for asset in range(len(age_i_t)): #
    age_i_t[asset][0].value = age_i_0[asset][0]
    age_i_t[asset][1].value = ((age_i_t[asset][0].value) -((xl[asset,1])*(age_i_t[asset][1].value)+(xs[asset,1])*.33*(age_i_t[asset][0].value)-(1*((xl[asset,1])+(xs[asset,1])))))
    # p.st( age_i_t[asset][1].value <= 10)
for i in range(roads): age_i_t[i][1].value <= 10
    
solver(int, br_tech=glpk.GLP_BR_PCH)
PYM._math.__pow__(12,3)





for asset in range(age_i_0.shape[0]):
    p.st(age_i_t[asset,1] >= ((age_i_t[asset,0]) -((xl[asset,1])*(age_i_t[asset,1])+((xs[asset,1])*.33)*(age_i_t[asset,0])-(((xl[asset,1])+(xs[asset,1]))))))
PYM.solver(int,MIP_presolver='glpk.GLP_ON')
p.solve()
p.sensitivity()
print(p.status(),"Objective value ",p.get_obj_name(),": is $",p.get_obj_val())
PYM.std_basis()


p.end()



######################## Just one period first age is a variable not a parameter##############################
# from pymprog import model

# p = model("5 roads and 1 period")
# p.verbose(True)
from __future__ import print_function
import numpy as np
# import pymprog as PYM
from pymprog import *
np.set_printoptions(precision = 2, linewidth = 400)
from random import Random

rand = Random()
roads =5
time = 1
# initializing indices
M = [(i,t) for i in range(roads) for t in range(time+1)]
age_i_0 = np.array(np.random.randint(1,11,(5,1)))

# PYM.begin(p)
begin("5 roads and 1 period")
#action variables xl is large action, xs is small action ## Slice notation a[start_index:end_index:step]
xl = var('xl', M[1::2], bool)
xs = var('xs', M[1::2], bool)
#age variables not above 10 years old
age_i_t = var('age',M, bounds = (0,10))
print("\n*Variables*\n"),xl, print("\n"),xs, print("\n"),age_i_t

#Setting objective function
minimize(sum(xl[i]*200+xs[i]*75 for i in M[1::2]),'Cost')
print("\nprint(p.get_obj_name()) = ",print(get_obj_name()),"\n")

cons_list = list()
print("Constraints: ",cons_list)#,p.
#subject to: Only one type of action per asset per step
for i in M[1::2]:
    R = xl[i] + xs[i] <=0
    cons_list.append(R)
print(cons_list)

cons_dict = dict()
counter = 0
for assests in range(age_i_0.shape[0]):
    st(age_i_t[assests,0] = age_i_0[assests,0]) # '== (?)'setting random initial conditions
    st(age_i_t[assests,1] <= min(((age_i_t[assests,0]) -((xl[assests,1])*(age_i_t[assests,1])+(xs[assests,1])*.33*(age_i_t[assests,0])-(1*((xl[assests,1])+(xs[assests,1]))))),10)) # <= 10)
    st(age_i_t[assests,1] <= 10)




solve()

print(get_obj_val())
end()

######################## Just one period first ##############################
from pymprog import model

p = model("5 roads and 1 period")
p.verbose(True)
from __future__ import print_function
import numpy as np


np.set_printoptions(precision = 2, linewidth = 200)
from random import Random

rand = Random()
roads =5
time = 1
# initializing indices
M = [(i,t) for i in range(roads) for t in range(time+1)]

#action variables xl is large action, xs is small action ## Slice notation a[start_index:end_index:step]
xl = p.var('xl', M[1::2], bool)
xs = p.var('xs', M[1::2], bool)
#age variables not above 10 years old
import pymprog as PYM
age_i_t = PYM.par('age',M[1::2])#, bounds = (0,10))
#minimize the cost of actions
# p.min(sum(xl[i,1]*200+xs[i,1]*75 for i in range(len(M)),'Cost')
p.min(sum(xl[i]*200+xs[i]*75 for i in M[1::2]),'Cost')
#subject to: Only one type of action per asset per step
for i in M[1::2]:
    xl[i] + xs[i] <=1

age_i_0 = np.array(np.random.randint(1,11,(5,1)))
#setting random initial conditions
# # # # for assests in range(age_i_0.shape[0]):
    # # # # age_i_t[assests,0] == age_i_0[assests,0]
for assests in range(len(age_i_t)): #
    age_i_t[assests][0].value = age_i_0[assests][0]
    age_i_t[assests][1].value = ((age_i_t[assests][0].value) -((xl[assests,1])*(age_i_t[assests][1].value)+(xs[assests,1])*.33*(age_i_t[assests][0].value)-(1*((xl[assests,1])+(xs[assests,1])))))
    p.st( age_i_t[assests][1].value <= 10)


p.solve()
p.end()

### JUNK (?) #####

#Next year's age
def ageFUNC_III(age_i_t):
    k_minus1 = (0,0)
    for k in M[1::2]:
        if xl[k] == 1:
            newage = 0
        elif xs[k] == 1:
            newage = age_i_t[k_minus1]*.33
        else:
            newage = age_i_t[k_minus1]+1
        age_i_t[k].value = newage
    return age_i_t
 # http://pymprog.sourceforge.net/constr.html
###############################################1-11-18#####below#########









# http://cvxopt.org/examples/tutorial/lp.html>>> 
from cvxopt import matrix, solvers
A = matrix([ [-1.0, -1.0, 0.0, 1.0], [1.0, -1.0, -1.0, -2.0] ])
b = matrix([ 1.0, -2.0, 0.0, 4.0 ])
c = matrix([ 2.0, 1.0 ])
sol=solvers.lp(c,A,b)
print(sol['x'])

http://cvxopt.org/userguide/index.html
http://cvxopt.org/userguide/matrices.html
A simple assignment (A = B) is given the standard Python interpretation, i.e., it assigns to the variable A a reference (or pointer) to the object referenced by B.

B = matrix([[1.,2.], [3.,4.]])
print(B)
A = B
A[0,0] = -1
print(B)   # modifying A[0,0] also modified B[0,0]

The regular (i.e., not in-place) arithmetic operations always return new objects.
B = matrix([[1.,2.], [3.,4.]])
A = +B
A[0,0] = -1
print(B)   # modifying A[0,0] does not modify B[0,0]

The in-place operations directly modify the coefficients of the existing matrix object and do not create a new object.

B = matrix([[1.,2.], [3.,4.]])
A = B
A *= 2
print(B)   # in-place operation also changed B
A = 2*A
print(B)   # regular operation creates a new A, so does not change B

http://cvxopt.org/userguide/blas.html

Level 1 BLAS
The level 1 functions implement vector operations.

cvxopt.blas.scal(alpha, x)
Scales a vector by a constant:

x := alpha*x.

If x is a real matrix, the scalar argument alpha must be a Python integer or float. If x is complex, alpha can be an integer, float, or complex.



from cvxopt import matrix, solvers
import numpy as np
numb_ASSETS = 10
assetAGE = np.array(np.random.random_integers(0,7,(len(activity_i),10)))
assetBINARY = np.array(np.zeros(numb_ASSETS),10)
# assetBINARY.shape=(numb_ASSETS,1)
activity_i = np.array(np.zeros(numb_ASSETS),10)
actCOST = np.array(np.zeros(len(activity_i)),10)
# costDICT = { 0 : 0, 1 : 50, 2 : 120}

def obejectivefunc(activity_i,actCOST):
    costDICT = { 0 : 0, 1 : 50, 2 : 120}
    # actCOST = np.array(np.zeros(len(activity_i)))
    for i in range(len(actCOST)):
        actCOST[i] = costDICT[activity_i[i]]
    print("\nactCOST = ",actCOST,"\n")
    return actCOST
    
def ageFUNC(activity_i):
    # https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.random.html
    # assetAGE = np.array(np.random.rand(len(assetBINARY),1))
    assetAGE = np.array(np.random.random_integers(0,7,(len(activity_i),1)))
    for i in range(len(assetAGE)):
        if activity_i[i] == 0:
            assetAGE[i] += assetAGE[i]
        elif activity_i[i] == 1:
            assetAGE[i] = round(assetAGE[i]*.5,0)
        elif activity_i[i] == 1:
            assetAGE[i] = min(assetAGE[i] - 10, 0)
    print("\nassetAGE = ",assetAGE,"\n")
    return assetAGE
    
#constraints
assetAGE[] <= 10
    
from cvxopt.modeling import variable
from cvxopt.modeling import op
from cvxopt import matrix, div
    
assetBINARY = variable(10,'assetBINARY')
age = variable(10,'age')
activity_i = variable(10,'activity_i')
actCOST = variable(10,'actCOST')

c1 = (ageFUNC(activity_i) <= 10)
c2 = (activity_i <= 2)
c3 = (activity_i >= 0)
c4 = (div(activity_i,activity_i) == 1)

lp1 = op(actCOST, [c1,c2,c3,c4])
lp1.solve()
lp1,status
print(lp1.objective.value())
print(x.value)

# import sagemath # Not sure this is the one to use but seems robust

import pymprog as pmg # http://pymprog.sourceforge.net/tutorial.html
# http://pymprog.sourceforge.net/advanced.html
# use parameters for automatic model update
# c = par('c', c) # when their values change
import numpy as np


def age_i_t(XL,XS,age_i_tminus1):
    age_i_t = (age_i_tminus1)-((XL*age_i_tminus1)+(XS*.66*age_i_tminus1)-(1)**(XL+XS))
    return print(age_i_t)
# age1 = list()
age1.append(5)
XL_1 = 0
XS_1 = 0
age_i_tminus1 = 4

age_i_t(0,0,4)
age_i_t(1,0,4)
age_i_t(0,1,4)

 
XL_i_t = np.zeros((10,10))
XS_i_t = np.zeros((10,10))
minimize: np.sum(50*XS_i_t + 120*XL_i_t)
xs = np.array(np.random.randint(0,2,(10,11)))
xl = np.array(np.random.randint(0,2,(10,11)))
min::np.sum(50*xs + 120*xl)

age_i_t = np.zeros((10,10))
age_i_0 = np.array(np.random.randint(1,8,(10,1)))
age_i_t = np.append(age_i_0,age_i_t, axis = 1)
print("age_i_0 = ",age_i_0,"\nage_i_t = \n",age_i_t)


for row in range(10):
    for col in range(1,11):
        age_i_t[row,col] = (age_i_t[row,col-1])-((xl[row,col]*age_i_t[row,col-1])+(xs[row,col]*.66*age_i_t[row,col-1])-(1**(xl[row,col]+xs[row,col])))
    

    
from __future__ import print_function
import numpy as np
# import pymprog as pmg
from pymprog import *
np.set_printoptions(precision = 2, linewidth = 200)


rand = Random()



def ageFUNC_II(numbOfAssets, T_n_p1, xs=None, xl=None):
    age_i_0 = np.array(np.random.randint(1,8,(10,1))) # Random beginning life values
    age_i_t = np.zeros((numbOfAssets,T_n_p1))
    age_i_t = np.append(age_i_0,age_i_t, axis = 1)
    for row in range(age_i_t.shape[0]):
        for col in range(1,age_i_t.shape[1]):
            age_i_t[row,col] =(age_i_t[row,col-1])+1
    return age_i_t
    
    

## RESTSET AGE ARRAY
age_i_t = ageFUNC_II(numbOfAssets=10, T_n_p1=10) 
xs_np = np.array(np.random.randint(0,2,(10,11)))
xl_np = np.array(np.random.randint(0,2,(10,11)))




begin('test run') # begin modeling
verbose(True) # be verbose
xs = var('xs', 100, kind=bool) # create 100 variables #try one variable with bounds=(0,numb_activities..)
xl = var('xl', 100, kind=bool) # create 100 variables
age_i_t = var('age_it', 110, bounds=(0,10))
minimize(sum(50*xs + 120*xl), 'cost over 10 years')
### http://pymprog.sourceforge.net/pars.html

 # Random beginning life values

for row in range(10,109):
    # print("row= ", age_i_t[row]) # Yikes printing this is crazy age_i_t[row])
    # age_i_t[row] = ((age_i_t[row-10])-((xl[row]*age_i_t[row-10])+(xs[row]*.66*age_i_t[row-10])) <= 10
    ((age_i_t[row-10])-((xl[row]*age_i_t[row-10])+(xs[row]*.66*age_i_t[row-10])) <= 10
    -(1**(xl[row]+xs[row]))) <= 10
    
    
for i in range(len(xl)):
    xl[i] + xs[i] <=1
        
for ii in range(len(age_i_t)):
    age_i_t[ii] <= 10
        
age_i_0 = np.array(np.random.randint(1,8,(10,1)))
for iii in range(age_i_0.shape[0]):
    age_i_t[iii] == age_i_0[iii,0]
## making parameter




from random import Random
rand = Random()


for row in range(10):
    for col in range(1,11):
        age_i_t[row,col] = (age_i_t[row,col-1])-((xl[row,col]*age_i_t[row,col-1])+(xs[row,col]*.66*age_i_t[row,col-1])-(1**(xl[row,col]+xs[row,col]))) <= 10
        xl[row,col] + [row,col] <=1


from __future__ import print_function
import numpy as np
# import pymprog as pmg

np.set_printoptions(precision = 2, linewidth = 200)
from random import Random

rand = Random()
roads = 10
time = 10
M = [(i,t) for i in range(roads) for t in range(time+1)]
        
age_i_0 = [rand.randint(1,10) for i in range(roads)]

import pymprog as PYM
PYM.begin('test run') # begin modeling        
age = PYM.var('age_i_o',M, bounds = (0,10))


PYM.verbose(True) # be verbose
xs = PYM.var('xs', M, kind=bool) # create 100 variables #try one variable with bounds=(0,numb_activities..)
xl = PYM.var('xl', M, kind=bool) # create 100 variables
minimize(sum(50*xs + 120*xl), 'cost over 10 years')

cons_dict = {}
for i,j in xl:
    xl[i,j] + xs[i,j] <=1
    R.name = 'Only one type of activity per asset per step_' + str(i)
    cons_dict.update(str(R))
    print("R.name = ",R.name,"\n R = ",R)
for iii in range(len(age_i_0)):
    age[iii,0] == age_i_0[iii]

for i,j in M:
    # xl[i,j] + xs[i,j] <=1
    if j == 0:
        age[i,j] == age_i_0[i]
    else:
        ## need to make xl and xs into the same [i,j] notations as age is now.
        age[i,j] == ((age[i,j-1])-((int(xl[i,j])*int(age[i,j-1]))+(int(xs[i,j])*.66*int(age[i,j-1]))-(1**(int(xl[i,j])+int(xs[i,j]))))) 
        age[i,j] == (age[i,j-1]) + 1 <= 10
        age[2,3] == (age[2,3-1]) + 1

    print(age[i,j])
    


## how do we do to the power of?
age[i,j] == ((age[i,j-1])-((xl[i,j])*(age[i,j-1])+(xs[i,j])*.66*(age[i,j-1]))-(1**(xl[i,j])+(xs[i,j])))



for i,j in M:
    print(age[i,j])





#############TRASH
for assests in range(age_i_0.shape[0]):
    W = age_i_t[assests,0] = age_i_0[assests,0] # '== (?)'setting random initial conditions
    # cons_list.append(W)
    
    # cons_dict.update(("R"+str(counter))=W)
    # counter += counter 
    age_i_t[assests,1] <= min(((age_i_t[assests,0]) -((xl[assests,1])*(age_i_t[assests,1])+(xs[assests,1])*.33*(age_i_t[assests,0])-(1*((xl[assests,1])+(xs[assests,1]))))),10) # <= 10)
    # cons_list.append(ZZ)
    # cons_dict.update(("R",counter),ZZ)
    # counter += counter 
    PP = st(age_i_t[assests,1] <= 10)
    # cons_list.append(PP)
    # cons_dict.update(("R",counter),PP)
    # counter += counter 
print(cons_list,cons_dict)