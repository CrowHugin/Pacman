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
    %% Définition de l'Interface et Périphériques
    subgraph UI [Interface & Entrées]
        Display[Moteur de Rendu Visuel]
        Inputs[Contrôles Joueur]
    end

    %% Définition du Moteur de Jeu (Core Logic)
    subgraph Engine [Moteur de Jeu]
        GameLoop{Boucle de Jeu Principale- Pygame}
        
        subgraph Logic [Systèmes Logiques]
            direction TB
            State["Gestionnaire d'États (Menu/Jeu/Game Over)"]
            Collision[Détection des Collisions]
            Score["Gestionnaire des Scores & Vies"]
        end
    end

    %% Définition des Entités Actives
    subgraph Entities [Entités du Jeu]
        Pacman["Pac-Man (Modèle Joueur)"]
        Ghosts["Fantômes (IA: Poursuite/Fuite)"]
        Map["Labyrinthe & Pac-Gommes"]
    end

    %% Définition du Stockage / Assets
    subgraph Data [Ressources & Sauvegardes]
        Assets[Sprites]
        SaveData[("Sauvegarde des Meilleurs Scores")]
    end

    %% Connexions et Flux de données
    Inputs -->|Commandes de direction| Pacman

    GameLoop -->|"Mise à jour (ex: 60 FPS)"| Logic
    GameLoop -->|Rafraîchit l'écran| Display

    State -->|Active/Désactive| Entities
    Pacman -->|Se déplace dans| Map
    Ghosts -->|"Pathfinding (IA)"| Map
    
    Pacman -->|Position exacte| Collision
    Ghosts -->|Position exacte| Collision
    Map -->|État des pac-gommes| Collision

    Collision -->|Touche un fantôme / Mange un fruit| Score
    Collision -->|"Mort (plus de vies)"| State
    
    Display -->|Charge les textures| Assets
    Score <-->|Lit / Enregistre| SaveData
```

### *Project management*
![project_image](./README_images/Board.png)
![project_timeline](./README_images/timeline.png)



- [github](https://github.com/users/CrowHugin/projects/4)
