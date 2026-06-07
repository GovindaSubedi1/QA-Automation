from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD

def test_valid_login(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)

    assert "inventory" in page.url