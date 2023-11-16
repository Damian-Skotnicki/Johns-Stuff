from firebase import firebase
import time
myDBConn = firebase.FirebaseApplication('https://amazing-school-work-default-default-rtdb.europe-west1.firebasedatabase.app/',None)

data = {
    "ID":2,
    "age":21,
    "name":"John",
    "surname":"Alter"
    }

myDBConn.patch('/User0/'+str(int(time.time() * 1000)),data)

result = myDBConn.get('/User0/',None)
print(result)
for key in result:
    print(type(result[key]))
    for k,v in result[key].items():
        print(k +" -- "+str(v))
    print(key)
    

    

