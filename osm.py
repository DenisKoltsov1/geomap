
import pandas as pd
import folium
import  geopy
from geopy.geocoders import Nominatim
from ipyleaflet import AntPath, WidgetControl
from ipyleaflet import Map, Marker, Popup
from ipyleaflet import Map, ImageOverlay
from ipywidgets import IntSlider, jslink
from ipyleaflet import (
    Map, basemaps, basemap_to_tiles,
    Circle, Marker, Rectangle, LayerGroup
)

base_map= ''
def generateBaseMap(Startlocation, default_zoom_start,StartPoint,geolocator):
    base_map = folium.Map(location=[Startlocation[0],Startlocation[1]], control_scale=True, zoom_start=default_zoom_start)
    Startlocation = geolocator.geocode(StartPoint)
    folium.Marker(location=[Startlocation.latitude,Startlocation.longitude],tooltip='Азаматово').add_to(base_map)
    base_map.save("map.html")
    return base_map

#Terrain = input("Введите город :")
NamePoint ={ 'Азаматово': [56.19086928652996, 52.62623364317579],
            'Медведка':[56.18628418696123, 52.66811901725518] }



marathon_path = AntPath(
    locations=[
        [56.19070193097982, 52.62467892081803], [56.190442918459574, 52.62361217774634], [56.189957265271495, 52.62365096840349],
        [56.18900752571756, 52.62345701511773], [56.188154898593915, 52.623301852489114], [56.187075596585274, 52.623088503874776],
        [56.186560943746706, 52.62315799717405], [56.186560943746706, 52.62315799717405], [56.18547147584242, 52.62567310849855],
        [56.18482411943403, 52.630115539502725], [56.184316600991565, 52.633559495919684], [56.18309202896541, 52.641539483550595], 
        [56.18620274063837, 52.64563549341678], [56.186787850184615, 52.646622546289564], [56.18567243844135, 52.64997972682077], 
        [56.18456022058328, 52.65219145916522], [56.18447124176217, 52.65251122769695], [56.18447124176217, 52.65251122769695], 
        [56.18200852074819, 52.65621248792867], [56.1816478402372, 52.65728370804196], [56.182102500971645, 52.660202327603656],[56.182102500971645, 52.660202327603656],[56.18381055470611, 52.663815878167576],[56.18488493665813, 52.666389914185714],
        [56.18606947676946, 52.668221439814005]
    ],
    dash_array=[1, 10],
    delay=1000,
    color='#9500ff',
    pulse_color='#9500ff'
    )

StartPoint = input("Введите начальную точку поездки :")




if NamePoint.get(StartPoint) !=  'default':
   print(NamePoint.get(StartPoint))
   Startlocation =NamePoint.get(StartPoint)
    
else: 
    geolocator = Nominatim(user_agent="dublin87@mail.ru")
    Startlocation = geolocator.geocode(StartPoint)

EndPoint = input("Введите конечную  точку поездки :")

if NamePoint.get(EndPoint) !=  'default':
   print(NamePoint.get(EndPoint))
   Endlocation =NamePoint.get(EndPoint)
    
else: 
    geolocator = Nominatim(user_agent="dublin87@mail.ru")
    Endlocation = geolocator.geocode(EndPoint)


print(Startlocation[0])
print(Startlocation[1])
print(Startlocation)
#generateBaseMap(Startlocation, default_zoom_start=12, StartPoint=StartPoint, geolocator=geolocator)
#base_map= folium.Map(location=[Startlocation[0],Startlocation[1]], control_scale=True, zoom_start=13)
m = Map(center=(Startlocation[0], Startlocation[1]), zoom=18)
m.add_layer(marathon_path)
start_marker = Marker(location=(Startlocation[0], Startlocation[1]))
m.add_layer(start_marker)

finish_marker = Marker(location=(Endlocation[0], Endlocation[1]))
m.add_layer(finish_marker)
'''
start = ''
finish = ''
start.value = "Азаматово"                                                                      
finish.value = "Медведка"                                                                      
start_marker.popup = start
finish_marker.popup = finish
'''
marker = Marker(location=(50, 354))
circle = Circle(location=(50, 370), radius=50000, color="yellow", fill_color="yellow")
rectangle = Rectangle(bounds=((54, 354), (55, 360)), color="orange", fill_color="orange")
layer_group = LayerGroup(layers=(marker, circle))
m.add_layer(layer_group)
layer_group.add_layer(rectangle)

car =open('c:\\geomap\\car.jpg')

#картинка автомобиля
image = ImageOverlay(
    url="c://geomap//car1.png",
    # url='../06Q1fSz.png',
    bounds=((Startlocation[0], Startlocation[1]))
)


m.add_layer(image)
zoom_slider = IntSlider(description='Масштаб:', min=3, max=13, value=16)
jslink((zoom_slider, 'value'), (m, 'zoom'))
widget_control1 = WidgetControl(widget=zoom_slider, position='topright')
m.add_control(widget_control1)

m.save('map.html')


#folium.Marker(location=[Startlocation[0],Startlocation[1]],tooltip='Азаматово').add_to(base_map)
#folium.Marker(location=[Endlocation[0],Endlocation[1]],tooltip='Медведка').add_to(base_map)
#base_map.add_layer(marathon_path)
#base_map.save("map.html")
'''
#Startlocation = [56.18590207060007, 52.66829067862436]
EndPoint = input("Введите конечную  точку поездки :")
geolocator = Nominatim(user_agent="dublin87@mail.ru")
TerrainLocation =geolocator.geocode(Terrain)
default_zoom_start =12
Startlocation = geolocator.geocode(StartPoint)
Endlocation = geolocator.geocode(EndPoint)
print(Startlocation.address)
print(Endlocation.address)
print(Startlocation.latitude,Startlocation.longitude)
#print(Endlocation.latitude,Endlocation.longitude)
#Функция для генерации объекта базовой карты


popup1 = str(StartPoint)
generateBaseMap(default_location=[TerrainLocation.latitude,TerrainLocation.longitude], default_zoom_start=12, StartPoint=StartPoint, geolocator=geolocator)
base_map = base_map
path = 'c:\\geomap\\map.html'
f = open(path)



#One_Point_Marker(base_map,default_location=[Startlocation.latitude,Startlocation.longitude])


#56.18590207060007, 52.66829067862436
#56.19086928652996, 52.62623364317579
'''