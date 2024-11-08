username = input("Enter ur user name, it must be of 6 character: ")

if len(username) == 6:
    print('length is ok')
    if username.isalpha():
         print('username is ok')
    else:
         print('username is not ok') 

else:
     print('length is not ok')

