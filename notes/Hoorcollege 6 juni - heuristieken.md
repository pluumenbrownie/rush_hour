Optimalisatie. Linear programming
$$
S=6A+5B
$$
$A+B \le 5$
$3A+2B \ge 12$
$A \ge 0 \vee B \ge 0$
Vind optimale oplossing voor gegeven beperkingen.

## Free Optimization Problem
Bijvoorbeeld lineaire regressie. Geen inherente limieten van je oplossing
## Constraint Optimization Problem
Oplossing is beperkt: objecten in rugzak, kan niet meer zijn dan capaciteit. "Optimale" oplossing van CSP. 
## Constraint Satisfaction Problem
Bijvoorbeeld een sudoku, eenmaal ingevuld is een sudoku opgelost. Alleen eindresultaat is belangrijk. 

## Statespace
De verzameling van alle mogelijke configuraties van een probleem. Maar wat betekent dit? Hangt af van doel. 
Omzetten van 3 schakelaars:
Hoe kan ik alle schakelaars aanzetten? statespace = 6
Welke configuratie kunnen de schakelaar staan? statespace = 8
Hoeveelheid oplossingen neemt exponentieel toe. Slimmere aanpak kan veel tijd schelen.

Combinations and permutations  | Repetition allowed | forbidden
---:|:----:|:---:
Order important | $n ^{k}$| $\frac{n!}{(n-r)!}$
irrelevant |$\frac{(r+n-1)!}{r!(n-1)!}$|$\frac{n!}{r!(n-r)!}$

Voorbeeld: N-Queen puzzel. N schaak-koninginnen. Hoeveel passen op een bord zonder elkaar te kunnen slaan? 
voor 8x8: duurt 4.42 s
voor 20x20: $8\cdot 10^{20}$ jaar
Het probleem schaalt factoriaal.

# Algoritmes
Bubble sort: goed als lijst al ongeveer gesorteerd is, traag in slechtste geval. 
Sorteren is opgelost probleem, voor bijvoorbeeld sudoku's niet. Probleem is non-polynomiaal. 
Versnel je algoritme met heuristieken. 
Sudoku is moeilijk om op te lossen, makkelijk om te controlleren. 
Schaken: wat is de beste openingszet. Moeilijk op te lossen, moeilijk te controleren. 
Probeer alle mogelijkheden en kies de beste: Greedy algorithm.

# Moeilijkheid + Statespace
Puzzelstukjes met twee kleuren, kleuren moeten elkaar raken:
Alle kleuren uniek -> makkelijk
Weinig kleurencombinaties -> makkelijk
Daar tussenin -> moeilijk

De N-Queen puzzel: er staat altijd maar 1 koningin in iedere rij/kolom. Nu maar $8! = 40320$ keuzes.

Wat maakt een probleem moeilijk op te lossen? Goldy Locks zone van complexiteit.

# Vorm van de Statespace
Voor een convexe statespace is er een globaal minimum. Makkelijk op te lossen via gradient decent.

Niet convexe statespace: lokale minimum.
