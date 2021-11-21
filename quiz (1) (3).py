from Tkinter import *
import random
import tkMessageBox
import pickle
top = Tk()
top.configure(background='black')
rules=Button(top, text= 'Welcome to Quizzy Q, an interactive quiz game', relief= 'flat',bg='black',fg='white',font='Narkisim')
rules.pack()
t=0
class comp:
    def __init__(self):
        self.file=open("comp.txt","r")
        self.l=self.file.readlines()
        self.an={1:'Registered Jack-45',2:'VOIP',3:'HTTP',4:'Node',5:'Bandwidth'}
        self.ans={1:'Random Jack-45',2:'POP',3:'HTML',4:'Server',5:'Range'}
        self.ansc={1:'Radio Jack-45',2:'SMTP',3:'IP',4:'Hub',5:'Topology'}
        self.answ={1:'Range Jack-45',2:'TCP',3:'URL',4:'Gateway',5:'Amplitude'}
        self.scorer=0        
    def choice(self):
        self.ch=random.choice(self.l)
        x=0
        for i in range(len(self.ch)):
            if self.ch[i]==')':
                x=i+1
        self.quesbutton=Button(top, text= self.ch[x:len(self.ch)] , relief= 'flat',bg='white',fg='blue',font='Narkisim')
        self.quesbutton.pack()
    def namegetting(self):
        def get():
            Name=E1.get()
            self.gname=open('historycs.txt','a')
            self.gname.write(Name)
            self.gname.close()          
            E1.pack_forget()
            L1.pack_forget()
            g.pack_forget()
        L1 = Label(top, text="Enter Name",bg='blue',fg='white')
        g=Button(top, text='Enter',command=get,bg='blue',fg='white',font='Narkisim')
        L1.pack( side = 'top')
        E1 =Entry(top, bd =5,bg='white')
        E1.pack(side ='top')
        g.pack()        
    def scoree(self):
        self.ghistory=open("historycs.txt",'a')
        print str(self.scorer)
        self.ghistory.write(' '+'*'+str(self.scorer)+'\n')
        self.ghistory.close()
        file=open('historyp.txt','r')
        l=file.readlines()
        self.scorelist=[]
        self.namelist=[]
        for i in l:
            for j in range(len(i)):
                if i[j]=='*':
                    self.namelist.append(i[0:j])
                    s=i[j+1:len(i)]
                    print s
                    self.scorelist.append(int(s))
        print 'Top Scores:'
        while self.scorelist!=[]:
                for i in range(5):
                    if self.scorelist!=[]:
                        maxscore=max(self.scorelist)
                        maxname=self.namelist[self.scorelist.index(maxscore)-1]
                        print maxscore,'\t',maxname
                        self.scorelist.remove(maxscore)
                        self.namelist.remove(maxname)
    def score(self):
        global t
        self.scorer+=1
        t=self.scorer
    def ques(self):
        self.choice()
        self.m=random.choice([i for i in range(1,25)])
        if self.m==1:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optb.pack()
            self.optc.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==2:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optb.pack()
            self.optd.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==3:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optc.pack()
            self.optb.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==4:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optc.pack()
            self.optd.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==5:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optd.pack()
            self.optb.pack()
            self.optc.pack()
        elif self.m==6:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optd.pack()
            self.optc.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==7:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.opta.pack()
            self.optc.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==8:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.opta.pack()
            self.optd.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==9:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optc.pack()
            self.opta.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==10:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optc.pack()
            self.optd.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==11:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optd.pack()
            self.opta.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==12:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optd.pack()
            self.optc.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==13:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.opta.pack()
            self.optb.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==14:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.opta.pack()
            self.optd.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==15:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optb.pack()
            self.opta.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==16:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optb.pack()
            self.optd.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==17:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optd.pack()
            self.opta.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==18:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optd.pack()
            self.optb.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==19:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.opta.pack()
            self.optb.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==20:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.opta.pack()
            self.optc.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==21:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optb.pack()
            self.opta.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==22:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optb.pack()
            self.optc.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==23:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optc.pack()
            self.opta.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==24:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optc.pack()
            self.optb.pack()
            self.opta.pack()
            self.l.remove(self.ch)
            
