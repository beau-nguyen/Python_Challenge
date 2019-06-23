#Dependencies
import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath, newline='') as csvfile:

    #set variable
    vote_count= []
    candidatelist = []
    unique_candidate= []
    vote_percent= []
    count=0

        
 # Initialize csv.writer
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   

    
    print(csvreader)

    for row in csvreader:   
        vote_count.append(row[1])
        candidatelist.append(row[2])

        count= count + 1

    for x in set(candidatelist):
        unique_candidate.append(x)

        y= candidatelist.count(x)
        vote_count.append(y) 

        a= (y/count) *100
        vote_percent.append(a)


        
print("Election Results")   
print("-------------------") 
print(f"Total Votes: {len(vote_count)}")
for i in range(len(unique_candidate)):
          print(unique_candidate[i]) 
          print(str(vote_percent[i]) + "%")
          

text_file = open("main.txt","w",newline='')

text_file.write(("Finacial Analysis"))
text_file.write("--------------------")
text_file.write(f"Total Votes: {len(vote_count)}")
for i in range(len(unique_candidate)):      
    text_file.write(unique_candidate[i])
    text_file.write(str(vote_percent[i]))
text_file.close()          

