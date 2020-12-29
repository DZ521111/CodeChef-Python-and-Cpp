'''
Author : Dhruv B Kakadiya

'''
x=[]
for i in range(int(input())):
    y,w,p,c1,c2,c3,c4,d1,d2,d3,d4=[],[],[],0,0,0,0,0,0,0,0
    for j in range(12):
        y.append(input())
    for j in y:
        j=j.split()
        w.append(j[0]),w.append(j[4])
    [t1,t2,t3,t4]=list(set(w))
    for i in y:
        b=i.split()
        c=[int(k) for k in b if k.isdigit()]
        if c[0]>c[1]:
            p.append([b[0],3,c[0]-c[1]])
            p.append([b[4],0,c[1]-c[0]])
        if c[0]==c[1]:
            p.append([b[0],1,0])
            p.append([b[4],1,0])
        if c[1]>c[0]:
            p.append([b[4],3,c[1]-c[0]])
            p.append([b[0],0,c[0]-c[1]])
    for j in range(len(p)):
        if p[j][0]==t1:
            c1+=p[j][1]
            d1+=p[j][2]
        elif p[j][0]==t2:
            c2+=p[j][1]
            d2+=p[j][2]
        elif p[j][0]==t3:
            c3+=p[j][1]
            d3+=p[j][2]
        elif p[j][0]==t4:
            c4+=p[j][1]
            d4+=p[j][2]
    y=[[t1,c1,d1],[t2,c2,d2],[t3,c3,d3],[t4,c4,d4]]
    for i in range(len(y)):
        for j in range(len(y)):
            if i!=j:
                if y[j][1]<y[i][1]:y[j],y[i]=y[i],y[j]
                elif y[j][1]==y[i][1]:
                    if y[j][2]<y[i][2]:
                        y[j],y[i]=y[i],y[j]
    x.append([y[0][0],y[1][0]])
for i in range(len(x)):
    print(x[i][0],' ',x[i][1])