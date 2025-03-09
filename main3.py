#list to dictionaries
def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result
student=[[1,'john doe',7],[2,'jane doe',3]]
print("original list is: ",student)
print(test(student))