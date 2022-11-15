with open('earthquakes.txt') as file:
    file.readline()
    content=file.readlines()
    biglist=[]
    for i in content:
        newlist=i.split()
        for j in range(1,len(newlist)-7):
            newlist[7]+=' '+newlist[7+j]
        newlist=newlist[:8]
        biglist.append(newlist)


    locations={}
    largerlist=[]
    greater_than_five_count=len(content)
    for i in biglist:
        sublist=[]
        greatlist=[]
        majorlist=[]
        stronglist=[]
        moderatelist=[]
        magnitude=float(i[1])
        if i[-1] not in locations:

            if magnitude <5.0:
                greater_than_five_count-=1
                pass
            elif magnitude >=5.0 and magnitude <=5.9:
                moderatelist.append(magnitude)
            elif magnitude >=6.0 and magnitude <=6.9:
                stronglist.append(magnitude)
            elif magnitude >=7.0 and magnitude <=7.9:
                majorlist.append(magnitude)
            else:
                greatlist.append(i[1])
            sublist.append(moderatelist)
            sublist.append(stronglist)
            sublist.append(majorlist)
            sublist.append(greatlist)
            locations[i[-1]]=sublist
        else:
            if magnitude <5.0:
                greater_than_five_count-=1
                pass
            elif  magnitude >=5.0 and magnitude <=5.9:
                locations[i[-1]][0].append(magnitude)
            elif  magnitude >=6.0 and magnitude <=6.9:
                locations[i[-1]][1].append(magnitude)
            elif  magnitude >=7.0 and magnitude <=7.9:
                locations[i[-1]][2].append(magnitude)
            else:
                locations[i[-1]][3].append(magnitude)
            
##    for i in locations:
##        print(i,locations[i])

        countdict={}
    for i in locations:
        quakecount=[]
        quakecount.append(len(locations[i][0]))
        quakecount.append(len(locations[i][1]))
        quakecount.append(len(locations[i][2]))
        quakecount.append(len(locations[i][3]))
        quakecount.append(len(locations[i][0]) + len(locations[i][1]) +len(locations[i][2])+len(locations[i][3]) )
        countdict[i]=quakecount

##    for i in countdict:
##        print(i,countdict[i])
    
    quakecount=0
    for i in countdict:
        if countdict[i][-1] > quakecount:
            mostquakes=i
            quakecount=countdict[i][-1]
    print('Processing Complete!')

    for i in countdict:
        spacescount=45-len(i)
        spaces=spacescount*' '
        if countdict[i][0]>9:
            spaces0=' '
        else:
            spaces0='  '
        if countdict[i][1]>9:
            spaces1=' '
        else:
            spaces1='  '
        if countdict[i][2]>9:
            spaces2=' '
        else:
            spaces2='  '
            
        #print('{}{}{}{}{}{}{}{}{}'.format(i,spaces,countdict[i][0],spaces0,countdict[i][1],spaces1,countdict[i][2],spaces2,countdict[i][3]))
##
        with open('earthquakes-sorted.csv','w') as file:
            file.writelines('Region,Moderate,Strong,Major,Great,Overall\n')
            for i in countdict:
                overall=countdict[i][0]+countdict[i][1]+countdict[i][2]+countdict[i][3]
                file.write('{},{},{},{},{},{}\n'.format(str(i.replace(',','-')),countdict[i][0],countdict[i][1],countdict[i][2],countdict[i][3],overall))

        with open('summary.txt','w') as file2:
            file2.write('{} had the most quakes with {} earthquakes\n'.format(mostquakes,quakecount))
            file2.write('{} locations have more than  magnitude 5 earthquakes\n'.format(greater_than_five_count))