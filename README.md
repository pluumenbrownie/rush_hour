# Rush hour
Rush hour is een relatief eenvoudig spelletje met als doel de rode auto uit de 'file' te krijgen. Op het bord staan echter verschillende auto's, die allemaal slechts in twee richtingen kunnen bewegen. Als een auto horizontaal staat, kan de auto naar links of rechts bewegen. Als een auto verticaal staat, kan de auto naar boven en onder. 

### Vereisten 
De code is geschreven met behulp van python 3.11. In requirements staat de packages die je nodig hebt om de code succesvol te kunnen laten runnen. Dit is de instructie daarvoor: 

`pip install -r requirements.txt`

### Gebruik 
Het programma kan worden aangeroepen door main.py aan te roepen. In de command line moet je de volgende argumenten meegeven: boardsize (bijvoorbeeld 6), boardfile en het algoritme dat je wil uitvoeren. Als je het random algoritme wil uitvoeren, gebruik je deze regel: 

`python3 code/main.py 12 gameboards/Rushhour12x12_7.csv random` 

### Structuur
In de lijst hieronder staat beschreven waar de belangrijkste bestanden en mappen te vinden zijn: 
* `/code`: bevat alle code van het project, waaronder main.py en pygame_rushhour.py. De laatste is voor de visualisatie. 
  * `/code/algorithms`: bevat de algoritmen
  * `/code/classes`: bevat de verschillende classes die we voor dit project hebben aangemaakt, zoals models.py (classes RushHour en Board), vehicle.py (classes Vehicle, Car en Truck) en graphs.py (classes Node en Graph). 
  * `/code/experiments`: hierin staan de bestanden die nodig zijn voor de experimenten. Dit gaat om experimenten voor de beam search, breadth first, depth first, random en random optimized. 
  * `/code/visualisation`: bevat bestanden die nodig zijn voor het visualiseren, zoals een bestand met kleuren die gebruikt wordt voor pygame. Ook de code voor de histogrammen staan hier. 
* `/gameboards`: hier staan alle bestanden van de spelborden
* `/images`: als we ergens in de README een afbeelding gebruiken, komt deze hier te staan
* `/results`: hier staan csv bestanden met uitkomsten gegenereerd door onze algoritmes. 

### Auteurs
* Amber van der Eijden
* Wessel Beumer
* Dionne Spaltman
