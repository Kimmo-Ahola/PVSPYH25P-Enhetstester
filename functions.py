import math


def add(a, b):
    """Adderar två tal"""
    return a + b


def subtract(a, b):
    """Subtraherar b från a"""
    return a - b


def multiply(a, b):
    """Multiplicerar två tal"""
    return a * b


def divide(a, b):
    """Dividerar två tal"""
    if b == 0:
        return math.inf

    return a / b


def reverse_string(text):
    """Vänder en sträng baklänges. Får inte använda inbyggd reverse-funktion från Python."""
    if len(text) == 0:
        return ""

    return text[::-1]


def capitalize_words(text):
    """Gör första bokstaven i varje ord till versal. Får inte ändra Pythons inbygga title()."""

    if len(text) == 0:
        return ""

    split = text.split(" ")

    if len(split) == 1:
        return text[0].upper() + text[1::].lower()

    res = ""
    for word in split:
        res = res + word[0].upper() + word[1::].lower() + " "

    return res.strip()


def count_vowels(text, language="en"):
    """Räknar antalet vokaler i en sträng"""
    en_vowels = "aeiou"
    swe_vowels = "aeiouyåäö"
    counter = 0
    if language == "en":
        for t in text:
            if t in en_vowels:
                counter += 1
    elif language == "sv":
        for t in text:
            if t in swe_vowels:
                counter += 1
    return counter


def is_palindrome(text):
    """Kontrollerar om en sträng är ett palindrom. Palindrom är att ordet är likadant baklänges."""
    pass
