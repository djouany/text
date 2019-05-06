
# TEXT Classification
API de recommandation de tags pour les posts stackoverflow

URL : http://danjo23.pythonanywhere.com

**Méthode :** POSTS

**Entrée :** Texte en saisie libre dans l'interface

**Sortie :** Liste de tags et probabilités associées


## Traitement
- Suppression des balises HTML
- Passage en minuscule
- Suppression des stopwords
- Remplacement par dictionnaire de mots ou abréviations clés
- Suppression de la ponctuation
- Suppression des caractères alphanumériques isolés
- Stemming
- Vectorisation TF-IDF
- Prédiction des tags

