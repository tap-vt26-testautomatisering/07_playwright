import pytest

# Anledningar till att man kan behöva en timeout:
# + Att ladda en webbsida kan ta tid - kan bero på servrar. Här används 30 sek. som standard
# + Animationer måste köra klart innan Playwright ser elementet. Sätt timeout lite högre än animationens längd.
# + Vänta på att appen uppdateras med data från ett API. Detta kan ta mellan 10-100 ms i normala fall.

@pytest.fixture
def context(context):
    # tal kan skrivas vanligt (1000) eller med tusentals-separator (1_000)
    context.set_default_timeout(1_000)
    return context

