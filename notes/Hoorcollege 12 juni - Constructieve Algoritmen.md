Hele decision tree bouwen
# Breadth first
gebruik queue
voeg nodes van laag toe aan queue, lees node uit queue, voeg children van node toe aan queue, herhaal. 
Geeft keuzeboom laag voor laag.
Kan ook met "generaties"
Beter voor oplossing met minimale hoeveelheid stappen (COP)

# Depth first
gebruik stack
Geeft eerst lagere nodes voor naar parallelle node te gaan.
Kan recursief
Snelle manier om een oplossing te vinden (CSP)

Breadth first gebruikt veel geheugen ($2^N$). Depth first per laag doen kan breadth first simuleren, maar herhaalt veel werk.
![blue berries](https://images.unsplash.com/photo-1568477070800-66719cd52be2?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wzNjAwOTd8MHwxfHNlYXJjaHwxM3x8cHJ1bmV8ZW58MHwwfHx8MTY4NjU4MDIxM3ww&ixlib=rb-4.0.3&q=80&w=1080)
*Photo by [Waldemar](https://unsplash.com/@waldemarbrandt67w?utm_source=Obsidian%20Image%20Inserter%20Plugin&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=Obsidian%20Image%20Inserter%20Plugin&utm_medium=referral)*

# Optimaal prunen
bijknippen
Takken wegknippen waarin het optimale antwoord zeker weten niet zit.
Door snel te checken of een pad nutteloos is, kan de grootte van de hoeveelheid te controleren states beperkt worden.
Archief: sla states op die al bezocht zijn. Bijv. in een set/dict
Branch and bound: Zoek Depth first, maar niet dieper dan het kortste al gevonden pad.
Dijkstra Kortste Pad Algoritme: Voor kortste pad in een graaf met verschillende kosten. Garantie kortste pad bij alleen positieve kosten.
A*: Optimalisatie Dijkstra. Maak schatting van de kosten van het nog af te leggen pad. Moet admissable zijn (geen overschattingen).
Domein specifiek prunen: bewijs snel of een situatie ubh een oplossing heeft.

# Niet-optimaal prunen
Soms moet je offers maken.
Breadth first met Beam search: zoek alleen verder met de beste N takken in de keuzeboom. Lost ook geheugenprobleem op. $N=1$ is greedy algoritme.
Greedy met look-ahead: probeer keuzes die naar doorlopende einden lopen te vermijden. Kijk N stappen vooruit om een pad te kiezen. op $N=\infty$ is dit depth first.
Slimme heuristieken kunnen veel tijd besparen.

