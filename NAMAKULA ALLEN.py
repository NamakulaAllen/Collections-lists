student_marks = [60,80,90, 98]
#data type of student_name
#print(type(student_marks))
print(student_marks)

#list accessing positive
print(student_marks[2])
#negative
print(student_marks[-2])


#list slicing
print(student_marks[1:2])

#checking if item exists
#if 80 in student_marks:
 #print("Yes,80 is in exist")
#else:
 #print("no, 80 doesnt exist")

 #change 80 to 89 in the list
student_marks [1] = 89
print(student_marks)

 #add a new item 55(apend a new list)
student_marks = [60, 80, 90,98]
student_marks.append(55)
print(student_marks)

#find the size of the list having added 55
print(len(student_marks))

#write a python program to sum all items in the list

total=sum(student_marks)
print(total)


#Write a python function that takes two lists and returns if they have atleast one common member.
list1 = input("Enter items 1;")
list2 =input("Enter items 2;")


  