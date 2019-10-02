# -*- coding: utf-8 -*-
import urllib2
import json
apikey='&appid=700292771ff999637c89a3a9f4a6ec3a'

x=0
y=0

url='http://api.openweathermap.org/data/2.5/weather?id='
def search(request):
    finalurl=url+request+apikey
    finalurl=urllib2.urlopen(finalurl)
    city_file=json.load(finalurl)
    return city_file


poleis={'Alexandroupoli':'8133894', 'Volos':'8133894','Lesvos':'256866',
        'Chalkida':'260133', 'Chios':'8133821', 'Paros':'8133699', 'Karpathos':'8133955',
        'Heraklion':'8133920', 'Chania':'8133762', 'Kerkyra': '8133855', 'Argostoli':'264668',
        'Amaliada':'265252','Gytheio':'251297','Chania':'8133762',
        'Rethimno':'8133759','Shteia':'8133948','Makry Gialos':'7668056',
        'Lemnos':'8133757','Kalamaria':'8133959','Kavala':'8133899','Thasos':'8133898','Pefkochori':'6692661','Thessaloniki':'8133841',
        'Igoumenitsa':'261807','Parga':'255736','Preveza':'8133743','Lefkada':'258445','Agioi Saranta':'363243',
        'Kalamata':'8133971','Pylos':'255293','Kythira':'8133702','Neapoli':'256589',
        'Piraeus':'8133777','Korinthos':'259289','Nafplio':'8133806','Ydra':'8133769','Kea':'260348',
        'Syros-⁠Ermoupoli':'8133927','Serifos':'8133682','Milos':'256952','Ios':'8133833','Ikaria':'8133747','Amorgos':'8133934',
        'Poros':'254865','Ithaki':'261708','Planos':'255096','Lixourion':'258175','Vasiliki':'252200',
        'Spetses':'253356','Parga':'255736','Ierapetra':'8133930','Astypalaia':'8133811','Pefkochori':'6692661','Lemnos':'8133757','Thasos':'8133898',
        'Kastelorizo':'8133700','Kefalos':'260308','Kardamaina':'261003','Kos':'8133957','Megalo Chorio':'257400','Mandraki':'257804','Rhodes':'8133781',
        'Samothraki':'734359','Bozcaada':'320700',
        'Tympaki':'252862',
        'Lesbos':'8133755','Chios':'8133821','Andros':'8133830','Ikaria':'8133747','Samos':'8133749','Foca':'314903'}


con={}

for i in poleis:
    a=poleis[i]
    b=search(a)
    try:
        winds=b['wind']['deg']
        if winds>=22.5 and winds<=67.5:
            direction='NE'
        if winds>=67.5 and winds<=112.5:
            direction='N'
        if winds>=112.5 and winds<=157.5:
            direction='NW'
        if winds>=157.5 and winds<=202.5:
            direction='W'
        if winds>=202.5 and winds<=247.5:
            direction='SW'
        if winds>=247.5 and winds<=292.5:
            direction='S'
        if winds>=292.5 and winds<=337.5:
            direction='SE'
        if winds<=22.5 and winds>=337.5:
            direction='E'
    except KeyError:
        direction='X'
        print 'error stin poli'+i
    con[poleis[i]]={'Tep':str(b['main']['temp']- 273),'icon':str(b['weather'][0]['icon']),'pressure':str(b['main']['pressure']),'windspeed':str(b['wind']['speed']),'winddirection':direction}
    
from  Tkinter import *
############CALLBACK########################
def callback(event):
    if (event.x>=278 and event.x<=480) and (event.y>=571 and event.y<=660):
        print_kriti()
    if (event.x>=133 and event.x<=259) and (event.y>=481 and event.y<=537):
        print_katw_pellop()
    if (event.x>=483 and event.x<=618) and (event.y>=447 and event.y<=599):
        print_rhodes()
    if (event.x>=332 and event.x<=436) and (event.y>=368 and event.y<=518):
        print_kiklades()
    if (event.x>=387 and event.x<=526) and (event.y>=233 and event.y<=367):
        print_lesvos()
    if (event.x>=0 and event.x<=119) and (event.y>=190 and event.y<=375):
        print_kerkira()
    if (event.x>=216 and event.x<=348) and (event.y>=151 and event.y<=241):
        print_salo()
    if (event.x>=263 and event.x<=329) and (event.y>=379 and event.y<=490):
        print_attiki()
