# E2E med Playwright

```text
tests/e2e/test_agile_helper.py
```

## Kör testerna
1. Klona repot. PyCharm: File -> Project from Version Control
2. Kontrollera att PyCharm installerar paketen i requirements.txt och ett du får ett virtual environment (syns till höger i statusfältet och att det finns en .venv-mapp)
3. Öppna PyCharms inbyggda terminal
4. Skriv: `pytest`

Första gången måste du installera Playwright, skriv i så fall `playwright install`.

## Arbetsgång

1. Tillsammans med kund/beställare, ta fram en kravspecifikation
2. Formulera funktionella krav som user stories
3. Ta fram acceptanskriterier (AK) för varje user story
4. Konstruera ett testscenario (TS) för manuellt test, för varje AK
5. Skriv ett testfall för varje TS

```python
# Klicka eller använd expect
locator = page.get_by_role("button").get_by_text("Exempel")
locator.click()
expect(locator).to_be_visible()
```
