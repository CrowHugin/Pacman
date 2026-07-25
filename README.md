*This activity has been created as part of the 42 curriculum by ahalifa and bkuntz*

---
## ***Description***

This activity is about creating a pacman from a maze generator. 

---
## ***Instructions***

Makefile

| Commands    | Use                                 |
| ----------- | ----------------------------------- |
| all         | Default behavior see run            |
| run         | Run the script within the env       |
| debug       | Run debuger                         |
| clean       | Remove all cache file and venv      |
| lint        | Run flake8 and mypy                 |
| lint-strict | Run flake8 and mypy --strict        |
| tests       | Run Tests, see Test folder          |
| build ?     | make the build, see if needed later |

## ***Resources***

- [unittest](https://docs.python.org/3/library/unittest.html)
- [pygame](https://www.pygame.org/docs/)
### *Configuration*
---
### *Highscore*

### *Maze Generation*

The assigned packaged was used to randomly create mazes.
The level_1 is created with a seed (which one ?), the others are random
### *Implementation*

### *General Software Architecture*

```mermaid
flowchart TB
    %% Définition du Frontend
    subgraph Client [Frontend - Interface Client]
        Web[Application Web]
        Mobile[Application Mobile]
    end

    %% Définition du Backend
    subgraph Backend [Backend - Serveur API]
        Gateway{API Gateway}
        
        subgraph Modules [Modules Métier]
            direction TB
            Auth[Module Authentification]
            Users[Module Utilisateurs]
            Core[Module Traitement Core]
        end
    end

    %% Définition des Bases de données
    subgraph Data [Couche de Données]
        DB[(Base de Données SQL)]
        Cache[(Cache Redis)]
    end

    %% Connexions et Flux de données
    Web -->|Requêtes HTTP/REST| Gateway
    Mobile -->|Requêtes HTTP/REST| Gateway

    Gateway -->|Valide le token| Auth
    Gateway -->|Routes /users| Users
    Gateway -->|Routes métier| Core

    Auth -->|Vérifie les identifiants| DB
    Users -->|CRUD Utilisateurs| DB
    Core -->|Lecture / Écriture| DB
    Core -->|Stockage rapide| Cache
```

### *Project management*
![project_image](./README_images/Board.png)
![project_timeline](./README_images/timeline.png)



- [github](https://github.com/users/CrowHugin/projects/4)
