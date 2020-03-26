#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:27:31 2020

@author: oskargeddon
"""
import pandas as pd
from operator import itemgetter, attrgetter, methodcaller
print('Какой турнир вы хотите выбрать?\n 1-Итальянская лига серии A,2-USA MLS')
n=int(input())
a=[int(i) for i in range(6,72)]
print(a)
if n==2:
    t='USA.csv'
else:
    t='I1.csv'
unik_teams=[]
a=['Team Name','Number of games played','Number of wins','Number of draws','Number of losses','Goal difference','Points','Ranking place']
df = pd.read_csv(t)
if n!=2:
    df.rename(columns={'FTHG':'HG','FTAG':'AG','HomeTeam':'Home','AwayTeam':'Away'},inplace=True)
    df.drop(df.iloc[:, 6:73], inplace = True, axis = 1)#удаляем ненужное
else:
    df.drop(['Res', 'PH','PD','PA','MaxH','MaxD','MaxA','AvgH','AvgD','AvgA'], axis='columns', inplace=True)#чистим датасет
def given_name(team):
    X_team=df[(df['Home'].str.contains(team) | df['Away'].str.contains(team))]
    return(X_team)
def given_date(date):
    date.replace('.','/')
    Y_maches=df[(df['Date'].str.contains(date))]
    return(Y_maches)
print(given_date('21/07/2012'))
for index, row in df.iterrows():
    print(index, row)
    if [row['Home']] not in unik_teams:
        unik_teams.append([row['Home']])
    if [row['Away']] not in unik_teams:
        unik_teams.append([row['Away']])
if n==2:
    for i in unik_teams:
        i.append(0)#games played(i[0]-team name)    1
        i.append(0)#wins    2
        i.append(0)#draws   3
        i.append(0)#loses   4
        i.append(0)#diiference  5
        i.append(0)#poits   6
        i.append(0)#place   7
        i.append(0)#goals 8
    for index, row in df.iterrows():
        print(index, row)
        for i in unik_teams:
            if (row['Home']==i[0] or row['Away']==i[0]):#количество сыгранных матчей
                i[1]=i[1]+1
            if row['Home']==i[0] and row['HG']>row['AG']:#победы
                i[2]=i[2]+1
                i[5]=i[5]+row['HG']-row['AG']#difference
                i[8]=i[8]+row['HG']
            if row['Away']==i[0] and row['AG']>row['HG']:#победы
                i[2]=i[2]+1
                i[5]=i[5]+row['AG']-row['HG']#difference
                i[8]=i[8]+row['AG']
            if ((row['Away']==i[0] or row['Home']==i[0]) and (row['AG']==row['HG'])):#ничьи
                i[3]=i[3]+1
            if row['Away']==i[0] and row['AG']<row['HG']:#поражения,можно было посчитать как матчи-победы-ничьи
                i[4]=i[4]+1
                i[5]=i[5]+row['AG']-row['HG']#difference
                i[8]=i[8]+row['AG']
            if row['Home']==i[0] and row['HG']<row['AG']:#поражения,можно было посчитать как матчи-победы-ничьи
                i[5]=i[5]+row['HG']-row['AG']#difference
                i[4]=i[4]+1
                i[8]=i[8]+row['HG']
            #для ничей differece всегда=0
            #формирование списков закончено,щас будем делать поинты и расставлять по местам сортировкой
   
    for i in unik_teams:
        i[6]=i[2]*3+i[3]#начисляем поинты по нашим правилам
    s = sorted(unik_teams, key=itemgetter(6),reverse=True)#вначале сортируем по очкам
    sorted(s,key=itemgetter(5),reverse=True)#потом по разности пропущенных и забытых голов
    sorted(s,key=itemgetter(8),reverse=True)#потом по количеству забитых голов
    for i in  range (len(s)):
        s[i][7]=i+1
    s.insert(0,a)
    for i in range(1,len(s)):
        for k in range(i,len(s)):
            if (s[i][6]==s[k][6] and s[i][8]==s[k][8]):#если так произошло что кол-во голов и поинты одинаковые, приравниваем место в таблице
                t=s[i][7]
                s[k][7]=t
    for i in range(len(s)-1):#приводим уменьшаем места дальше, так как образуется пробел если этого не сделать
        if s[i][7]==s[i+1][7]:
            for k in range(i+2,len(s)):
                s[k][7]=s[k][7]-1
    print(s)
    for row in s:
        for elem in row:
            print(elem, end=' ')
        print()
    dt=pd.DataFrame(s)
    dt.to_csv('filename4task2U9.csv', index=False)
else:
    for i in unik_teams:
        i.append(0)#games played(i[0]-team name)    1
        i.append(0)#wins    2
        i.append(0)#draws   3
        i.append(0)#loses   4
        i.append(0)#diiference  5
        i.append(0)#poits   6
        i.append(0)#place   7
        i.append(0)#goals 8
    for index, row in df.iterrows():
        print(index, row)
        for i in unik_teams:
            if (row['Home']==i[0] or row['Away']==i[0]):#количество сыгранных матчей
                i[1]=i[1]+1
            if row['Home']==i[0] and row['HG']>row['AG']:#победы
                i[2]=i[2]+1
                i[5]=i[5]+row['HG']-row['AG']#difference
                i[8]=i[8]+row['HG']
            if row['Away']==i[0] and row['AG']>row['HG']:#победы
                i[2]=i[2]+1
                i[5]=i[5]+row['AG']-row['HG']#difference
                i[8]=i[8]+row['AG']
            if ((row['Away']==i[0] or row['Home']==i[0]) and (row['AG']==row['HG'])):#ничьи
                i[3]=i[3]+1
            if row['Away']==i[0] and row['AG']<row['HG']:#поражения,можно было посчитать как матчи-победы-ничьи
                i[4]=i[4]+1
                i[5]=i[5]+row['AG']-row['HG']#difference
                i[8]=i[8]+row['AG']
            if row['Home']==i[0] and row['HG']<row['AG']:#поражения,можно было посчитать как матчи-победы-ничьи
                i[5]=i[5]+row['HG']-row['AG']#difference
                i[4]=i[4]+1
                i[8]=i[8]+row['HG']
            
        #для ничей differece всегда=0
        #формирование списков закончено,щас будем делать поинты и расставлять по местам сортировкой
    for i in unik_teams:
        i[6]=i[2]*3+i[3]#начисляем поинты по нашим правилам
    s = sorted(unik_teams, key=itemgetter(6),reverse=True)#вначале сортируем по очкам
    for i in  range(len(s)):
        s[i][7]=i+1
    s.insert(0,a)
    for i in range(len(s)-1):#это самая сложная сортировка по многим параметрам
        if s[i][6]==s[i+1][6]:
            a=s[i][0]
            b=s[i+1][0]
            k=i+1
            aw=0#победы команды а
            bw=0#побелы команды b
            ag=0#голы команды a
            bg=0#голы команды b
            d1=s[i][5]#разность голов для а
            d2=s[i+1][5]#разность голов для b
            maxa=0#максимум голов в матче для а
            maxb=0#максимум голов в матче для b
            for index, row in df.iterrows():
                print(index, row)
                if ((row['Home']==a) and (row['Away']==b) and (row['HG']>row['AG'])):
                    aw=aw+1
                    ag=ag+row['HG']
                    if row['HG']>maxa:#смотрим максимальное кол-во голов только в матче в котором команда выиграла,так как в том в котором проиграла у другой команды будет точно больше и смотреть бессмысленно
                        maxa=row['HG']
                if ((row['Home']==a) and (row['Away']==b) and (row['HG']<row['AG'])):
                    bw=bw+1
                    bg=bg+row['AG']
                    if row['AG']>maxb:
                        maxb=row['AG']
                if ((row['Away']==a) and (row['Home']==b) and (row['AG']<row['HG'])):
                    bw=bw+1
                    bg=bg+row['HG']
                    if row['HG']>maxb:
                        maxb=row['HG']
                if ((row['Home']==a) and (row['Away']==b) and (row['HG']<row['AG'])):
                    aw=aw+1
                    ag=ag+row['AG']
                    if row['AG']>maxa:
                        maxa=row['AG']
                if (row['Away']==a) and (row['Home']==b) and (row['AG']==row['HG']) and (maxa>row['AG']):
                    maxa=row['AG']
                if (row['Away']==a) and (row['Home']==b) and (row['AG']==row['HG']) and (maxb>row['HG']):
                    maxb=row['HG']
                if ((row['Home']==a or row['Away']==b) and (row['AG']==row['HG'])) and (maxb>row['HG']):
                    maxb=row['HG']
                if ((row['Home']==a or row['Away']==b) and (row['AG']==row['HG'])) and (maxa>row['AG']):
                    maxa=row['AG']
                    
            if bw>aw:#у нас и так в таблице будет так
                dt=pd.DataFrame(s)
                dt.to_csv('filename4task3.csv', index=False)#делаем таблицу и выходим из программы
                exit
            if aw>bw:
                s[i+1],s[i]=s[i],s[i+1]
            if aw==bw:
                if ag<bg:
                    dt=pd.DataFrame(s)
                    dt.to_csv('filename4task3.csv', index=False)#делаем таблицу и выходим из программы у нас и так в таблице такое расположение
                    exit
                if ag>bg:
                    s[i+1],s[i]=s[i],s[i+1]
                if ag==bg:
                    if d1<d2:
                        dt=pd.DataFrame(s)
                        dt.to_csv('filename4task3.csv', index=False)#делаем таблицу и выходим из программы у нас и так в таблице такое расположение
                        exit
                    if d1>d2:
                        s[i+1],s[i]=s[i],s[i+1]
                    if d1==d2:
                        if maxa<maxb:
                            dt=pd.DataFrame(s)
                            dt.to_csv('filename4task3.csv', index=False)#делаем таблицу и выходим из программы у нас и так в таблице такое расположение
                            exit
                        if maxa>maxb:
                            s[i+1],s[i]=s[i],s[i+1]
                        if maxa==maxb:
                            t=s[i][7]
                            s[k][7]=t
                            for i in range(len(s)-1):#приводим уменьшаем места дальше, так как образуется пробел если этого не сделать
                                if s[i][7]==s[i+1][7]:
                                    for k in range(i+2,len(s)):
                                        s[k][7]=s[k][7]-1
    dt=pd.DataFrame(s)
    dt.to_csv('filename4task3.csv', index=False)
    #РЕЗУЛЬТАТ СМОТРЕТЬ В CSV ФАЙЛЕ НА КОМПЬЮТЕРЕ!
                        
                            
                            
                            
                        
                        
                    
                    
                    
                
                
                    
                
            
            
            
      
        
    

