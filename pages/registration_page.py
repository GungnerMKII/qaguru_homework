from selene import browser, have, command
from data.users import User
from resources import path
import allure


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.state = browser.element("#state")

    with allure.step("Открываем форму регистрации"):

        def open_form(self):
            browser.open("/automation-practice-form")

    def fill_first_name(self, name):
        self.first_name.type(name)

    def fill_last_name(self, last_name):
        self.last_name.type(last_name)

    def fill_email(self, email):
        browser.element("#userEmail").send_keys(email)

    def select_gender(self, gender):
        gender = gender.capitalize()
        browser.element(f'//label[text() = "{gender}"]').click()

    def fill_phone_number(self, phone):
        browser.element("#userNumber").send_keys(phone)

    def select_date_of_birth(self, month, day, year):
        month = month.capitalize()
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(f'//*[text()="{month}"]').click()

        browser.element(".react-datepicker__year-select").click()
        browser.element(f"//*[text()={year}]").click()
        browser.element(f"//div[text()={day}]").click()

        browser.element("#firstName").click()

    def select_subject(self, subject):
        browser.element("#subjectsInput").type(f"{subject}").press_enter()

    def select_hobbies(self):
        browser.element('//label[@for="hobbies-checkbox-1"]').click()
        browser.element('//label[@for="hobbies-checkbox-3"]').click()

    def upload_picture(self, value):
        browser.element("#uploadPicture").send_keys(path(value))

    def fill_address(self, address):
        browser.element("#currentAddress").send_keys(f"{address}")

    def select_state(self, state):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(state)
        ).click()

    def select_city(self, city):
        city = city.capitalize()
        browser.element("#city").click()
        browser.element(f'//*[text()="{city}"]').click()

    def submit(self):
        browser.element("#submit").perform(command.js.click)

    with allure.step("Регистрируем юзера"):

        def register(self, user: User):
            self.fill_first_name(user.first_name)
            self.fill_last_name(user.last_name)
            self.fill_email(user.email)
            self.select_gender(user.gender)
            self.fill_phone_number(user.phone)
            self.select_date_of_birth(user.month_birth, user.day_birth, user.year_birth)
            self.select_subject(user.subject)
            self.select_hobbies()
            self.upload_picture(user.photo)
            self.fill_address(user.current_address)
            self.select_state(user.state)
            self.select_city(user.city)
            self.submit()

    with allure.step("Проверяем регистрацию"):

        def should_registered_user_with(self, user: User):
            browser.element(".table").all("td").even.should(
                have.exact_texts(
                    f"{user.first_name} {user.last_name}",
                    user.email,
                    user.gender,
                    user.phone,
                    f"{user.day_birth} {user.month_birth},{user.year_birth}",
                    user.subject,
                    user.hobbies,
                    user.photo,
                    user.current_address,
                    f"{user.state} {user.city}",
                )
            )
