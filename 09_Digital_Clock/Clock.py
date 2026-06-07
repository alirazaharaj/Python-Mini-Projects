from tkinter import *
import datetime as dt

def time():
    da=dt.datetime.now()
    hour=da.strftime('%I')
    min=da.strftime('%M')
    sec=da.strftime('%S')
    am=da.strftime('%p')
    la_hour.config(text=hour)
    la_mint.config(text=min)
    la_second.config(text=sec)
    la_am.config(text=am)

    date=da.strftime('%d')
    month=da.strftime('%m')
    year=da.strftime('%y')
    day=da.strftime('%a')
    la_date.config(text=date)
    la_month.config(text=month)
    la_year.config(text=year)
    la_day.config(text=day)

    la_hour.after(200,time)

app=Tk()

app.title('DIgital Clock')
app.geometry('560x400')
app.config(bg='white')

la_hour=Label(app,text='00',font=('Lucida Handwriting',25,'bold'))
la_hour.place(x=50,y=30,height=40,width=100)
la_hour_text=Label(app,text='Hour',font=('Lucida Handwriting',25,'bold'),bg='pink')
la_hour_text.place(x=50,y=80,height=40,width=100)

la_mint=Label(app,text='00',font=('Lucida Handwriting',25,'bold'))
la_mint.place(x=170,y=30,height=40,width=100)
la_mint_text=Label(app,text='Mint',font=('Lucida Handwriting',25,'bold'),bg='pink')
la_mint_text.place(x=170,y=80,height=40,width=100)

la_second=Label(app,text='00',font=('Lucida Handwriting',25,'bold'))
la_second.place(x=290,y=30,height=40,width=100)
la_second_text=Label(app,text='Sec',font=('Lucida Handwriting',25,'bold'),bg='pink')
la_second_text.place(x=290,y=80,height=40,width=100)

la_am=Label(app,text='00',font=('Lucida Handwriting',25,'bold'))
la_am.place(x=410,y=30,height=40,width=100)
la_am_text=Label(app,text='AM/PM',font=('Lucida Handwriting',18,'bold'),bg='pink')
la_am_text.place(x=410,y=80,height=40,width=100)


la_date=Label(app,text='00',font=('Lucida Handwriting',25,'bold'))
la_date.place(x=50,y=190,height=40,width=100)
la_date_text=Label(app,text='Date',font=('Lucida Handwriting',20,'bold'),bg='pink')
la_date_text.place(x=50,y=240,height=40,width=100)

la_month=Label(app,text='00',font=('Lucida Handwriting',25,'bold'))
la_month.place(x=170,y=190,height=40,width=100)
la_month_text=Label(app,text='Month',font=('Lucida Handwriting',20,'bold'),bg='pink')
la_month_text.place(x=170,y=240,height=40,width=100)

la_year=Label(app,text='00',font=('Lucida Handwriting',25,'bold'))
la_year.place(x=290,y=190,height=40,width=100)
la_year_text=Label(app,text='Year',font=('Lucida Handwriting',25,'bold'),bg='pink')
la_year_text.place(x=290,y=240,height=40,width=100)

la_day=Label(app,text='00',font=('Lucida Handwriting',25,'bold'))
la_day.place(x=410,y=190,height=40,width=100)
la_day_text=Label(app,text='Day',font=('Lucida Handwriting',25,'bold'),bg='pink')
la_day_text.place(x=410,y=240,height=40,width=100)


time()
app.mainloop()

