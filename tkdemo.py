from tkinter import*
w=Tk()
w.title='Top'
w.geometry('400x600')
text='''
 _________________
|name:xxx|score=10|
 _________________
'''
name=[]
def
lw=Button(w,text="按'w'向上",sticky=W,command=set_last)
# lw.grid(row=0)

content=Label(w, text=text,sticky=W)
content.grid(row=1)
ls=Label(w,text="按's'向下",sticky=W)
ls.grid(row=2)
w.mainloop()