class phy:
    def __init__(self):
        self.file=open("Physics.txt","r")
        self.l=self.file.readlines()
        self.an={1:'Radially inward',2:'Has a constant non zero value',3:'Electrons',4:'Increase',5:'Weakly repelled by an external magnetic field',6:'1.2*10^-6 nm',7:'H^1/2',8:'MnO',9:'Microwave region'}
        self.ans={1:'Upward along the wire',2:'Is variable',3:'Electrons, neutrons and protons',4:'Remains the same',5:'Strongly repelled by an external magnetic field',6:'1.2 nm',7:'H^0',8:'Fe',9:'Infrared region'}
        self.ansc={1:'Radially outward',2:'Is zero',3:'neutrons and protons',4:'Decrease',5:'Strongly attracted by the external magnetic field',6:'1.2*10^-3 nm',7:'H^-1/2',8:'O2',9:'Ultraviolet region'}
        self.answ={1:'Downward along the wire',2:'Cannot be determined with the information given',3:'Only protons',4:'Depends on the charges',5:'None of the above',6:'1.2*10 nm',7:'H',8:'Ni',9:'Visible region'}
        self.scorer=0
    def choice(self):
        self.ch=random.choice(self.l)
        x=0
        for i in range(len(self.ch)):
            if self.ch[i]==')':
                x=i+1
        self.quesbutton=Button(top, text= self.ch[x:len(self.ch)] , relief= 'flat',bg='white',fg='blue',font='Narkisim')
        self.quesbutton.pack()

    def score(self):
        global t
        self.scorer+=1
        t=self.scorer
    def namegetting(self):
        def get():
            Name=E1.get()
            self.gname=open('historyp.txt','a')
            self.gname.write(Name)
            self.gname.close()
            E1.pack_forget()
            L1.pack_forget()
            g.pack_forget()
        L1 = Label(top, text="Enter Name",bg='blue',fg='white')
        g=Button(top, text='Enter',command=get,bg='blue',fg='white',font='Narkisim')
        L1.pack( side = 'top')
        E1 =Entry(top, bd =5,bg='white')
        E1.pack(side ='top')
        g.pack()    
    def ques(self):
        self.choice()
        self.m=random.choice([i for i in range(1,25)])
        if self.m==1:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optb.pack()
            self.optc.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==2:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optb.pack()
            self.optd.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==3:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optc.pack()
            self.optb.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==4:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optc.pack()
            self.optd.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==5:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.opta.pack()
            self.optd.pack()
            self.optb.pack()
            self.optc.pack()
        elif self.m==6:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optd.pack()
            self.optc.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==7:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.opta.pack()
            self.optc.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==8:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.opta.pack()
            self.optd.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==9:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optc.pack()
            self.opta.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==10:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optc.pack()
            self.optd.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==11:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optd.pack()
            self.opta.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==12:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optd.pack()
            self.optc.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==13:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.opta.pack()
            self.optb.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==14:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.opta.pack()
            self.optd.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==15:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optb.pack()
            self.opta.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==16:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optb.pack()
            self.optd.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==17:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optd.pack()
            self.opta.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==18:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optd.pack()
            self.optb.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==19:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.opta.pack()
            self.optb.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==20:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.opta.pack()
            self.optc.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==21:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optb.pack()
            self.opta.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==22:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optb.pack()
            self.optc.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==23:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optc.pack()
            self.opta.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==24:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optc.pack()
            self.optb.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        
    def scoree(self):
        self.ghistory=open("historyp.txt",'a')
        print str(self.scorer)
        self.ghistory.write(' '+'*'+str(self.scorer)+'\n')
        self.ghistory.close()
        file=open('historyp.txt','r')
        l=file.readlines()
        self.scorelist=[]
        self.namelist=[]
        for i in l:
            for j in range(len(i)):
                if i[j]=='*':
                    self.namelist.append(i[0:j])
                    s=i[j+1:len(i)]
                    print s
                    self.scorelist.append(int(s))
        print 'Top Scores:'
        while self.scorelist!=[]:
                for i in range(5):
                    if self.scorelist!=[]:
                        maxscore=max(self.scorelist)
                        maxname=self.namelist[self.scorelist.index(maxscore)-1]
                        print maxscore,'\t',maxname
                        self.scorelist.remove(maxscore)
                        self.namelist.remove(maxname)
        
