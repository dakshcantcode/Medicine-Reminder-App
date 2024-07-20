# Python program to create a table
  
import  tkinter as tk
from tkinter import filedialog as fd 
from PIL import ImageTk, Image
import datetime
import time
import winsound
from playsound import playsound 
import threading as th
import random
import multiprocessing
#import AlarmUtils.py

 
 
root=tk.Tk()
rowCnt=1
rows = []
checkbutton_vals = {}
activeAlarm = {}
activeAlarmMusic = {}
StopAllAlarm=False
alarmSound_g=""
def add_row():
            global rowCnt
            checkbutton_val = tk.IntVar()
            checkbutton_vals[rowCnt-1]=checkbutton_val
            rowCnt =rowCnt+1
            row = []
            
            c = tk.Checkbutton(root, variable = checkbutton_val)
            print(c.grid_info())
            c.grid(row = rowCnt, column = 0)
            row.append(checkbutton_val)
            row.append(c)
            print(c.grid_info())
            for j in range(1,3): #Columns

                    col = tk.Text(root, width=16, height=1)
                    col.grid(row=rowCnt, column=j)
                    row.append(col)
                    print(row[0])
                    print(row[1])
            
            
            lvar=random.randint(1, 100)
            activeAlarm[lvar]=True
            alm_btn= tk.Button(root, image=ImgToset,command=lambda rowCtx=row:alarmPopUp(lvar))
            alm_btn.grid(row=rowCnt,column=3)
            #Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)
            row.append(alm_btn)
            row.append(lvar)#Alarm Identifier
            rows.append(row)        
#https://blog.finxter.com/how-to-remove-items-from-a-list-while-iterating/            
def delete_row(): #[(1, ['x', 'y']), (0, ['a', 'b'])]
    alarmTorem={}
    print(list(reversed(list(enumerate(rows))[:])))
    for rowno, row in reversed(list(enumerate(rows))[:]):
        print(list(reversed(list(enumerate(rows))[:])))
        print(row[0].get())
        print(checkbutton_vals[rowno].get())
        if row[0].get() == 1:
            alarmIdfy=-1
            for i in row[1:]:
                if isinstance(i, int):
                    activeAlarm[i]= True
                    alarmTorem[i]= activeAlarm[i]
                else: 
                    i.destroy()
            rows.pop(rowno)
            alarmRegCleanUp(activeAlarm,alarmTorem)

def alarmRegCleanUp(orginalDic,alarmTorem):
    for keyToremove in alarmTorem :
        time.sleep(2)
        orginalDic.pop(keyToremove)
        
# setting the windows size
root.geometry("600x400")
btn_img = Image.open('resources/clock.PNG')
click_btn_img = btn_img.resize((30, 30), Image.Resampling.LANCZOS)
ImgToset =ImageTk.PhotoImage(click_btn_img)

btn_add_img = Image.open('resources/add.PNG')
click_btn_add_img = btn_add_img.resize((30, 30), Image.Resampling.LANCZOS)
AddImgToset =ImageTk.PhotoImage(click_btn_add_img)

addbutton= tk.Button(root, image=AddImgToset,text="Add")
addbutton.grid(column=0,row=0)
addbutton['command'] = add_row

dl = tk.Button(root , text = 'Delete Row')
dl.grid(row =0, column=1)
dl['command'] = delete_row

v0 = tk.StringVar()
e0 = tk.Entry(root, textvariable = v0,state = 'readonly')
v0.set('Select')
e0.grid(row = 1, column = 0 )

v1 = tk.StringVar()
e1 = tk.Entry(root, textvariable = v1, state = 'readonly')
v1.set('Col1')
e1.grid(row = 1, column = 1 )

v2 = tk.StringVar()
e2 = tk.Entry(root, textvariable = v2, state = 'readonly')
v2.set('Col2')
e2.grid(row = 1, column = 2)

v3 = tk.StringVar()
e3 = tk.Entry(root, textvariable = v3,state = 'readonly')
v3.set('Col3')
e3.grid(row = 1, column = 3  )

v4 = tk.StringVar()
e4 = tk.Entry(root, textvariable = v4,state = 'readonly')
v4.set('Col4')
e4.grid(row = 1, column = 4 )

hour = tk.StringVar(root)
minute = tk.StringVar(root)
second = tk.StringVar(root)
# Use Threading
def Threading(btn1,btn2,_id):
   # _parent.destroy()#Close Alarm Frame
    btn1['state'] = tk.DISABLED
    btn2['state'] = tk.NORMAL
    if _id in activeAlarm and activeAlarm[_id]== True:
        activeAlarm[_id]= False
##    else:
##        activeAlarm[_id]= True
        
    t1=th.Thread(target=alarm,args=(_id,))
    
    t1.start()
def dismissAlarm(btn1,btn2,_id):
    print(_id)
    activeAlarm[_id]= True
    btn2['state'] = tk.DISABLED
    btn1['state'] = tk.NORMAL
    print(alarmSound_g)
def closeAlarmWin(_parent):
    _parent.destroy()#Close Alarm Frame
    
