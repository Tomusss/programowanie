# Mates łapie owoce

Prototyp gry, w której gracz steruje postacią Mateusza, aby łapać spadające owoce i unikać bomb. Gra staje się coraz trudniejsza w miarę zdobywania punktów.

## Instrukcje uruchomienia prototypu

1. **Klonowanie repozytorium:**
    ```bash
    git clone https://github.com/yourusername/mates-lapie-owoce.git
    cd mates-lapie-owoce
    ```

2. **Instalacja wymaganych bibliotek:**
    Upewnij się, że masz zainstalowane `pip` oraz Python w wersji 3.6 lub wyższej. Następnie uruchom poniższe polecenie:
    ```bash
    pip install -r requirements.txt
    ```

3. **Uruchomienie gry:**
    ```bash
    python main.py
    ```

## Lista wymaganych bibliotek

- Pygame

## Instrukcje użytkowania

### Sterowanie

- Strzałka w lewo (`LEFT ARROW`): Przesuń gracza w lewo.
- Strzałka w prawo (`RIGHT ARROW`): Przesuń gracza w prawo.
- Spacja (`SPACE`): Wstrzymaj/Wznow grę.

### Zasady gry

1. **Zbieranie owoców:** 
   - Gracz steruje niebieskim prostokątem, który musi łapać spadające czerwone owoce.
   - Za każdy złapany owoc gracz otrzymuje punkt.
   - Po zdobyciu 5 punktów zwiększa się poziom trudności: owoce i bomby zaczynają spadać szybciej.
   - Co 10 punktów, zwiększa się maksymalna liczba owoców i bomb na ekranie.

2. **Unikanie bomb:**
   - Gracz musi unikać spadających czarnych bomb.
   - Jeśli gracz dotknie bombę, gra kończy się.

3. **Życia:**
   - Gracz zaczyna z 3 życiami.
   - Każdy spadający owoc, który nie zostanie złapany, kosztuje gracza jedno życie.
   - Jeśli liczba żyć spadnie do zera, gra się kończy.

Ciesz się grą i powodzenia!
