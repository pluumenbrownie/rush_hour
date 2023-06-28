# Rush hour
Rush hour is een spelletje dat bestaat uit een bord van 6x6. Op het bord zijn verschillende voertuigen geplaatst, waaronder een rode auto. Het doel van het spelletje is om de rode auto naar de uitgang te 'schuiven'.  Er staan echter voertuigen in de weg. De voertuigen zijn allemaal twee of drie vakjes groot (auto's en vrachtwagens) en ze hebben een bepaalde oriëntatie die niet aangepast kan worden: de voertuigen staan verticaal op het bord of horizontaal. Als een voertuig horizontaal op het bord staat, kan het alleen naar links of naar rechts schuiven. Een voertuig dat verticaal op het bord staat, kan alleen naar boven of beneden. En heel belangrijk: voertuigen kunnen niet botsen (oftewel op hetzelfde vakje staan). De uitdaging van het spel is om het rode autootje in zo min mogelijk moves naar de uitgang te krijgen. 

### Vereisten 
De code is geschreven met behulp van python 3.11. In requirements staat de packages die je nodig hebt om de code succesvol te kunnen laten runnen. Dit is de instructie daarvoor: 
```
pip install -r requirements.txt
```
### Gebruik 
Het programma kan worden aangeroepen door main.py aan te roepen. In de command line moet je de volgende argumenten meegeven: boardfile en het algoritme dat je wil uitvoeren. Als je het random algoritme wil uitvoeren, gebruik je deze regel: 
```
python3 code/main.py gameboards/Rushhour12x12_7.csv random
```

### Structuur
In de lijst hieronder staat beschreven waar de belangrijkste bestanden en mappen te vinden zijn: 
* `/code`: bevat alle code van het project, waaronder main.py en pygame_rushhour.py. De laatste is voor de visualisatie. 
  * `/code/algorithms`: bevat de algoritmen. 
  * `/code/classes`: bevat de verschillende classes die we voor dit project hebben aangemaakt, zoals models.py (classes RushHour en Board), vehicle.py (classes Vehicle, Car en Truck) en graphs.py (classes Node en Graph). 
  * `/code/experiments`: hierin staan de bestanden die nodig zijn voor de experimenten. Dit gaat om experimenten voor de beam search, breadth first, depth first, random en random optimized. 
  * `/code/visualisation`: bevat bestanden die nodig zijn voor het visualiseren, zoals een bestand met kleuren die gebruikt wordt voor pygame. Ook de code voor de histogrammen staan hier. 
* `/gameboards`: hier staan alle bestanden van de spelborden. 
* `/graphs`: hier staan de grafieken en histogrammen die we hebben gemaakt. 
* `/images`: als we ergens in de README een afbeelding gebruiken, komt deze hier te staan. 
* `/results`: hier staan csv bestanden met uitkomsten gegenereerd door onze algoritmes. 
  * `/results/best_solutions`: hier staan csv files met exacte moves en door welk voertuig deze is gedaan om tot de beste oplossing te komen
* `/requirements.txt`: in dit bestand staan alles wat je moet installeren om te zorgen dat onze code werkt. 


### Auteurs
* Amber van der Eijden
* Wessel Beumer
* Dionne Spaltman
