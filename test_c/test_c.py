from selenium import webdriver
import time

# options
options = webdriver.ChromeOptions()

# headless mode
options.headless = True

driver = webdriver.Chrome(executable_path='/Users/evgeniyasipkov/Desktop/Python/testirovanie/test_c/chromedriver',
                          options=options)


def web_interface(url):
    try:
        driver.get(url=url)
        time.sleep(1)
        input_values = driver.find_element_by_id('argumentConv')
        input_values.clear()
        input_values.send_keys('1')
        time.sleep(1)
        result = driver.find_element_by_id('answer').text
        result = result[result.find("=") + 2:]
        return result
    except Exception as ex:
        print(ex)
    finally:
        # driver.close() - urllib3.exceptions.MaxRetryError
        # driver.quit() - urllib3.exceptions.MaxRetryError
        pass


def test_celsius_fahrenheit():
    url_celsius = 'https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm'
    result = web_interface(url_celsius)
    result_fahrenheit = '33.80000°F'
    assert result == result_fahrenheit, """1°C= 33.80000°F"""


def test_meters_feet():
    url_meters = 'https://www.metric-conversions.org/length/meters-to-feet.htm'
    result = web_interface(url_meters)
    result_feet = '3ft 3.370079in'
    assert result == result_feet, """1m= 3ft 3.370079in"""


def test_ounces_grams():
    url_ounces = 'https://www.metric-conversions.org/weight/ounces-to-grams.htm'
    result = web_interface(url_ounces)
    result_grams = '28.34952g'
    assert result == result_grams, """1oz= 28.34952g"""