############CALLBACK########################
root=Tk()
#root.wm_geometry("930x989+0+0")
root.wm_geometry("630x670+0+0")
c=Canvas(width=1000, height=1000)
#c.bind("<Button-⁠1>", callback)
c.pack()
image=PhotoImage(file="greece.gif")
X=PhotoImage(file="X.gif")
W=PhotoImage(file="W.gif")
SW=PhotoImage(file="SW.gif")
NW=PhotoImage(file="NW.gif")
E=PhotoImage(file="E.gif")
NE=PhotoImage(file="NE.gif")
SE=PhotoImage(file="SE.gif")
N=PhotoImage(file="N.gif")
S=PhotoImage(file="S.gif")

direc={'W':W,'N':N,'S':S,'E':E,'NE':NE,'NW':NW,'SW':SW,'SE':SE,'X':X}

c.create_image(0, 0, anchor="nw", image=image)


c.create_image(385+x,560+y,anchor="nw", image=direc[con[poleis['Heraklion']]['winddirection']])
c.create_text(410+x,592+y, text=con[poleis['Heraklion']]['windspeed']+'m/s', fill="white")
c.create_image(438+x,110+y,anchor="nw", image=direc[con[poleis['Alexandroupoli']]['winddirection']])
c.create_text(454+x,150+y, text=con[poleis['Alexandroupoli']]['windspeed']+'m/s', fill="white")
c.create_image(280+x,228+y,anchor="nw", image=direc[con[poleis['Volos']]['winddirection']])
c.create_text(295+x,260+y, text=con[poleis['Volos']]['windspeed']+'m/s', fill="white")
c.create_image(440+x,268+y,anchor="nw", image=direc[con[poleis['Lesvos']]['winddirection']])
c.create_text(465+x,305+y, text=con[poleis['Lesvos']]['windspeed']+'m/s', fill="white")
c.create_image(340+x,314+y,anchor="nw", image=direc[con[poleis['Chalkida']]['winddirection']])
c.create_text(363+x,349+y, text=con[poleis['Chalkida']]['windspeed']+'m/s', fill="white")
c.create_image(458+x,342+y,anchor="nw", image=direc[con[poleis['Chios']]['winddirection']])
c.create_text(470+x,380+y, text=con[poleis['Chios']]['windspeed']+'m/s', fill="white")
c.create_image(420+x,460+y,anchor="nw", image=direc[con[poleis['Paros']]['winddirection']])
c.create_text(435+x,497+y, text=con[poleis['Paros']]['windspeed']+'m/s', fill="white")
c.create_image(560+x,551+y,anchor="nw", image=direc[con[poleis['Karpathos']]['winddirection']])
c.create_text(575+x,585+y, text=con[poleis['Karpathos']]['windspeed']+'m/s', fill="white")
c.create_image(300+x,530+y,anchor="nw", image=direc[con[poleis['Chania']]['winddirection']])
c.create_text(310+x,565+y, text=con[poleis['Chania']]['windspeed']+'m/s', fill="white")
c.create_image(20+x,220+y,anchor="nw", image=direc[con[poleis['Kerkyra']]['winddirection']])
c.create_text(40+x,265+y, text=con[poleis['Kerkyra']]['windspeed']+'m/s', fill="white")
c.create_image(65+x,392+y,anchor="nw", image=direc[con[poleis['Argostoli']]['winddirection']])
c.create_text(90+x,430+y, text=con[poleis['Argostoli']]['windspeed']+'m/s', fill="white")
c.create_image(127+x,436+y,anchor="nw", image=direc[con[poleis['Amaliada']]['winddirection']])
c.create_text(147+x,470+y, text=con[poleis['Amaliada']]['windspeed']+'m/s', fill="white")
c.create_image(190+x,500+y,anchor="nw", image=direc[con[poleis['Gytheio']]['winddirection']])
c.create_text(200+x,535+y, text=con[poleis['Gytheio']]['windspeed']+'m/s', fill="white")
c.create_image(298+x,450+y,anchor="nw", image=direc[con[poleis['Spetses']]['winddirection']])
c.create_text(315+x,490+y, text=con[poleis['Spetses']]['windspeed']+'m/s', fill="white")
c.create_image(50+x,277+y,anchor="nw", image=direc[con[poleis['Parga']]['winddirection']])
c.create_text(75+x,320+y, text=con[poleis['Parga']]['windspeed']+'m/s', fill="white")
c.create_image(485+x,590+y,anchor="nw", image=direc[con[poleis['Ierapetra']]['winddirection']])
c.create_text(499+x,625+y, text=con[poleis['Ierapetra']]['windspeed']+'m/s', fill="white")
c.create_image(465+x,510+y,anchor="nw", image=direc[con[poleis['Astypalaia']]['winddirection']])
c.create_text(480+x,545+y, text=con[poleis['Astypalaia']]['windspeed']+'m/s', fill="white")
c.create_image(335+x,195+y,anchor="nw", image=direc[con[poleis['Pefkochori']]['winddirection']])
c.create_text(358+x,235+y, text=con[poleis['Pefkochori']]['windspeed']+'m/s', fill="white")
c.create_image(420+x,187+y,anchor="nw", image=direc[con[poleis['Lemnos']]['winddirection']])
c.create_text(437+x,237+y, text=con[poleis['Lemnos']]['windspeed']+'m/s', fill="white")
c.create_image(375+x,135+y,anchor="nw", image=direc[con[poleis['Thasos']]['winddirection']])
c.create_text(390+x,170+y, text=con[poleis['Thasos']]['windspeed']+'m/s', fill="white")
c.create_image(490+x,440+y,anchor="nw", image=direc[con[poleis['Ikaria']]['winddirection']])
c.create_text(505+x,480+y, text=con[poleis['Ikaria']]['windspeed']+'m/s', fill="white")
c.create_image(100+x,550+y,anchor="nw", image=direc[con[poleis['Pylos']]['winddirection']])
c.create_text(115+x,590+y, text=con[poleis['Pylos']]['windspeed']+'m/s', fill="white")



