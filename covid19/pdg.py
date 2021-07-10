from tkinter import *
import requests
from matplotlib.backends.backend_tkagg \
import FigureCanvasTkAgg
from matplotlib.figure import Figure
#import json
import numpy as np

from tkinter import messagebox as tkMessageBox
from PIL import ImageTk,Image
#import matplotlib.animation as animation



m = Tk()
m.title("COVID 19 GRAPHIC BUILDER")
m.iconbitmap('vrs.ico')

m.configure(bg='#8b8682')



art = ImageTk.PhotoImage(file = "vrs.pgm")
arkaplan = Label(image=art)
arkaplan.pack()

url= "https://api.covid19api.com/countries"
gunlukurl="https://api.covid19api.com/total/dayone/country/"
toplamurl="https://api.covid19api.com/total/country/"
globalurl="https://api.covid19api.com/summary"

response=requests.get(url)
data=response.json()
listboxlength=len(data)





lblulke=Label(m,width=26,text="Country Selection")
lblulke.pack(side="left")
lblulke.place(x=0,y=5)

lbldatatype=Label(m,width=26,text="Data Selection")
lbldatatype.pack(side="left")
lbldatatype.place(x=0,y=390)



ulkelist=[]

listboxulke = Listbox(m, width=30, height=22,selectmode=SINGLE ,exportselection=0)
listboxulke.pack(side="left")
listboxulke.place(x=0,y=30)


for i in range(0,listboxlength):
    ulkelist.insert(i, data[i]["Slug"])
    listboxulke.insert(i, data[i]["Country"])




listboxdatatype= Listbox(m, width=30,height=9,selectmode=SINGLE,exportselection=0)
listboxdatatype.insert(0,"Confirmed")
listboxdatatype.insert(1,"Deaths")
listboxdatatype.insert(2,"Recovered")
listboxdatatype.insert(3,"Active")
listboxdatatype.insert(4,"Confirmed-Daily")
listboxdatatype.insert(5,"Deaths-Daily")
listboxdatatype.insert(6,"Recovered-Daily")
listboxdatatype.insert(7,"Active-Daily")

listboxdatatype.pack(side="left")
listboxdatatype.place(x=0,y=415)


def deathsdaily():
    f = Figure(figsize=(10, 7), dpi=80)

    queue = listboxulke.get(0, "end").index(listboxulke.get(ACTIVE))
    response2 = requests.get(gunlukurl + ulkelist[queue])
    data = response2.json()

    xlist = []

    ylist = []

    for j in range(1, len(data)):
        xlist.append(j)

    for k in range(1, len(data)):
        ylist.insert(k, (data[k]["Deaths"] - data[k - 1]["Deaths"]))

    x = np.array(xlist)
    y = np.array(ylist)
    deathsdaily = f.add_subplot(111)
    deathsdaily.set_title(listboxulke.get(ACTIVE), fontsize=12)
    deathsdaily.set_xlabel("Day", fontsize=9)
    deathsdaily.set_ylabel("Deaths Day", fontsize=9)
    deathsdaily.plot(x, y,color='red', label="Deaths")
    deathsdaily.legend(shadow='true')

    #deathsdaily.plot(x, y)
    #deathsdaily.barh(x, y,color='red')
    #deathsdaily.plot(x, y,"r")
    #deathsdaily.bar(x,y)

    canvas = FigureCanvasTkAgg(f, master=m)
    canvas.get_tk_widget().place(x=200, y=25)

def confirmeddaily():
    f = Figure(figsize=(10, 7), dpi=80)

    queue = listboxulke.get(0, "end").index(listboxulke.get(ACTIVE))
    response2 = requests.get(gunlukurl+ulkelist[queue])
    data = response2.json()

    xlist=[]

    ylist=[]

    for j in range(1,len(data)):
        xlist.append(j)

    for k in range(1,len(data)):
        ylist.insert(k,(data[k]["Confirmed"]-data[k-1]["Confirmed"]))

    x= np.array (xlist)
    y= np.array (ylist)
    confirmeddaily=f.add_subplot(111)
    confirmeddaily.set_title(listboxulke.get(ACTIVE), fontsize=12)
    confirmeddaily.set_xlabel("Day",fontsize=9)
    confirmeddaily.set_ylabel("Confirmed Day",fontsize=9)
    confirmeddaily.plot(x, y,color='orange', label="Confirmed")
    confirmeddaily.legend(shadow='true')
    #confirmeddailyv.plot(x,y)
    #confirmeddaily.savefig("grafigim1.png")
    canvas = FigureCanvasTkAgg(f, master=m)
    canvas.get_tk_widget().place(x=200,y=25)

