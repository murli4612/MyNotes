def passed_studentd(students, scores):
    # print(students)
    map1 = {}
    result_passed =[]
    for student  in students:
        id = student.get("id")
        name = student.get("name")
        map1[id] = name
    for score in scores:
        id = score.get("id")
        marks = score.get('marks')
        
        if id in map1 and marks > 35:
            result_passed.append(map1.get(id))
    return ",".join(result_passed)
            
            
            
    
        
students = [
       { "id": 1 , "name": "Murli"},
       {"id": 2 , "name": "Manohar"},
       { "id": 3 , "name": "Mohan"}
]
    
    
    
scores = [
    {"id": 1 , "marks": 60},
    { "id": 2 , "marks": 33},
    {"id": 3 , "marks": 57}
        
]
    
    
# select st.id, st.name , sc.marks 
# from students As st  
# join scores as sc 
# on st.id = sc.id
    
# print(passed_studentd(students,score))


def frequency_count(stringA):
    
    freq_count = {}
    
    for char in stringA:
        # if char in freq_count:
        freq_count[char]  = freq_count.get(char,0) + 1
            
        # else:
        #     freq_count[char] = 1
            
    for key, value in freq_count.items():
        if value > 1:
            print(key ,"---->",value)
            
print(frequency_count("waterwate"))