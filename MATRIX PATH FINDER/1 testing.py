print("hello world")
def test():
    print("into the function")
test()
class bus:
    s="oh apdiys visayam"
    z=0
    def classcall(self):
        fcc="FCC CALL"
        print("callin through class")
        print(fcc)
q=bus()
print(q.s)
print(q.z)
q.classcall()
def rec(x):
    x=x%5
    if(x==0):
        return x
    else:
        rec(x)
def pqwe(t,s):
    print("PQWE PRINTER")
    for i in range(0,5):
        for j in range(0,5):
            print(t[i][j],end=" ")
        print("")
    print("PRINTING STARTING VALUE hdfghrfghfg",s)
    exit()

def mre(q,i,j,g):
    print("CALL",i,j)
    if(j==5):
        if(i==4 and j==5):
            print("AT END OF MATRIX")
            print("IN MRE FUNCTION")
            g+=1
            pqwe(q,g)
        else:
            print("IN")
            j=0
            i+=1
            mre(q,i,j,g)
    if(q[i][j]==4):
        print("THIS IS FOUR MRE")
        if(i!=0 and i!=4 and j!=0 and j!=4):
            if(q[i-1][j]==3 or q[i-1][j-1]==3 or q[i-1][j+1]==3 or q[i][j-1]==3 or q[i+1][j-1]==3 or q[i+1][j]==3 or q[i+1][j+1]==3 or q[i][j+1]==3):
                pqwe(q,g)
                exit()
    if(q[i][j]==3):
        print("HERE")
        print(i,j)
        if(j!=4 and q[i][j+1]==0):
            q[i][j+1]=3
            j+=1
            mre(q,i,j,g)
        if(j!=0 and q[i][j-1]==0):
            q[i][j-1]=3
            j+=1
            mre(q,i,j,g)
        if(i!=0 and q[i-1][j]==0):
            q[i-1][j]=3
            j+=1
            mre(q,i,j,g) 
        if(i!=4 and q[i+1][j]==0):
            q[i+1][j]=3
            j+=1
            mre(q,i,j,g)
        if(j!=0 and i!=0 and q[i-1][j-1]==0): 
            q[i-1][j-1]=3
            j+=1
            mre(q,i,j,g)
        if(j!=4 and i!=4 and q[i+1][j+1]==0): 
            q[i+1][j+1]=3
            j+=1
            mre(q,i,j,g)
        if(j!=4 and i!=0 and q[i-1][j+1]==0):
            q[i-1][j+1]=3
            j+=1
            mre(q,i,j,g)
        if(j!=0 and i!=4 and q[i+1][j-1]==0):
            q[i+1][j-1]=3
            j+=1
            mre(q,i,j,g)
        if(q[i][j]==4):
            print("REACHED END FOUND 4 AT",i,j)
        else:
            print("CALLED ELSE")
            j=j+1
            print(j)
            mre(q,i,j,g)
    else:
        j=j+1
        mre(q,i,j,g)







def end(v,x):
    for i in range(0,5):
        for j in range(0,5):
            print(v[i][j],end=" ")
        print("")
    print("PE")
    if(x<5):
        mrec(v,0,0,x)
    else:
        mre(v,0,0,x)
m=25
a=rec(m)
#c=([3,1,0,0,0],[0,1,0,1,0],[0,1,0,1,0],[0,1,0,1,0],[0,0,0,1,4])
#c=([3,0,0,0,0],[0,0,0,0,0],[0,0,0,4,0],[0,0,0,0,0],[0,0,0,0,0])
c=([1,1,1,1,1],[1,1,1,1,1],[1,1,4,0,1],[1,1,1,0,3],[1,1,1,1,1])
o=0
print("REMAINDER",a)
def mrec(q,i,j,u):
    print("CALL",i,j)
    if(j==5):
        if(i==4 and j==5):
            print("AT END OF MATRIX")
            u+=1
            end(q,u)
        else:
            print("IN")
            j=0
            i+=1
            mrec(q,i,j,u)
    if(q[i][j]==4):
        if(i!=0 and i!=4 and j!=0 and j!=4):
            if(q[i-1][j]==3 or q[i-1][j-1]==3 or q[i-1][j+1]==3 or q[i][j-1]==3 or q[i+1][j-1]==3 or q[i+1][j]==3 or q[i+1][j+1]==3 or q[i][j+1]==3):
                print("THIS IS FOUR")
                pqwe(q,u)
    if(q[i][j]==3):
        print("HERE")
        print(i,j)
        if(j!=4 and q[i][j+1]==0):
            print("1")
            q[i][j+1]=3
            j+=1
            mrec(q,i,j,u)
        if(j!=0 and q[i][j-1]==0):
            q[i][j-1]=3
            j+=1
            mrec(q,i,j,u)
        if(i!=0 and q[i-1][j]==0):
            q[i-1][j]=3
            j+=1
            mrec(q,i,j,u) 
        if(i!=4 and q[i+1][j]==0):
            print("2")
            q[i+1][j]=3
            j+=1
            mrec(q,i,j,u)
        if(j!=0 and i!=0 and q[i-1][j-1]==0): 
            q[i-1][j-1]=3
            j+=1
            mrec(q,i,j,u)
        if(j!=4 and i!=4 and q[i+1][j+1]==0):
            print("3") 
            q[i+1][j+1]=3
            j+=1
            mrec(q,i,j,u)
        if(j!=4 and i!=0 and q[i-1][j+1]==0):
            q[i-1][j+1]=3
            j+=1
            mrec(q,i,j,u)
        if(j!=0 and i!=4 and q[i+1][j-1]==0):
            q[i+1][j-1]=3
            j+=1
            mrec(q,i,j,u)
        if(q[i][j]==4):
            print("REACHED END FOUND 4 AT",i,j)
        else:
            print("CALLED ELSE")
            j=j+1
            print(j)
            mrec(q,i,j,u)
    else:
        j=j+1
        mrec(q,i,j,u)

w=0
e=0

y=0
mrec(c,0,0,y)


#mrec(b,w,e)
#mrec(b,w,e)

#mrec(b,w,e)
#mrec(b,w,e)
print("OUT OF FUNC")