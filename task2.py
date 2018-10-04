import csv   
import tabulate
with open('Crime.csv', 'r') as myfile:  #pe the csv file
  csv_read = csv.reader(myfile)
  crime_type=[]     #contains all crimes
  crime_id=[]       #contains all crime ids
  li= []
  print (csv_read)   #gives object id of the file 
  for line in csv_read:  
	  c_id=line[7]
	  c_type=line[8]
	
	  crime_type.append(c_type)  
	  crime_id.append(c_id)
	  c=list(zip(crime_type,crime_id))  #zip the crime type and crime ids together in a list
          
  print(c)


  for t in c:
       cli_count=0
	
  
	for b in c:
		if b[0]==t[0]:
			li_count=li_count+1
	print(t, li_count)
	li.append((t,li_count))
   print(li)























