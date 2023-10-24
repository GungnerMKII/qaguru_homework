import allure
from selene import browser
from selene.support.shared.jquery_style import s
from selene.support import by
from selene.support.conditions import be

@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий')
def find_repository(repo):
    s(".header-search-button").click()
    s('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Переходим в репозиторий')
def open_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issues_tab():
    s("#issues-tab").click()


@allure.step('Проверяем наличие Issue с номером 1')
def find_issue():
    s(by.partial_text("#1")).should(be.visible)