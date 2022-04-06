# Méthodes volumes finis pour la résolution de la dynamique des gaz eulérienne et lagrangienne en 1D

```{tableofcontents}
```

Le but de ce dépôt est de fournir des solutions approchées aux problèmes de Riemann associés aux équations d'Euler unidimensionnelles par la méthode volumes finis.

On donnera la solution exacte du problème de Riemann qui est utile à plusieurs égards. Elle représente la solution d'un système de lois de conservation hyperboliques soumises aux conditions initiales les plus simples et non triviales; elle contient néanmoins le caractère physique et mathématique fondamental de l'ensemble des lois de conservation concerné. 
La solution du problème de Riemann est également une solution de référence pour vérifier l'exactitude des programmes en début de développement. La solution exacte ou approchée peut aussi être utilisée localement dans la méthode  de Godunov et dans ses extensions d'ordre élevé; c'est l'un des rôles principaux du problème de Riemann. Nous nous limiterons à la méthode d'ordre 1 de Godunov.
Nous définirons ensuite des solveurs de Riemann approchés. 
Existe-t-il un solveur qui soit meilleur que tous les autres ? Est-ce valable dans tous les cas ? 
Nous allons essayer d'apporter des réponses à ces interrogations.

```{bibliography}
```