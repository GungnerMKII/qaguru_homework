from selene import browser, be, have
import os.path

def test_form():
    browser.open('/automation-practice-form') 
    browser.element('#firstName').should(be.blank).type('Test')
    browser.element('#lastName').should(be.blank).type('Testov')
    browser.element('#userEmail').should(be.blank).type('Testov@test.com')
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').should(be.blank).type('9628082744')
    browser.element('#dateOfBirth').click()
    browser.element('.react-datepicker__month-select').click().element('[value="0"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1991"]').click()
    browser.element('[class = "react-datepicker__day react-datepicker__day--010"]').click()
    browser.element('#subjectsInput').should(be.blank).type('Che').press_enter()
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img/meme.png'))
    browser.element('#currentAddress').should(be.blank).type('Testova str, 8, apt.10')
    browser.element('#state').click()
    browser.element('#react-select-3-input').should(be.blank).type('N').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').should(be.blank).type('D').press_enter()
    browser.element('#submit').click()
    
    browser.element('.modal-dialog').should(be.existing)
    browser.element('.table').all('td:nth-child(2)').should(
        have.texts('Test Testov',
                   'Testov@test.com',
                   'Male',
                   '9628082744',
                   "10 January,1991",
                   'Chemistry',
                   'Sports',
                   'meme.png',
                   'Testova str, 8, apt.10',
                   'NCR Delhi'))
    
    
    