class chem:
    def __init__(self):
        self.file=open("chem.txt","r")
        self.l=self.file.readlines()
        self.an={1:'65Å',2:'7.0',3:'Terylene',4:'15 kg',5:'base and acid',6:'Both form soluble bicarbonates',7:'6',8:'Cytosine',9:'Cetyltrimethyl ammonium bromide'}
        self.ans={1:'4.76Å',2:'7.2',3:'Nylon 6,6',4:'37.5 kg',5:' base and base',6:' Both form nitrides',7:'2',8:'Cystine',9:'Sodium stearate'}
        self.ansc={1:'212Å',2:'6.9',3:'Nylon 6',4:'7.5 kg ',5:'acid and base',6:'Both form basic carbonates',7:'4',8:'Cysteine ',9:'Sodium lauryl sulphate'}
        self.answ={1:'0.529Å',2:'1.0',3:'Bakelite',4:'10 kg',5:'acid and acid',6:'Nitrates of both yield NO2 and O2 on heating',7:'0',8:'Methionine',9:'Glyceryl oleate'}
        self.scorer=0
        
    def choice(self):
        self.ch=random.choice(self.l)
        x=0
        for i in range(len(self.ch)):
            if self.ch[i]==')':
                x=i+1
        quesbutton=Button(top, text= self.ch[x:len(self.ch)] , relief= 'flat',bg='blue',fg='white',font='Narkisim')
        quesbutton.pack()

    def score(self):
        global t
        self.scorer+=1
        t=self.scorer
    def namegetting(self):
        def get():
            Name=E1.get()
            self.gname=open('historychem.txt','a')
            self.gname.write(Name)
            self.gname.close()          
            E1.pack_forget()
            L1.pack_forget()
            g.pack_forget()
        L1 = Label(top, text="Enter Name",bg='blue',fg='white')
        g=Button(top, text='Enter',command=get,bg='blue',fg='white',font='Narkisim')
        L1.pack( side = 'top')
        E1 =Entry(top, bd =5,bg='white')
        E1.pack(side ='top')
        g.pack()
    def scoree(self):
        self.ghistory=open("historychem.txt",'a')
        print str(self.scorer)
        self.ghistory.write(' '+'*'+str(self.scorer)+'\n')
        self.ghistory.close()
        file=open('historyp.txt','r')
        l=file.readlines()
        self.scorelist=[]
        self.namelist=[]
        for i in l:
            for j in range(len(i)):
                if i[j]=='*':
                    self.namelist.append(i[0:j])
                    s=i[j+1:len(i)]
                    print s
                    self.scorelist.append(int(s))
        print 'Top Scores:'
        while self.scorelist!=[]:
                for i in range(5):
                    if self.scorelist!=[]:
                        maxscore=max(self.scorelist)
                        maxname=self.namelist[self.scorelist.index(maxscore)-1]
                        print maxscore,'\t',maxname
                        self.scorelist.remove(maxscore)
                        self.namelist.remove(maxname)
    
    def ques(self):
        self.choice()
        self.m=random.choice([i for i in range(1,25)])
        if self.m==1:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optb.pack()
            self.optc.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==2:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optb.pack()
            self.optd.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==3:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optc.pack()
            self.optb.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==4:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optc.pack()
            self.optd.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==5:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.opta.pack()
            self.optd.pack()
            self.optb.pack()
            self.optc.pack()
        elif self.m==6:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optd.pack()
            self.optc.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==7:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.opta.pack()
            self.optc.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==8:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.opta.pack()
            self.optd.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==9:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optc.pack()
            self.opta.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==10:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optc.pack()
            self.optd.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==11:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optd.pack()
            self.opta.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==12:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optd.pack()
            self.optc.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==13:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.opta.pack()
            self.optb.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==14:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.opta.pack()
            self.optd.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==15:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optb.pack()
            self.opta.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==16:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optb.pack()
            self.optd.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==17:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optd.pack()
            self.opta.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==18:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optd.pack()
            self.optb.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==19:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.opta.pack()
            self.optb.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==20:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.opta.pack()
            self.optc.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==21:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optb.pack()
            self.opta.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==22:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optb.pack()
            self.optc.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==23:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optc.pack()
            self.opta.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==24:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optc.pack()
            self.optb.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        
