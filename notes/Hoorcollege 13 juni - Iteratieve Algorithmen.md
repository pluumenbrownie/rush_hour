Herhalend: Kier random start state, doe een kleine aanpassing, doe de aanpassing terug als de nieuwe state slechter is.
# Hill climber
Hill climber/Gradient ascent: niet verzekert van absoluut maximum. Soms maximaliseren, soms minimaliseren.
	Convergentie: soms loop het algoritme vast op een punt. 

Restart hill climber: Stop nadat er N keer niets verbetert. Begin steeds opnieuw.

Constraint relaxation: Geldige start state kan moeilijk zijn. Schendingen van case zijn duur i.p.v. onmogelijk.

Steepest ascent hill climber: Kies de beste van alle mogelijke stappen ipv random. Als geen verbeterende stappen: Gegarandeerd (lokaal) minimum.

# Simulated Annealing
Voor functie met veel kleine lokale minima. 
"Schud" je lokale oplossing. Schud steeds minder hard, zodat de oplossing in het absoluut minimum terecht komt.
Bij het minimaliseren: acceptatiekans = $2^{(\text{score\_old}-\text{score\_new})}$. Kleine kans om nieuwe oplossing te accepteren bij hogere score.
Met "temperatuur": $$2^{\frac{(\text{score\_old}-\text{score\_new})}{\text{temperature}}}$$Temperatuur neemt af voor N iteraties via een functie.

# Population based
Maak X hill climbers. Deze krijgen kinderen, selecteer de beste X. 
Plant propagation: Planten planten voort door uitlopers. Uitlopers kort als condities lokaal goed zijn. Langer als conditie slechter is. Algoritme loopt zo sneller weg van suboptimale oplossingen.
Genetic Algorithm: Hill climbers hebben "genetisch materiaal". Kinderen hebben mix van twee ouders, met kleine variatie. 