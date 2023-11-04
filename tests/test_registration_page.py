from pages.registration_page import RegistrationPage


def test_registration_page():
    registration_page = RegistrationPage()

    registration_page.open_form()
    registration_page.fill_first_name("Test")
    registration_page.fill_last_name("Testov")
    registration_page.fill_email("Testov@test.com")
    registration_page.select_gender("male")
    registration_page.fill_phone_number("9628082744")
    registration_page.select_date_of_birth("january", 1, 1991)
    registration_page.select_subject("math")
    registration_page.select_hobbies()
    registration_page.upload_picture()
    registration_page.fill_address("Testova str, 8, apt.10")
    registration_page.select_state("NCR")
    registration_page.select_city("Delhi")
    registration_page.submit()

    registration_page.should_registered_user_with(
        "Test Testov",
        "Testov@test.com",
        "Male",
        "9628082744",
        "01 January,1991",
        "Maths",
        "Sports, Music",
        "meme.png",
        "Testova str, 8, apt.10",
        "NCR Delhi",
    )
