from .pages.PersonalInfoPage import PersonalInfoPage

# DOF page link
url = "https://www.lynxbroker.de/wertpapierdepot/depoteroeffnung/antrag"


def test_dof_cannot_submit_form_without_required_fields(browser):
    page = PersonalInfoPage(browser, url)
    page.accept_all_cookies()
    page.click_next()
    page.should_be_submit_error_message()
    firstPageURL = 'https://www.lynxbroker.de/wertpapierdepot/depoteroeffnung/antrag/wizard/start'
    page.should_be_url(firstPageURL)


def test_dof_go_to_second_page_success(browser):
    page = PersonalInfoPage(browser, url)
    page.accept_all_cookies()
    page.select_gender_male()
    page.set_first_name("Test")
    page.set_last_name("Test")
    page.set_email("Test@test.com")
    page.set_mobile("012345")
    page.set_street("TestStreet")
    page.set_street_number("TestStreetNumber")
    page.set_postal_code("TestPostCode")
    page.set_city("TestCity")
    page.select_province("Berlin")
    page.select_birthday_day("1")
    page.select_birthday_month("1")  # January
    page.select_birthday_year("2000")
    page.set_birth_place("TestBirthPlace")
    page.select_marriage_single()
    page.set_security_answer_1("TestAnswer1")
    page.set_security_answer_2("TestAnswer2")
    page.set_security_answer_3("TestAnswer3")

    page.click_next()
    secondPageURL = 'https://www.lynxbroker.de/wertpapierdepot/depoteroeffnung/antrag/wizard/personal/2'
    page.should_be_url(secondPageURL)
