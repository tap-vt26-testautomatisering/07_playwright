import re
from playwright.sync_api import Page, expect

# User story (US) -> Acceptanskriterier (AK) -> Testscenarier -> E2E-test!

# US1
# Som en besökare,
# vill jag kunna se sidan både på svenska och engelska,
# så att jag kan lära mig på båda språk.

# AK1. När jag kommer till sidan ska den visas på svenska
# 1. texten "Vilken dag under sprinten" ska finnas
# AK2. När jag klickar på engelska flaggan ska språket ändras
# 1. texten "Vilken dag under sprinten" har försvunnit
# 2. texten "What day of the sprint" ska finnas

# Scenario 1:
# 1. ladda sidan
# 2. kontrollera att texten i AK1.1 visas
# 3. klicka på engelska flaggan
# 4. kontrollera att texten i AK1.1 är borta
# 5. kontrollera att texten i AK2.2 visas

def test_switch_languages(page: Page):
    swedish_text = page.get_by_text(re.compile("Vilken dag under sprinten"))
    expect(swedish_text).to_be_visible()

    page.get_by_test_id("language-en").click(timeout=500)

    expect(swedish_text).not_to_be_visible()

    english_text = page.get_by_text(re.compile("What day of the sprint"))
    expect(english_text).to_be_visible()

