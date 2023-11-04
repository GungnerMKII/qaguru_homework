from pages.registration_page import RegistrationPage
from data import users


def test_registration_page():
    registration_page = RegistrationPage()
    registration_page.open_form()
    registration_page.register(users.admin)

    registration_page.should_registered_user_with(users.admin)