def print_kriti():
    top_kriti=Toplevel(root)
    top_kriti.wm_geometry("630x690+0+0")
    k1=Canvas(top_kriti,  height=600, width=600)
    image1=PhotoImage(file="kriti.gif")
    k1.create_image(0, 0, anchor="nw", image=image1)
    k1.create_image(348+x,75+y,anchor="nw", image=direc[con[poleis['Heraklion']]['winddirection']])
    k1.create_text(348+x,110+y, text=con[poleis['Heraklion']]['windspeed']+'m/s', fill="white")
    k1.create_text(386+x,110+y, text=con[poleis['Heraklion']]['pressure']+'P', fill="white")
    k1.create_text(360+x,125+y, text=con[poleis['Heraklion']]['Tep']+'C', fill="white")
    k1.create_image(242+x,80+y,anchor="nw", image=direc[con[poleis['Rethimno']]['winddirection']])
    k1.create_text(231+x,117+y, text=con[poleis['Rethimno']]['windspeed']+'m/s', fill="white")
    k1.create_text(273+x,117+y, text=con[poleis['Rethimno']]['pressure']+'P', fill="white")
    k1.create_text(255+x,132+y, text=con[poleis['Rethimno']]['Tep']+'C', fill="white")
    k1.create_image(107+x,195+y,anchor="nw", image=direc[con[poleis['Rethimno']]['winddirection']])
    k1.create_text(100+x,230+y, text=con[poleis['Rethimno']]['windspeed']+'m/s', fill="white")
    k1.create_text(147+x,230+y, text=con[poleis['Rethimno']]['pressure']+'P', fill="white")
    k1.create_text(120+x,250+y, text=con[poleis['Rethimno']]['Tep']+'C', fill="white")
    k1.create_image(447+x,105+y,anchor="nw", image=direc[con[poleis['Shteia']]['winddirection']])
    k1.create_text(438+x,145+y, text=con[poleis['Shteia']]['windspeed']+'m/s', fill="white")
    k1.create_text(492+x,145+y, text=con[poleis['Shteia']]['pressure']+'P', fill="white")
    k1.create_text(465+x,160+y, text=con[poleis['Shteia']]['Tep']+'C', fill="white")
    k1.create_image(150+x,50+y,anchor="nw", image=direc[con[poleis['Chania']]['winddirection']])
    k1.create_text(145+x,90+y, text=con[poleis['Chania']]['windspeed']+'m/s', fill="white")
    k1.create_text(190+x,90+y, text=con[poleis['Chania']]['pressure']+'P', fill="white")
    k1.create_text(162+x,105+y, text=con[poleis['Chania']]['Tep']+'C', fill="white")
    k1.create_image(441+x,220+y,anchor="nw", image=direc[con[poleis['Makry Gialos']]['winddirection']])
    k1.create_text(429+x,250+y, text=con[poleis['Makry Gialos']]['windspeed']+'m/s', fill="white")
    k1.create_text(482+x,250+y, text=con[poleis['Makry Gialos']]['Tep']+'P', fill="white")
    k1.create_text(455+x,270+y, text=con[poleis['Makry Gialos']]['Tep']+'C', fill="white")
    k1.create_image(342+x,237+y,anchor="nw", image=direc[con[poleis['Ierapetra']]['winddirection']])
    k1.create_text(335+x,275+y, text=con[poleis['Ierapetra']]['windspeed']+'m/s', fill="white")
    k1.create_text(382+x,275+y, text=con[poleis['Ierapetra']]['Tep']+'P', fill="white")
    k1.create_text(360+x,295+y, text=con[poleis['Ierapetra']]['Tep']+'C', fill="white")
    k1.create_image(232+x,205+y,anchor="nw", image=direc[con[poleis['Tympaki']]['winddirection']])
    k1.create_text(227+x,240+y, text=con[poleis['Tympaki']]['windspeed']+'m/s', fill="white")
    k1.create_text(273+x,240+y, text=con[poleis['Tympaki']]['Tep']+'P', fill="white")
    k1.create_text(250+x,260+y, text=con[poleis['Tympaki']]['Tep']+'C', fill="white")
    k1.pack(side=TOP)
    b1=Frame(top_kriti)
    b1.pack()
    B1=Button(b1,text='Done',command=top_kriti.destroy)
    B1.pack(side=TOP)
    k1.mainloop()
    top_kriti.mainloop()
def print_kiklades():
    top_kiklades=Toplevel(root)
    top_kiklades.wm_geometry("630x690+0+0")
    k2=Canvas(top_kiklades,  height=600, width=600)
    image2=PhotoImage(file="kiklades.gif")
    k2.create_image(0, 0, anchor="nw", image=image2)
    k2.create_image(280+x,290+y,anchor="nw", image=direc[con[poleis['Paros']]['winddirection']])
    k2.create_text(280+x,330+y, text=con[poleis['Paros']]['windspeed']+"m/s", fill="white")
    k2.create_text(325+x,330+y, text="1000a", fill="white")
    k2.create_text(300+x,350+y, text="25.18c", fill="white")
    k2.create_image(210+x,200+y,anchor="nw", image=direc[con[poleis['Syros-⁠Ermoupoli']]['winddirection']])
    k2.create_text(205+x,240+y, text=con[poleis['Syros-⁠Ermoupoli']]['windspeed']+"m/s", fill="white")
    k2.create_text(245+x,240+y, text="1000a", fill="white")
    k2.create_text(225+x,260+y, text="25.18c", fill="white")
    k2.create_image(50+x,200+y,anchor="nw", image=direc[con[poleis['Serifos']]['winddirection']])
    k2.create_text(45+x,240+y, text=con[poleis['Serifos']]['windspeed']+"m/s", fill="white")
    k2.create_text(95+x,240+y, text="1000a", fill="white")
    k2.create_text(75+x,260+y, text="25.18c", fill="white")
    k2.create_image(100+x,400+y,anchor="nw", image=direc[con[poleis['Milos']]['winddirection']])
    k2.create_text(100+x,440+y, text=con[poleis['Milos']]['windspeed']+"m/s", fill="white")
    k2.create_text(140+x,440+y, text="1000a", fill="white")
    k2.create_text(110+x,460+y, text="25.18c", fill="white")
    k2.create_image(280+x,380+y,anchor="nw", image=direc[con[poleis['Ios']]['winddirection']])
    k2.create_text(280+x,420+y, text=con[poleis['Ios']]['windspeed']+"m/s", fill="white")
    k2.create_text(320+x,420+y, text="1000a", fill="white")
    k2.create_text(300+x,440+y, text="25.18c", fill="white")
    k2.create_image(460+x,180+y,anchor="nw", image=direc[con[poleis['Ikaria']]['winddirection']])
    k2.create_text(460+x,220+y, text=con[poleis['Ikaria']]['windspeed']+"m/s", fill="white")
    k2.create_text(510+x,220+y, text="1000a", fill="white")
    k2.create_text(470+x,240+y, text="25.18c", fill="white")
    k2.create_image(300+x,60+y,anchor="nw", image=direc[con[poleis['Ikaria']]['winddirection']])
    k2.create_text(300+x,100+y, text=con[poleis['Ikaria']]['windspeed']+"m/s", fill="white")
    k2.create_text(340+x,100+y, text="1000a", fill="white")
    k2.create_text(310+x,120+y, text="25.18c", fill="white")
    k2.create_image(460+x,310+y,anchor="nw", image=direc[con[poleis['Amorgos']]['winddirection']])
    k2.create_text(460+x,350+y, text=con[poleis['Amorgos']]['windspeed']+"m/s", fill="white")
    k2.create_text(510+x,350+y, text="1000a", fill="white")
    k2.create_text(470+x,370+y, text="25.18c", fill="white")
    k2.pack(side=TOP)
    b2=Frame(top_kiklades)
    b2.pack()
    B2=Button(b2,text='Done',command=top_kiklades.destroy)
    B2.pack(side=TOP)
    k2.mainloop()
    top_kiklades.mainloop()
def print_rhodes():
    top_rhodes=Toplevel(root)
    top_rhodes.wm_geometry("630x690+0+0")
    k3=Canvas(top_rhodes,  height=600, width=600)
    image3=PhotoImage(file="rhodes.gif")
    k3.create_image(0, 0, anchor="nw", image=image3)
    k3.pack(side=TOP)
    b3=Frame(top_rhodes)
    b3.pack()
    B3=Button(b3,text='Done',command=top_rhodes.destroy)
    B3.pack(side=TOP)
    k3.mainloop()
    top_rhodes.mainloop()
def print_attiki():
    top_attiki=Toplevel(root)
    top_attiki.wm_geometry("630x690+0+0")
    k4=Canvas(top_attiki,  height=600, width=600)
    image4=PhotoImage(file="attiki.gif")
    k4.create_image(0, 0, anchor="nw", image=image4)
    k4.pack(side=TOP)
    b4=Frame(top_attiki)
    b4.pack()
    B4=Button(b4,text='Done',command=top_attiki.destroy)
    B4.pack(side=TOP)
    k4.mainloop()
    top_attiki.mainloop()
def print_salo():
    top_salo=Toplevel(root)
    top_salo.wm_geometry("630x690+0+0")
    k5=Canvas(top_salo,  height=600, width=600)
    image5=PhotoImage(file="salo.gif")
    k5.create_image(0, 0, anchor="nw", image=image5)
    k5.pack(side=TOP)
    b5=Frame(top_salo)
    b5.pack()
    B5=Button(b5,text='Done',command=top_salo.destroy)
    B5.pack(side=TOP)
    k5.mainloop()
    top_salo.mainloop()
def print_lesvos():
    top_lesvos=Toplevel(root)
    top_lesvos.wm_geometry("630x690+0+0")
    k6=Canvas(top_lesvos,  height=600, width=600)
    image6=PhotoImage(file="lesvos.gif")
    k6.create_image(0, 0, anchor="nw", image=image6)
    k6.pack(side=TOP)
    b6=Frame(top_lesvos)
    b6.pack()
    B6=Button(b6,text='Done',command=top_lesvos.destroy)
    B6.pack(side=TOP)
    k6.mainloop()
    top_lesvos.mainloop()
def print_thraki():
    top_thraki=Toplevel(root)
    top_thraki.wm_geometry("630x690+0+0")
    k7=Canvas(top_thraki,  height=600, width=600)
    image7=PhotoImage(file="thraki.gif")
    k7.create_image(0, 0, anchor="nw", image=image7)
    k7.pack(side=TOP)
    b7=Frame(top_thraki)
    b7.pack()
    B7=Button(b7,text='Done',command=top_thraki.destroy)
    B7.pack(side=TOP)
    k7.mainloop()
    top_thraki.mainloop()
def print_volos():
    top_volos=Toplevel(root)
    top_volos.wm_geometry("630x690+0+0")
    k8=Canvas(top_volos,  height=600, width=600)
    image8=PhotoImage(file="volos.gif")
    k8.create_image(0, 0, anchor="nw", image=image8)
    k8.pack(side=TOP)
    b8=Frame(top_volos)
    b8.pack()
    B8=Button(b8,text='Done',command=top_volos.destroy)
    B8.pack(side=TOP)
    k8.mainloop()
    top_volos.mainloop()
def print_panwpellop():
    top_panwpellop=Toplevel(root)
    top_panwpellop.wm_geometry("630x690+0+0")
    k9=Canvas(top_panwpellop,  height=600, width=600)
    image9=PhotoImage(file="panwpellop.gif")
    k9.create_image(0, 0, anchor="nw", image=image9)
    k9.pack(side=TOP)
    b9=Frame(top_panwpellop)
    b9.pack()
    B9=Button(b9,text='Done',command=top_panwpellop.destroy)
    B9.pack(side=TOP)
    k9.mainloop()
    top_panwpellop.mainloop()
def print_katw_pellop():
    top_katw_pellop=Toplevel(root)
    top_katw_pellop.wm_geometry("630x690+0+0")
    k10=Canvas(top_katw_pellop,  height=600, width=600)
    image10=PhotoImage(file="katw_pellop.gif")
    k10.create_image(0, 0, anchor="nw", image=image10)
    k10.pack(side=TOP)
    b10=Frame(top_katw_pellop)
    b10.pack()
    B10=Button(b10,text='Done',command=top_katw_pellop.destroy)
    B10.pack(side=TOP)
    k10.mainloop()
    top_katw_pellop.mainloop()
