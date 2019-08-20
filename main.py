import header as h

counter = 0;
with open("/afs/cern.ch/user/i/ibordule/public/list.txt", "r") as f:
    for line in f:
        splitted_line = line.split("\t")
        if line[0] != 'E':  #If this is not a first line
            counter += 1
            h.EQIPMENT_IDs += [splitted_line[0]] 
            h.OTHER_IDs += [splitted_line[2]]
            h.MTF_IDs += [splitted_line[3]]
            h.SerNums += [splitted_line[4]]
            if splitted_line[5] == "":
                h.Correct_OTHER_IDs += [splitted_line[6]]
                h.Correct_SerNums += [splitted_line[7][:-1]] #The last symbol is \n
            else:
                h.Correct_OTHER_IDs += [splitted_line[5]]
                h.Correct_SerNums += [splitted_line[6][:-1]] #The last symbol is \n

with open("new_list.txt", "w") as f:
    f.write('EQIPMENT_ID\tOTHER_ID\tMTF_ID\t\tSerNum\t\tCorrect_OTHERID\tCorrect_SerNum\tDuplicates\tRemove_or_Keep\n')

#Calculate dupes
    for i in range(0, len(h.OTHER_IDs)):
        Number_of_dupes = 0;
        for j in range(0, len(h.OTHER_IDs)):
            if (i != j) and (h.Correct_OTHER_IDs[i] == h.Correct_OTHER_IDs[j]):
                Number_of_dupes += 1
        h.Dupes += [Number_of_dupes]
#Decide, which dupe we will keep in base, and which we will remove. See the rule.
    for i in range(0, len(h.Dupes)):
        if h.Dupes[i] != 0:
            for j in range(0, len(h.Correct_OTHER_IDs)): #Look again for all Dupes of this chip
                if (h.Correct_OTHER_IDs[i] == h.Correct_OTHER_IDs[j]) and (i != j): #If we found one
                    if i < j: # And it is first in our list
                        h.Remove_or_Keep += ['K'] #we will keep it
                        break
                    else:
                        h.Remove_or_Keep += ['R'] #... remove it
                        break
        else: # if this chip has no Dupes
            h.Remove_or_Keep += ['K']
        f.write(h.EQIPMENT_IDs[i] +  "\t\t" + h.OTHER_IDs[i] + "\t" + h.MTF_IDs[i] + "\t" + h.SerNums[i] + "\t\t" + h.Correct_OTHER_IDs[i] + "\t" + h.Correct_SerNums[i] + "\t\t" + str(h.Dupes[i]) + "\t\t" + h.Remove_or_Keep[i] + "\n")    
