
# TEXT Classification
API de recommandation de tags pour les posts stackoverflow

**Méthode :** POSTS

**Entrée :** format JSON
{"texte": "Texte libre (langue anglaise)"} 
> NB : Les caractères **"** doivent être échappés par un **\\**

**Sortie :** Liste de tags

URL : http://danjo23.pythonanywhere.com/text

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

