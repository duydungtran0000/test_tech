## Architecture
- Refactorer la structure du projet selon les bonnes pratiques de Clean Architecture. Par exemple :
  - `entities/` : objets métiers (ex : Stack, Operation)
  - `services/` : logique métier (ex : `StackService`)
  - `repositories/` : couche d'accès aux données (ex : base SQLite ou PostgreSQL)
- Évolution vers une architecture microservices :
  - Un service dédié à la gestion des piles
  - Un service pour les opérations mathématiques

## Fonctionnalités
- Affecter chaque pile à un utilisateur spécifique (multi-session, authentification JWT)
- Réinitialiser une pile sans la supprimer (`DELETE` des éléments mais pas l’ID)
- Opérations avancées : `mod`, `sqrt`, `pow`, `neg`, `abs`

## Logging & DevOps
- Mise en place de `logging` Python (niveaux DEBUG / INFO / ERROR), avec affichage en console et sauvegarde dans un fichier `.log`
- Intégration d’un dashboard Grafana + Prometheus pour superviser les performances (latence, erreurs, charge)
- Création d’un endpoint `/health` pour le monitoring applicatif

## Bonnes pratiques & Qualité
- Vérification automatique de la qualité du code :
  - Linting avec `flake8`
  - Formatage avec `black`
  - Couverture de tests avec `pytest-cov`
- Intégration d'un pipeline CI avec GitHub Actions
- (Optionnel) Intégration de SonarQube ou SonarCloud pour l’analyse statique du code et la dette technique