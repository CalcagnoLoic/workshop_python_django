# Introduction à Python 

## Interprété vs compilé? 

Python est un langage fonctionnant en 2 étapes grâce à un interpréteur: 

* lecture du fichier `.py` par l'interpréteur pour fournir un fichier binaire `.pyc`

* interprétation du fichier binaire en langage bas niveau 

## La syntaxe de Python 

Un des points central de Python est son système d'indentation. En effet, dans ce langage, l'indentation est primordiale car elle permet de faire comprendre à l'interpréteur les différents blocs de code ainsi que la dépendance de ces blocs.

Un autre élément est l'utilisation du `:` remplaçant le système de `{}` présent dans les autres langages de programmation. 

## Quelques principes de base pour utiliser Django 

#### Les objets de stockage

Il existe 4 types d'objet de stockage en python : 

* Les listes : ce sont des collections d'éléments ordonnés, modifiables et pouvant contenir plusieurs fois la même valeur ;

* Les tuples : ce sont des collections d'éléments ordonnés, immuables et pouvant contenir plusieurs fois la même valeur ;

* Les dictionnaires : ce sont des collections d'éléments non ordonnés indexés, modifiables et fonctionnant avec un système de clé:valeur. C'est l'équivalent des arrays associatifs en PHP) ;

* Les set : ce sont des collections d'éléments non ordonnés et non indexés, ne pouvant contenir deux fois la même valeur

Voici des  exemples d'objets de stockage :

````python
liste = ["Steph", False, 42]

tuple1 = ("Steph", False, 42)
tuple2 = ("Steph", False, 42, ("Steph", True, 19))

dict = {"nom" = "Steph", "age" = 19, "sport" = False}

set = {"Steph", 29, True}
````

### Les boucles conditionnelles

La philosophie des boucles reste similaire à ce que l'on connait déjà. Il y a néanmoins quelques petites différentes propre à la syntaxe Python. 

#### Les boucles if

````python
if(condition1):
    print("sortie")
elif(condition2):
    print("sortie")
else:
    print("sortie")
````

#### Les boucles for

````python
list = [1,2,3]
for(elem in list):
    print(elem)
````

#### Les boucles while

````python
x=0
while(x>5):
    x+=1
    print(x)
````

### Les fonctions

Pour écrire un  fonction en Python, il suffit de mettre le mot-clé `def` devant la fonction pour faire comprendre à l'interpréteur de notre bloc de code correspond à une fonction. 

 ````python
def addition(x, y):
    print("L'addition vaut ", x + y)

addition(4,5)
//L'addition vaut 9
````

[Quelques petits exercices? Ok, si vous insistez!](https://github.com/CalcagnoLoic/workshop_python/blob/main/1.Introduction_python/intro_python.ipynb)
