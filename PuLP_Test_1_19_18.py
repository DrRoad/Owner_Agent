##C:\ProgramData\Anaconda3\Lib\site-packages\pulp\solverdir - for solver dir

http://localhost:8889/notebooks/PuLP_Test_1_19_18.ipynb#





# # # http://www.gurobi.com/academia/for-universities
# # # https://user.gurobi.com/download/licenses/academic/3368141e-fd37-11e7-baf8-0a4522cc772c
# # # file:///C:/gurobi752/win64/ReleaseNotes.html
# # # file:///C:/gurobi752/win64/docs/quickstart/starting_gurobi_remote_ser.html#subsection:startremoteservices
# # # with VPN into drexel grbgetkey 3368141e-fd37-11e7-baf8-0a4522cc772c
# # # #https://conda.io/docs/user-guide/tasks/manage-environments.html
# # # http://www.gurobi.com/documentation/7.5/quickstart_mac/installing_the_anaconda_py.html#section:Anaconda
# To activate this environment, use:
# > activate py36
#
# To deactivate an active environment, use:
# > deactivate




## TEST ##
import pulp # PLP.pulpTestAll()
import pandas as pd
import numpy as np
np.set_printoptions(precision = 2, linewidth = 400)
from random import Random
from _optiHelper import optiHelper as _opti




# # Instantiate the model    # Create the 'prob' variable to contain the problem data
prob = pulp.LpProblem("Cost Minimization of Maintenance Activities to achieve a max life threshold",pulp.LpMinimize)



rand = Random()
roads =5
time = 1
# initializing indices
M = [(i,t) for i in range(roads) for t in range(time+1)]
age_i_t_DF = _opti.makeDataFrames_age(roads, time)
XLnXS_i_t_DF = _opti.makeDataFrames_Activities(roads, time,age_i_t_DF)


# https://stackoverflow.com/questions/35464931/how-to-get-the-optimal-optimization-variables-in-pulp-with-python


# https://pythonhosted.org/PuLP/pulp.html#pulp.LpVariable 
# xl_1_1 = pulp.LpVariable("xl(1:1)",0,1,pulp.LpInteger)
# Declaring Variables
roadlist = list()
counter = 0
for i,j in M[1::2]:
    # roadlist.append('Road_'+str(counter))
    roadlist.append(str(str(i)+str(j)))
    counter += 1
    
big_jobs_xl = [LpVariable(roadlist[i], cat='Binary') for i in range(len(roadlist)) ]
small_jobs_xs = [LpVariable(roadlist[i], cat='Binary') for i in range(len(roadlist)) ] #lowBound = 0, upBound = 10) for i in range(3) ]#pulp.LpVariable.dicts("xl", roadlist, cat='Binary')
small_jobs_xs = pulp.LpVariable.dicts("xs", roadlist, cat='Binary')

ageDICT = dict()
agelist = list()
# for i in range(0,roads*2):
for i,j in M[::]:
    agelist.append(str(str(i)+str(j)))
    # j = 0 #should be i,j from M but its not working for i,j in M[0::2]:
    print("i = ",i," j = ",j, end='\r')
    ageDICT.update( {str(str(age_i_t_DF.index[i])+ "_0") : str( age_i_t_DF.iloc[i,j] )} )
    ageDICT.update( {str(str(age_i_t_DF.index[i])+ "_1") : str( int(age_i_t_DF.iloc[i,j])+1 ) } )
age_varDICT = pulp.LpVariable.dicts("age_i_t",agelist)



##Defining the objective statements
prob += pulp.lpSum( [big_jobs_xl[str(str(i)+str(j))] * 200 for i,j in M[1::2] ] + [small_jobs_xs[str(str(i)+str(j))] * 75 )

for i,j in M[1::2]:
    prob += 0 <= big_jobs_xl[str(str(i)+str(j))] + small_jobs_xs[str(str(i)+str(j))] <= 1
##Defining Contrains
for i,j in M[0::2]:
    prob += age_varDICT[str(str(i)+str(j))] == age_i_t_DF.iloc[i,j]

# # # (age_i_t[asset][0]) - ( ((xl[asset,1]) * (age_i_t[asset][0])) + ( ((xs[asset,1]) * .33) * (age_i_t[asset][0])) - ( 1 - ( (xl[asset,1]) + (xs[asset,1]) )) ) ) <= 5)
for i,j in M[1::2]:
   
    prob += age_varDICT[str(str(i)+str(j))] == ( (age_i_t_DF.iloc[i-1,j]) - ( ((big_jobs_xl[str(str(i)+str(j))]) * (age_i_t_DF.iloc[i-1,j)) + ( ((small_jobs_xs[str(str(i)+str(j))]) * .33) * (age_i_t_DF.iloc[i-1,j)) - ( 1 - ( (big_jobs_xl[str(str(i)+str(j))]) + (small_jobs_xs[str(str(i)+str(j))]) )) ) )
    
##http://benalexkeen.com/linear-programming-with-python-and-pulp-part-6/
# https://pythonhosted.org/PuLP/pulp.html#pulp.LpVariable
# https://pythonhosted.org/PuLP/CaseStudies/a_blending_problem.html

 # prob += 0 <= age_varDICT[str(str(i)+str(j))] == ( (age_i_t_DF.iloc[i-1,j]) ( ((big_jobs_xl[str(str(i)+str(j))]) * (age_i_t_DF.iloc[i-1,j)) + ( ((small_jobs_xs[str(str(i)+str(j))]) * .33) * (age_i_t_DF.iloc[i-1,j)) - ( 1 - ( (big_jobs_xl[str(str(i)+str(j))]) + (small_jobs_xs[str(str(i)+str(j))]) )) ) ) <= 5


