# Welkom bij de experimentenfolder van Rushhour!

## Usage 
Standaard input om met de algoritmen te experimenteren:

Let op! In de main.py moet het board overeenkomen met de gameboardfile, anders werkt het niet. 

```
python3 code/main.py [gameboardsize] gameboards/[gameboardfile] [algorithm] histogram 
```
Voor gameboardsize kan er worden gekozen om een 6, 9 of 12 aan te geven. 
In de map gameboards staan vervolgens een aantal gameboardfiles, deze staan van makkelijk naar moeilijk. Voor [gameboardfile] kan je de file kiezen door de naam van het bestand in te vullen. Om het vervolgens te runnen met het experiment moet je histogram als arg[4] geven.

## Experiments
### Random
De benodigde input om de volgende resultaten van het random algoritme krijgen. Let hierbij erop dat in de main.py board = "6x6_1". Verder staat de binsize in histogram.py op 100.  

In de grafiek is besloten om alle runs die meer dan 50000 moves nodig hadden om het bord op te lossen niet mee te nemen. Dit zijn de zogenoemde outliers. De staart van de grafiek wordt zo minder lang en het gedeelte waar de meeste oplossingen worden gevonden wordt zo ook beter zichtbaar. De outliers zijn verder wel meegenomen in het gemiddelde. 

In dit experiment heeft het random algoritme een uur gedraaid. Het aantal runs staat gelijk aan het aantal oplossingen wat het random algoritme heeft gevonden in dit uur.   

Het random algoritme probeert door middel van het kiezen van een random voertuig en een random directie tot een oplossing te komen. 

```
python3 main.py 6 gameboards/Rushhour6x6_1.csv random histogram
```
![exp_6x6_1_random_graph_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_6x6_1_random_graph_moves.png)

### Random optimized
Om deze output te krijgen is de benodigde input van het random_optimized algoritme nodig. Let hierbij erop dat in de main.py board = "6x6_1". Verder staat de binsize in histogram.py op 30. Deze beslissing is gemaakt doordat de grafiek anders vertekend werd doordat de meeste oplossingen een eigen bin hadden en sommige 2 bins.   

In dit experiment heeft het random_optimized algoritme een uur gedraaid. Het aantal runs staat gelijk aan het aantal oplossingen wat het random algoritme heeft gevonden in dit uur.  

Het random_optimized algoritme voert als eerst het random algoritme uit. Vervolgens verwijderd het alle states waarin het al eerder is geweest.  

```
python3 main.py 6 gameboards/Rushhour6x6_1.csv random_optimized histogram
```
![exp_6x6_1_random_graph_optimized_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_6x6_1_random_graph_optimized_moves.png)

### Greedy
De benodigde input om de volgende resultaten van het random algoritme krijgen. Let hierbij erop dat in de main.py board = "6x6_1". Verder staat de binsize in histogram.py op 100.  

In de grafiek is besloten om alle runs die meer dan 50000 moves nodig hadden om het bord op te lossen niet mee te nemen. Dit zijn de zogenoemde outliers. De staart van de grafiek wordt zo minder lang en het gedeelte waar de meeste oplossingen worden gevonden wordt zo ook beter zichtbaar. De outliers zijn verder wel meegenomen in het gemiddelde.  

In dit experiment heeft het random algoritme een uur gedraaid. Het aantal runs staat gelijk aan het aantal oplossingen wat het random algoritme heeft gevonden in dit uur.   

Het greedy algoritme probeert door middel van twee heuristieken tot een oplossing te komen. Eerst kijkt het of de rode auto kan bewegen, vervolgens kijkt het of de auto die voor de rode auto staat kan bewegen en daarna kiest het een random voertuig. Zo probeert het algoritme sneller tot een oplossing te komen dan het random algoritme. 

```
python3 main.py 6 gameboards/Rushhour6x6_1.csv greedy histogram
```
![exp_6x6_1_greedy_graph_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_6x6_1_greedy_graph_moves.png)
