import tkinter as tk
import numpy as np
from tkinter import messagebox
import random as rand

class inv:
	def __init__(self,l,r):
		self.l=l;
		self.r=r;

num=0
catch=0
t=0
arr=np.empty((1, 1), dtype=tk.Entry)
name=np.empty(num, dtype=str)
pro=np.empty(num, dtype=float)
intv=np.empty(num,dtype=inv)
res=0
prod=1
def re():
	check=np.zeros(num,dtype=int)
	tr=0
	for i in range(catch):
		t=rand.randint(0,res+prod-1)
		flag=False
		for j in range(num):
			if(t>=intv[j].l and t<=intv[j].r):
				flag=True
				check[j]+=1
				break
		if flag==False:
			tr+=1

	for i in range(num):
		tk.Label(width=10,text=arr[i][0].get()).grid(padx=5,pady=5,row=num+6,column=i+1)
		tk.Label(width=10,text=str(check[i])).grid(padx=5,pady=5,row=num+7,column=i+1)

	tk.Label(width=10,text='垃圾').grid(padx=5,pady=5,row=num+6,column=num+1)
	tk.Label(width=10,text=str(tr)).grid(padx=5,pady=5,row=num+7,column=num+1)

	tk.Button(win,text='重抽',command=re,width=10).grid(padx=5,pady=5,row=num+6,column=0)
def test():
	mi=1000000.0
	global prod,intv,res,pro
	prod=1
	tr=0
	check=np.zeros(num,dtype=int)
	for i in range(num):
		mi=min(mi,pro[i])

	while(int(mi*prod)!=mi*prod):
		prod*=10

	for i in range(num):
		pro[i]*=prod;

	intv=np.empty(num,dtype=inv)
	sum1=0;
	for i in range(num):
		intv[i]=inv(sum1,pro[i]+sum1-1)
		sum1+=int(pro[i]);

	res=sum1
	flag=False
	for i in range(catch):
		t=rand.randint(0,sum1+prod-1)
		flag=False
		for j in range(num):
			if(t>=intv[j].l and t<=intv[j].r):
				flag=True
				check[j]+=1
				break
		if flag==False:
			tr+=1

	for i in range(num):
		tk.Label(width=10,text=arr[i][0].get()).grid(padx=5,pady=5,row=num+6,column=i+1)
		tk.Label(width=10,text=str(check[i])).grid(padx=5,pady=5,row=num+7,column=i+1)

	tk.Label(width=10,text='垃圾').grid(padx=5,pady=5,row=num+6,column=num+1)
	tk.Label(width=10,text=str(tr)).grid(padx=5,pady=5,row=num+7,column=num+1)

	tk.Button(win,text='重抽',command=re,width=10).grid(padx=5,pady=5,row=num+6,column=0)

def cal():
	global name,pro,catch
	sum1=0.0
	ans1=1.0;
	catch=int(e1.get())
	name=np.empty(num, dtype=str)
	pro=np.empty(num, dtype=float)
	for i in range(num):
		name[i]=str(arr[i][0].get())
		pro[i]=float(arr[i][1].get())

	tk.Label(win,width=10,text='至少一隻').grid(padx=5,pady=5,row=4,column=3)
	for i in range(num):
		sum1+=pro[i];

	if(sum1==0.0):
		messagebox.showinfo('output','ㄞ 別亂搞')

	#至少一隻
	sum1=(1-sum1)
	for i in range(catch):
		ans1=ans1*sum1

	str1=str(int((1-ans1)*100.0))+' %'
	tk.Label(win,width=10,text=str(str1)).grid(padx=5,pady=5,row=5,column=3)

def gen():
	global arr,num
	num=int(e2.get())
	tk.Label(win,text='name').grid(padx=5,pady=5,row=4,column=1)
	tk.Label(win,text='Probability').grid(padx=5,pady=5,row=4,column=2)
	arr=np.empty((num, 2), dtype=tk.Entry)
	for i in range(num):
		arr[i][0]=tk.Entry(win,width=10)
		arr[i][0].grid(padx=5,pady=5,row=i+5,column=1)
		arr[i][1]=tk.Entry(win,width=10)
		arr[i][1].grid(padx=5,pady=5,row=i+5,column=2)

	tk.Button(win,text='calculate',command=cal,width=10).grid(padx=5,pady=5,row=3,column=2)
	tk.Button(win,width=10,text='test',command=test).grid(padx=5,pady=5,row=num+5,column=0)
	
win = tk.Tk()
win.title('轉蛋機率計算')
win.geometry('1000x600+250+150')

tk.Label(win,text='輸入次數 : ').grid(padx=5,pady=5,row=0,column=0)
e1 = tk.Entry(win,width=10)
e1.grid(padx=5,pady=5,row=0,column=1);

tk.Label(win,text='想抽到啥 : ').grid(padx=5,pady=5,row=1,column=0)
tk.Label(win,text='個數 : ').grid(padx=5,pady=5,row=2,column=0)
e2 = tk.Entry(win,width=10)
e2.grid(padx=5,pady=5,row=2,column=1,sticky='w')

tk.Button(win,text='input',command=gen,width=10).grid(padx=5,pady=5,row=3,column=1,sticky='w')
win.mainloop()