def alarm(_id):
    # Set Alarm
    print(minute.get())
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    print(set_alarm_time)
    print(alarmSound_g)
    alarmMusic=alarmSound_g# Making local copy so global will not change slected sound
    # Infinite Loop
    while not StopAllAlarm:
        
        if activeAlarm[_id]== True:
            activeAlarm[_id]= False
            break
        # Wait for one seconds
        time.sleep(1)
 
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            #winsound.PlaySound(alarmMusic,winsound.SND_ASYNC)
            print(alarmMusic)
            #p = multiprocessing.Process(target=playsound, args=(alarmMusic,))
            #activeAlarmMusic[_id]=p
            #p.start()
            #input("press ENTER to stop playback")
            #p.terminate()
            #playMp3(_id,alarmMusic)
            playsound(alarmMusic)
    #print(activeAlarm)
    #activeAlarm.pop(_id) #Update Alarm Identifier List
    print("Closing alarm...!!!")
    #print(activeAlarm)
def snooz(_id):
    activeAlarmMusic[_id].terminate()
    
def playMp3(_id,alarmMusic):
    p = multiprocessing.Process(target=playsound, args=(alarmMusic,))
    activeAlarmMusic[_id]=p
    p.start()
    
    
def openFile():  
   # selecting the file using the askopenfilename() method of filedialog  
   global alarmSound_g
   alarmSound_g = fd.askopenfilename(  
      title = "Select a file of any type",  
      filetypes = [("All files", "*.*")]  
      )
   
   print(alarmSound_g)
   
def alarmPopUp(_id): 
    # Add Labels, Frame, Button, Optionmenus
    #frameRoot=tk.Tk()
    print(_id)
    frame = tk.Toplevel(root)
    frame.geometry("400x250")
    
    tk.Label(frame,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").grid(row = 1, column = 3)
    tk.Label(frame,text="Set Time",font=("Helvetica 15 bold")).grid(row = 2, column = 3)
     
    
     
    #hour = tk.StringVar(root)
    hours = ('00', '01', '02', '03', '04', '05', '06', '07',
             '08', '09', '10', '11', '12', '13', '14', '15',
             '16', '17', '18', '19', '20', '21', '22', '23', '24'
            )
    print(len(hour.get().strip()))
    hour.set(hours[0] if len(hour.get().strip())==0 else hour.get())
     
    hrs = tk.OptionMenu(frame, hour, *hours).grid(row = 3, column = 3)
    #hrs.pack(side=LEFT)
     
    #minute = tk.StringVar(root)
    minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
               '08', '09', '10', '11', '12', '13', '14', '15',
               '16', '17', '18', '19', '20', '21', '22', '23',
               '24', '25', '26', '27', '28', '29', '30', '31',
               '32', '33', '34', '35', '36', '37', '38', '39',
               '40', '41', '42', '43', '44', '45', '46', '47',
               '48', '49', '50', '51', '52', '53', '54', '55',
               '56', '57', '58', '59', '60')
    minute.set(minutes[0])
     
    mins = tk.OptionMenu(frame, minute, *minutes).grid(row = 3, column = 4)
    #mins.pack(side=LEFT)
    
     
    #second = tk.StringVar(root)
    seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
               '08', '09', '10', '11', '12', '13', '14', '15',
               '16', '17', '18', '19', '20', '21', '22', '23',
               '24', '25', '26', '27', '28', '29', '30', '31',
               '32', '33', '34', '35', '36', '37', '38', '39',
               '40', '41', '42', '43', '44', '45', '46', '47',
               '48', '49', '50', '51', '52', '53', '54', '55',
               '56', '57', '58', '59', '60')
    second.set(seconds[0])
     
    secs = tk.OptionMenu(frame, second, *seconds).grid(row = 3, column = 5)
    #secs.pack(side=LEFT)
    setCloseAlarmBtn=tk.Button(frame,text="Close Alarm",font=("Helvetica 15"))
    setCloseAlarmBtn.grid(row = 5, column =4)
    setCloseAlarmBtn['command']=lambda _parent=frame:closeAlarmWin(_parent)
    
    setAlarmBtn=tk.Button(frame,text="Set Alarm",font=("Helvetica 15"))
    setAlarmBtn.grid(row = 4, column =3)

    fileDialog=tk.Button(frame,text="Select File",font=("Helvetica 15"),command=openFile)
    fileDialog.grid(row = 4, column =4)
    #fileDialog['command']=lambda :openFile

    snoozbtn=tk.Button(frame,text="Snooz music",font=("Helvetica 15"))
    snoozbtn.grid(row = 4, column =5)
    snoozbtn['command']=lambda :snooz(_id)
    
    setDismissAlarmBtn=tk.Button(frame,text="Dismiss Alarm",font=("Helvetica 15"))
    setDismissAlarmBtn.grid(row = 5, column =3)
    
    setAlarmBtn['command']=command=lambda btn1=setAlarmBtn,btn2=setDismissAlarmBtn:Threading(btn1,btn2,_id)
    setDismissAlarmBtn['command']=lambda btn1=setAlarmBtn,btn2=setDismissAlarmBtn:dismissAlarm(btn1,btn2,_id)
    
    if _id in activeAlarm and activeAlarm[_id]== True:
        setAlarmBtn['state'] = tk.NORMAL
    else:
        setAlarmBtn['state'] = tk.DISABLED
    
        
    
    
    if _id in activeAlarm and activeAlarm[_id]== False:
        setDismissAlarmBtn['state'] = tk.NORMAL
    else:
        setDismissAlarmBtn['state'] = tk.DISABLED
    #tk.Button(frame,text="Done",font=("Helvetica 15"),command=lambda idx=1,parent=frame:addRow(idx,binst)).grid(row = 4, column =4)
    frame.grab_set()
    frame.mainloop()


root.mainloop()
StopAllAlarm=True
  
