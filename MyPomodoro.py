from tkinter import *
from tkinter import ttk
import threading
import time


# Functionality

skip = False
stop = False
pomodoros = 0


def start_timer_thread():
    t = threading.Thread(target = start_timer)
    t.start()


def start_timer():
    global stop, skip,pomodoros
    stop = False
    skip = False
    pomodoros = 0
    timer_id = notebook.index(notebook.select()) + 1

    if timer_id == 1:
        secs = 60*25
        while secs > 0 and not stop:
            minutes, seconds = divmod(secs, 60)
            pomodoro_label.config(text=f"{minutes:02d}:{seconds:02d}")
            window.update()
            time.sleep(1)
            secs -= 1
        if not stop or skip:
            pomodoros+=1
            pomodoro_count.config(text=f"Pomodoros: {pomodoros}")
            if pomodoros % 4 == 0:
                notebook.select(2)

            else:
                notebook.select(1)
                start_timer()

    elif timer_id == 2:
        secs = 60*5
        while secs > 0 and not stop:
            minutes, seconds = divmod(secs, 60)
            short_break_label.config(text=f"{minutes:02d}:{seconds:02d}")
            window.update()
            time.sleep(1)
            secs -= 1
        if not stop or skip:
            notebook.select(0)
            start_timer()
    elif timer_id == 3:
        secs = 60*15
        while secs > 0 and not stop:
            minutes, seconds = divmod(secs, 60)
            long_break_label.config(text=f"{minutes:02d}:{seconds:02d}")
            window.update()
            time.sleep(1)
            secs -= 1
        if not stop or skip:
            notebook.select(0)
            start_timer()
        





def reset_time():
    global stop, skip, pomodoros
    stop= True
    skip= False
    pomodoros = 0
    pomodoro_label.config(text='25:00')
    short_break_label.config(text="5:00")
    long_break_label.config(text='15:00')
    pomodoro_count.config(text='Pomodoros: 0')



def skip_time():
    global stop, skip
    current = notebook.index(notebook.select())
    if current == 0:
        pomodoro_label.config(text='25:00')
    elif current == 1:
        short_break_label.config(text="05:00")
    elif current == 2:
        long_break_label.config(text="5:00")
    stop = True
    skip = True




# GUI
window =Tk()
window.geometry('450x400')
window.title('POMODORO')
window.resizable(0,0)

#  create a notebook
notebook = ttk.Notebook(window)
notebook.pack(fill='both',expand=True,pady=2)

# create frames for each tab
pomodoro_tab = ttk.Frame(notebook, width=450,height=200)
short_break_tab = ttk.Frame(notebook,width=450,height=200)
long_break_tab = ttk.Frame(notebook,width=450,height=200)

# add text to tabs
notebook.add(pomodoro_tab,text='Pomodoro')
notebook.add(short_break_tab,text='Short break')
notebook.add(long_break_tab,text='Long break')

# create labels for each tab
pomodoro_label = ttk.Label(pomodoro_tab, text='25:00',font = ('',60,'bold'))
pomodoro_label.pack()
short_break_label = ttk.Label(short_break_tab, text='5:00',font=('',60,'bold'))
short_break_label.pack()
long_break_label = ttk.Label(long_break_tab, text='15:00',font=('',60,'bold'))
long_break_label.pack()

# add text to labels
pomodoro_text = ttk.Label(pomodoro_tab, text=' Time to focus!! ',font = ('',30,'bold'))
pomodoro_text.pack(pady=20)
short_break_text = ttk.Label(short_break_tab, text='Take a break!!',font=('',30,'bold'))
short_break_text.pack(pady=20)
long_break_text = ttk.Label(long_break_tab, text='Take a break you deserve it!',font=('',28,'bold'))
long_break_text.pack(pady=20)

# add messagebox to store task
instruction_task = ttk.Label(window,text='Enter task below',font=('',15,'bold'))
instruction_task.pack(pady=0,fill='both', )
enter_task = Entry(window,width=49)
enter_task.pack(pady=0)
enter_task.focus_set()

# add star, reset and skip grid
grid = ttk.Frame(window)
grid.pack(pady=10)

start_button = ttk.Button(grid,text='Start', command=start_timer_thread)
start_button.grid(row=0,column=0)
reset_button = ttk.Button(grid, text='Reset', command=reset_time)
reset_button.grid(row=0,column=1)
skip_button=ttk.Button(grid,text='Skip',command=skip_time)
skip_button.grid(row=0,column=2)

pomodoro_count =  ttk.Label(grid,text='POMODOROS: ',font=('',15,'bold'))
pomodoro_count.grid(row=1,column=0,columnspan=4)



window.mainloop()