def recovereddaily():
    f = Figure(figsize=(10, 7), dpi=80)

    queue = listboxulke.get(0, "end").index(listboxulke.get(ACTIVE))
    response2 = requests.get(gunlukurl+ulkelist[queue])
    data = response2.json()

    xlist=[]

    ylist=[]

    for j in range(1,len(data)):
        xlist.append(j)

    for k in range(1,len(data)):
        ylist.insert(k,(data[k]["Recovered"]-data[k-1]["Recovered"]))

    x= np.array (xlist)
    y= np.array (ylist)
    recovereddaily=f.add_subplot(111)
    recovereddaily.set_title(listboxulke.get(ACTIVE), fontsize=12)
    recovereddaily.set_xlabel("Day",fontsize=9)
    recovereddaily.set_ylabel("Recovered Day",fontsize=9)
    recovereddaily.plot(x, y, color='green', label="Recovered")
    recovereddaily.legend(shadow='true')
    #recovereddaily.plot(x,y)
    canvas = FigureCanvasTkAgg(f, master=m)
    canvas.get_tk_widget().place(x=200,y=25)

def activedaily():
        f = Figure(figsize=(10, 7), dpi=80)

        queue = listboxulke.get(0, "end").index(listboxulke.get(ACTIVE))
        response2 = requests.get(gunlukurl + ulkelist[queue])
        data = response2.json()

        xlist = []

        ylist = []

        for j in range(1, len(data)):
            xlist.append(j)

        for k in range(1, len(data)):
            ylist.insert(k, (data[k]["Active"] - data[k - 1]["Active"]))

        x = np.array(xlist)
        y = np.array(ylist)
        activedaily = f.add_subplot(111)
        activedaily.set_title(listboxulke.get(ACTIVE), fontsize=12)
        activedaily.set_xlabel("Day", fontsize=9)
        activedaily.set_ylabel("Active Day", fontsize=9)
        activedaily.plot(x, y, color='purple', label="Active")
        activedaily.legend(shadow = 'true')
        #plt.plot(x, y)
        canvas = FigureCanvasTkAgg(f, master=m)
        canvas.get_tk_widget().place(x=200, y=25)

def confirmedd():
    f = Figure(figsize=(10, 7), dpi=80)

    queue = listboxulke.get(0, "end").index(listboxulke.get(ACTIVE))
    response2 = requests.get(toplamurl+ulkelist[queue])
    data = response2.json()

    xlist=[]
    ylist=[]

    for j in range(0,len(data)):
        xlist.append(j)

    for k in range(0,len(data)):
        ylist.insert(k,data[k]["Confirmed"])


    x= np.array (xlist)
    y= np.array (ylist)
    confirmedd=f.add_subplot(111)
    confirmedd.set_title(listboxulke.get(ACTIVE), fontsize=12)
    confirmedd.set_xlabel("Day",fontsize=9)
    confirmedd.set_ylabel("Confirmed",fontsize=9)

    #confirmedd.plot(x,y)
    confirmedd.bar(x, y,color='orange',  label="Confirmed")
    confirmedd.legend( shadow='true')
    #confirmedd.bar(x,y)
    canvas = FigureCanvasTkAgg(f, master=m)
    canvas.get_tk_widget().place(x=200,y=25)

def recovered():
    f = Figure(figsize=(10, 7), dpi=80)

    queue = listboxulke.get(0, "end").index(listboxulke.get(ACTIVE))
    response2 = requests.get(toplamurl+ulkelist[queue])
    data = response2.json()

    xlist=[]
    ylist=[]

    for j in range(0,len(data)):
        xlist.append(j)

    for k in range(0,len(data)):
        ylist.insert(k,data[k]["Recovered"])


    x= np.array (xlist)
    y= np.array (ylist)
    precovered=f.add_subplot(111)
    precovered.set_title(listboxulke.get(ACTIVE), fontsize=12)
    precovered.set_xlabel("Day",fontsize=9)
    precovered.set_ylabel("Recovered",fontsize=9)

    #precovered.plot(x,y)
    precovered.bar(x, y, color='green', label="Recovered")
    precovered.legend( shadow='true')
    canvas = FigureCanvasTkAgg(f, master=m)
    canvas.get_tk_widget().place(x=200,y=25)

