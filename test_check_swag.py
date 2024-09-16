from pages.swag_labs import SwagLabs

def test_icon_exists(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.find_element()
    assert swag_labs_page.exist_icon()

def test_username_exists(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    swag_labs_page.find_element()
    assert swag_labs_page.exist_username()

def test_password_exists(browser):
    swag_labs = SwagLabs(browser)
    swag_labs.visit()
    swag_labs_page.find_element()
    assert swag_labs_page.exist_password()


  
  
