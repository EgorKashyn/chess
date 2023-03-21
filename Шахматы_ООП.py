#!/usr/bin/env python
# coding: utf-8

# In[1]:


letters1={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}
class Board(object):
    def __init__(self):
        self.board=[[Dot('A1','None') for j in range(8)] for i in range(8)]
    def printboard(self):
        s1=[' ',' ','A','B','C','D','E','F','G','H',' ',' ']
        s2=[' ' for i in range(12)]
        for line in s1:
            print(line, end=' ')
        print()
        for line in s2:
            print(line, end=' ')
        print()
        for j in range(len(self.board),0,-1):
            line=self.board[abs(j-8)]
            s=[str(j), ' ']+line+[' ', str(j)]
            for i in s:
                print(i, end=' ')
            print()
        for line in s2:
            print(line, end=' ')
        print()           
        for line in s1:
            print(line, end=' ')
        print()


# In[6]:


letters={'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7}
class Figure(Board):
    def __init__(self,a):
        self.x=letters[a[0]]
        self.y=8-int(a[1])
    def move(self,a):
        x1=letters[a[0]]
        y1=8-int(a[1])
        x2=letters[a[3]]
        y2=8-int(a[4])
        board.board[y2][x2]=board.board[self.y][self.x]
        self.x=x2
        self.y=y2
        board.board[y1][x1]=Dot('A1','None')
class Dot(Figure):
    def __init__(self,a,side):
        super().__init__(a)
        self.side=side
    def __str__(self):
        return '.'
    def chek_dvish2(self,a):
        return False
class King(Figure):
    def __init__(self,a,side):
        super().__init__(a)
        self.side=side
    def __str__(self):
        return 'k' if self.side=='black' else 'K'
    def move(self,a):
        x1=letters[a[0]]
        y1=8-int(a[1])
        x2=letters[a[3]]
        y2=8-int(a[4])
        board.board[y2][x2]=board.board[self.y][self.x]
        self.x=x2
        self.y=y2
        board.board[y1][x1]=Dot('A1','None')
    def chek_dvish(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and board.board[y2][x2]=='.':
            if abs(self.x-x2)==1 and abs(self.y-y2)==1 or abs(self.x-x2)==0 and abs(self.y-y2)==1 or abs(self.x-x2)==1 and abs(self.y-y2)==0:
                return True
            else:
                print("Ход не может быть совершен, попробуйте снова")
            return False
        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
            if abs(self.x-x2)==1 and abs(self.y-y2)==1 or abs(self.x-x2)==0 and abs(self.y-y2)==1 or abs(self.x-x2)==1 and abs(self.y-y2)==0:
                return True
            else:
                print("Ход не может быть совершен, попробуйте снова")
            return False
        else:
            print("Ход не может быть совершен, попробуйте снова")
            return False
    def chek_dvish2(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and board.board[y2][x2]=='.':
            if abs(self.x-x2)==1 and abs(self.y-y2)==1 or abs(self.x-x2)==0 and abs(self.y-y2)==1 or abs(self.x-x2)==1 and abs(self.y-y2)==0:
                return True
            else:
                return False
        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
            if abs(self.x-x2)==1 and abs(self.y-y2)==1 or abs(self.x-x2)==0 and abs(self.y-y2)==1 or abs(self.x-x2)==1 and abs(self.y-y2)==0:
                return True
            else:
                return False
        else:
            return False

class Queen(Figure):
    def __init__(self,a,side):
        super().__init__(a)
        self.side=side
    def __str__(self):
        return 'q' if self.side=='black' else 'Q'
    def move(self,a):
        x1=letters[a[0]]
        y1=8-int(a[1])
        x2=letters[a[3]]
        y2=8-int(a[4])
        board.board[y2][x2]=board.board[self.y][self.x]
        self.x=x2
        self.y=y2
        board.board[y1][x1]=Dot('A1','None')
    def chek_dvish(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        k=2
              #диагональ
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and board.board[y2][x2]=='.':
            if abs(self.x-x2)==abs(self.y-y2):
                k=0
                if self.x>x2 and self.y>y2 or self.x<x2 and self.y<y2:
                    for i in range(min(self.y,y2)+1, max(self.y,y2)):
                        for j in range(min(self.x,x2)+1, max(self.x,x2)): 
                            if board.board[i][j]!='.':
                                k+=1
                else:
                    q1=self.x
                    q2=self.y
                    if self.y>y2:
                        for i in range(1,self.y-y2):
                            q1=self.x+i
                            q2=self.y-i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                k+=1
                    else:
                        for i in range(1, y2-self.y):
                            q1=self.x-i
                            q2=self.y+i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                    k+=1
            elif (self.x-x2==0 or self.y-y2==0) and ((self.x-x2)**2 + (self.y-y2)**2)!=0:
                k=0
                if x2-self.x==0:
                    a1=min(self.y,y2)
                    a2=max(self.y,y2)
                    for i in range(a1+1,a2):
                        if board.board[i][self.x]!=Dot('A1','None'):
                            k+=1
                else:
                    a1=min(self.x,x2)
                    a2=max(self.x,x2)
                    for i in range(a1+1,a2):
                        if board.board[self.y][i]!=Dot('A1','None'):
                            k+=1
            if k<1:
                return True
            else:
                print("Ход не может быть совершен, попробуйте снова")
                return False

        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
            if abs(self.x-x2)==abs(self.y-y2):
                k=0
                if self.x>x2 and self.y>y2 or self.x<x2 and self.y<y2:
                    for i in range(min(self.y,y2)+1, max(self.y,y2)):
                        for j in range(min(self.x,x2)+1, max(self.x,x2)): 
                            if board.board[i][j]!=Dot('A1','None'):
                                k+=1
                else:
                    q1=self.x
                    q2=self.y
                    if self.y>y2:
                        for i in range(1,self.y-y2):
                            q1=self.x+i
                            q2=self.y-i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                k+=1
                    else:
                        for i in range(1, y2-self.y):
                            q1=self.x-i
                            q2=self.y+i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                    k+=1
            elif (self.x-x2==0 or self.y-y2==0) and ((self.x-x2)**2 + (self.y-y2)**2)!=0:
                k=0
                if x2-self.x==0:
                    a1=min(self.y,y2)
                    a2=max(self.y,y2)
                    for i in range(a1+1,a2):
                        if board.board[i][self.x]!=Dot('A1','None'):
                            k+=1
                else:
                    a1=min(self.x,x2)
                    a2=max(self.x,x2)
                    for i in range(a1+1,a2):
                        if board.board[self.y][i]!=Dot('A1','None'):
                            k+=1
            if k<1:
                return True
            else:
                print("Ход не может быть совершен, попробуйте снова")
                return False
        else:
            print("Ход не может быть совершен, попробуйте снова")
            return False
    def chek_dvish2(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        k=2
              #диагональ
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and board.board[y2][x2].__class__.__name__ == 'Dot':
            if abs(self.x-x2)==abs(self.y-y2):
                k=0
                if self.x>x2 and self.y>y2 or self.x<x2 and self.y<y2:
                    for i in range(min(self.y,y2)+1, max(self.y,y2)):
                        for j in range(min(self.x,x2)+1, max(self.x,x2)): 
                            if board.board[i][j]!=Dot('A1','None'):
                                k+=1
                else:
                    q1=self.x
                    q2=self.y
                    if self.y>y2:
                        for i in range(1,self.y-y2):
                            q1=self.x+i
                            q2=self.y-i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                k+=1
                    else:
                        for i in range(1, y2-self.y):
                            q1=self.x-i
                            q2=self.y+i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                    k+=1
            elif (self.x-x2==0 or self.y-y2==0) and ((self.x-x2)**2 + (self.y-y2)**2)!=0:
                k=0
                if x2-self.x==0:
                    a1=min(self.y,y2)
                    a2=max(self.y,y2)
                    for i in range(a1+1,a2):
                        if board.board[i][self.x]!=Dot('A1','None'):
                            k+=1
                else:
                    a1=min(self.x,x2)
                    a2=max(self.x,x2)
                    for i in range(a1+1,a2):
                        if board.board[self.y][i]!=Dot('A1','None'):
                            k+=1
            if k<1:
                return True
            else:
                return False

        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
            if abs(self.x-x2)==abs(self.y-y2):
                k=0
                if self.x>x2 and self.y>y2 or self.x<x2 and self.y<y2:
                    for i in range(min(self.y,y2)+1, max(self.y,y2)):
                        for j in range(min(self.x,x2)+1, max(self.x,x2)): 
                            if board.board[i][j]!=Dot('A1','None'):
                                k+=1
                else:
                    q1=self.x
                    q2=self.y
                    if self.y>y2:
                        for i in range(1,self.y-y2):
                            q1=self.x+i
                            q2=self.y-i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                k+=1
                    else:
                        for i in range(1, y2-self.y):
                            q1=self.x-i
                            q2=self.y+i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                    k+=1
            elif (self.x-x2==0 or self.y-y2==0) and ((self.x-x2)**2 + (self.y-y2)**2)!=0:
                k=0
                if x2-self.x==0:
                    a1=min(self.y,y2)
                    a2=max(self.y,y2)
                    for i in range(a1+1,a2):
                        if board.board[i][self.x]!=Dot('A1','None'):
                            k+=1
                else:
                    a1=min(self.x,x2)
                    a2=max(self.x,x2)
                    for i in range(a1+1,a2):
                        if board.board[self.y][i]!=Dot('A1','None'):
                            k+=1
            if k<1:
                return True
            else:
                return False
        else:
            return False


class Rook(Figure):
    def __init__(self,a,side):
        super().__init__(a)
        self.side=side
    def __str__(self):
        return 'r' if self.side=='black' else 'R'
    def move(self,a):
        x1=letters[a[0]]
        y1=8-int(a[1])
        x2=letters[a[3]]
        y2=8-int(a[4])
        board.board[y2][x2]=board.board[self.y][self.x]
        self.x=x2
        self.y=y2
        board.board[y1][x1]=Dot('A1','None')
    def chek_dvish(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        k=2
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and board.board[y2][x2].__class__.__name__ == 'Dot':
            if (self.x-x2==0 or self.y-y2==0) and ((self.x-x2)**2 + (self.y-y2)**2)!=0:
                k=1
                if x2-self.x==0:
                    a1=min(self.y,y2)
                    a2=max(self.y,y2)
                    for i in range(a1+1,a2):
                        if board.board[i][self.x]!=Dot('A1','None'):
                            k+=1
                else:
                    a1=min(self.x,x2)
                    a2=max(self.x,x2)
                    for i in range(a1+1,a2):
                        if board.board[self.y][i]!=Dot('A1','None'):
                            k+=1
            if k<2:
                return True
            else:
                print("Ход не может быть совершен, попробуйте снова")
                return False
        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
            if (self.x-x2==0 or self.y-y2==0) and ((self.x-x2)**2 + (self.y-y2)**2)!=0:
                k=1
                if x2-self.x==0:
                    a1=min(self.y,y2)
                    a2=max(self.y,y2)
                    for i in range(a1+1,a2):
                        if board.board[i][self.x]!=Dot('A1','None'):
                            k+=1
                else:
                    a1=min(self.x,x2)
                    a2=max(self.x,x2)
                    for i in range(a1+1,a2):
                        if board.board[self.y][i]!=Dot('A1','None'):
                            k+=1
            if k<2:
                return True
            else:
                print("Ход не может быть совершен, попробуйте снова")
                return False
        else:
            print("Ход не может быть совершен, попробуйте снова")
            return False
    def chek_dvish2(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        k=2
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and board.board[y2][x2].__class__.__name__ == 'Dot':
            if (self.x-x2==0 or self.y-y2==0) and ((self.x-x2)**2 + (self.y-y2)**2)!=0:
                k=1
                if x2-self.x==0:
                    a1=min(self.y,y2)
                    a2=max(self.y,y2)
                    for i in range(a1+1,a2):
                        if board.board[i][self.x]!=Dot('A1','None'):
                            k+=1
                else:
                    a1=min(self.x,x2)
                    a2=max(self.x,x2)
                    for i in range(a1+1,a2):
                        if board.board[self.y][i]!=Dot('A1','None'):
                            k+=1
            if k<2:
                return True
            else:
                return False
        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
            if (self.x-x2==0 or self.y-y2==0) and ((self.x-x2)**2 + (self.y-y2)**2)!=0:
                k=1
                if x2-self.x==0:
                    a1=min(self.y,y2)
                    a2=max(self.y,y2)
                    for i in range(a1+1,a2):
                        if board.board[i][self.x]!=Dot('A1','None'):
                            k+=1
                else:
                    a1=min(self.x,x2)
                    a2=max(self.x,x2)
                    for i in range(a1+1,a2):
                        if board.board[self.y][i]!=Dot('A1','None'):
                            k+=1
            if k<2:
                return True
            else:
                return False
        else:
            return False
class Knight(Figure):
    def __init__(self,a,side):
        super().__init__(a)
        self.side=side
    def __str__(self):
        return 'n' if self.side=='black' else 'N'
    def move(self,a):
        x1=letters[a[0]]
        y1=8-int(a[1])
        x2=letters[a[3]]
        y2=8-int(a[4])
        board.board[y2][x2]=board.board[self.y][self.x]
        self.x=x2
        self.y=y2
        board.board[y1][x1]=Dot('A1','None')
    def chek_dvish(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and board.board[y2][x2].__class__.__name__ == 'Dot':
            if (self.x-x2)!=0 and (self.y-y2)!=0 and (abs(self.x-x2)+abs(self.y-y2))==3:
                return True
            else:
                print('Ход не может быть совершен, попробуйте снова')
                return False
        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
            if (self.x-x2)!=0 and (self.y-y2)!=0 and (abs(self.x-x2)+abs(self.y-y2))==3:
                return True
            else:
                print('Ход не может быть совершен, попробуйте снова')
                return False
        else:
            print('Ход не может быть совершен, попробуйте снова')
            return False
    def chek_dvish2(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and board.board[y2][x2].__class__.__name__ == 'Dot':
            if (self.x-x2)!=0 and (self.y-y2)!=0 and (abs(self.x-x2)+abs(self.y-y2))==3:
                return True
            else:
                return False
        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
            if (self.x-x2)!=0 and (self.y-y2)!=0 and (abs(self.x-x2)+abs(self.y-y2))==3:
                return True
            else:
                return False
        else:
            return False
class Bishop(Figure):
    def __init__(self,a,side):
        super().__init__(a)
        self.side=side
    def __str__(self):
        return 'b' if self.side=='black' else 'B'
    def move(self,a):
        x1=letters[a[0]]
        y1=8-int(a[1])
        x2=letters[a[3]]
        y2=8-int(a[4])
        board.board[y2][x2]=board.board[self.y][self.x]
        self.x=x2
        self.y=y2
        board.board[y1][x1]=Dot('A1','None')
    def chek_dvish(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        k=2
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and board.board[y2][x2].__class__.__name__ == 'Dot':
              #диагональ
            if abs(self.x-x2)==abs(self.y-y2):
                k=0
                if self.x>x2 and self.y>y2 or self.x<x2 and self.y<y2:
                    for i in range(min(self.y,y2)+1, max(self.y,y2)):
                        for j in range(min(self.x,x2)+1, max(self.x,x2)): 
                            if board.board[i][j]!=Dot('A1','None'):
                                k+=1
                else:
                    q1=self.x
                    q2=self.y
                    if self.y>y2:
                        for i in range(1,self.y-y2):
                            q1=self.x+i
                            q2=self.y-i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                k+=1
                    else:
                        for i in range(1, y2-self.y):
                            q1=self.x-i
                            q2=self.y+i
                            if board.board[q2][q1]!='.':
                                    k+=1
            if k<1:
                return True
            else:
                print("Ход не может быть совершен, попробуйте снова")
                return False
        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
              #диагональ
            if abs(self.x-x2)==abs(self.y-y2):
                k=0
                if self.x>x2 and self.y>y2 or self.x<x2 and self.y<y2:
                    for i in range(min(self.y,y2)+1, max(self.y,y2)):
                        for j in range(min(self.x,x2)+1, max(self.x,x2)): 
                            if board.board[i][j]!=Dot('A1','None'):
                                k+=1
                else:
                    q1=self.x
                    q2=self.y
                    if self.y>y2:
                        for i in range(1,self.y-y2):
                            q1=self.x+i
                            q2=self.y-i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                k+=1
                    else:
                        for i in range(1, y2-self.y):
                            q1=self.x-i
                            q2=self.y+i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                    k+=1
            if k<1:
                return True
            else:
                print("Ход не может быть совершен, попробуйте снова")
                return False
        else:
            print("Ход не может быть совершен, попробуйте снова")
            return False
    def chek_dvish2(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        k=2
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and board.board[y2][x2].__class__.__name__ == 'Dot':
              #диагональ
            if abs(self.x-x2)==abs(self.y-y2):
                k=0
                if self.x>x2 and self.y>y2 or self.x<x2 and self.y<y2:
                    for i in range(min(self.y,y2)+1, max(self.y,y2)):
                        for j in range(min(self.x,x2)+1, max(self.x,x2)): 
                            if board.board[i][j]!=Dot('A1','None'):
                                k+=1
                else:
                    q1=self.x
                    q2=self.y
                    if self.y>y2:
                        for i in range(1,self.y-y2):
                            q1=self.x+i
                            q2=self.y-i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                k+=1
                    else:
                        for i in range(1, y2-self.y):
                            q1=self.x-i
                            q2=self.y+i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                    k+=1
            if k<1:
                return True
            else:
                return False
        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
              #диагональ
            if abs(self.x-x2)==abs(self.y-y2):
                k=0
                if self.x>x2 and self.y>y2 or self.x<x2 and self.y<y2:
                    for i in range(min(self.y,y2)+1, max(self.y,y2)):
                        for j in range(min(self.x,x2)+1, max(self.x,x2)):
                            if board.board[i][j].__class__.__name__ != 'Dot':
#                             if board.board[i][j]!=Dot('A1','None'):
                                k+=1
                else:
                    q1=self.x
                    q2=self.y
                    if self.y>y2:
                        for i in range(1,self.y-y2):
                            q1=self.x+i
                            q2=self.y-i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                k+=1
                    else:
                        for i in range(1, y2-self.y):
                            q1=self.x-i
                            q2=self.y+i
                            if board.board[q2][q1]!=Dot('A1','None'):
                                    k+=1
            if k<1:
                return True
            else:
                return False
        else:
            return False
class Pawn(Figure):
    def __init__(self,a,side):
        super().__init__(a)
        self.side=side
    def __str__(self):
        return 'p' if self.side=='black' else 'P'
    def move(self,a):
        x1=letters[a[0]]
        y1=8-int(a[1])
        x2=letters[a[3]]
        y2=8-int(a[4])
        board.board[y2][x2]=board.board[self.y][self.x]
        self.x=x2
        self.y=y2
        board.board[y1][x1]=Dot('A1','None')
    def chek_dvish(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and x1==x2 and board.board[y2][x2].__class__.__name__ == 'Dot':
            if (abs(self.y-y2)==1 and self.x==x2 or abs(self.y-y2)==2 and x1==x2 and (self.side=='white' and self.y==6 or self.side=='black' and self.y==1) or abs(self.x-x2)==1 and abs(self.y-y2)==1 and board.board[y2][x2]!=Dot('A1','None')):
                return True
            else:
                print("Ход не может быть совершен, попробуйте снова")
                return False
        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
            if (abs(self.y-y2)==1 and self.x==x2 or abs(self.y-y2)==2 and x1==x2 and (self.side=='white' and self.y==6 or self.side=='black' and self.y==1) or abs(self.x-x2)==1 and abs(self.y-y2)==1 and board.board[y2][x2]!=Dot('A1','None')):
                return True
            else:
                print("Ход не может быть совершен, попробуйте снова")
                return False
        else:
            print("Ход не может быть совершен, попробуйте снова")
            return False
    def chek_dvish2(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        if (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and x1==x2 and board.board[y2][x2].__class__.__name__ == 'Dot':
            if (abs(self.y-y2)==1 and self.x==x2 or abs(self.y-y2)==2 and x1==x2 and (self.side=='white' and self.y==6 or self.side=='black' and self.y==1) or abs(self.x-x2)==1 and abs(self.y-y2)==1 and board.board[y2][x2]!=Dot('A1','None')):
                return True
            else:
                return False
        elif (n%2==0 and self.side=='white' or n%2!=0 and self.side=='black') and self.side!=board.board[y2][x2].side:
            if (abs(self.y-y2)==1 and self.x==x2 or abs(self.y-y2)==2 and x1==x2 and (self.side=='white' and self.y==6 or self.side=='black' and self.y==1) or abs(self.x-x2)==1 and abs(self.y-y2)==1 and board.board[y2][x2]!=Dot('A1','None')):
                return True
            else:
                return False
        else:
            return False
class Menister(Figure):
    def __init__(self,a,side):
        super().__init__(a)
        self.side=side
    def __str__(self):
        return 'm' if self.side=='black' else 'M'
    def move(self,a):
        x1=letters[a[0]]
        y1=8-int(a[1])
        x2=letters[a[3]]
        y2=8-int(a[4])
        board.board[y2][x2]=board.board[self.y][self.x]
        self.x=x2
        self.y=y2
        board.board[y1][x1]=Dot('A1','None')
    def chek_dvish(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        if abs(self.y-y2)==1 and abs(self.x-x2)==1 and board.board[y2][x2].__class__.__name__ == 'Dot':
            return True
        elif abs(self.y-y2)==1 and abs(self.x-x2)==1 and self.side!=board.board[y2][x2].side:
              return True
        else:
            print("Ход не может быть совершен, попробуйте снова")
            return False
    def chek_dvish2(self,a):
        x2=letters[a[3]]
        y2=8-int(a[4])
        if abs(self.y-y2)==1 and abs(self.x-x2)==1 and board.board[y2][x2].__class__.__name__ == 'Dot':
            return True
        elif abs(self.y-y2)==1 and abs(self.x-x2)==1 and self.side!=board.board[y2][x2].side:
              return True
        else:
            return False
def net_korol(k1,K1):
    korol={k1 : 0, K1 : 0}
    for i in range(8):
        for j in range(8):
            if board.board[i][j] == k1:
                korol[k1] = 1
            elif board.board[i][j] == K1:
                korol[K1] = 1
    if not korol[k1]:
        print('игра закончена, победили белые')
        return True
    elif not korol[K1]:
        print('игра закончена, победили черные')
        return True
    else:
        return False


# In[9]:


letters={'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7}
letters1={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}
board=Board()
r1=Rook('A8','black')
board.board[r1.y][r1.x]=r1
r2=Rook('H8','black')
board.board[r2.y][r2.x]=r2
R1=Rook('A1','white')
board.board[R1.y][R1.x]=R1
R2=Rook('H1','white')
board.board[R2.y][R2.x]=R2

n1=Knight('B8','black')
board.board[n1.y][n1.x]=n1
n2=Knight('G8','black')
board.board[n2.y][n2.x]=n2
N1=Knight('B1','white')
board.board[N1.y][N1.x]=N1
N2=Knight('G1','white')
board.board[N2.y][N2.x]=N2

b1=Bishop('C8','black')
board.board[b1.y][b1.x]=b1
b2=Bishop('F8','black')
board.board[b2.y][b2.x]=b2
B1=Bishop('C1','white')
board.board[B1.y][B1.x]=B1
B2=Bishop('F1','white')
board.board[B2.y][B2.x]=B2

q1=Queen('D8','black')
board.board[q1.y][q1.x]=q1
Q1=Queen('D1','white')
board.board[Q1.y][Q1.x]=Q1

k1=King('E8','black')
board.board[k1.y][k1.x]=k1
K1=King('E1','white')
board.board[K1.y][K1.x]=K1

p1=Pawn('A7','black')
board.board[p1.y][p1.x]=p1
p2=Pawn('B7','black')
board.board[p2.y][p2.x]=p2
p3=Pawn('C7','black')
board.board[p3.y][p3.x]=p3
m1=Menister('D7','black')
board.board[m1.y][m1.x]=m1
m2=Menister('E7','black')
board.board[m2.y][m2.x]=m2
p6=Pawn('F7','black')
board.board[p6.y][p6.x]=p6
p7=Pawn('G7','black')
board.board[p7.y][p7.x]=p7
p8=Pawn('H7','black')
board.board[p8.y][p8.x]=p8

P1=Pawn('A2','white')
board.board[P1.y][P1.x]=P1
P2=Pawn('B2','white')
board.board[P2.y][P2.x]=P2
P3=Pawn('C2','white')
board.board[P3.y][P3.x]=P3
M1=Menister('D2','white')
board.board[M1.y][M1.x]=M1
M2=Menister('E2','white')
board.board[M2.y][M2.x]=M2
P6=Pawn('F2','white')
board.board[P6.y][P6.x]=P6
P7=Pawn('G2','white')
board.board[P7.y][P7.x]=P7
P8=Pawn('H2','white')
board.board[P8.y][P8.x]=P8

n=0
board.printboard()
while True:
    n1=n
    print('ход белых', end=':')
    while n1==n:
        a1=str(input())
        xx=letters[a1[0]]
        yy=8-int(a1[1])
        print('Возможные ходы:')
        for i in range(8):
            for j in range(8):
                a4=a1+'-'+str(letters1[j])+str(abs(8-i))
                x2=letters[a4[3]]
                y2=8-int(a4[4])
                if board.board[yy][xx].chek_dvish2(a4) and (board.board[yy][xx].__class__.__name__ == 'Pawn' and xx==x2 or board.board[yy][xx].__class__.__name__ != 'Pawn'):
                    print(letters1[j], abs(8-i))
                    y2=i
                    x2=j
        a2=str(input())
        a=a1+'-'+a2
        x1=letters[a[0]]
        y1=8-int(a[1])
        x2=letters[a[3]]
        y2=8-int(a[4])
        if board.board[y1][x1].chek_dvish(a):
            if (board.board[y1][x1].__class__.__name__ == 'Pawn' and xx==x2 or board.board[y1][x1].__class__.__name__ != 'Pawn'):
                n+=1
                board.board[y1][x1].move(a)
            else:
                print("Ход не может быть совершен, попробуйте снова")
    if net_korol(k1,K1):
        break
    print('\n'*5)
    board.printboard()
    print('ход черных', end=':')
    while n1+1==n:
        a1=str(input())
        xx=letters[a1[0]]
        yy=8-int(a1[1])
        print('Возможные ходы:')
        for i in range(8):
            for j in range(8):
                a4=a1+'-'+str(letters1[j])+str(abs(8-i))
                if board.board[yy][xx].chek_dvish2(a4) and (board.board[yy][xx].__class__.__name__ == 'Pawn' and xx==x2 or board.board[yy][xx].__class__.__name__ != 'Pawn'):
                    print(letters1[j], abs(8-i))
                    y2=i
                    x2=j
        a2=str(input())
        a=a1+'-'+a2
        x1=letters[a[0]]
        y1=8-int(a[1])
        x2=letters[a[3]]
        y2=8-int(a[4])
        if board.board[y1][x1].chek_dvish(a):
            if (board.board[y1][x1].__class__.__name__ == 'Pawn' and xx==x2 or board.board[y1][x1].__class__.__name__ != 'Pawn'):
                n+=1
                board.board[y1][x1].move(a)
            else:
                print("Ход не может быть совершен, попробуйте снова")
    if net_korol(k1,K1):
        break
    print('\n'*5)
    board.printboard()


# In[ ]:





# In[ ]:




