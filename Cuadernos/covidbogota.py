import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive
import ipywidgets as widgets
import numpy as np
from IPython.core.display import HTML, display
url='BaseCovid.xlsx'
df=pd.read_excel(url)
df["Estado"]=[i.replace("Fallecido (No aplica, No causa Directa)","Falleci. NA,OC") for i in df["Estado"]]
df["Estado"]=[i.replace(" ","")for i in df["Estado"]]
df["Ubicación"]=[i.replace(" ","")for i in df["Ubicación"]]
df["Ubicación"]=[i.replace("Fallecido(Noaplica,NocausaDirecta)","Falleci. NA,OC") for i in df["Ubicación"]]
df["Tipo de caso"]=[i.replace(" ","")for i in df["Tipo de caso"]]
Pobl_Estudio=df['Localidad de residencia'].value_counts().sort_values(ascending=False)
Pobl_Estudio=Pobl_Estudio.sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(5, 4))
ax.set_ylabel('LOCALIDAD')
ax.set_title('NUMERO DE MUESTRAS TOMADAS EN BOGOTÁ')
display(HTML(    '<h1>COVID 19 A LA FECHA EN BOGOTÁ</h1>'+   
        '<h2>Numero de muestras por localidades del estudio a Analizar</h2>'+
                '<p>En este grafico se observa que la localidad que mas ha recibido la atención de la secretaria '+
             'de salud en cuanto a campañas de detección ha sido la de Kennedy, seguido de la localidad de Suba '+
             'igualmente es de observar que en el tercer rango ascendente se encuentra un segmento importante sin '+
             'dato de localidad:</p>'))

Pobl_Estudio.plot(kind='barh')
#WIDGET 2
display(HTML(    '<h2>DESCRIPCION GENERAL DE LOS CASOS</h2>'+   
        '<h2>Participacion por Estado actual de los casos confirmados a la fecha</h2>'+
                '<p>Un porcentaje importante de los recuperados viene aumentando.:</p>'))
localidad=fig.add_subplot(411)
def f(localidad):
    dfA=df[df["Localidad de residencia"]==localidad].groupby("Estado").count()
    ind=dfA.index
    data=dfA["Edad"]
    fig, ax = plt.subplots(figsize=(4, 5), subplot_kw=dict(aspect="equal"))
    wedges, texts = ax.pie(data,wedgeprops=dict(width=0.5),
                                      startangle=78)
    pct=["{:.2%}".format(da/sum(data)) for da in data]
    bbox_props = dict(boxstyle="rarrow", fc="w", ec="k", lw=0.20)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=5, va="bottom")
        
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))        
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "arc3,rad=0.0".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(ind[i]+"  "+pct[i], xy=(x, y),
                    xytext=(1*np.sign(x), 1*y),
                    horizontalalignment=horizontalalignment, **kw)
    ax.set_title("Distribución de casos en "+localidad+
                 "\n\n"+str(sum(data))+" por Estado Actual"+"\n")

    plt.show()
    return
dfA=df.groupby("Localidad de residencia").count().index
W2=interact(f, localidad=widgets.Dropdown(options=dfA,value="Usme", 
                                       description="Localidad:", 
                                       disabled=False,))
display(HTML(    '<h2>DESCRIPCION GENERAL DE LOS CASOS</h2>'+   
        '<h1>Distribucion de casos por el tipo de caso detectado</h2>'+
                '<p>Se observa una distancia enorme entre los casos identificados y los que estan en estudio.:</p>'))
display(W2)

localidad1=fig.add_subplot(412)
def g(localidad1):
    dfA=df[df["Localidad de residencia"]==localidad1].groupby("Tipo de caso").count()
    ind=dfA.index
    data=dfA["Edad"]
    fig, ax1 = plt.subplots(figsize=(4, 5), subplot_kw=dict(aspect="equal"))
    wedges, texts = ax1.pie(data,wedgeprops=dict(width=0.44),
                                      startangle=40)
    pct=["{:.2%}".format(da/sum(data)) for da in data]
    bbox_props = dict(boxstyle="square,pad=0.1", fc="w", ec="k", lw=0.50)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="bottom")
    
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))        
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax1.annotate(ind[i]+"  "+pct[i], xy=(x, y),
                    xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)
    ax1.set_title("Distribución de casos en "+localidad1+
                 "\n\n"+str(sum(data))+" Tipo de caso"+"\n")

    plt.show()
    return
dfA=df.groupby("Localidad de residencia").count().index
W3=interact(g, localidad1=widgets.Dropdown(options=dfA,value="Usme", 
                                       description="Localidad:", 
                                       disabled=False,))
