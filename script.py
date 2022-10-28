import os
import csv


fic = open('usercache.json', 'r')
ndata = fic.read()
fic.close()

ndata = ndata.replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace('"', "").replace("name:", "").replace("uuid:", "")
ndata_list = ndata.split(",")


i = 0
while i < len(ndata_list):
    i += 2
    ndata_list.pop(i)
 
    
ndata_list_pseudo = []
for e in ndata_list:
    ndata_list_pseudo.append(e)   
i = 0
while i < len(ndata_list_pseudo):
    i += 1
    ndata_list_pseudo.pop(i)  


ndata_list_uuid = []
for e in ndata_list:
    ndata_list_uuid.append(e)
i = 0
while i < len(ndata_list_uuid)-1:
    ndata_list_uuid.pop(i)
    i += 1


i1, i2 = 0, 0
ndata_dic_keypseudo = {}
while i1 < len(ndata_list_uuid) and i2 < len(ndata_list_pseudo):
    ndata_dic_keypseudo[ndata_list_pseudo[i1]] = ndata_list_uuid[i2]
    i1, i2 = i1 + 1, i2 + 1
i1, i2 = 0, 0
ndata_dic_keyuuid = {}
while i1 < len(ndata_list_uuid) and i2 < len(ndata_list_pseudo):
    ndata_dic_keyuuid[ndata_list_uuid[i1]] = ndata_list_pseudo[i2]
    i1, i2 = i1 + 1, i2 + 1

sdata_dic = {}
sdata_list_all =[]
for i1 in range(len(ndata_list_uuid)):
    if os.path.exists(ndata_list_uuid[i1]+'.json'):
        fic = open(ndata_list_uuid[i1]+'.json','r')
        sdata = fic.read()
        fic.close()
        
        
        sdata = sdata.replace('"', "").replace("stats:", "").replace("}", "|").replace("{", "|")
        sdata_list = sdata.split("|")
        sdata_list.pop(0)
        sdata_list.pop(0)
        sdata_list.pop(len(sdata_list)-1)
        sdata_list.pop(len(sdata_list)-1)
        sdata_list.pop(len(sdata_list)-1)


        for i2 in range(1, len(sdata_list), 2):
            sdata_list[i2] = sdata_list[i2].split(",")
        
    
   
        for i3 in range(1, len(sdata_list), 2):    
            i4 = 0
            for e in sdata_list[i3]:
                sdata_list[i3][i4] = sdata_list[i3-1].replace("_", " ").replace("minecraft:", "").replace(":", " ").replace(", ", "").replace(",", "") + e.replace(",", "").replace("_", " ").replace("minecraft:", "")
                i4 += 1            
             
        
        for i5 in range(0, int(len(sdata_list)/2)):
            sdata_list.pop(i5)
            
        sdata_list_all.append(ndata_list_pseudo[i1])
        sdata_list_all.append(sdata_list)
        

        
    else:
        print(ndata_dic_keyuuid[ndata_list_uuid[i1]], "does unfortunately not exist in stats with uuid", ndata_list_uuid[i1])



mcdata_list = []
for i in range(1, len(sdata_list_all), 2):
    i1 = 0
    for e1 in sdata_list_all[i]:
        i2 = 0
        for e2 in e1:
            sdata_list_all[i][i1][i2] = e2.split(":")
            i2 += 1
        i1 += 1   

    for i1 in range(len(sdata_list_all[i])):
        
        for i2 in range(len(sdata_list_all[i][i1])):        
            mcdata_list.append(sdata_list_all[i][i1][i2][0])
        


mcdata_list_killed = []
mcdata_list_killed_by = []
mcdata_list_custom = []
mcdata_list_mined = []
mcdata_list_used = []
mcdata_list_crafted = []
mcdata_list_picked_up = []
mcdata_list_all = []
for e in mcdata_list:

    if e.startswith("killed by"):
        if e not in mcdata_list_killed_by:
            mcdata_list_killed_by.append(e)

            
    if e.startswith("killed"):
        if e not in mcdata_list_killed_by and e not in mcdata_list_killed:
            mcdata_list_killed.append(e)
                        
    if e.startswith("custom"):
        if e not in mcdata_list_custom:
            mcdata_list_custom.append(e.replace("custom ", ""))
                    
    if e.startswith("mined"):
        if e not in mcdata_list_mined:
            mcdata_list_mined.append(e)
            
    if e.startswith("used"):
        if e not in mcdata_list_used:
            mcdata_list_used.append(e)
            
    if e.startswith("crafted"):
        if e not in mcdata_list_crafted:
            mcdata_list_crafted.append(e)

    if e.startswith("picked up"):
        if e not in mcdata_list_picked_up:
            mcdata_list_picked_up.append(e)
            
for e in mcdata_list_killed_by:
    mcdata_list_all.append(e)
for e in mcdata_list_killed:
    mcdata_list_all.append(e)
for e in mcdata_list_custom:
    mcdata_list_all.append(e)
for e in mcdata_list_mined:
    mcdata_list_all.append(e)
for e in mcdata_list_used:
    mcdata_list_all.append(e)
for e in mcdata_list_crafted:
    mcdata_list_all.append(e)
for e in mcdata_list_picked_up:
    mcdata_list_all.append(e)


if not os.path.exists('data.csv'):
    with open('data.csv', 'w'): pass
 
 

for i in range(int(len(sdata_list_all)/2)):
    sdata_list_all.pop(i)



sdata_list_all_0 = []
i = 0
for e in sdata_list_all:
    i1 = 0
    sdata_list_all_1 = []
    for e1 in sdata_list_all[i]:
        i2 = 0
        for e2 in sdata_list_all[i][i1]:
            for e3 in sdata_list_all[i][i1][i2]:
                sdata_list_all_1.append(e3.replace("custom ", ""))
            i2 += 1
        i1 += 1
    sdata_list_all_0.append(sdata_list_all_1)
    i += 1
   
  
mcsdata = []
for e in mcdata_list_all:
    mcsdata.append(e)
    
for i0 in range(len(sdata_list_all_0)):
    i = 0
    for e in mcdata_list_all:
        if e not in sdata_list_all_0[i0]:
            mcsdata[i] = mcsdata[i] + ",0"
        i += 1
    for i in range(0, len(sdata_list_all_0[i0]), 2): 
        i1 = 0     
        for e in mcdata_list_all:  
            if sdata_list_all_0[i0][i] == e:
                mcsdata[i1] = mcsdata[i1] + "," + sdata_list_all_0[i0][i+1]  
            i1 +=1   


ndata_list_pseudo_csv = ["Data"]
for e in ndata_list_pseudo:
    ndata_list_pseudo_csv.append(e)
  


fic = open('data.csv', 'w')

for e in ndata_list_pseudo_csv:
    fic.write(e + ",")
fic.write("\n")

mcsdata1 = []
for e in mcsdata:
    if e not in mcsdata1:
        mcsdata1.append(e)
        
    
for e in mcsdata1:  
    fic.write(e)
    fic.write("\n")
    
fic.close()

print("Done !")
   
