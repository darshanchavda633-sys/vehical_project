import json
try:
    with open("vehical.json", "r") as f:
        vehical_list = json.load(f)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    vehical_list = []
while True:
    print("***********************")
    
    print("1.Insert data")
    print("2.update data")
    print("3.Delete Data")
    print("4.show data")
    print("5.Exit")

    choice=int(input("Enter your choice : "))
    #insert data

    if choice==1:
        vehical={}
        vehical_id=int(input("Enter vehicle_id : "))
        vehical_name=input("Enter vehical name :")
        vehical_type=input("Enter vehical type : ")
        owner_name=input("Enter owner name : ")
        registration_no=input("Enter registration_no :")
        contact=int(input("Enter contact number :"))

        vehical["vehical_id"]=vehical_id
        vehical["vehical_name"]=vehical_name
        vehical["vehical_type"]=vehical_type
        vehical["owner_name"]=owner_name
        vehical["registration_no"]=registration_no
        vehical["contact"]=contact

        vehical_list.append(vehical)

        with open("vehical.json","w") as f:
            json.dump(vehical_list,f,indent=4)
        print("Data insert successfully !! ")

    #update data

    elif choice==2:
        vehical_id=int(input("Enter vehical ID : "))
        found=False
        for vehical in vehical_list:
            if vehical["vehical_id"]==vehical_id:
                print("vehical found ! Enter new data !")

                
                vehical["vehical_name"]=input("Enter vehical name :")
                vehical["vehical_type"]=input("Enter vehical type : ")
                vehical["owner_name"]=input("Enter owner name : ")
                vehical["registration_no"]=input("Enter registration_no :")
                vehical["contact"]=int(input("Enter contact number :"))

                found=True
                break
            if found:
                with open("vehical.json","w") as f:
                    json.dump(vehical_list,f,indent=4)
                print("data updated successfully")
            else:
                print("vehical not found")

    # delete data

    elif choice==3:
        vehical_id=int(input("Enter vehical ID :"))
        found=False
        for vehical in vehical_list:
          
            if vehical["vehical_id"]==vehical_id:
                vehical_list.remove(vehical)
                found=True
                break
        if found:
            with open("vehical.json","w") as f:
                json.dump(vehical_list,f,indent=4)
            print("vehical deleted successfully !")
        else:
            print("vehical not found !")

    # show data
    elif choice==4:
        if not vehical_list:
            print ("No data available  ! ")
        else:
            print("===vehical Data=====")
            for vehical in vehical_list:
                print("----------------------------------")
                print("ID : ",vehical["vehical_id"])
                print("NAME: ",vehical["vehical_name"])
                print("TYPE : ",vehical["vehical_type"])
                print("OWNER NAME : ",vehical["owner_name"])
                print("Registration Number  : ",vehical["registration_no"])
                print("CONTACT : ",vehical["contact"])

    # Exit this program
    elif choice==5:
        print("Exit")
        break
    else:
        print("Invalid choice ! please select 1 or 2 ")


    
    
