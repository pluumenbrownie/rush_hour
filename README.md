# Rush hour
Rush hour is een spelletje dat bestaat uit een bord van 6x6. Op het bord zijn verschillende voertuigen geplaatst, waaronder een rode auto. Het doel van het spelletje is om de rode auto naar de uitgang te 'schuiven'.  Er staan echter voertuigen in de weg. De voertuigen zijn allemaal twee of drie vakjes groot (auto's en vrachtwagens) en ze hebben een bepaalde oriëntatie die niet aangepast kan worden: de voertuigen staan verticaal op het bord of horizontaal. Als een voertuig horizontaal op het bord staat, kan het alleen naar links of naar rechts schuiven. Een voertuig dat verticaal op het bord staat, kan alleen naar boven of beneden. En heel belangrijk: voertuigen kunnen niet botsen (oftewel op hetzelfde vakje staan). De uitdaging van het spel is om het rode autootje in zo min mogelijk moves naar de uitgang te krijgen. 

## Vereisten 
De code is geschreven met behulp van python 3.11. In requirements staat de packages die je nodig hebt om de code succesvol te kunnen laten runnen. Dit is de instructie daarvoor: 
```
pip install -r requirements.txt
```
## Gebruik 
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

## Structuur
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

## Statespace
Bij het nadenken over onze statespace hebben wij de beslissing genomen dat een state voor ons een versie is van het spelbord. 

Wij gaan daarnaast uit van de situatie dat je een leeg bord vult met voertuigen. Als je op die manier redeneert, is er geen sprake van repetition omdat je voertuigen niet twee keer op het bord kan zetten. Er is geen order, omdat het niet uitmaakt of je eerst het ene autootje plaatst en daarna de ander. Je zou ook kunnen rederenen vanuit moves: dan is er wel repetition omdat je vaker dan eens kan kiezen voor +1 of -1. Maar dit hebben wij dus niet gedaan. 

Er is geen repetition en geen order, dus komen we uit bij de volgende formule: n!/(r!*(n-r)!)

Onze aannames zijn dat het bord vierkant is, dat voertuigen niet kunnen wisselen van rij en dat we rekening houden met voertuigen in dezelfde rij/kolom (ze kunnen dus niet botsen). Wel is het nog mogelijk voor voertuigen om te botsen als ze niet in dezelfde kolom of rij zitten. Voertuigen in dezelfde rij kunnen elkaar niet 'inhalen'. 

Voor elke rij en kolom doen wij de eerdergenoemde formule en al die resultaten vermenigvuldigen we met elkaar om tot de uiteindelijke statespace te komen. 

### Voorbeeld berekening statespace 
Met een voorbeeld willen we laten zien dat de formule klopt. Bedenk een rij van een 6x6 bord met daarop twee auto's. De mogelijkheden die er dan bestaan zijn (V = voertuig, O = open vakje): VOOV, VOVO, VVOO, OVVO, OVOV, OOVV. Er zijn dus zes mogelijkheden van dit bord. 
In dit geval is het aantal keuzes dat je moet maken (r) gelijk aan het aantal voertuigen dat je op het bord moet plaatsen. Dat zijn er dus 2, omdat er twee auto's zijn. De keuzemogelijkheden is het aantal open vakjes plus het aantal voertuigen. Dat is dus 2 open vakjes plus 2 auto's = 4 keuzemogelijkheden. 
n!/(r!*(n-r)!)= 4!/(2!*(4-2)!)=4!/(2!*(2)!)=6

Als je een vrachtwagen hebt en een auto, ziet het er weer anders uit: VOV, VVO, OVV. Je hebt dan dus maar drie mogelijkheden. Het aantal keuzes dat je moet maken (r) is gelijk aan het aantal voertuigen, dus dat is 2. De keuzemogelijkheden is het aantal open vakjes plus het aantal voertuigen, dus 3. 
In de formule zou dat moeten zijn n!/(r!*(n-r)!)= 3!/(2!*(3-2)!) = 3.

Voor het grootste bord is de statespace 1.124.640.192.614.400. Je kan de statespace voor elk ander bord laten uitrekenen door het volgende aan te roepen: 

`python3 code/main.py gameboards/Rushhour12x12_7.csv statespace`

## Auteurs
* Amber van der Eijden
* Wessel Beumer
* Dionne Spaltman
