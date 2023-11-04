from selene import browser, be, have, command
import resources


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.state = browser.element("#state")

    def open_form(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, name):
        browser.element("#firstName").send_keys(name)

    def fill_last_name(self, last_name):
        browser.element("#lastName").send_keys(last_name)

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

    def upload_picture(self):
        browser.element("#uploadPicture").should(be.blank).send_keys(
            resources.path("img/meme.png")
        )

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

    def should_registered_user_with(
        self,
        full_name,
        email,
        gender,
        phone,
        date_of_birth,
        subject,
        hobbies,
        file,
        address,
        state_city,
    ):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subject,
                hobbies,
                file,
                address,
                state_city,
            )
        )

        browser.element("#closeLargeModal").click()
