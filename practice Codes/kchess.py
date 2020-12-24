'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
for _ in range(int(input())):
    n= int(input())
    z=[]
    for _ in range(n):
        x,y= map(int,input().split())
        z.append([x,y])
        
    k=[int(i) for i in input().split()]
    p=[k, [ k[0]-1, k[1] ], [ k[0]-1,k[1]-1 ], [ k[0],k[1]-1 ],[ k[0]+1,k[1]+1 ] ,[ k[0],k[1]+1 ],[ k[0]+1,k[1] ],
       [k[0]+1,k[1]-1], [ k[0]-1,k[1]+1 ] ]
    #count=0
    for j in z:
        t= [j[0]+2,j[1]+1]
        u= [j[0]+1,j[1]+2]
        v= [j[0]+2,j[1]-1]
        w= [j[0]+1,j[1]-2]
        s= [j[0]-2,j[1]+1]
        o= [j[0]-1,j[1]+2]
        m= [j[0]-2,j[1]-1]
        g= [j[0]-1,j[1]-2]
        
        if t in p:
            p.remove(t)
            
        if u in p:
            p.remove(u)
            
        if v in p:
            p.remove(v)
            
        if w in p:
            p.remove(w)
            
        if s in p:
            p.remove(s)
            
        if o in p:
            p.remove(o)
            
        if m in p:
            p.remove(m)
            
        if g in p:
            p.remove(g)
            
        if len(p)==0:
            break
            
    if len(p)==0:
        print("YES")
    else:
        print("NO")