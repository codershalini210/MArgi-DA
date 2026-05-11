data = [ [10, 20, 30],
         [40, 50, 60],
         [70, 80, 90]]

# data[0][0]  ,data[0][1],data[0,2]  
# data[1][0]  ,data[1][1],data[1,2]  
# data[2][0]  ,data[2][1],data[2,2]  


collength = len(data[0])
rowlength = len(data)
for col in range(collength):
    sum = 0 
    for row in  range(rowlength):
        sum = sum + data[row][col]
    print(sum ,end=" - ")



# for i in data :
#     for j in i:
#         print(j,end=" ")
#     print("")