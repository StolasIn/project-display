import tkinter as tk
import numpy as np
from tkinter import messagebox

thr_n=0
res_n=0
allo = np.empty((thr_n, res_n), dtype=tk.Entry)
need = np.empty((thr_n, res_n), dtype=tk.Entry)
avl = np.empty(res_n,dtype=tk.Entry)
def gen():
	global thr_n,res_n,allo,need,avl
	thr_n=int(e1.get())
	res_n=int(e2.get())
	allo = np.empty((thr_n, res_n), dtype=tk.Entry)
	need = np.empty((thr_n, res_n), dtype=tk.Entry)
	avl = np.empty(res_n,dtype=tk.Entry)
	for i in range(1,res_n+1):
		str2 = 'allocation_'+str(i)
		tk.Label(win,text=str2).grid(row=3, column=i)

	for i in range(thr_n):
		str1 = 'thread_'+str(i)
		tk.Label(win,text=str1).grid(row=i+4, column=0, padx=5, pady=5,sticky='w')
		for j in range(res_n):
			allo[i][j] = tk.Entry(win,width=6)
			allo[i][j].grid(row=i+4, column=j+1, padx=5, pady=5)

	for i in range(1,res_n+1):
		str2 = 'request_'+str(i)
		tk.Label(win,text=str2).grid(row=3, column=i+thr_n+1,padx=5, pady=5)

	for i in range(thr_n):
		for j in range(res_n):
			need[i][j] = tk.Entry(win,width=6)
			need[i][j].grid(row=i+4, column=j+2+thr_n, padx=5, pady=5)

	str3='Available : '
	tk.Label(win,text=str3).grid(row=thr_n+4, column=0,padx=5, pady=5,sticky='w')
	for i in range(res_n):
		avl[i] = tk.Entry(win,width=6)
		avl[i].grid(row=thr_n+4, column=i+1, padx=5,pady=5)

def cmpa(a,b):
	for i in range(len(a)):
		if a[i]<b[i]:
			return False
	return True

def fill(a,b):
	for i in range(len(a)):
		a[i]+=b[i]

def solve():
	allos=np.zeros((thr_n, res_n))
	needs=np.zeros((thr_n, res_n))
	avls=np.zeros(res_n)
	vis=np.zeros(thr_n)
	for i in range(len(allo)):
		for j in range(len(allo[i])):
			allos[i][j]=allo[i][j].get()

	for i in range(len(need)):
		for j in range(len(need[i])):
			needs[i][j]=need[i][j].get()

	for i in range(len(avl)):
		avls[i]=avl[i].get()

	for i in range(len(allos)):
		for j in range(len(allos[i])):
			avls[j]-=allos[i][j]
	print(avls)
	cnt = 0;
	for i in range(thr_n):
		for j in range(thr_n):
			if vis[j]==0 and cmpa(avls,needs[j]):
				cnt+=1
				fill(avls,allos[j])
				print(avls)
				vis[j]=1
				break

	if cnt==thr_n:
		messagebox.showinfo('output', 'safe state')
	else:
		messagebox.showinfo('output', 'deadlock')



win = tk.Tk()
win.title("banker's problem")
win.geometry("1000x600+250+150")

tk.Label(win,text='number of thread').grid(row=0, column=0, padx=5, pady=5,sticky='w')

e1 = tk.Entry(win,width=10)
e1.grid(row=0,column=1, padx=5,pady=5)

tk.Label(win,text='number of resource').grid(row=1,column=0,padx=5, pady=5,sticky='w')

e2 = tk.Entry(win,width=10)
e2.grid(row=1,column=1, padx=5,pady=5)


check= tk.Button(win,text='check',command=gen)
check.grid(row=2,column=1, pady=5)

sol= tk.Button(win,text='solve',command=solve)
sol.grid(row=thr_n+10,column=1, pady=5)
win.mainloop()