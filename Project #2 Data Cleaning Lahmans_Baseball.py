import mysql.connector as mysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import tabulate

### SQL QUERY SECTION*******************************************************************************
cnx = mysql.connect(
    host="mysqllahmansbaseball.mysql.database.azure.com", # this server will not remain available in the long term
    user="newuser@mysqllahmansbaseball",                  # this user name will not remain available in the long term
    password="Pa$$w0rd",                                  # this password will not remain available in the long term
    port=3306,
    database="lahmansbaseballdb")
print(cnx)

cursor = cnx.cursor()
sql = """
SELECT p.nameFirst, p.nameLast, p.Height, p.Weight, p.throws, p.bats,
p.birthyear, p.birthMonth,p.birthday,p.birthCountry,p.birthState,p.birthCity, b.*

FROM People p
JOIN Batting b ON b.playerID = p.playerID

WHERE b.yearID between 2014 and 2019 AND b.g >= "50"
ORDER BY b.yearID Desc
#LIMIT 50;
"""
cursor.execute(sql)
results = cursor.fetchall()
for x in results:
    pass
    #print(x)

df_baseball = pd.DataFrame(results)
print(df_baseball)

#print(type(cursor.description))
#print(type(cursor.description[0]))
#print(cursor.description)
    
from mysql.connector import FieldType

for i in range(len(cursor.description)):
  #print("Column {}:".format(i+1))
  desc = cursor.description[i]
  #print("  column_name = {}".format(desc[0]))
  #print("  type = {} ({})".format(desc[1], FieldType.get_info(desc[1])))
  #print("  null_ok = {}".format(desc[6]))
  #print("  column_flags = {}".format(desc[7]))

headers = [i[0] for i in cursor.description]
#print(headers)
#print(type(headers))

playerName = list(df_baseball[0] + ", " + df_baseball[1])



df_baseball = pd.DataFrame(results, columns = [headers[0],headers[1],headers[2],headers[3],headers[4],headers[5],headers[6],headers[7],headers[8],headers[9],headers[10],
                                      headers[11],headers[12],headers[13],headers[14],headers[15],headers[16],headers[17],headers[18],headers[19],headers[20],
                                      headers[21],headers[22],headers[23],headers[24],headers[25],headers[26],headers[27],headers[28],
                                      headers[29],headers[30],headers[31],headers[32],headers[33],headers[34],headers[35],headers[36]],index=playerName)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


#print(df_baseball)

###DATA FRAME CLEANING SECTION*********************************************************************** 
print('*----data frame cleaning-------*')

df_baseball.reset_index(level=0, inplace=True)
df_baseball=df_baseball.rename(columns={'index': 'player_name'})
df_baseball = df_baseball.rename(columns={'3B':'Triples'})

                   #df = df.rename(columns={'$a':'a'})

df_baseball['B_Avg']= (df_baseball['H']/df_baseball['AB'])
df_baseball.B_Avg = df_baseball.B_Avg.round(3)
df_baseball['birthday_C'] = pd.to_datetime(dict(year=df_baseball.birthyear, month=df_baseball.birthMonth, day=df_baseball.birthday))
df_baseball['CY']=2019
df_baseball['age']= df_baseball['CY']-df_baseball['birthyear']


##still need to delete rows with nulls
df_baseball.dropna()
df_baseball=df_baseball.drop(['nameFirst','nameLast','birthyear','birthMonth','birthday','CY'],axis=1 )
print(df_baseball.head())

###****END DATA CLEANING***************************************************************************
###****Question Section****************************************************************************
print('-------Question section----------')
print("which player had the most RBI's between 2015 and 2018")
df_RBI = df_baseball[['player_name','playerID','yearID','RBI',]]
df_RBI = df_RBI[df_RBI.yearID != 2019]
df_RBI = df_RBI[df_RBI.yearID != 2014]

PlayerRBI=(df_RBI.groupby(['player_name']).RBI.sum())
PlayerRBI=PlayerRBI.sort_values(ascending=False)
print(PlayerRBI.head())
print("The player with the most RBI's between 2015 and 2018 is: ", PlayerRBI.iloc[:1])

###Albert Puljols section Albert, Pujols
print('******************************************')
print("How many double plays did Albert Puljols ground into in 2016?")

        #df.loc[df['column_name'] == some_value]
df_GIDP = df_baseball[['player_name','playerID','yearID','GIDP',]]
            ###***setrow index code******myDataFrame.set_index('column_name')
            ###df[df['model'].str.match('Mac')]
df_GIDP_Albert=df_GIDP[df_GIDP['player_name'].str.match('Albert, Pujols')]
print(df_GIDP_Albert.head())
print('Albert Puljols grounded into:', df_GIDP_Albert.iloc[3,3],'double plays in 2016')

###MATPLOTLIB QUESTIONS
print('********************MATPLOTLIB QUESTIONS******************************************************')
##had issues using 3B in an aggredation used a different syntax in the end  -- df = df.rename(columns={'$a':'a'})
##grouping stolen bases an triples
print('******************TRIPLES/STOLEN BASES DataFrame*******************************************')
print(df_baseball.describe())                                 
df_3b = (df_baseball.groupby(['yearID'])['Triples','SB'].sum())##sum triples and SB to given year
### PlayerRBI=(df_RBI.groupby(['player_name']).RBI.sum())
print(df_3b.describe())


##Histograms
df_baseball.hist(column='Triples',bins=15)
plt.title("Triples player Counts")
plt.xlabel("number of triples")
plt.ylabel("player count for triples")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

