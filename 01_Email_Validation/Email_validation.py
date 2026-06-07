import re

email=input('Enter Email: ')
#  Ya condition check kara ga pahla ka start [a-z] tak ho phir [._] dono ma sa aik dafa aya phir
#  [@] aik dafa aya Phir [.] -2,-3 number pa aik dafa aya $ sign (-)ve ko show karta ha  
email_condition='^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'    

if re.search(email_condition,email):
    print('Valid Email.........')
else:
    print('Invalid Email!!!!!!')