def print_kerkira():
    top_kerkira=Toplevel(root)
    top_kerkira.wm_geometry("630x690+0+0")
    k11=Canvas(top_kerkira,  height=600, width=600)
    image11=PhotoImage(file="kerkira.gif")
    k11.create_image(0, 0, anchor="nw", image=image11)
    k11.create_image(100,80,anchor="nw", image=direc[con[poleis['Agioi Saranta']]['winddirection']])
    k11.create_text(90,115, text=con[poleis['Agioi Saranta']]['windspeed']+'m/s', fill="white")
    k11.create_text(140,115, text=con[poleis['Agioi Saranta']]['pressure']+'A', fill="white")
    k11.create_text(115,140, text=con[poleis['Agioi Saranta']]['Tep']+'C', fill="white")
    k11.create_image(100,250,anchor="nw", image=direc[con[poleis['Kerkyra']]['winddirection']])
    k11.create_text(90,280, text=con[poleis['Kerkyra']]['windspeed']+'m/s', fill="white")
    k11.create_text(140,280, text=con[poleis['Kerkyra']]['pressure']+'A', fill="white")
    k11.create_text(115,300, text=con[poleis['Kerkyra']]['Tep']+'C', fill="white")
    k11.create_image(240,190,anchor="nw", image=direc[con[poleis['Igoumenitsa']]['winddirection']])
    k11.create_text(230,220, text=con[poleis['Igoumenitsa']]['windspeed']+'m/s', fill="white")
    k11.create_text(280,220, text=con[poleis['Igoumenitsa']]['pressure']+'A', fill="white")
    k11.create_text(245,240, text=con[poleis['Igoumenitsa']]['Tep']+'C', fill="white")
    k11.create_image(180,350,anchor="nw", image=direc[con[poleis['Kerkyra']]['winddirection']])
    k11.create_text(170,380, text=con[poleis['Kerkyra']]['windspeed']+'m/s', fill="white")
    k11.create_text(220,380, text=con[poleis['Kerkyra']]['pressure']+'A', fill="white")
    k11.create_text(195,400, text=con[poleis['Kerkyra']]['Tep']+'C', fill="white")
    k11.create_image(370,370,anchor="nw", image=direc[con[poleis['Parga']]['winddirection']])
    k11.create_text(360,400,text=con[poleis['Parga']]['windspeed']+'m/s', fill="white")
    k11.create_text(400,400, text=con[poleis['Parga']]['pressure']+'A', fill="white")
    k11.create_text(380,420, text=con[poleis['Parga']]['Tep']+'C', fill="white")
    k11.create_image(350,450,anchor="nw", image=direc[con[poleis['Preveza']]['winddirection']])
    k11.create_text(340,485,text=con[poleis['Preveza']]['windspeed']+'m/s', fill="white")
    k11.create_text(380,485, text=con[poleis['Preveza']]['pressure']+'A', fill="white")
    k11.create_text(360,505, text=con[poleis['Preveza']]['Tep']+'C', fill="white")
    k11.create_image(250,500,anchor="nw", image=direc[con[poleis['Lefkada']]['winddirection']])
    k11.create_text(240,535,text=con[poleis['Lefkada']]['windspeed']+'m/s', fill="white")
    k11.create_text(280,535, text=con[poleis['Lefkada']]['pressure']+'A', fill="white")
    k11.create_text(260,555, text=con[poleis['Lefkada']]['Tep']+'C', fill="white")
    k11.pack(side=TOP)
    b11=Frame(top_kerkira)
    b11.pack()
    B11=Button(b11,text='Done',command=top_kerkira.destroy)
    B11.pack(side=TOP)
    k11.mainloop()
    top_kerkira.mainloop()
class ManosButtons:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        menu=Menu(root)
        root.config(menu=menu)
        subMenu=Menu(menu)
        menu.add_cascade(label="Locations",menu=subMenu)
        subMenu.add_command(label="Creta", command=print_kriti)
        subMenu.add_separator()
        subMenu.add_command(label="Kiklades", command=print_kiklades)
        subMenu.add_separator()
        subMenu.add_command(label="Rhodes", command=print_rhodes)
        subMenu.add_separator()
        subMenu.add_command(label="Kerkira", command=print_kerkira)
        subMenu.add_separator()
        subMenu.add_command(label="Attiki", command=print_attiki)
        subMenu.add_separator()
        subMenu.add_command(label="Thessaloniki", command=print_salo)
        subMenu.add_separator()
        subMenu.add_command(label="Lesvos", command=print_lesvos)
        subMenu.add_separator()
        subMenu.add_command(label="Thraki", command=print_thraki)
        subMenu.add_separator()
        subMenu.add_command(label="KatwPelopo", command=print_katw_pellop)
        subMenu.add_separator()
       
b=ManosButtons(root)
root.mainloop()
