from selenium.webdriver.common.by import By


class PersonalInfoPageLocators:
    ACCEPT_ALL_COOKIES_BUTTON = (By.CSS_SELECTOR, "button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    BUTTON_GENDER_MALE = (By.CSS_SELECTOR, "button[uib-btn-radio=\"'male'\"]")
    BUTTON_GENDER_FEMALE = (By.CSS_SELECTOR, "button[uib-btn-radio=\"'female'\"]")
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "input#firstname")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "input#lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input#email")
    INPUT_MOBILE = (By.CSS_SELECTOR, "input[name='mobile']")
    INPUT_STREET = (By.CSS_SELECTOR, "input#street")
    INPUT_STREET_NUMBER = (By.CSS_SELECTOR, "input#streetnumber")
    INPUT_POSTAL_CODE = (By.CSS_SELECTOR, "input#zip")
    INPUT_CITY = (By.CSS_SELECTOR, "input#city")
    SELECT_PROVINCE = (By.CSS_SELECTOR, "select[ng-model='province']")
    SELECT_BIRTHDAY_DAY = (By.CSS_SELECTOR, "select[ng-model='day']")
    SELECT_BIRTHDAY_MONTH = (By.XPATH, "//div[@class='col-sm-5 hidden-xs']/select[@ng-model='month']")
    SELECT_BIRTHDAY_YEAR = (By.CSS_SELECTOR, "select[ng-model='year']")
    INPUT_BIRTH_PLACE = (By.CSS_SELECTOR, "input#place_of_birth")
    BUTTON_MARRIAGE_SINGLE = (By.CSS_SELECTOR, "button[uib-btn-radio=\"'single'\"]")
    INPUT_1_SECURITY_QUESTION = (By.CSS_SELECTOR, "input[name='first_question']")
    INPUT_2_SECURITY_QUESTION = (By.CSS_SELECTOR, "input[name='second_question_answer']")
    INPUT_3_SECURITY_QUESTION = (By.CSS_SELECTOR, "input[name='third_question_answer']")
    BUTTON_NEXT = (By.XPATH, "//span[text()='Weiter']/parent::button")
    ERROR_SUBMIT_HINT = (By.XPATH, "//span[text()='Bitte korrigieren Sie Ihre Angaben in den rot markierten Feldern']")

