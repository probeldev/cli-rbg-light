import sys
from yeelight import Bulb
from time import sleep


class LightGroup:
    def __init__(self, sstr):
        self.devices = []
        if sys.argv[1] == "strip":
            self.devices.append(Bulb("192.168.0.117", auto_on=True))
        elif sys.argv[1] == "mainroom":
            self.devices.append(Bulb("192.168.0.160", auto_on=True))
            self.devices.append(Bulb("192.168.0.144", auto_on=True))
        elif sys.argv[1] == "all":
            self.devices.append(Bulb("192.168.0.117", auto_on=True))
            self.devices.append(Bulb("192.168.0.160", auto_on=True))
            self.devices.append(Bulb("192.168.0.144", auto_on=True))
        else:
            print("Устройство не найдено")
            exit(0)

    def device_on(self):
        for bulb in self.devices:
            bulb.turn_on(effect="smooth")

    def device_off(self):
        for bulb in self.devices:
            bulb.turn_off()

    def device_color(self, r, g, b):
        for bulb in self.devices:
            bulb.set_rgb(int(r), int(g), int(b))

    def device_brig(self, br):
        for bulb in self.devices:
            bulb.set_brightness(int(br))

    def device_temp(self, temp):
        for bulb in self.devices:
            bulb.set_color_temp(int(temp))

    def device_favorite(self, fav):
        for bulb in self.devices:

            if fav == "blue":
                self.device_color(0, 0, 255)
                self.device_brig(100)

            if fav == "red":
                self.device_color(255, 0, 0)
                self.device_brig(50)

            if fav == "green":
                self.device_color(0, 255, 0)
                self.device_brig(10)

            if fav == "home":
                self.device_brig(50)
                self.device_temp(4000)



lg = LightGroup(sys.argv[1])

if sys.argv[2] == "on":
    lg.device_on()
elif sys.argv[2] == "off":
    lg.device_off()
elif sys.argv[2] == "color":
    if len(sys.argv) == 6:
        lg.device_color(sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("Неверное количество аргументов")
elif  sys.argv[2] == "brig":
    if len(sys.argv) == 4:
        lg.device_brig(sys.argv[3])
    else:
        print("Неверное количество аргументов")
elif sys.argv[2] == "temp":
    if len(sys.argv) == 4:
        lg.device_temp(sys.argv[3])
    else:
        print("Неверное количество аргументов")
elif sys.argv[2] == "favorite":
    if len(sys.argv) == 4:
        lg.device_favorite(sys.argv[3])
    else:
        print("Неверное количество аргументов")
else:
    print("Не вереный аргумент")