class bio:
    def __init__(self):
        self.file=open("Bio.txt","r")
        self.l=self.file.readlines()
        self.an={1:'Registered Jack-45',2:'VOIP',3:'HTTP',4:'Node',5:'Bandwidth'}
        self.ans={1:'Random Jack-45',2:'POP',3:'HTML',4:'Server',5:'Range'}
        self.ansc={1:'Radio Jack-45',2:'SMTP',3:'IP',4:'Hub',5:'Topology'}
        self.answ={1:'Range Jack-45',2:'TCP',3:'URL',4:'Gateway',5:'Amplitude'}
        self.scorer=0
        
    def choice(self):
        self.ch=random.choice(self.l)
        x=0
        for i in range(len(self.ch)):
            if self.ch[i]==')':
                x=i+1
        self.quesbutton=Button(top, text= self.ch[x:len(self.ch)] , relief= 'flat',bg='blue',fg='white',font='Narkisim')
        self.quesbutton.pack()

    def score(self):
        global t
        self.scorer+=1
        t=self.scorer
    def namegetting(self):
        def get():
            Name=E1.get()
            self.gname=open('historybio.txt','a')
            self.gname.write(Name)
            self.gname.close()          
            E1.pack_forget()
            L1.pack_forget()
            g.pack_forget()
        L1 = Label(top, text="Enter Name",bg='blue',fg='white')
        g=Button(top, text='Enter',command=get,bg='blue',fg='white',font='Narkisim')
        L1.pack( side = 'top')
        E1 =Entry(top, bd =5,bg='white')
        E1.pack(side ='top')
        g.pack()
    def scoree(self):
        self.ghistory=open("historybio.txt",'a')
        print str(self.scorer)
        self.ghistory.write(' '+'*'+str(self.scorer)+'\n')
        self.ghistory.close()
        file=open('historybio.txt','r')
        l=file.readlines()
        self.scorelist=[]
        self.namelist=[]
        for i in l:
            for j in range(len(i)):
                if i[j]=='*':
                    self.namelist.append(i[0:j])
                    s=i[j+1:len(i)]
                    print s
                    self.scorelist.append(int(s))
        print 'Top Scores:'
        print self.scorelist
        while self.scorelist!=[]:
                for i in range(5):
                    if self.scorelist!=[]:
                        maxscore=max(self.scorelist)
                        maxname=self.namelist[self.scorelist.index(maxscore)-1]
                        print maxscore,'\t',maxname
                        self.scorelist.remove(maxscore)
                        self.namelist.remove(maxname)
    def ques(self):
        self.choice()
        self.m=random.choice([i for i in range(1,25)])
        if self.m==1:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optb.pack()
            self.optc.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==2:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optb.pack()
            self.optd.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==3:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optc.pack()
            self.optb.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==4:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optc.pack()
            self.optd.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==5:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.opta.pack()
            self.optd.pack()
            self.optb.pack()
            self.optc.pack()
        elif self.m==6:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.opta.pack()
            self.optd.pack()
            self.optc.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==7:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.opta.pack()
            self.optc.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==8:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.opta.pack()
            self.optd.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==9:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optc.pack()
            self.opta.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==10:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optc.pack()
            self.optd.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==11:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optd.pack()
            self.opta.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==12:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optb.pack()
            self.optd.pack()
            self.optc.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==13:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.opta.pack()
            self.optb.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==14:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.opta.pack()
            self.optd.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==15:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optb.pack()
            self.opta.pack()
            self.optd.pack()
            self.l.remove(self.ch)
        elif self.m==16:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optb.pack()
            self.optd.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==17:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optd.pack()
            self.opta.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==18:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc.pack()
            self.optd.pack()
            self.optb.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==19:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.opta.pack()
            self.optb.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==20:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.opta.pack()
            self.optc.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==21:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optb.pack()
            self.opta.pack()
            self.optc.pack()
            self.l.remove(self.ch)
        elif self.m==22:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optb.pack()
            self.optc.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        elif self.m==23:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optc.pack()
            self.opta.pack()
            self.optb.pack()
            self.l.remove(self.ch)
        elif self.m==24:
            self.opta=Button(top, text= self.an[int(self.ch[0])], bg='blue',fg='white',font='Narkisim',command=self.score)
            self.optb=Button(top, text= self.ans[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optc=Button(top, text= self.ansc[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd=Button(top, text= self.answ[int(self.ch[0])], bg='blue',fg='white',font='Narkisim')
            self.optd.pack()
            self.optc.pack()
            self.optb.pack()
            self.opta.pack()
            self.l.remove(self.ch)
        
def scoree():
    global objectinlist
    q=objectinlist[0]
    global t
    f='Your score is'+' '+str(t)
    tkMessageBox.showinfo('Congrats',f)
    scoreboard=Button(text='Scoreboard',command=scoring,font='Narkisim',bg='white')
    scoreboard.pack()
    objectinlist.append(scoreboard)
def scoring():
    global objectinlist
    q=objectinlist[0]
    q.scoree()
    top.destroy()
objectinlist=[]
def create_objectc():
    R1.pack_forget()
    R2.pack_forget()
    R3.pack_forget()
    R4.pack_forget()
    q=comp()
    q.namegetting()
    objectinlist.append(q)
    for i in range(3):
        q.ques()
    end_quiz()
    
def create_objectch():
    R1.pack_forget()
    R2.pack_forget()
    R3.pack_forget()
    R4.pack_forget()
    q=chem()
    objectinlist.append(q)
    q.namegetting()
    for i in range(3):
        q.ques()
    end_quiz()
    
def create_objectp():
    R1.pack_forget()
    R2.pack_forget()
    R3.pack_forget()
    R4.pack_forget()
    q=phy()
    q.namegetting()
    objectinlist.append(q)
    for i in range(3):
        q.ques()
    end_quiz()
    
def create_objectm():
    R1.pack_forget()
    R2.pack_forget()
    R3.pack_forget()
    R4.pack_forget()
    q=bio()
    q.namegetting()
    for i in range(3):
        q.ques()
    end_quiz()

def end_quiz():
    end=Button(top,text='End Quiz',command=scoree,bg='grey',fg='black',font='Narkisim')
    end.pack()
var = IntVar()
R1 = Radiobutton(top, text="Computer", variable=var, value=1,command=create_objectc,bg='black',fg='white')
R1.pack( anchor = W )
R2 = Radiobutton(top, text="Chemistry",variable=var, value=2,command=create_objectch,bg='black',fg='white')
R2.pack( anchor = W )
R3 = Radiobutton(top, text="Physics",variable=var, value=3,command=create_objectp,bg='black',fg='white')
R3.pack( anchor = W)
R4 = Radiobutton(top, text="Biology",variable=var, value=4,command=create_objectm,bg='black',fg='white')
R4.pack( anchor = W)
top.mainloop()  
