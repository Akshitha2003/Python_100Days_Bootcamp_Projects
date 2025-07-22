import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(5)

language_selection = driver.find_element(By.ID, "languageSelectHeader")
if language_selection is not None:
    select_english = driver.find_element(By.ID, "langSelect-EN")
    select_english.click()

time.sleep(2)

cookie = driver.find_element(By.ID, "bigCookie")
time_start = time.time()
timeout_step = 1
while time.time() < time_start + 300:
    cookie.click()
    if int(time.time()) == int(time_start) + 5 * timeout_step:
        products = driver.find_elements(By.CLASS_NAME, "product")
        for product in reversed(products):
            if 'enabled' in product.get_attribute("class"):
                product.click()
                print(f"Purchased: {product.get_attribute('id')}")
                break
        timeout_step += 1

final_per_second = driver.find_element(By.ID, "cookiesPerSecond").text.split()[2]
print(f"Result: {final_per_second}")

driver.quit()
