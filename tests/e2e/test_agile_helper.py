import re
# re == reguljära uttryck == "regex"
from playwright.sync_api import Page, expect

#base_url = "https://lejonmanen.github.io/agile-helper/"

# Vanligt smoke test
def test_has_title(page: Page):
#    page.goto(base_url)
    # TODO: flytta page.goto till en gemensam funktion i environment.py i stället - nästa vecka

    expect(page).to_have_title(re.compile("Agile helper"))



# User story:
# som en användare
# vill jag kunna läsa om Sprint retrospective
# så att jag slutar en sprint på rätt sätt.

# Manuellt test
# 1. surfa till webbsidan
# 2. klicka på knappen med texten "Sista"
# 3. klicka på knappen med texten "Sprint retrospective"
# 4. leta upp rubriken med texten "Sprint retrospective"
# 5. kontrollera att rubriken är synlig
#
# Alternativ till pkt 4: välj ut baserat på CSS-klass - fungerar men rekommenderas inte

def test_read_sprint_retrospective(page: Page):
    button_locator = page.get_by_role("button")
    button_last = button_locator.get_by_text("Sista")
    button_last.click()

    page.get_by_role("button").get_by_text(re.compile("Sprint retrospective")).click()

    heading = page.get_by_role("heading").get_by_text(re.compile("Sprint retrospective"))

    expect(heading).to_be_visible()


# AK: Om jag klickar på en annan knapp än "Sista", då ska inte knappen med texten "Sprint retrospective" vara synlig

def test_sprint_retro_navigation(page: Page):
    page.get_by_role("button").get_by_text(re.compile("Första")).click()
    button = page.get_by_role("button").get_by_text(re.compile("Sprint retrospective"))

    expect(button).not_to_be_visible()

