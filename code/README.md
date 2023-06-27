# Uitleg over deze map code
In deze map staat de code voor de algoritmes, de classes en de experimenten. 

De algoritmes die we hebben geschreven: 
* Random: een willekeurige auto en een willekeurige richting wordt gekozen. Daarna wordt gekeken of dit een valide move is en het voertuig daadwerkelijk zo kan bewegen. Als het niet kan, gaan we terug de loop in. Dit gaat door totdat er de rode auto bij de uitgang is. 
* Random optimized: hierbij wordt random gerund. Vervolgens wordt een functie aangeroepen in models.py optimize solution die tussenstappen verwijderd. 
* Greedy: greedy bestaat uit drie mogelijke stappen en gaat door totdat hij bij een opgeloste staat is. Als eerste wordt er gekeken of de rode auto richting de uitgang kan bewegen. Als dat niet kan, dan wordt er gekeken welke auto de rode auto aan het blokkeren is. Als die niet kan worden verplaatst, wordt er een random voertuig en een random richting gekozen. 
* Depth-first search (DFS): bij de DFS wordt zo ver mogelijk gezocht in een 'branch' voordat verder wordt gekeken naar de volgende branch. Er wordt gebruik gemaakt van een stack. 
* Breadth-first search (BFS): bij de BFS worden alle staten geinspecteerd op het hoogste niveau voordat er een niveau lager wordt gekeken. De code is gebaseerd op die van DFS, maar maakt gebruik van een queue in plaats van een stack. 
* Beam search: er zijn meerdere versies van beam search online te vinden. Volgens het hoorcollege en wikipedia gebruikt BFS om de states te bezoeken. In plaats van alle states langs te gaan, wordt er (niet optimaal) gepruned. Bij de 'build children' functie wordt de queue gesorteerd op basis van een heuristiek. De beam size bepaalt vervolgens hoeveel daarvan worden bewaard. Als je een beam size van 1 hebt, is het in principe een greedy algoritme, omdat steeds de beste keuze wordt genomen volgens de heuristiek. Bij een te kleine beam search vindt het algoritme soms geen resultaat. 
* Branch and bound: hiervoor is depth first gekopieerd en aangepast. Archief dat depth first heeft gevbruikt, vervangen door en dicitonary. Hierin houdt hij aan in welke laag de kortste route naar de oplossing is gevonden. Het algoritme gaat niet verder dan het niveau met de best move count. 


