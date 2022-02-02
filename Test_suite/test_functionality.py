import time
import traceback
import pytest
from utilities.read_properties import read_Config
from selenium.webdriver.common.by import By

playground = read_Config.get_url()

input_first_name_loc = "FirstName"
input_last_name_loc = "LastName"
input_email_loc = "Email"
input_phone_number_loc = "PhoneNumber"
input_gender_loc = "Gender"
check_male_loc = '/html/body/div/form/div[1]/input'
check_female_loc = '/html/body/div/form/div[2]/input'
input_terms_loc = "Agreement"
submit_button_loc = "submitbutton"


@pytest.mark.usefixtures("chrome_setup")
class BaseTest:
    pass


class Test_playground_input_enabled(BaseTest):
    def test_first_name_enabled(self):
        self.driver.get(playground)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        first_name = self.driver.find_element(By.NAME, input_first_name_loc).is_enabled()
        if first_name:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_last_name_enabled(self):
        self.driver.implicitly_wait(5)
        last_name = self.driver.find_element(By.NAME, input_last_name_loc).is_enabled()
        if last_name:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_email_enabled(self):
        self.driver.implicitly_wait(5)
        email = self.driver.find_element(By.NAME, input_email_loc).is_enabled()
        if email:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_phone_number_enabled(self):
        self.driver.implicitly_wait(5)
        phone_number = self.driver.find_element(By.NAME, input_phone_number_loc).is_enabled()
        if phone_number:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_gender_enabled(self):
        self.driver.implicitly_wait(5)
        gender = self.driver.find_element(By.NAME, input_gender_loc).is_enabled()
        if gender:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_terms_enabled(self):
        self.driver.implicitly_wait(5)
        terms = self.driver.find_element(By.NAME, input_terms_loc).is_enabled()
        if terms:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_submit_button_enabled(self):
        self.driver.implicitly_wait(5)
        submit_button = self.driver.find_element(By.NAME, submit_button_loc).is_enabled()
        if submit_button:
            assert True
        else:
            traceback.format_exc()
            assert False


class Test_playground_functionality(BaseTest):
    def test_first_name(self):
        self.driver.get(playground)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        first_name = self.driver.find_element(By.NAME, input_first_name_loc)
        first_name.send_keys("testJhon")
        if first_name:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_last_name(self):
        self.driver.implicitly_wait(5)
        last_name = self.driver.find_element(By.NAME, input_last_name_loc)
        last_name.send_keys("testMichael")
        if last_name:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_email(self):
        self.driver.implicitly_wait(5)
        email = self.driver.find_element(By.NAME, input_email_loc)
        email.send_keys("testmech@test.fun")
        if email:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_phone_number(self):
        self.driver.implicitly_wait(5)
        phone_number = self.driver.find_element(By.NAME, input_phone_number_loc)
        phone_number.send_keys("999881112233")
        if phone_number:
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_choose_gender(self):
        driver = self.driver
        self.driver.implicitly_wait(5)
        male = self.driver.find_element(By.XPATH, check_male_loc).is_selected()
        female = self.driver.find_element(By.XPATH, check_female_loc).is_selected()
        if not male:
            driver.find_element(By.XPATH, check_male_loc).click()
        elif not female:
            driver.find_element(By.XPATH, check_female_loc).click()
        time.sleep(5)

    def test_check_terms(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, input_terms_loc).click()

    def test_submit_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, submit_button_loc).click()
        time.sleep(5)

    def test_confirm_alert(self):
        self.driver.switch_to.alert.accept()
