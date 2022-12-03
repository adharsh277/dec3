import datetime  
birthday=input("Enter your Date of Birth (in DD/MM/YYYY) ")  
birthdate=datetime.datetime.strptime(birthday,"%d/%m/%Y").date()  
today=datetime.date.today();  
days=today-birthdate;  
print("Total Days lived on earth till today's date without counting the leap year:", days.days);  
a= (int(today.strftime('%Y'))-int(birthdate.strftime('%Y'))) #for counting the leap year
print("This is the total years you lived:",a) 
b=a//4 # Now divided by four to know the leap years dates
print("This the number of yours leap years dates:", b)
print("So now this is the actual number of days you lived in earth till today's date including the count of leap years:",days.days-b);
Footer
