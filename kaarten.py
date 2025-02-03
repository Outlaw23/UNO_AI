#---class-kaarten---
class Kaarten:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    def __str__(self):
        return f"{self.color} {self.number}"
#---class-kaarten---

#---class-pest-kaarten-kleur---
class PestKaartenColor:
    def __init__(self, colorPest, text, waarde):
        self.colorPest = colorPest
        self.text = text
        self.waarde = waarde
    def __str__(self):
        return f"{self.colorPest} {self.text}"
#---class-pest-kaarten-kleur---

#---class-pest-kaarten-zwart---
class KaartenPestZwart:
    def __init__(self,colorZwart ,text, waarde):
        self.colorZwart = colorZwart
        self.text = text
        self.waarde = waarde
    def __str__(self):
        return f"{self.colorZwart} {self.text}"
#---class-pest-kaarten-zwart---

# ---variabele---
colorZwart = "zwart"
colors = ["blauw", "groen", "rood", "geel"]
pestKaarten = ["pak 2 kaarten", "klok draait", "beurt overslaan"]
pestKaartenZwartList = ["pak 4 kaarten", "kleur kiezen"]
numbers = -1
numberColor = -1
num = -1
legenList = []
normalenKaartenNum = 20
pestKaartenNum = 6
unoDeck = []
# ---variabele---

# ---loop-voor-normaal-kaarten---
for color in colors:
    numberColor += 1
    numbers = -1
    for i in range(normalenKaartenNum):
        numbers += 1
        kaarten = Kaarten(colors[numberColor], numbers)
        legenList.append(kaarten)
        unoDeck.append(kaarten)
        if len(legenList) == 10:
            numbers = -1
            legenList = []
# ---loop-voor-normaal-kaarten---

# ---loop-voor-pestkaarten---
numberColor = -1
legenList = []
for color in colors:
    numberColor += 1
    numbers = -1
    for x in range(pestKaartenNum):
        numbers += 1
        pestKaart = PestKaartenColor(colors[numberColor], pestKaarten[numbers], 0)
        legenList.append(pestKaart)
        unoDeck.append(pestKaart)
        if len(legenList) == 3:
            numbers = -1
            legenList = []
# ---loop-voor-pestkaarten---

# ---loop-voor-pestkaartenZwart---
numberColor = 8
legenList = []
numbers = -1
for q in range(numberColor):
    pestKaartenZwart = KaartenPestZwart(colorZwart, pestKaartenZwartList[numbers], 0)
    legenList.append(pestKaartenZwart)
    unoDeck.append(pestKaartenZwart)
    if len(legenList) == 4:
        numbers += 1
# ---loop-voor-pestkaartenZwart---


#---print-van-uno-deck---
for y in range(112):
    num += 1
    print(unoDeck[num])
#---print-van-uno-deck---
