from importlib.resources import path
from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import funtions as ft
import folium
from folium import plugins
import streamlit.components.v1 as stc 


# pongo mis datos 
st.write("""Laura García Sánchez\n
Proyecto EDA realizado para el bootcamp de **Data Science** en The Bridge
""")

# titulo EDA, centro el texto para que quede mejor
st.markdown("<h1 style='text-align: center; color: black;'>Exploratory and Data Analisys</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>Airbnb</h1>", unsafe_allow_html=True)
#st.title('Airbnb  ')
# st.title(' Exploratory and Data Analisys')
# pongo la foto principal de Airbnb
st.image('./barcelona//img/airbnb-Barcelona.jpg',width=1100)

# aqui pongo la descripción inicial del estudio
st.markdown('> ### Análisis:')
st.markdown('#### Mi análisis principal se ha basado en elegir cuatro de las ciudades más caras del mundo, dos en Estados Unidos, y las otras dos en Europa. \
    \n #### Inicialmente de las 4 escogidas, *New York* es la que el coste de vida es más elevado. \
        Y quiero comprobar con mi análisis si también lo será en Airbnb. \
            Además de analizar los diferentes distritos y alojamientos con los que cuenta cada ciudad. \
            Así como información interesante de una ciudad a otra ') 


# poner en contexto qué es Airbnb
st.markdown('> ### ¿Qué es Airbnb?')
st.markdown('#### Airbnb es una plataforma online que pone en contacto a personas que tienen una vivienda que ofrecer, \
con personas que necesitan un lugar en dónde quedarse de forma temporal. \
    Airbnb se ha convertido en una web de referencia para el alquiler de viviendas.') # acabar de poner bien la descripción 


# Quiero mostrar las ciudades elegidas
st.markdown('> ### Ciudades elegidas: ')

# creo columnas para poder mostrarlas de dos en dos 
col1, col2= st.columns(2) 
with col1:
    st.write(" #### Barcelona")
    with open(".//barcelona//img/Mapa_geojson_bcn_general_bcn.htlm", "r") as f:
        text = f.read()
    stc.html(text, width=800, height=650)
with col2:
    st.write("#### Copenhague")
    with open(".//copenhague//img/Mapa_geojson_cop_general.htlm", "r") as f:
        text1 = f.read()
    stc.html(text1, width=500, height=650)

col1, col2= st.columns(2) # si ponemos 4 hemos de usar 4, son columnas
with col1:
    st.write("#### New York")
    with open(".//new_york//img/Mapa_geojson_general_nw.htlm", "r") as f:
        text = f.read()
    stc.html(text, width=800, height=650)
with col2:
    st.write("#### Seattle")
    with open(".//Seattle//img/Mapa_geojson_cop_general.htlm", "r") as f:
        text = f.read()
    stc.html(text, width=500, height=650)


# Analizo como están distribuidos los alojamientos Airbnb en los barrios en las ciudades elegidas
st.markdown('> ### ¿Cómo están distribuidos los Airbnb en los barrios? ')
#st.write("Barcelona")
st.image('./barcelona/img/barrio_distribucion.png',width=1400)
#st.write("Copenhagen")
st.caption("* La ciudad de Copenhague en Airbnb está solo distribuida por distritos")
st.image('./copenhague/img/alojamiento_por_distritos_10.png', width=1400)
#st.write("New York")
st.image('./new_york/img/alojamiento_por_barrios_10_nw.png', width=1400)
#st.write("Seattle")
st.image('./seattle/img/alojamiento_por_barrios_10_seattle.png', width=1400)

