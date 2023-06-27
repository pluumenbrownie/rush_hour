# Welkom bij de experimentenfolder van Rushhour!

## Usage 
Standaard input om met de algoritmen te experimenteren:



```
python3 code/main.py [gameboardsize] gameboards/[gameboardfile] [algorithm] histogram 
```
Voor gameboardsize kan er worden gekozen om een 6, 9 of 12 aan te geven. 
In de map gameboards staan vervolgens een aantal gameboardfiles, deze staan van makkelijk naar moeilijk. Voor [gameboardfile] kan je de file kiezen door de naam van het bestand in te vullen. Om het vervolgens te runnen met het experiment moet je histogram als arg[4] geven.

## Experiments
*<b style="color:red"> ***Let op!***</b>*  
Voor de volgende figuren in random, random_optimized & greedy geldt het volgende:   
Voor Figuur 1 moet in main.py board = "6x6_1"   
Voor Figuur2 moet in main.py board = "9x9_4"   
Voor Figuur 3 moet in main.py board = "12x12_7"  

### Random
Het random algoritme probeert door middel van het kiezen van een random voertuig en een random directie tot een oplossing te komen.  

Hieronder zullen drie grafieken te zien zijn die de uitput van het random algoritme weergeven. De eerste grafiek laat het random algoritme zien op het 6x6_1 bord, de tweede op het 9x9_4 bord en het derde op het 12x12_7 bord. De volgende input is nodig om de volgende resultaten van het random algoritme te verkrijgen.  
In histogram.py staat de binsize bij elk figuur op 100.  
  

In grafiek 1 is besloten om alle runs die meer dan 50000 moves nodig hadden om het bord op te lossen niet mee te nemen. Dit zijn de zogenoemde outliers. De staart van de grafiek wordt zo minder lang en het gedeelte waar de meeste oplossingen worden gevonden wordt zo ook beter zichtbaar. De outliers zijn verder wel meegenomen in het gemiddelde.  
In grafiek 2 en 3 zijn alle runs meegenomen.    

Voor het experiment wat bij elk bord heeft plaatsgevonden heeft het random algoritme een uur gedraaid. Het aantal runs staat gelijk aan het aantal oplossingen wat het random algoritme heeft gevonden in dit uur.   

Input 6x6_1 bord:
```
python3 main.py 6 gameboards/Rushhour6x6_1.csv random histogram
```
![exp_6x6_1_random_graph_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_6x6_1_random_graph_moves.png)

Input 9x9_4 bord:
```
python3 main.py 9 gameboards/Rushhour9x9_4.csv random histogram
```
![exp_9x9_4_random_graph_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_9x9_4_random_graph_moves.png)  
Input 12x12_7 bord:
```
python3 main.py 12 gameboards/Rushhour12x12_7.csv random histogram
```  
![exp_12x12_7_random_graph_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_12x12_7_random_graph_moves.png)



### Random optimized
Om deze output te krijgen is de benodigde input van het random_optimized algoritme nodig. Let hierbij er weer op dat in de main.py de board variabele moet worden aangepast bij de bijbehorende boardfile. Verder staat de binsize in histogram.py op 30. Deze beslissing is gemaakt doordat de grafiek anders vertekend werd doordat de meeste oplossingen een eigen bin hadden en sommige 2 bins.   

In dit experiment heeft het random_optimized algoritme een uur gedraaid op de verschillende borden. Het aantal runs staat gelijk aan het aantal oplossingen wat het random algoritme heeft gevonden in dit uur.  

Het random_optimized algoritme voert als eerst het random algoritme uit. Vervolgens verwijderd het alle states waarin het al eerder is geweest.  

```
python3 main.py 6 gameboards/Rushhour6x6_1.csv random_optimized histogram
```
![exp_6x6_1_random_graph_optimized_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_6x6_1_random_graph_optimized_moves.png)  
Input 9x9_4 bord:
```
python3 main.py 9 gameboards/Rushhour9x9_4.csv random_optimized histogram
```
![exp_9x9_4_random_graph_optimized_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_9x9_4_random_graph_optimized_moves.png)  
Input 12x12_7 bord:
```
python3 main.py 12 gameboards/Rushhour12x12_7.csv random_optimized histogram
```  
![exp_12x12_7_random_graph_optimized_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_12x12_7_random_graph_optimized_moves.png)



