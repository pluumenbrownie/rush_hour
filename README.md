# Rush hour
Rush hour is een relatief eenvoudig spelletje met als doel de rode auto uit de 'file' te krijgen. Op het bord staan echter verschillende auto's, die allemaal slechts in twee richtingen kunnen bewegen. Als een auto horizontaal staat, kan de auto naar links of rechts bewegen. Als een auto verticaal staat, kan de auto naar boven en onder. 

# Vereisten 
De code is geschreven met behulp van python 3.11. In requirements staat de packages die je nodig hebt om de code succesvol te kunnen laten runnen. Dit is de instructie daarvoor: 
```
pip install -r requirements.txt
```
# Gebruik 
Het programma kan worden aangeroepen door main.py aan te roepen. In de command line moet je de volgende argumenten meegeven: boardfile en het algoritme dat je wil uitvoeren. Als je een algoritme wilt uitvoeren, gebruik je deze volgende format: 
```
python3 code/main.py gameboards/Rushhour12x12_7.csv [naam_algoritme] <opties>
```
Bij `[naam_algoritme]` kan de naam van het algoritme worden ingevult. Bijvoorbeeld: voor het random algoritme schrijf je:
```
python3 code/main.py gameboards/Rushhour12x12_7.csv random
```
Dit zijn de mogelijke algoritmes. Er hoeven geen opties meegegeven worden, tenzij anders vermeldt.
- random
- greedy
- random_optimized
- depthfirst
- breadthfirst
- branchandbound
- beamsearch
  - beamsearch heeft twee opties nodig:
  - de heuristiek: h1/h2/h3
  - de beam grootte: een getal.
- dijkstra

## Animate
Wanneer de eerste optie na een algoritme `animate` is, wordt het gegeven bord geopent in pygame. Hier kan de gevonden oplossing geanimeerd bekeken worden. De volgende algoritmes ondersteunen `animate`:
- random
- greedy
- random_optimized
- depthfirst
- breadthfirst
- branchandbound
- dijkstra

## Histogram
Wanneer de eerste optie na een algoritme `histogram` is, kunnen van bepaalde willekeurige algoritmes een histogram gemaakt worden. De algoritmes worden voor een uur gedraait, waarna er een histogram wordt gemaakt van de lengtes van de gevonden oplossingen. De volgende algoritmes ondersteunen `histogram`:
- random
- random_optimized
- greedy
- depthfirst

### Opnieuw plotten
Soms wil je van dezelfde data van een van de vorige experimenten opnieuw een plot maken, bijvoorbeeld na het veranderen van de opmaak van de plot. Hiervoor kunnen ook de volgende argumenten als `[naam_algoritme]` aangeroepen worden:
- randomplt
- greedyplt
- random_optimized_plt
- depthfirstplt

## Overige experimenten
Er kunnen ook vele andere experimenten uitgevoerd worden. Meer informatie is te vinden in de README in de experiments folder, maar dit zijn de overige opties:
- statespace
- depth_exp
- breadth_exp
- beam_exp
- mem_exp
- graph
- dijkstra_exp
- compare
- bfcompare
- play
  - Hiermee kun je in de terminal zelf het spel proberen op te lossen.

# Structuur
In de lijst hieronder staat beschreven waar de belangrijkste bestanden en mappen te vinden zijn: 
* `/code`: bevat alle code van het project, waaronder main.py en pygame_rushhour.py. De laatste is voor de visualisatie. 
  * `/code/algorithms`: bevat de algoritmen. 
  * `/code/classes`: bevat de verschillende classes die we voor dit project hebben aangemaakt, zoals models.py (classes RushHour en Board), vehicle.py (classes Vehicle, Car en Truck) en graphs.py (classes Node en Graph). 
  * `/code/experiments`: hierin staan de bestanden die nodig zijn voor de experimenten. Dit gaat om experimenten voor de beam search, breadth first, depth first, random en random optimized. 
  * `/code/visualisation`: bevat bestanden die nodig zijn voor het visualiseren, zoals een bestand met kleuren die gebruikt wordt voor pygame. Ook de code voor de histogrammen staan hier. 
* `/gameboards`: hier staan alle bestanden van de spelborden. 
* `/images`: als we ergens in de README een afbeelding gebruiken, komt deze hier te staan. 
* `/results`: hier staan csv bestanden met uitkomsten gegenereerd door onze algoritmes. 
  * `/results/best_solutions`: hier staan csv files met exacte moves en door welk voertuig deze is gedaan om tot de beste oplossing te komen

# Auteurs
* Amber van der Eijden
* Wessel Beumer
* Dionne Spaltman
