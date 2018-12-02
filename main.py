# See https://docs.pycom.io for more information regarding library specifics

from pysense import Pysense
# seule la librairie pour la température est importée pour ce modèle
from SI7006A20 import SI7006A20

from wifi import WiFi
from mqtt import MQTTClient
import time

IBMorgID='czxe2n' # Identifiant de l'instance 'IoT PLatform' sur 6 caractères
deviceType='Captor' # Nom du 'Device Type' défini dans le IoT Platform
deviceID='device1' # ID du device (4 dernieres caractères du SSID)
deviceToken='ag4qH!nBvOgF&i(b2?' # Token (mot de passe) défini pour le device dans le Iot Platform


py = Pysense()
si = SI7006A20(py)

wifi = WiFi()

print("Temperature: " + str(si.temperature())+ " deg C and Relative Humidity: " + str(si.humidity()) + " %RH")
print("Dew point: "+ str(si.dew_point()) + " deg C")

#print (WiFi.connectwifi('SSID','pwd'))

# Syntaxe pour envoyer un paquet MQTT à IBM Cloud
client = MQTTClient("d:"+IBMorgID+":"+deviceType+":"+deviceID, IBMorgID +".messaging.internetofthings.ibmcloud.com", user="use-token-auth", password=deviceToken, port=1883)
client.connect();
while True:
    print("Sending")
    mqttMsg = '{'
    mqttMsg = mqttMsg + '"t":' + str(si.temperature())
    mqttMsg = mqttMsg + '}'
    print(mqttMsg)
    client.publish(topic="iot-2/evt/data/fmt/json", msg=mqttMsg)
    time.sleep(1)
