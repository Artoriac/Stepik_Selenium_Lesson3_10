from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_btn(browser):
    browser.get(link)
    add_button = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))
    assert add_button > 0, "Add button is not displayed"
