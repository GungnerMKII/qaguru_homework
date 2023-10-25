from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure
from allure_commons.types import Severity
import steps

repo = "GungnerMKII/qaguru_homework"

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "shendrim")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка наличия Issue в репозитории")
@allure.link("https://github.com", name="Testing")
def test_selene():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo).press_enter()

    s(by.link_text(repo)).click()

    s("#issues-tab").click()

    s(by.partial_text("#1")).should(be.visible)

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "shendrim")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка наличия Issue в репозитории")
@allure.link("https://github.com", name="Testing")    
def test_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys(repo).press_enter()

    with allure.step("Переходим в репозиторий"):
        s(by.link_text(repo)).click()
        
    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()
        
    with allure.step("Проверяем наличие Issue с номером 1"):
        s(by.partial_text("#1")).should(be.visible)
        
@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "shendrim")
@allure.feature("Задачи в репозитории")
@allure.story("Проверка наличия Issue в репозитории")
@allure.link("https://github.com", name="Testing")
def test_with_decorators():
    steps.open_main_page()
    steps.find_repository(repo)
    steps.open_repository(repo)
    steps.open_issues_tab()
    steps.find_issue()


