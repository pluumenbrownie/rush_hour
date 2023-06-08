# rush_hour - Freeway Frenzies

### Studenten: Amber van der Eijden, Wessel Beumer en Dionne Spaltman

### Versimpelende aannames
- Het bord is vierkant (bijvoorbeeld 6x6, 9x9, 12x12)
- Voertuigen kunnen niet wisselen van rij (dit heeft te maken met hun rijrichting) 
- Het aantal posities dat auto's op een bord kunnen hebben is de lengte van het bord min 1 (als er geen andere voertuigen zijn)
- Het aantal posities dat vrachtwagens op een bord kunnen hebben is de lengte van het bord min 2 (als er geen andere voertuigen zijn)

Aanvankelijk hadden we een formule waarin voertuigen op elkaar kunnen botsen, zowel op voertuigen in hun eigen rij als op voertuigen die dwars in hun rij staan. 
Uiteindelijk zijn we op een formule gekomen waarin we meenemen dat voertuigen niet op voertuigen in hun eigen rij kunnen botsen. We hebben (nog) niet meegenomen dat ze op voertuigen kunnen botsen die dwars staan. 

Om een idee te geven: bij onze eerste formule was de statespace bij game 1 (6x6) 976 562 000. Bij de nieuwe formule is de statespace
2 250 000. Dus we zijn van bijna een miljard naar iets meer dan 2 miljoen gegaan. 



