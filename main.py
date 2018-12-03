# See https://docs.pycom.io for more information regarding library specifics
print("test")
from pysense import Pysense
# seule la librairie pour la température est importée pour ce modèle
from SI7006A20 import SI7006A20

from wifi import WiFi
from mqtt import MQTTClient
import time

IBMorgID='cnqzlg' # Identifiant de l'instance 'IoT PLatform' sur 6 caractères
deviceType='PyCom' # Nom du 'Device Type' défini dans le IoT Platform
deviceID='device-1' # ID du device (4 dernieres caractères du SSID)
deviceToken='rp0bTVq!-o4@vVlMWs' # Token (mot de passe) défini pour le device dans le Iot Platform

#IBMorgID='514y4j' # Identifiant de l'instance 'IoT PLatform' sur 6 caractères
#deviceType='PyCom' # Nom du 'Device Type' défini dans le IoT Platform
#deviceID='sdbd' # ID du device (4 dernieres caractères du SSID)
#deviceToken='gVVxAcc!tzALKKGHjn'


py = Pysense()
si = SI7006A20(py)

print("wifi before")
wifi = WiFi()
#print (WiFi.connectwifi('d-01','123456789'))
#print (WiFi.connectwifi('E-01','11111111'))
#print (WiFi.connectwifi('Gustavo','LMDTBM74'))
print (WiFi.connectwifi('floki_io','F10kiN37w0rk!'))
print("wifi done")
client = MQTTClient("d:"+IBMorgID+":"+deviceType+":"+deviceID, IBMorgID +".messaging.internetofthings.ibmcloud.com", user="use-token-auth", password=deviceToken, port=1883)

# Syntaxe pour envoyer un paquet MQTT à IBM Cloud

try:
    client.connect()
    while True:
        print("-------------------------")
        print("Sending")
        print("Temperature: " + str(si.temperature())+ " deg C")
        print("Relative Humidity: " + str(si.humidity()) + " %RH")
        print("Dew point: "+ str(si.dew_point()) + " deg C")
        mqttMsg = '{'
        mqttMsg = mqttMsg + '"t":' + str(si.temperature()) + ','
        mqttMsg = mqttMsg + '"h":' + str(si.humidity())
        mqttMsg = mqttMsg + '}'
        print(mqttMsg)
        client.publish(topic="iot-2/evt/data/fmt/json", msg=mqttMsg)
        time.sleep(1)
except Exception as e:
    print(e.args)
