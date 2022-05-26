import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestConferenceRegistration(unittest.TestCase):
    """TestingConferenceRegistration
    https://confengine.com/conferences/selenium-conf-2022/register/selection"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "https://confengine.com/conferences/selenium-conf-2022/register/selection"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_set_up_alert_with_no_selected_passes(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        conf_engine = self.driver.find_element(By.CSS_SELECTOR, ".copyright > strong:nth-child(6) > a:nth-child(1)")
        self.assertTrue(conf_engine)
        set_up_alert = driver.find_element(By.CSS_SELECTOR, "#price_alert")
        self.assertTrue(set_up_alert)
        action = ActionChains(driver)
        action.move_to_element(set_up_alert).perform()
        set_up_alert.click()
        pop_up = driver.find_element(By.CSS_SELECTOR, "#price_alert_error > div:nth-child(1)")
        self.assertTrue(pop_up)
        time.sleep(2)

        driver.save_screenshot("missing_selection.png")
        time.sleep(5)

    def test_set_up_alert_with_selected_passes(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        drop_down = driver.find_element(By.CSS_SELECTOR, "#confseat-1621")
        self.assertTrue(drop_down)
        drop_down.click()
        time.sleep(2)
        hidden_option = driver.find_element(By.CSS_SELECTOR, "#confseat-1621 > option:nth-child(2)")
        self.assertTrue(hidden_option)
        hidden_option.click()
        time.sleep(2)
        set_up_alert = driver.find_element(By.CSS_SELECTOR, "#price_alert")
        self.assertTrue(set_up_alert)
        action = ActionChains(driver)
        action.move_to_element(set_up_alert).perform()
        set_up_alert.click()
        pop_up = driver.find_element(By.CSS_SELECTOR, "#price_alert_info > div:nth-child(1)")
        self.assertTrue(pop_up)
        time.sleep(2)
        enter_email_field = driver.find_element(By.CSS_SELECTOR, "#email_id")
        self.assertTrue(enter_email_field)
        enter_email_field.send_keys("example@gmail.com")
        button = driver.find_element(By.CSS_SELECTOR, "#price_alert_submit")
        self.assertTrue(button)
        button.click()
        time.sleep(2)

        driver.save_screenshot("notification_is_sent.png")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
