import os
import pandas as pd
import json


def ConvertAndInsert(path):
    # Aggregated_Transactions Column_1

    path1 = path+"/aggregated/transaction/country/india/state/"

    agg_tran_list = os.listdir(path1)

    columns1={"States":[],"Years":[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}
    for state in agg_tran_list:
        cur_state = path1+state+"/"
        agg_year_list = os.listdir(cur_state)
        
        for year in agg_year_list:
            cur_year = cur_state+year+"/"
            agg_file_list = os.listdir(cur_year)

            for file in agg_file_list:
                cur_file = cur_year+file
                data = open(cur_file,"r")

                A= json.load(data)

                for i in A["data"]["transactionData"]:
                    name =i["name"]
                    count = i["paymentInstruments"][0]["count"]
                    amount = i["paymentInstruments"][0]["amount"]
                    columns1["Transaction_type"].append(name)
                    columns1["Transaction_count"].append(count)
                    columns1["Transaction_amount"].append(amount)
                    columns1["States"].append(state)
                    columns1["Years"].append(year)
                    columns1["Quarter"].append(int(file.strip(".json")))

    aggre_transaction = pd.DataFrame(columns1)

    aggre_transaction["States"] = aggre_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
    aggre_transaction["States"] = aggre_transaction["States"].str.replace("-"," ")
    aggre_transaction["States"] = aggre_transaction["States"].str.title()
    aggre_transaction["States"] = aggre_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")

    #Aggregated User Column_2

    path2 =  path+"/aggregated/user/country/india/state/"
            
    agg_user_list = os.listdir(path2)

    columns2 = {"States":[], "Years":[], "Quarter":[], "Brands":[],"Transaction_count":[], "Percentage":[]}

    for state in agg_user_list:
        cur_states = path2+state+"/"
        agg_year_list = os.listdir(cur_states)
        
        for year in agg_year_list:
            cur_years = cur_states+year+"/"
            agg_file_list = os.listdir(cur_years)
            
            for file in agg_file_list:
                cur_files = cur_years+file
                data = open(cur_files,"r")
                B = json.load(data)

                try:

                    for i in B["data"]["usersByDevice"]:
                        brand = i["brand"]
                        count = i["count"]
                        percentage = i["percentage"]
                        columns2["Brands"].append(brand)
                        columns2["Transaction_count"].append(count)
                        columns2["Percentage"].append(percentage)
                        columns2["States"].append(state)
                        columns2["Years"].append(year)
                        columns2["Quarter"].append(int(file.strip(".json")))
                
                except:
                    pass

    aggre_user = pd.DataFrame(columns2)

    aggre_user["States"] = aggre_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
    aggre_user["States"] = aggre_user["States"].str.replace("-"," ")
    aggre_user["States"] = aggre_user["States"].str.title()
    aggre_user['States'] = aggre_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


    #Aggregated Insurance Column_3

    path3 =  path+"/aggregated/insurance/country/india/state/"
            
    agg_user_list = os.listdir(path3)

    columns3 = {"States":[], "Years":[], "Quarter":[], "Insurance_type":[],"Insurance_count":[], "Insurance_amount":[]}

    for state in agg_user_list:
        cur_states = path3+state+"/"
        agg_year_list = os.listdir(cur_states)
        
        for year in agg_year_list:
            cur_years = cur_states+year+"/"
            agg_file_list = os.listdir(cur_years)
            
            for file in agg_file_list:
                cur_files = cur_years+file
                data = open(cur_files,"r")
                C = json.load(data)


                for i in C["data"]["transactionData"]:
                    name = i["name"]
                    count = i["paymentInstruments"][0]["count"]
                    amount = i["paymentInstruments"][0]["amount"]
                    columns3["Insurance_type"].append(name)
                    columns3["Insurance_count"].append(count)
                    columns3["Insurance_amount"].append(amount)
                    columns3["States"].append(state)
                    columns3["Years"].append(year)
                    columns3["Quarter"].append(int(file.strip(".json")))
                

    aggre_insurance = pd.DataFrame(columns2)

    aggre_insurance["States"] = aggre_insurance["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
    aggre_insurance["States"] = aggre_insurance["States"].str.replace("-"," ")
    aggre_insurance["States"] = aggre_insurance["States"].str.title()
    aggre_insurance['States'] = aggre_insurance['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


    #Map Insurance columns_4

    path4=  path+"/map/insurance/hover/country/india/state/"

    map_insur_list= os.listdir(path4)

    columns4= {"States":[], "Years":[], "Quarter":[], "Districts":[], "Transaction_count":[],"Transaction_amount":[] }

    for state in map_insur_list:
        cur_states =path4+state+"/"
        map_year_list = os.listdir(cur_states)

        for year in map_year_list:
            cur_years = cur_states+year+"/"
            map_file_list = os.listdir(cur_years)

            for file in map_file_list:
                cur_files = cur_years+file
                data = open(cur_files,"r")
                D = json.load(data)

                for i in D['data']['hoverDataList']:
                    name = i["name"]
                    count = i["metric"][0]["count"]
                    amount = i["metric"][0]["amount"]
                    columns4["Districts"].append(name)
                    columns4["Transaction_count"].append(count)
                    columns4["Transaction_amount"].append(amount)
                    columns4["States"].append(state)
                    columns4["Years"].append(year)
                    columns4["Quarter"].append(int(file.strip(".json")))


    map_insurance = pd.DataFrame(columns4)

    map_insurance["States"] = map_insurance["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
    map_insurance["States"] = map_insurance["States"].str.replace("-"," ")
    map_insurance["States"] = map_insurance["States"].str.title()
    map_insurance['States'] = map_insurance['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


    #Map_transaction column_5

    path5 =  path+"/map/transaction/hover/country/india/state/"

    map_tran_list= os.listdir(path5)

    columns5= {"States":[], "Years":[], "Quarter":[], "Districts":[], "Transaction_count":[],"Transaction_amount":[] }

    for state in map_tran_list:
        cur_states =path5+state+"/"
        agg_year_list = os.listdir(cur_states)

        for year in agg_year_list:
            cur_years = cur_states+year+"/"
            agg_file_list = os.listdir(cur_years)

            for file in agg_file_list:
                cur_files = cur_years+file
                data = open(cur_files,"r")
                E = json.load(data)

                for i in E['data']['hoverDataList']:
                    name = i["name"]
                    count = i["metric"][0]["count"]
                    amount = i["metric"][0]["amount"]
                    columns5["Districts"].append(name)
                    columns5["Transaction_count"].append(count)
                    columns5["Transaction_amount"].append(amount)
                    columns5["States"].append(state)
                    columns5["Years"].append(year)
                    columns5["Quarter"].append(int(file.strip(".json")))


    map_transaction = pd.DataFrame(columns5)

    map_transaction["States"] = map_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
    map_transaction["States"] = map_transaction["States"].str.replace("-"," ")
    map_transaction["States"] = map_transaction["States"].str.title()
    map_transaction['States'] = map_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")


    #map user column_6

    path6 =  path+"/map/user/hover/country/india/state/"

    map_user_list = os.listdir(path6)

    columns6 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "RegisteredUser":[], "AppOpens":[]}

    for state in map_user_list:
        cur_states = path6+state+"/"
        map_year_list = os.listdir(cur_states)
        
        for year in map_year_list:
            cur_years = cur_states+year+"/"
            map_file_list = os.listdir(cur_years)
            
            for file in map_file_list:
                cur_files = cur_years+file
                data = open(cur_files,"r")
                F = json.load(data)

                for i in F["data"]["hoverData"].items():
                    district = i[0]
                    registereduser = i[1]["registeredUsers"]
                    appopens = i[1]["appOpens"]
                    columns6["Districts"].append(district)
                    columns6["RegisteredUser"].append(registereduser)
                    columns6["AppOpens"].append(appopens)
                    columns6["States"].append(state)
                    columns6["Years"].append(year)
                    columns6["Quarter"].append(int(file.strip(".json")))

    map_user = pd.DataFrame(columns6)

    map_user["States"] = map_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
    map_user["States"] = map_user["States"].str.replace("-"," ")
    map_user["States"] = map_user["States"].str.title()
    map_user['States'] = map_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")



    #Top Transaction column_7

    path7 =  path+"/top/transaction/country/india/state/"

    map_user_list = os.listdir(path7)

    columns7 = {"States":[], "Years":[], "Quarter":[],  "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

    for state in map_user_list:
        cur_states = path7+state+"/"
        top_year_list = os.listdir(cur_states)
        
        for year in top_year_list:
            cur_years = cur_states+year+"/"
            top_file_list = os.listdir(cur_years)
            
            for file in top_file_list:
                cur_files = cur_years+file
                data = open(cur_files,"r")
                G = json.load(data)

                for i in G["data"]["pincodes"]:
                    entityName = i["entityName"]
                    count = i["metric"]["count"]
                    amount = i["metric"]["amount"]
                    columns7["Pincodes"].append(entityName)
                    columns7["Transaction_count"].append(count)
                    columns7["Transaction_amount"].append(amount)
                    columns7["States"].append(state)
                    columns7["Years"].append(year)
                    columns7["Quarter"].append(int(file.strip(".json")))

    top_transaction = pd.DataFrame(columns7)

    top_transaction["States"] = top_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
    top_transaction["States"] = top_transaction["States"].str.replace("-"," ")
    top_transaction["States"] = top_transaction["States"].str.title()
    top_transaction['States'] = top_transaction['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")



    # Top user Column_8

    path8 =  path+"/top/user/country/india/state/"

    map_user_list = os.listdir(path8)

    columns8 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "RegisteredUser":[]}

    for state in map_user_list:
        cur_states = path8+state+"/"
        top_year_list = os.listdir(cur_states)
        
        for year in top_year_list:
            cur_years = cur_states+year+"/"
            top_file_list = os.listdir(cur_years)
            
            for file in top_file_list:
                cur_files = cur_years+file
                data = open(cur_files,"r")
                H = json.load(data)

                for i in H["data"]["pincodes"]:
                    name = i["name"]
                    registeredusers = i["registeredUsers"]
                    columns8["Pincodes"].append(name)
                    columns8["RegisteredUser"].append(registereduser)
                    columns8["States"].append(state)
                    columns8["Years"].append(year)
                    columns8["Quarter"].append(int(file.strip(".json")))

    top_user = pd.DataFrame(columns8)

    top_user["States"] = top_user["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
    top_user["States"] = top_user["States"].str.replace("-"," ")
    top_user["States"] = top_user["States"].str.title()
    top_user['States'] = top_user['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")



    #Top insurance column_9

    path9 =  path+"/top/insurance/country/india/state/"

    top_insur_list = os.listdir(path9)

    columns9 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

    for state in top_insur_list:
        cur_states = path9+state+"/"
        top_year_list = os.listdir(cur_states)

        for year in top_year_list:
            cur_years = cur_states+year+"/"
            top_file_list = os.listdir(cur_years)

            for file in top_file_list:
                cur_files = cur_years+file
                data = open(cur_files,"r")
                I = json.load(data)

                for i in I["data"]["pincodes"]:
                    entityName = i["entityName"]
                    count = i["metric"]["count"]
                    amount = i["metric"]["amount"]
                    columns9["Pincodes"].append(entityName)
                    columns9["Transaction_count"].append(count)
                    columns9["Transaction_amount"].append(amount)
                    columns9["States"].append(state)
                    columns9["Years"].append(year)
                    columns9["Quarter"].append(int(file.strip(".json")))

    top_insurance = pd.DataFrame(columns9)

    top_insurance["States"] = top_insurance["States"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
    top_insurance["States"] = top_insurance["States"].str.replace("-"," ")
    top_insurance["States"] = top_insurance["States"].str.title()
    top_insurance['States'] = top_insurance['States'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
    
    return aggre_transaction,aggre_user,aggre_insurance,map_insurance,map_transaction,map_user,top_transaction,top_user,top_insurance
