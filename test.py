def kaarten():
    normaalKaarten = 19
    kleurPestKaarten = 3
    kaartNumber = -1
    tellerPestKaarten = 0
    for x in range(int(normaalKaarten)):
        kaartNumber += 1
        blauw.append(f"{colors[0]} {kaartNumber}")
        blauwNum.append(kaartNumber)
        if len(blauw) == 10:
            kaartNumber = 9
        groen.append(f"{colors[1]} {kaartNumber}")
        groenNum.append(kaartNumber)
        if len(groen) == 10:
            kaartNumber = 9
        rood.append(f"{colors[2]} {kaartNumber}")
        roodNum.append(kaartNumber)
        if len(rood) == 10:
            kaartNumber = 9
        geel.append(f"{colors[3]} {kaartNumber}")
        roodNum.append(kaartNumber)
        if len(geel) == 10:
            kaartNumber = 0
    for y in range(int(kleurPestKaarten)):
        blauw.append(f"{colors[0]} {pestkaart[tellerPestKaarten]}")
        groen.append(f"{colors[1]} {pestkaart[tellerPestKaarten]}")
        rood.append(f"{colors[2]} {pestkaart[tellerPestKaarten]}")
        geel.append(f"{colors[3]} {pestkaart[tellerPestKaarten]}")
        blauw.append(f"{colors[0]} {pestkaart[tellerPestKaarten]}")
        groen.append(f"{colors[1]} {pestkaart[tellerPestKaarten]}")
        rood.append(f"{colors[2]} {pestkaart[tellerPestKaarten]}")
        geel.append(f"{colors[3]} {pestkaart[tellerPestKaarten]}")
        tellerPestKaarten += 1
    uno_deck.append(blauw)
    uno_deck.append(groen)
    uno_deck.append(rood)
    uno_deck.append(geel)
    print(blauw)
    print(groen)
    print(rood)
    print(geel)
    print(uno_deck)