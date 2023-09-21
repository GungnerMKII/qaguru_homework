from selene.support.shared import browser
from selene import be, have


def test_google_search_success(open_google):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))  
    
def test_google_search_none(open_google):
    browser.element('[name="q"]').should(be.blank).type('sdfgfhjfghkjhgd').press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
    print("Nothing found")
    
def test_text_form(open_demoqa_textbox): 
    browser.element('#userForm #userName').should(be.blank).type('testov test testovich') 
    browser.element('#userForm  #userEmail').should(be.blank).type('test@test.com')
    browser.element('#userForm  #currentAddress').should(be.blank).type('adress')
    browser.element('#userForm  #permanentAddress').should(be.blank).type('same as current')
    
    browser.element('#submit').click()
    
    browser.element('#output').should(be.visible)     
    browser.element('#output #name').should(have.text('testov test testovich'))
    browser.element('#output #email').should(have.text('test@test.com'))
    browser.element('#output #currentAddress').should(have.text('adress'))
    browser.element('#output #permanentAddress').should(have.text('same as current'))
    