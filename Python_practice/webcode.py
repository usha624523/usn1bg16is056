username=dict()
username={'usha123':'1234','uk1234':'624523'}
name=input("enter username:")
pw=input("enter password")
while username[name]==pw:
        print("login succesfull!")
        break
else:
    print("invalid!")
    