def deaths():
    f = Figure(figsize=(10, 7), dpi=80)

    queue = listboxulke.get(0, "end").index(listboxulke.get(ACTIVE))
    response2 = requests.get(toplamurl+ulkelist[queue])
    data = response2.json()

    xlist=[]
    ylist=[]

    for j in range(0,len(data)):
        xlist.append(j)

    for k in range(0,len(data)):
        ylist.insert(k,data[k]["Deaths"])

    x= np.array (xlist)
    y= np.array (ylist)
    pdeaths=f.add_subplot(111)
    pdeaths.set_title(listboxulke.get(ACTIVE), fontsize=12)
    pdeaths.set_xlabel("Day",fontsize=9)
    pdeaths.set_ylabel("Deaths",fontsize=9)

    #pdeaths.plot(x,y)
    #pdeaths.barh(x, y,color='red')
    pdeaths.bar(x, y,color='red',label="Deaths")
    pdeaths.legend(facecolor='gray',shadow='true')
    #pdeaths.figtext('.',listboxulke.get(ACTIVE), fontsize=12)
    canvas = FigureCanvasTkAgg(f, master=m)
    canvas.get_tk_widget().place(x=200,y=25)
def active():
    f = Figure(figsize=(10, 7), dpi=80)

    queue = listboxulke.get(0, "end").index(listboxulke.get(ACTIVE))
    response2 = requests.get(toplamurl + ulkelist[queue])
    data = response2.json()

    xlist = []
    ylist = []

    for j in range(0, len(data)):
        xlist.append(j)

    for k in range(0, len(data)):
        ylist.insert(k, data[k]["Active"])

    x = np.array(xlist)
    y = np.array(ylist)
    pdeaths = f.add_subplot(111)
    pdeaths.set_title(listboxulke.get(ACTIVE), fontsize=12)
    pdeaths.set_xlabel("Day", fontsize=9)
    pdeaths.set_ylabel("Deaths", fontsize=9)

    # pdeaths.plot(x,y)
    # pdeaths.barh(x, y,color='red')
    pdeaths.bar(x, y, color='purple', label="Active")
    pdeaths.legend( shadow='true')
    # pdeaths.figtext('.',listboxulke.get(ACTIVE), fontsize=12)
    canvas = FigureCanvasTkAgg(f, master=m)
    canvas.get_tk_widget().place(x=200, y=25)



def draw():
 try:
        if listboxdatatype.get(ACTIVE) == "Confirmed":
           confirmedd()
        elif listboxdatatype.get(ACTIVE) == "Deaths":
            deaths()
        elif listboxdatatype.get(ACTIVE) == "Recovered":
            recovered()
        elif listboxdatatype.get(ACTIVE) == "Active":
            active()
        elif listboxdatatype.get(ACTIVE) == "Confirmed-Daily":
            confirmeddaily()
        elif listboxdatatype.get(ACTIVE) == "Deaths-Daily":
            deathsdaily()
        elif listboxdatatype.get(ACTIVE) == "Recovered-Daily":
            recovereddaily()
        elif listboxdatatype.get(ACTIVE) == "Active-Daily":
            activedaily()

 except:
        print("hata")
        tkMessageBox.showerror(title="Hata", message="Lütfen çizilmek istenen grafiği seçiniz")

draw=Button(m,text="Draw",width=25,command=draw)
draw.pack(side="left" )
draw.place(x=0,y=567)


#"""

yan=Toplevel()
yan.title("Student")
yan.geometry("200x200+40+50")

yanlbl = Label(yan, text="WELCOME!!!")
yanlbl.pack(side="left")
yanlbl.place(x=0, y=10)

yanlbl2 = Label(yan, text="COVID19 GRAPHIC BUILDER")
yanlbl2.pack(side="left")
yanlbl2.place(x=0, y=35)

def globalstatistics():
    response = requests.get(globalurl)
    data = response.json()
    g = data["Global"];
    #print(type(data))
    #print(data["Global"])
    global1 = Label(m, text=(g))
    global1.pack(side="left")
    global1.place(x=0, y=637)






globalbtn=Button(m,text="Global Statistics",width=25,command=globalstatistics)
globalbtn.pack(side="left" )
globalbtn.place(x=0,y=607)
#607
#"""

m.geometry("1024x768+250+50")
m.mainloop()