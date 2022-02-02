import traceback
import pytest
from utilities.read_properties import read_Config
from selenium.webdriver.common.by import By

playground = read_Config.get_url()

first_name_loc = "#root > form > label:nth-child(1)"
last_name_loc = "#root > form > label:nth-child(3)"
email_loc = "#root > form > label:nth-child(5)"
phone_number_loc = "#root > form > label:nth-child(7)"
gender_loc = "#root > form > label:nth-child(9)"
terms_loc = "#root > form > label:nth-child(12)"
first_name_require_loc = '/html/body/div/form/p[1]'
last_name_require_loc = "/html/body/div/form/p[2]"
email_require_loc = "/html/body/div/form/p[3]"
phone_number_require_loc = "/html/body/div/form/p[4]"
gender_require_loc = "/html/body/div/form/p[5]"
terms_require_loc = "/html/body/div/form/p[6]"


@pytest.mark.usefixtures("chrome_setup")
class BaseTest:
    pass


class Test_playground_texts_displayed(BaseTest):
    def test_first_name_text_displayed(self):
        self.driver.get(playground)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        first_name = self.driver.find_element(By.CSS_SELECTOR, first_name_loc).is_displayed()
        if first_name:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_last_name_text_displayed(self):
        self.driver.implicitly_wait(5)
        last_name = self.driver.find_element(By.CSS_SELECTOR, last_name_loc).is_displayed()
        if last_name:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_email_text_displayed(self):
        self.driver.implicitly_wait(5)
        email = self.driver.find_element(By.CSS_SELECTOR, email_loc).is_displayed()
        if email:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_phone_number_text_displayed(self):
        self.driver.implicitly_wait(5)
        phone_number = self.driver.find_element(By.CSS_SELECTOR, phone_number_loc).is_displayed()
        if phone_number:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_gender_text_displayed(self):
        self.driver.implicitly_wait(5)
        first_name = self.driver.find_element(By.CSS_SELECTOR, gender_loc).is_displayed()
        if first_name:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_terms_text_displayed(self):
        self.driver.implicitly_wait(5)
        terms = self.driver.find_element(By.CSS_SELECTOR, terms_loc).is_displayed()
        if terms:
            assert True
        else:
            traceback.format_exc()
            assert False


class Test_playground_texts_correct(BaseTest):
    def test_first_name_text_match(self):
        self.driver.get(playground)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        first_name = self.driver.find_element(By.CSS_SELECTOR, first_name_loc)
        if "First name" in first_name.text:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_last_name_text_match(self):
        self.driver.implicitly_wait(5)
        last_name = self.driver.find_element(By.CSS_SELECTOR, last_name_loc)
        if "Last name" in last_name.text:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_email_name_text_match(self):
        self.driver.implicitly_wait(5)
        email = self.driver.find_element(By.CSS_SELECTOR, email_loc)
        if "Email" in email.text:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_phone_number_name_text_match(self):
        self.driver.implicitly_wait(5)
        phone_number = self.driver.find_element(By.CSS_SELECTOR, phone_number_loc)
        if "Phone number" in phone_number.text:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_gender_name_text_match(self):
        self.driver.implicitly_wait(5)
        gender = self.driver.find_element(By.CSS_SELECTOR, gender_loc)
        if "Gender" in gender.text:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_terms_name_text_match(self):
        self.driver.implicitly_wait(5)
        terms = self.driver.find_element(By.CSS_SELECTOR, terms_loc)
        if "I agree to the processing of personal data" in terms.text:
            assert True
        else:
            traceback.format_exc()
            assert False


class Test_playground_texts_required_displayed(BaseTest):
    def test_first_name_required(self):
        self.driver.get(playground)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        first_name = self.driver.find_element(By.XPATH, first_name_require_loc).is_displayed()
        if first_name:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_last_name_required(self):
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        last_name = self.driver.find_element(By.XPATH, last_name_require_loc).is_displayed()
        if last_name:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_email_required(self):
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        email = self.driver.find_element(By.XPATH, email_require_loc).is_displayed()
        if email:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_phone_number_required(self):
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        phone_number = self.driver.find_element(By.XPATH, phone_number_require_loc).is_displayed()
        if phone_number:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_gender_required(self):
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        gender = self.driver.find_element(By.XPATH, gender_require_loc).is_displayed()
        if gender:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_terms_required(self):
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        terms = self.driver.find_element(By.XPATH, terms_require_loc).is_displayed()
        if terms:
            assert True
        else:
            traceback.format_exc()
            assert False


class Test_playground_texts_required_correct(BaseTest):
    def test_first_name_required(self):
        self.driver.get(playground)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        first_name = self.driver.find_element(By.XPATH, first_name_require_loc)
        if "Valid first name is required." in first_name.text:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_last_name_required(self):
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        last_name = self.driver.find_element(By.XPATH, last_name_require_loc)
        if "Valid last name is required." in last_name.text:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_email_required(self):
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        email = self.driver.find_element(By.XPATH, email_require_loc)
        if "Valid email is required." in email.text:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_phone_number_required(self):
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        phone_number = self.driver.find_element(By.XPATH, phone_number_require_loc)
        if "Valid phone number is required." in phone_number.text:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_gender_required(self):
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        gender = self.driver.find_element(By.XPATH, gender_require_loc)
        if "Choose your gender." in gender.text:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_terms_required(self):
        self.driver.implicitly_wait(5)
        button = self.driver.find_element(By.NAME, "submitbutton")
        button.click()
        terms = self.driver.find_element(By.XPATH, terms_require_loc)
        if "You must agree to the processing of personal data." in terms.text:
            assert True
        else:
            traceback.format_exc()
            assert False