# Quiero saber qué barrios son los que tienen más de 900 alojamientos
st.markdown(' > ### Los barrios que tienen más alojamientos')
st.image('./barcelona/img/barrio_mas_concurrente_barcelona.png',width=1300)
st.image('./copenhague/img/barrio_mas_concurrente_cop.png', width=1300)
st.image('./new_york/img/barrio_mas_concurrente_ny.png', width=1300)
st.image('./seattle/img/barrio_mas_concurrente_seattle.png', width=1300)
st.caption("* Seattle no llega a los 900 alojamientos Airbnb por barrio, el máximo está en 300 alojamientos ")
# ranking
st.markdown(" #### El barrio máximo de Airbnb por ciudad:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("New York", "2825", "1")
col2.metric("Barcelona", "1933", "2")
col3.metric("Copenhague", "1712", "3")
col4.metric("Seattle", "300", "4")

# Quiero saber qué barrios son los que tienen menos alojamientos
st.markdown('> ###  Los barrios con menos alojamientos de Airbnb')
st.image('./barcelona/img/barrio_menos_concurrente_10.png',width=1300)
st.image('./copenhague/img/barrio_menos_concurrente_10_cop.png', width=1300)
st.image('./new_york/img/barrio_menos_concurrente_10_nw.png', width=1300)
st.image('./seattle/img/barrio_menos_concurrente_10_seattle.png', width=1300)
st.caption("* Seattle no llega a los 900 alojamientos Airbnb por barrio, el máximo está en 300 alojamientos ")
# ranking
st.markdown(" #### El mínimo de Airbnb por barrio:")
col1, col2, col3, col4 = st.columns(4)
col3.metric("New York", "1", "1")
col2.metric("Barcelona", "1", "1")
col1.metric("Copenhague", "226", '1')
col4.metric("Seattle", "1", "1")


##########################################################################

# # Quiero mostrar los barrios por ciudades lo quito porque no se ven las gráficas
st.markdown('> ### Barrios por ciudades en mapa: ')

# creo columnas para poder mostrarlas de dos en dos 
col1, col2= st.columns(2) 
with col1:
    st.write("Barcelona")
    with open("./barcelona/img/mapas/mapa_barrios_bcn.htlm", "r") as f:
        text = f.read()
    stc.html(text, width=800, height=650)
with col2:
    st.write("Copenhagen")
    with open("./copenhague/img/mapas/mapa_barrios_cop_tierra_cop.htlm", "r") as f:
        text1 = f.read()
    stc.html(text1, width=500, height=650)

col1, col2= st.columns(2) 
with col1:
    st.write("New York")
    with open("./new_york/img/mapas/mapa_barrios_ny.htlm", "r") as f:
        text = f.read()
    stc.html(text, width=800, height=650)
with col2:
    st.write("Seattle")
    with open("./seattle/img/mapas/mapa_barrios_seattle.htlm", "r") as f:
        text = f.read()
    stc.html(text, width=800, height=650) # he subido más el height



###############################################################################
# muestro como están distribuidos los Airbnb por los distritos de cada ciudad
st.write(' > ### ¿Cómo están distribuidos los Airbnb en los distritos de las ciudades? ')
#st.write("Barcelona")
st.image('./barcelona/img/alojamiento_por_distritos_10.png',width=1400)
#st.write("Copenhagen")
st.caption("* La ciudad de Copenhague en Airbnb está solo distribuida por distritos")
st.image('./copenhague/img/alojamiento_por_distritos_10.png', width=1400)
#st.write("New York")
st.image('./new_york/img/alojamiento_por_distritos_nw.png', width=1400)
#st.write("Seattle")
st.image('./seattle/img/alojamiento_por_distritos_seattle.png', width=1400)

# ranking
st.markdown(" #### El número máximo de Airbnb por distrito:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("New York", "16.086", "1")
col2.metric("Barcelona", "5555", "2")
col3.metric("Copenhague", "1712", '3')
col4.metric("Seattle", "944", "4")

# ranking total
# alojamientos totales por ciudad
st.markdown(" #### Airbnb totales por ciudad:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("New York", "37.631", "1")
col2.metric("Barcelona", "16.042", "2")
col3.metric("Copenhague", "10.250", '3')
col4.metric("Seattle", "4.883", "4")




# muestro como están distribuidos los Airbnb en los distritos con mapas
st.markdown('> ### Distritos por ciudades en mapas: ')

# creo columnas para poder mostrarlas de dos en dos, no me están cargando bien los mapas
col1, col2= st.columns(2) 
with col1:
    st.write("Barcelona")
    with open("./barcelona/img/mapas/Mapa_geojson_bcn_distritos_tierra.htlm", "r") as f:
        text = f.read()
    stc.html(text, width=800, height=650)
with col2:
    st.write("Copenhague")
    with open("./copenhague/img/mapas/mapa_barrios_cop_tierra_.htlm", "r") as f:
        text1 = f.read()
    stc.html(text1, width=500, height=650)

col1, col2= st.columns(2) # si ponemos 4 hemos de usar 4, son columnas
with col1:
    st.write("New York")
    with open("./new_york/img/mapas/Mapa_geojson_distritos_ny_tierra.htlm", "r") as f:
        text = f.read()
    stc.html(text, width=800, height=650)
with col2:
    st.write("Seattle")
    with open("./seattle/img/mapas/mapa_distritos_tierra_seattle.htlm", "r") as f:
        text = f.read()
    stc.html(text, width=500, height=650) # 


###############################################################################################################
# Analizando los precios 
# precio mínimo por distrito
st.markdown('> ##  Analizando los precios de Airbnb por distrito por día')
st.markdown('> ###  Precio mínimo de Airbnb por distrito por día')
st.image('./barcelona/img/precio_min_distrito.png',width=1300)
st.image('./copenhague/img/precio_min_distrito.png', width=1300)
st.image('./new_york/img/precio_min_distrito_nw.png', width=1300)
st.image('./seattle/img/precio_min_distrito_seattle.png', width=1300)
st.caption("* Seattle no llega a los 900 alojamientos Airbnb por barrio, el máximo está en 300 alojamientos ")

# ranking del precio mínimo
st.markdown(" #### Precio mínimo Airbnb por distrito:")
col1, col2, col3, col4 = st.columns(4)
col2.metric("New York", "10€", "2")
col4.metric("Barcelona", "8€", "1")
col1.metric("Copenhague", "75€", '1')
col3.metric("Seattle", "10€", "2")


# precio máximo por distrito
st.markdown('> ###  Precio máximo de Airbnb por distrito por día')
st.image('./barcelona/img/precio_max_distrito_todos_aloj.png',width=1300)
st.image('./copenhague/img/precio_max_distrito_todos_aloj.png', width=1300)
st.image('./new_york/img/precio_max_distrito_todos_aloj_nw.png', width=1300)
st.image('./seattle/img/precio_max_distrito_todos_aloj_seattle.png', width=1300)

# ranking del precio máximo
st.markdown(" #### Precio máximo de Airbnb por día por distrito:")
col1, col2, col3, col4 = st.columns(4)
col2.metric("New York", "10.000€", "2")
col3.metric("Barcelona", "9.200€", "3")
col1.metric("Copenhague", "100.00€", '1')
col4.metric("Seattle", "3.750€", "4")

# media del precio por distrito
st.markdown('> ###  Media del precio de Airbnb por distrito por día')
st.image('./barcelona/img/precio_media_distrito.png',width=1300)
st.image('./copenhague/img/precio_media_distrito.png', width=1300)
st.image('./new_york/img/precio_media_distrito_nw.png', width=1300)
st.image('./seattle/img/precio_media_distrito_seattle.png', width=1200)

# media del precio máximo
st.markdown(" #### Media precio de Airbnb por día:")
col1, col2, col3, col4 = st.columns(4)
col2.metric("New York", "166,33€", "2")
col4.metric("Barcelona", "118,99€", "4")
col1.metric("Copenhague", "1.125,51€", '1')
col3.metric("Seattle", "159,94€", "3")


########################################################################################
# Analizando los alojamientos
st.markdown('> ### Analizando los apartamentos\n #### Airbnb cuenta con 4 tipos de alojamientos:\n + \
Apartamento entero\n + Habitaciones privadas\n + Habitaciones compartidas\n + Habitaciones asociadas a algún hotel.')
st.image('./barcelona/img/volumen_alojamiento_distrito_bcn.png',width=1300)
st.image('./copenhague/img/volumen_alojamiento_distrito_cop.png', width=1300)
st.image('./new_york/img/volumen_alojamiento_distrito_nw.png', width=1300)
st.image('./seattle/img/volumen_alojamiento_distrito_seattle.png', width=1200)

# ranking
st.markdown("> ### Cantidad de Airbnb por ciudad por tipo de alojamiento:")
st.markdown(" ### Seattle:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "4.088")
col2.metric("Habitaciones privadas", "757")
col3.metric("Habitaciones compartidas", "36")
col4.metric("Habitaciones en hotel", "2")
st.markdown(" ### Copenhague:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "8.863")
col2.metric("Habitaciones privadas", "1.340")
col3.metric("Habitaciones compartidas", "27")
col4.metric("Habitaciones en hotel", "20")
st.markdown(" ### New York:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "20.362", '1')
col2.metric("Habitaciones privadas", "16.500", '1')
col3.metric("Habitaciones compartidas", "571", '1')
col4.metric("Habitaciones en hotel", "198")
st.markdown(" ### Barcelona:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "8.799")
col2.metric("Habitaciones privadas", "6.791")
col3.metric("Habitaciones compartidas", "234")
col4.metric("Habitaciones en hotel", "218", '1')

######################################################################################################

# Analizando el precio por alojamiento
# precio mínimo por alojamiento
st.markdown('> ### Antes hemos visto los precios en general por distrito, ahora vamos a ver los precios por tipo de alojamiento.')
st.markdown('>> ### Precio mínimo por tipo de alojamiento.')
st.image('./barcelona/img/precio_min_por_alojamiento_bcn.png',width=1300)
st.image('./copenhague/img/precio_min_por_alojamiento_cop.png', width=1300)
st.image('./new_york/img/precio_min_por_alojamiento_ny.png', width=1300)
st.image('./seattle/img/precio_min_por_alojamiento_seattle.png', width=1200)
st.markdown(" ### Precios mínimos por tipo de alojamiento:")
st.markdown(" ### New York:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "10€", '1')
col2.metric("Habitaciones privadas", "10€")
col3.metric("Habitaciones compartidas", "15€")
col4.metric("Habitaciones en hotel", "100€")
st.markdown(" ### Copenhague:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "75€", '1')
col2.metric("Habitaciones privadas", "103€")
col3.metric("Habitaciones compartidas", "250€")
col4.metric("Habitaciones en hotel", "178€")
st.markdown(" ### Seattle:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "10€", '1')
col2.metric("Habitaciones privadas", "13€")
col3.metric("Habitaciones compartidas", "18€")
col4.metric("Habitaciones en hotel", "128€")
st.markdown(" ### Barcelona:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "8€", '1')
col2.metric("Habitaciones privadas", "8€")
col3.metric("Habitaciones compartidas", "10€")
col4.metric("Habitaciones en hotel", "17€")

# precio máximo por alojamiento
st.markdown('>> ### Precio máximo por tipo de alojamiento.')
st.image('./barcelona/img/precio_max_por_alojamiento_bcn.png',width=1300)
st.image('./copenhague/img/precio_max_por_alojamiento_cop.png', width=1300)
st.image('./new_york/img/precio_max_por_alojamiento_ny.png', width=1300)
st.image('./seattle/img/precio_max_por_alojamiento_seattle.png', width=1200)
st.markdown(" ### Precios máximos por tipo de alojamiento:")
st.markdown(" ### New York:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "10.000€", '1')
col2.metric("Habitaciones privadas", "10.000€")
col3.metric("Habitaciones compartidas", "10.000€")
col4.metric("Habitaciones en hotel", "1600€")
st.markdown(" ### Copenhague:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "100.000€", '1')
col2.metric("Habitaciones privadas", "64.900€")
col3.metric("Habitaciones compartidas", "2.291€")
col4.metric("Habitaciones en hotel", "1.921€")
st.markdown(" ### Seattle:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "3750€", '1')
col2.metric("Habitaciones privadas", "999€")
col3.metric("Habitaciones compartidas", "80€")
col4.metric("Habitaciones en hotel", "128€")
st.markdown(" ### Barcelona:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "9.200€", '1')
col2.metric("Habitaciones privadas", "6.666€")
col3.metric("Habitaciones compartidas", "2.000€")
col4.metric("Habitaciones en hotel", "999€")


# media del precio por tipo  alojamiento
st.markdown('>> ### Media del precio por tipo de alojamiento.')
st.image('./barcelona/img/precio_medio_por_alojamiento_bcn.png',width=1300)
st.image('./copenhague/img/precio_medio_por_alojamiento_cop.png', width=1300)
st.image('./new_york/img/precio_medio_por_alojamiento_ny.png', width=1300)
st.image('./seattle/img/precio_medio_por_alojamiento_seattle.png', width=1200)
st.markdown(" ### Media del precio por tipo de alojamiento:")
st.markdown(" ### New York:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "216,92€")
col2.metric("Habitaciones privadas", "103,08€")
col3.metric("Habitaciones compartidas", "145,20")
col4.metric("Habitaciones en hotel", "295,74€")
st.markdown(" ### Copenhague:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "1.182,76€")
col2.metric("Habitaciones privadas", "758,85€")
col3.metric("Habitaciones compartidas", "549,10€")
col4.metric("Habitaciones en hotel", "959,07€")
st.markdown(" ### Seattle:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "174,75€")
col2.metric("Habitaciones privadas", "86,53€")
col3.metric("Habitaciones compartidas", "30,63€")
col4.metric("Habitaciones en hotel", "128,00€")
st.markdown(" ### Barcelona:")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Apartamentos enteros", "144,07€")
col2.metric("Habitaciones privadas", "84,82€")
col3.metric("Habitaciones compartidas", "57,93€")
col4.metric("Habitaciones en hotel", "163,09€")


######################################################################################################


# Outliers de los precios
st.markdown('>> ### Outliers de los precios.')
st.image('./barcelona/img/precio_boxplot_bcn.png',width=1300)
st.image('./copenhague/img/media_precio_boxplot_cop.png', width=1300)
st.image('./new_york/img/media_precio_boxplot_ny.png', width=1300)
st.image('./seattle/img/precio_boxplot_seattle.png', width=1200)

# st.markdown('>> ### Outliers de los precios por tipo de alojamiento en Airbnb.')
# st.image('./barcelona/img/outlier_precio_room_type.png',width=1300)
# st.image('./copenhagen/img/outlier_precio_room_type_cop.png', width=1300)
# st.image('./new_york/img/outlier_precio_room_type_ny.png', width=1300)
# st.image('./seattle/img/outlier_precio_room_type_seattle.png', width=1200)



######################################################################################################
# Analizando las reseñas
st.markdown('>> ### Analizando el número de reseñas por distrito.')
st.image('./barcelona/img/numreseñas_distrito_bcn.png',width=1300)
st.image('./copenhague/img/numreseñas_distrito_cop.png', width=1300)
st.image('./new_york/img/reseñas_sum_distrito_ny.png', width=1200)
st.image('./seattle/img/numreseñas_distrito_seattle_sum.png', width=1200)
st.markdown(" ### El distrito con más reseñas tiene un total de:")
col1, col2, col3, col4 = st.columns(4)
col2.metric("Barcelona", "241.503", '2')
col4.metric("Copenhague", "49.644", '4')
col1.metric("New York", "391.103", '1')
col3.metric("Seattle", "71.943", '3')
st.markdown(" ### Las ciudades cuentan con un total de reseñas:")
col1, col2, col3, col4 = st.columns(4)
col2.metric("Barcelona", "600.737", '2')
col4.metric("Copenhague", "201.064", '4')
col1.metric("New York", "928.095", '1')
col3.metric("Seattle", "306.868", '3')














# st.set_page_config(layout='wide')

# # foto de los mapas con las ciudades
# with open("./barcelona/img/Mapa_geojson_bcn_distritos_tierra.htlm", "r") as f:
#     text = f.read()
    


st.markdown("> ## Conclusión: Mi hipótesis finalmente ha sido *nula*, puesto que la ciudad de Copenhagen \
es mucho más cara en cuanto a Airbnb se refiere, y de las que he analizado en este análisis. ")




st.markdown("##### ¡Muchas gracias! :sunglasses:")



import streamlit as st
from fpdf import FPDF
import base64

report_text = st.text_input("Report Text")


export_as_pdf = st.button("Export Report")

def create_download_link(val, app_EDA):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{app_EDA}.pdf">Download file</a>'

if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, report_text)
    
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    st.markdown(html, unsafe_allow_html=True)