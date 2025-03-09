#creating Dictionaries
student={'name': 'Elvis Iyasele', 'Grade':8,'Age':12,'Fav Color':'red','Occupation':'IT Engineer'}
print(student)
student['Age']=13
print(student)
student['Gender' ]='Male'
print(student)
#pop
student.pop('Fav Color')
print(student)
print(student['name'])
student.clear()
print(student)
