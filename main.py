import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("Atualmente existem " + str(result["number"]) + " astronautas na ISS: \n\n")
people = result["people"]

#Escrever no arquivo o nome das pessoas a bordo da ISS
for p in people:
    file.write(p['name'] + " - a bordo" + "\n")
    
#printar longitude e latitude
g = geocoder.ip('me')
file.write("\n Suas coordenadas são: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

#configurar o mapa no mudulo turtle
screen = turtle.Screen()
screen.setup(1200,600)
screen.setworldcoordinates(-180, -90 , 180, 90)

#carregar a imagem do mapa
screen.bgpic("img/map.gif")
screen.register_shape("img/ISS.gif")
iss = turtle.Turtle()
iss.shape("img/ISS.gif")
iss.setheading(45)
iss.penup()

while True:
    #carregar os status da ISS em tempo real
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    #Localizar a ISS
    location = result["iss_position"]
    lat = location['latitude']
    long = location['longitude']
    
    #Resposta da longitude e latitude
    lat = float(lat)
    long = float(long)
    print("latitude: " + str(lat))
    print("longitude: " + str(long))
    
    #Atualizar a posição da ISS no mapa
    iss.goto(long, lat)
    
    #Delay de atualização
    time.sleep(10)