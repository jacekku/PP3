def quarter(x,y):
    translation=["pierwszej","drugiej","trzeciej","czwartej"]
    tab=[[True,True],[False,True],[False,False],[True,False]]
    qrt=translation[tab.index([x>0,y>0])]
    print(f'Punkt P({x},{y}) znajduje sie w {qrt} cwiartce ukladu wspolrzednych')


quarter(1,1)
quarter(-1,-1)
quarter(-1,1)
quarter(1,-1)