### Greedy
Het greedy algoritme probeert door middel van twee heuristieken tot een oplossing te komen. Eerst kijkt het of de rode auto kan bewegen, vervolgens kijkt het of de auto die voor de rode auto staat kan bewegen en daarna kiest het een random voertuig. Zo probeert het algoritme sneller tot een oplossing te komen dan het random algoritme.  

Dit algoritme heeft op twee borden een uur gedraaid.
De benodigde input om de volgende resultaten van het random algoritme krijgen. Let hierbij erop dat in de main.py board = "6x6_1". Verder staat de binsize in histogram.py op 100.  

In de eerste grafiek is besloten om alle runs die meer dan 50000 moves nodig hadden om het bord op te lossen niet mee te nemen. Dit zijn de zogenoemde outliers. De staart van de grafiek wordt zo minder lang en het gedeelte waar de meeste oplossingen worden gevonden wordt zo ook beter zichtbaar. De outliers zijn verder wel meegenomen in het gemiddelde.  

In dit experiment heeft het greedy algoritme een uur gedraaid op beide borden. Het aantal runs staat weer gelijk aan het aantal oplossingen wat het random algoritme heeft gevonden in dit uur.   
 

```
python3 main.py 6 gameboards/Rushhour6x6_1.csv greedy histogram
```
![exp_6x6_1_greedy_graph_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_6x6_1_greedy_graph_moves.png)  
```
python3 main.py 9 gameboards/Rushhour9x9_4.csv greedy histogram
```
![exp_9x9_4_greedy_graph_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_9x9_4_greedy_graph_moves.png)


### Depthfirst
Het depthfirst algoritme kijkt gaat door middel van een stack alle mogelijke states van het bord af en probeert zo tot de beste oplossing te komen.  
Het is een deterministish algoritme en zal daardoor altijd op dezelfde oplossing komen. Voor het 6x6_1 bord komt het dan ook altijd uit op 115.  
Echter voor het experiment is gekeken of de oplossing verbeterd kan worden door de moves te shuffelen voordat deze bij de stack komen.  

Voor het experiment heeft het depthfirst algoritme een uur gedraaid om te kijken hoe het aantal moves zich verhouden tot de deterministiche oplossing.  

Input:
```
python3 main.py 6 gameboards/Rushhour6x6_1.csv depthfirst histogram
```

![exp_6x6_1_depth_first_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_6x6_1_depth_first_moves.png) 

### Breadthfirst
Net zoals bij een depthfirst gaat het breadthfirst algorite alle mogelijke staten van het bord af en geeft door middel van een queue gelijk de beste oplossing.  

In het volgende figuur is te zien wat dit breathfirst algoritme als beste oplossing geeft voor de eerste 5 borden geeft.  

Door een tekort aan geheugen is het niet gelukt om borden 9x9_6 & 12x12_7 op te lossen met breadthfirst.  

Input:
```
python3 main.py 6 gameboards/Rushhour6x6_1.csv bf_compare
```

![breadth_first_scores.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/breadth_first_scores.png) 

### Beam search 
Bij beam search hebben we een grid search gedaan. Hierbij kijken we naar de verschillende heuristieken (H1, H2, H3) en naar verschillende beam sizes. Wat interessant is, is om te kijken welke heuristiek het over het algemeen het beste doet.

Om een experiment te runnen voor beam search moet je het volgende command gebruiken: 
```
python3 main.py 6 gameboards/Rushhour6x6_1.csv beam_exp
```

In het mapje results/beam_search staan de resultaten in een csv bestand. Je ziet hier vier kolommen: de grootte van het bord dat je gebruikt, de heuristiek, de beam size en het aantal states dat nodig was om de beste oplossing te bereiken. 

Op de kleinste borden doet H2, die kijkt naar het aantal blokkerende voertuigen, de beste resultaten levert. Het is nog niet gelukt om het algoritme te runnen op de 9x9 borden en het 12x12 bord. 





