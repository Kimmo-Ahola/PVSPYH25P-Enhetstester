# multiply-funktionen
1. Skriv minst 3 tester för multiply-funktionen
2. Tips: Testa positiva tal, negativa tal, multiplikation med noll

Exempel nedan på tomma tester.
```python
def test_multiply_positive():
    # TODO: Skriv ditt test här
    pass

def test_multiply_with_zero():
    # TODO: Skriv ditt test här
    pass

def test_multiply_negative():
    # TODO: Skriv ditt test här
    pass
```

# Division-funktion
1. Funktionen finns inte alls i functions.py och du måste skriva den själv.
2. Vad finns det för edge cases för division vi måste täcka upp för?


# capitalize_words-funktionen
1. Skriv tester för att kontrollera att funktionen fungerar korrekt

```python
def test_capitalize_single_word():
    # TODO: Skriv ditt test här
    # Tips: "hello" borde bli "Hello"
    pass


def test_capitalize_multiple_words():
    # TODO: Skriv ditt test här
    # Tips: "hello world" borde bli "Hello World"
    pass


def test_capitalize_already_capitalized():
    # TODO: Skriv ditt test här
    pass
```
# Reverse
1. Funktionen ska skicka tillbaka strängen omvänt.
2. Vad händer om man skickar in en tom sträng eller siffror?

# count_vowels-funktionen
1. Skriv tester för att räkna vokaler
2. Börja med engelska vokaler och skriv testet för det först.
3. Lägg till svenska vokaler och skriv tester för det.

```python
def test_count_vowels_simple():
    # TODO: Skriv ditt test här
    # Tips: "hello" har 2 vokaler (e, o)
    pass


def test_count_vowels_swedish():
    # TODO: Skriv ditt test här
    # Tips: "åäö" har 3 vokaler
    pass


def test_count_vowels_no_vowels():
    # TODO: Skriv ditt test här
    # Tips: "gym" har 0 vokaler på engelska. Hur är det på svenska?
    pass
```

# Testa is_palindrome-funktionen
1. Ett palindrom är ett ord som är samma framlänges som baklänges
2. Funktionen bör skicka tillbaka true/false.

```python
def test_palindrome_simple():
    # TODO: Skriv ditt test här
    # Tips: "anna" är ett palindrom
    pass


def test_palindrome_with_spaces():
    # TODO: Skriv ditt test här
    # Tips: "ni talar bra latin" är ett palindrom
    pass
    
def test_palindrome_with_spaces():
    # TODO: Skriv ditt test här
    # Tips: testa med siffror och se om det fungerar
    pass


def test_not_palindrome():
    # TODO: Skriv ditt test här
    # Tips: "hello" är INTE ett palindrom
    pass
```

# Lägg till ett test som räknar ord i en sträng

1. Testa vad som händer om man skickar in en tom sträng. Svaret bör bli 0.
2. Vad finns mellan varje ord som vi måste kolla efter?


# Skriv ett parametriserat test för subtract

```python
@pytest.mark.parametrize("a, b, expected", [
    # TODO: Lägg till testfall här
    # Format: (tal1, tal2, förväntat_resultat)
])
def test_subtract_parametrized(a, b, expected):
    # TODO: Implementera testet
    pass
```
