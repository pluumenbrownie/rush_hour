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
De benodigde input om de volgende resultaten van het random algoritme krijgen.

```
python3 main.py 6 gameboards/Rushhour6x6_1.csv random histogram
```
![exp_6x6_1_random_graph_moves.png](https://github.com/pluumenbrownie/rush_hour/blob/main/results/exp_6x6_1_random_graph_moves.png)