df_3b.hist(column='Triples',bins=10)
plt.title("Sum Triples between 2014 and 2019")
plt.xlabel("Total triples count by year")
plt.ylabel("Triple bin counts by year")
plt.xticks([700,720,740,760,780,800,820,840,860,880])
plt.yticks([1,2])



##ScatterPlotts
df_baseball.plot(kind='scatter',x='SB',y='Triples')
plt.xlabel("Plalyer Stolen Bases")
plt.ylabel("Player Triples")

print('The correlation coefficient for all stolen bases and triples is: ',df_baseball['Triples'].corr(df_baseball['SB']).round(2))
##simple pandascorrelation method#table['Group'].corr(table['Age'])
 
df_3b.plot(kind='scatter',x='SB',y='Triples')
plt.xlabel( "Stolen Bases by year")
plt.ylabel("Triples by year")
print('The correlation coefficient for stolen bases and triples by year is: ',df_3b['Triples'].corr(df_3b['SB']).round(2))
#plt.show()
#print(df_baseball.head())

###MY QUESTIONS
##Question #1
print("My three question**********************************************************************************")
print("#1.  which U.S. state originated the most players")
df_origin= df_baseball[["birthCountry","birthState"]]
df_origin_USA=df_origin[df_origin["birthCountry"].str.match("USA")]
### filter for USA only:  df_GIDP_Albert=df_GIDP[df_GIDP['player_name'].str.match('Albert, Pujols')] or df_RBI = df_RBI[df_RBI.yearID != 2019]
#df_origin = df_origin[df_origin.birthCountry == USA]           
print(df_origin_USA.describe())
origin_dist=df_origin_USA.groupby(["birthState"]).birthState.count()
print(origin_dist)

###Question #2
print('does player size have a direct impact on power numbers***************************')
df_powerSize=df_baseball[["Height","Weight","HR","2B","RBI","SO"]]
#print(df_powerSize.head())
df_powerSize["powerIndex"]=np.sqrt((df_powerSize["Height"]**2 + df_powerSize["Weight"]**2)/2)
print(df_powerSize.head())
df_powerSize.plot(kind='scatter', x="powerIndex", y="HR")
print("Homerun correlation",df_powerSize["powerIndex"].corr(df_powerSize["HR"]).round(2))
plt.title("PowerIndex x Homeruns")

df_powerSize.plot(kind='scatter', x="powerIndex", y="2B")
print("Doubles correlation: ", df_powerSize["powerIndex"].corr(df_powerSize["2B"]).round(2))
plt.title("PowerIndex x Doubles")

df_powerSize.plot(kind='scatter', x="powerIndex", y="RBI")
print('RBI correlation: ', df_powerSize["powerIndex"].corr(df_powerSize["RBI"]).round(2))
plt.title("PowerIndex x Runs Batted In")

df_powerSize.plot(kind='scatter', x="powerIndex", y="SO")
print('Strike Outs correlation: ', df_powerSize["powerIndex"].corr(df_powerSize["SO"]).round(2))
plt.title("PowerIndex x Strike Outs")

#plt.show()
###QUESTION #3
print("Do left handed batters have better batting statistics?")
df_LeftvRight=df_baseball[['player_name','bats','B_Avg', 'HR','RBI','SO']]

print(df_LeftvRight.groupby(['bats']).mean())
#print(df_LeftvRight.groupby(['bats']).max())

print("on average left handed batters have a slightly higher batting average and produce three more RBI's")
print("But, left handed batters also strike out 5 times more than righthanded batters.")


##new SQL query
print('***************NEW SQL QUERY FOR PITCHING DATA*************')
cursor = cnx.cursor()
sql = """
SELECT p.nameFirst, p.nameLast, p.Height, p.Weight, p.throws,
p.birthCountry,p.birthState,p.birthCity,pi.yearID, pi.G, pi.W, pi.L, pi.ER, pi.ERA, pi.BB,pi.SO

FROM People p
JOIN Pitching pi ON pi.playerID = p.playerID

WHERE pi.yearID between 2014 and 2019 AND pi.g >= "10"
ORDER BY pi.yearID Desc
#LIMIT 50;
"""

cursor.execute(sql)
results_2 = cursor.fetchall()
for x in results_2:
    pass
    #print(x)

pitch = pd.DataFrame(results_2)


playerName_2 = list(pitch[0] + ", " + pitch[1])

pitch = pd.DataFrame(results_2, columns = ['nameFirst','nameLast','Height','Weight','throws','birthCountry','birthState','birthCity','yearID','G',
                                                      'W','L','ER','ERA','BB','SO'],index=playerName_2)
print(pitch.head())
pitch.reset_index(level=0, inplace=True)
pitch=pitch.rename(columns={'index': 'player_name'})
pitch=pitch.drop(['nameFirst','nameLast'],axis=1)
pitch.dropna()


print(pitch.head())
#df_baseball=df_baseball.drop(['nameFirst','nameLast','birthyear','birthMonth','birthday','CY'],axis=1 )
##Pitching data Questions****************************
print('******************************************Pitching data questions***********************************************************')
print('Do left handed pitchers have more wins and strike outs compared to righthanded pitchers?')

print(pitch.groupby(['throws']).mean())

pitch.plot(kind='scatter',x='SO',y='ERA')
print('The correlation coefficient for Strikeouts and ERA is: ',pitch['SO'].corr(pitch['ERA']).round(2))
plt.title('STRIKEOUTS x ERA')
plt.xlabel("Strikeouts")
plt.ylabel("ERA")

print('Intersting pitching trends from 2014-2019')
pitch_trends=pitch.groupby(["yearID"])["SO","ERA","BB"].mean()
pitch_trends.plot(subplots=True)
#plt.title('Yearly Trends')

plt.show()


























