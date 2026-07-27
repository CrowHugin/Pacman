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

%% --- 1. DÉCLARATION DES BLOCS ---

subgraph Init["Initialization"]
    direction TB
    Start --> JSONParsing
    JSONParsing --> MenuManager
end

subgraph Levels["Level Creation"]
    direction TB
    Map["Labyrinth"] --> Pacgum["Pac-Dots"]
    Map --> Ghosts["Mobs (Ghosts)"]
    Map --> Pacman["Player (Pac-Man)"]
    
    Pacgum --> Sprites["Sprites Loading"]
    Ghosts --> Sprites
    Pacman --> Sprites
end

subgraph GameSystems["Loop and Game Systems"]
    direction TB
    PlayerControls --> Collisions
    Collisions --> ScoreLives
    ScoreLives --> EndGame
    EndGame <--> SaveHighscores
end

%% --- 2. LE VERROUILLAGE (L'arme absolue contre GitHub) ---
%% Ces liens invisibles forcent GitHub à empiler les blocs 
%% dans cet ordre précis, quoi qu'il arrive avec les autres flèches.
Init ~~~ Levels
Levels ~~~ GameSystems

%% --- 3. LE FLUX DESCENDANT ---
%% On utilise des flèches rallongées (--->) pour donner encore plus 
%% de poids à la direction "vers le bas".
MenuManager --->|Level creation| Map
Sprites --->|Start loop| PlayerControls

%% --- 4. LE FLUX REMONTANT (Syntaxe standard) ---
%% Syntaxe classique pointillée que GitHub comprend parfaitement.
%% Grâce au verrouillage (~~~), ça n'inversera pas les blocs.
EndGame -.->|Defeat / 10 victories: Menu| MenuManager
ScoreLives -.->|Victories: New levels| MenuManager

%% --- 5. STYLING ---
style Init fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
style Levels fill:#fff3e0,stroke:#f57c00,stroke-width:2px
style GameSystems fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
```

### *Project management*

Board management exemple:
![project_image](./README_images/Board.png)

Roadmap management exemple:
![project_timeline](./README_images/timeline.png)



- [github](https://github.com/users/CrowHugin/projects/4)
%%
