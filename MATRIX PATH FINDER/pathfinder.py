# m-[]
print("sathya")
matrix=([2,1,0,0,0],[0,1,0,1,0],[0,1,0,1,0],[0,1,0,1,0],[0,0,0,1,4])
#matrix=([2,0,0,0,0],[0,0,0,0,0],[0,0,0,4,0],[0,0,0,0,0],[0,0,0,0,0])
# m[5][5]=array.{0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0}
#for i in range(0,5):
    #a=[]
    #for j in range(0,5):
        #a.append(int(input()))
    #matrix.append(a)
for i in range(0,5):
    for j in range(0,5):
        print(matrix[i][j],end=" ")
print("looped completely MATRIX BUILT")
w=int(input("number of walls to build"))
#place to input number of walls and start and end point of finder
#for g in range(w):
    #wr=int(input("enter row number"))
    #wc=int(input("enter colomn number"))
    #matrix[wr][wc]=0
def ending():
    print("PATH FOUND")
e=0
t=0
for z in range(0,5):
    for i in range(0,5):
        for j in range(0,5):
            if(matrix[i][j]==3 or matrix[i][j]==2):
                if(j!=4 and matrix[i][j+1]==0):
                    matrix[i][j+1]=3
                if(j!=0 and matrix[i][j-1]==0):
                    matrix[i][j-1]=3
                if(i!=0 and matrix[i-1][j]==0):
                    matrix[i-1][j]=3 
                if(i!=4 and matrix[i+1][j]==0):
                    matrix[i+1][j]=3
                if(j!=0 and i!=0 and matrix[i-1][j-1]==0): 
                    matrix[i-1][j-1]=3
                if(j!=4 and i!=4 and matrix[i+1][j+1]==0): 
                    matrix[i+1][j+1]=3
                if(j!=4 and i!=0 and matrix[i-1][j+1]==0):
                    matrix[i-1][j+1]=3
                if(j!=0 and i!=4 and matrix[i+1][j-1]==0):
                    matrix[i+1][j-1]=3
                
                if(j!=4 and matrix[i][j+1]==4):
                    ending()
                if(j!=0 and matrix[i][j-1]==4):
                    ending()
                if(i!=0 and matrix[i-1][j]==4):
                    ending() 
                if(i!=4 and matrix[i+1][j]==4):
                    ending()
                if(j!=0 and i!=0 and matrix[i-1][j-1]==4): 
                    ending()
                if(j!=4 and i!=4 and matrix[i+1][j+1]==4): 
                    ending()
                if(j!=4 and i!=0 and matrix[i-1][j+1]==4):
                    ending()
                if(j!=0 and i!=4 and matrix[i+1][j-1]==4):
                    ending()
            
    print("while")    
                
for i in range(0,5):
    for j in range(0,5):
        if(matrix[i][j]==2):
            print("0",end=" ")
        if(matrix[i][j]==3):
            print("T",end=" ")
        if(matrix[i][j]==4):
            print("O",end=" ")
        if(matrix[i][j]==1):
            print("*",end=" ")
        #print(matrix[i][j],end=" ")
    print("")
