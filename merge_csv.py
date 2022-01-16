import pandas as pd
 
try:
    ls=[]
    list_csv=['csv_report_8851.csv', 'csv_report_8778.csv']
    survey_id1 = pd.read_csv(list_csv[0])
    survey_id2 = pd.read_csv(list_csv[1])
    file_a =list(survey_id1.columns)
    file_b =list(survey_id2.columns)

    if (len(file_a) == len(file_b)):
        for col in range(len(file_a)):
            if (file_a[col] == file_b[col]):
                ls.append(file_a[col])
                merged = pd.concat(map(pd.read_csv, list_csv), ignore_index=True)

            
        
            else:
                print("columns are not matched")
        print(merged)
        merged.fillna('', inplace=True)
        #merged.drop(columns=merged.columns[0],axis=1,inplace=True)
        #merged = merged.drop('column_name', 1)

        merged.to_csv("merged_file_8851_8778.csv",index=False)

    else:
        print("Count of Columns are mismatch")
##for col in survey_id1:
##    if (survey_id1.columns[col] != survey_id2.columns[col]):
##        ls.append(col)
##
## 
### displaying the list of column names
##print('List of column names : ',
##      ls)
    ## df = pd.concat(
    #map(pd.read_csv, ['mydata.csv', 'mydata1.csv']), ignore_index=True)
except:
    print ("Error occured, Please check your variables and File should be closed")
