# retry-budget-cascade

## Français

Calculer l’amplification des reprises et la borner sur un graphe de services.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m retry_budget_cascade examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Calcule la multiplication des tentatives dans un graphe d’appels imbriqués, y compris les dépendances partagées appelées par plusieurs chemins. Compare au graphe sans reprises et à un plafond global hypothétique explicitement non exécuté.

### Limites

50 services acycliques maximum ; borne de configuration où chaque reprise répète les enfants. Ni compteur réel, backoff, idempotence, cache ou probabilité de panne.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Compute retry amplification and bound it on a service graph.

Synthetic data; no network access or secret required.

```sh
python -m retry_budget_cascade examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Computes attempt multiplication in nested call graphs, including shared dependencies called through multiple paths. Compares with the no-retry graph and an explicitly unenforced hypothetical shared cap.

### Limits

At most 50 acyclic services; configuration upper bound where each retry repeats children. No actual counter, backoff, idempotency, cache or failure probability.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Calcular amplificación de reintentos y acotarla en un grafo.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m retry_budget_cascade examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Calcula multiplicación de intentos en grafos de llamadas anidadas, incluidas dependencias compartidas por varios caminos. Compara con grafo sin reintentos y límite global hipotético explícitamente no ejecutado.

### Límites

Máximo 50 servicios acíclicos; cota de configuración donde cada reintento repite hijos. Sin contador real, backoff, idempotencia, caché ni probabilidad de fallo.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://sre.google/sre-book/handling-overload/
