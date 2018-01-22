##C:\ProgramData\Anaconda3\Lib\site-packages\pulp\solverdir - for solver dir
## Created after a long night and working with the pymprog module : C:\GitHub\Owner_Agent\Optimization_Notes_1_18_18.py
## Trying to see if PuLP or Gurobi will be any easier or at least more robust
# To activate this environment, use:
# > activate py36
#
# To deactivate an active environment, use:
# > deactivate



class optiHelper:
    from pymprog import model
    import pandas as pd
    import numpy as np
    # import sumoPython_git_A as SP
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
    def testing_junk_from_ageing_function():
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
        pass

        
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
            XLnXS_i_t_DF.loc[DFrowLIST[counter-1],'xl_Primal']  = str(xl[i].primal)
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
        print("\n\nTotal Cost = ",XLnXS_i_t_DF.name," =(?)= ",p.vobj(),"\n",XLnXS_i_t_DF)
        return XLnXS_i_t_DF
        