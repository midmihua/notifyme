import requests as r
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SearchBy:

    @staticmethod
    def get_by_url(**kwargs):
        try:
            return {
                'result': r.get(kwargs['url']).json()[kwargs['param']]
            }
        except RuntimeError as ex:
            return {
                'result': ex
            }

    @staticmethod
    def get_by_non_ui_mode(**kwargs):
        try:

            # Setup non ui chrome mode
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(os.getcwd() + '/chromedriver', chrome_options=options)
            driver.maximize_window()

            # Get data
            driver.get(kwargs['url'])
            driver.find_element_by_xpath('//*[@id="input_2"]').send_keys(kwargs['_address'])
            query = driver.find_element_by_xpath('//*[@id="btn_2"]')
            query.click()

            # Wait element to be displayed
            time.sleep(kwargs['delay'])
            if driver.find_element_by_xpath('//*[@id="myanswer_2"]').is_displayed():
                return {
                    'result': str(driver.find_element_by_xpath('//*[@id="myanswer_2"]').text).split()[-1]
                }
        except RuntimeError as ex:
            return {
                'result': ex
            }
        finally:
            driver.quit()

    @staticmethod
    def parse(variant, **kwargs):
        if variant == 1:
            return SearchBy.get_by_url(**kwargs)
        elif variant == 2:
            return SearchBy.get_by_non_ui_mode(**kwargs)
