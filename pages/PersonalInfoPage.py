from .BasePage import BasePage
from .locators import PersonalInfoPageLocators


class PersonalInfoPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(PersonalInfoPage, self).__init__(*args, **kwargs)

    def accept_all_cookies(self):
        acceptAllCookiesButton = self.wait_and_find_element(*PersonalInfoPageLocators.ACCEPT_ALL_COOKIES_BUTTON)
        acceptAllCookiesButton.click()
        print("All cookies accepted")

    def select_gender_male(self):
        self.browser.find_element(*PersonalInfoPageLocators.BUTTON_GENDER_MALE).click()
        print("Button Gender 'male' clicked")

    def select_gender_female(self):
        self.browser.find_element(*PersonalInfoPageLocators.BUTTON_GENDER_FEMALE).click()
        print("Button Gender 'female' clicked")

    def click_next(self):
        self.browser.find_element(*PersonalInfoPageLocators.BUTTON_NEXT).click()
        print("Button 'Next' clicked")

    def select_marriage_single(self):
        self.browser.find_element(*PersonalInfoPageLocators.BUTTON_MARRIAGE_SINGLE).click()
        print("Button Marriage 'Single' clicked")

    def set_first_name(self, name):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_FIRSTNAME, name)

    def set_last_name(self, lastname):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_LASTNAME, lastname)

    def set_email(self, email):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_EMAIL, email)

    def set_mobile(self, mobile):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_MOBILE, mobile)

    def set_street(self, street):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_STREET, street)

    def set_street_number(self, streetnumber):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_STREET_NUMBER, streetnumber)

    def set_postal_code(self, postalcode):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_POSTAL_CODE, postalcode)

    def set_city(self, city):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_CITY, city)

    def select_province(self, province):
        self.select_by_value(*PersonalInfoPageLocators.SELECT_PROVINCE, "string:"+province)

    def select_birthday_day(self, day):
        self.select_by_value(*PersonalInfoPageLocators.SELECT_BIRTHDAY_DAY, "number:"+str(day))

    def select_birthday_month(self, month):
        self.select_by_value(*PersonalInfoPageLocators.SELECT_BIRTHDAY_MONTH, "number:"+str(month))

    def select_birthday_year(self, year):
        self.select_by_value(*PersonalInfoPageLocators.SELECT_BIRTHDAY_YEAR, "number:"+str(year))

    def set_birth_place(self, place):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_BIRTH_PLACE, place)

    def set_security_answer_1(self, answer1):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_1_SECURITY_QUESTION, answer1)

    def set_security_answer_2(self, answer2):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_2_SECURITY_QUESTION, answer2)

    def set_security_answer_3(self, answer3):
        self.set_text_input(*PersonalInfoPageLocators.INPUT_3_SECURITY_QUESTION, answer3)

    def should_be_submit_error_message(self):
        assert self.is_element_present(
            *PersonalInfoPageLocators.ERROR_SUBMIT_HINT), "Correct your information error message is not presented"

    def should_be_url(self, url):
        assert self.browser.current_url == url , \
            f"Current url:{self.browser.current_url}, but should be {url}"