display(HTML(    '<h2>DESCRIPCION GENERAL DE LOS CASOS</h2>'+   
        '<h1>Lugar actual de atención de los casos de contagio</h2>'+
                '<p>En este valor el numero de Asintomaticos genera una variación importante a la atención en casa:</p>'))
display(W3)

localidad2=fig.add_subplot(413)
def h(localidad2):
    dfA=df[df["Localidad de residencia"]==localidad2].groupby("Ubicación").count()
    ind=dfA.index
    data=dfA["Edad"]
    fig, ax2 = plt.subplots(figsize=(4, 5), subplot_kw=dict(aspect="equal"))
    wedges, texts = ax2.pie(data,wedgeprops=dict(width=0.4),
                                      startangle=400)
    pct=["{:.2%}".format(da/sum(data)) for da in data]
    bbox_props = dict(boxstyle="square,pad=0.1", fc="w", ec="k", lw=0.50)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="bottom")
    
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))        
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=5,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax2.annotate(ind[i]+"  "+pct[i], xy=(x, y),
                    xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)
    ax2.set_title("Distribución de casos en "+localidad2+
                 "\n\n"+str(sum(data))+" por lugar de Atención"+"\n")
    plt.show()
    return
dfA=df.groupby("Localidad de residencia").count().index
W4=interact(h, localidad2=widgets.Dropdown(options=dfA,value="Usme", 
                                       description="Localidad:", 
                                       disabled=False,))
display(HTML(    '<h2>DESCRIPCION GENERAL DE LOS CASOS</h2>'+   
        '<h1>Participacion por genero en el contagio</h2>'+
                '<p>Al observar los casos por genero en las localidades no se observa una diferencia sustancial entre los generos.:</p>'))
display(W4)

localidad3=fig.add_subplot(414)
def r(localidad3):
    dfA=df[df["Localidad de residencia"]==localidad3].groupby("Sexo").count()
    ind=dfA.index
    data=dfA["Edad"]
    fig, ax3 = plt.subplots(figsize=(4, 5), subplot_kw=dict(aspect="equal"))
    wedges, texts = ax3.pie(data,wedgeprops=dict(width=0.4),
                                      startangle=400)
    pct=["{:.2%}".format(da/sum(data)) for da in data]
    bbox_props = dict(boxstyle="square,pad=0.1", fc="w", ec="k", lw=0.50)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="bottom")
    
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))        
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=5,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax3.annotate(ind[i]+"  "+pct[i], xy=(x, y),
                    xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)
    ax3.set_title("Distribución de casos en "+localidad3+
                 "\n\n"+str(sum(data))+" por Genero"+"\n")
    plt.show()
    return
dfA=df.groupby("Localidad de residencia").count().index
W5=interact(r, localidad3=widgets.Dropdown(options=dfA,value="Usme", 
                                       description="Localidad:", 
                                       disabled=False,))

display(HTML(    '<h2>DESCRIPCION GENERAL DE LOS CASOS</h2>'+   
        '<h1>Afectacion en las localidades por estado de contagio</h2>'+
                '<p>Aca se observa de acuerdo al tipo de estado y si gravedad como se ha comportado en las localidades:</p>'))

display(W5)

filtq=df[(df["Estado"]== 'Recuperado')&(df["Localidad de residencia"])]
filtq

def filtroedad(estado):    
    Casos=filtq.groupby("Localidad de residencia").count()
    Casos=Casos.sort_values("Estado")
    fig, ax = plt.subplots(figsize=(10, 8))
    # Una función para poner la cantidad de casos
    def autolabel(rects):
        for rect in rects:
            width = rect.get_width()
            ax.annotate('{}'.format(width),
                        xy=(width,rect.get_y() + rect.get_height() / 2),
                        xytext=(3,0),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='left', va='center')

    rects=ax.barh(Casos.index,Casos["Estado"])
    ax.set(xlim=(0, max(Casos["Estado"])*1.12))
    plt.title("En total hay "+str(sum(Casos["Estado"]))+" en Bogotá")
    autolabel(rects)
    plt.show()
    return

Liloc=list(df["Estado"].unique()) 
W6=interact(filtroedad, estado=widgets.Dropdown(options=Liloc,value="Recuperado", 
                                       description="Seleccione la Localidad:", 
                                       disabled=False,))

display(HTML(    '<h2>REINAN MEDINA G.</h2>'+   
        '<h1>UNIVERSIDAD CENTRAL DE COLOMBIA</h2>'+
                '<p>**Visualizacion 2020/2**:</p>'))


