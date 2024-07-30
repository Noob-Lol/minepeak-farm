import time, os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

script_path = os.path.abspath(os.path.dirname(__file__))
options=webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-gpu')
extensions_path = os.path.expandvars('%LOCALAPPDATA%/Google/Chrome/User Data/Default/Extensions')
required_extensions=['cjpalhdlnbpafiamejdnhcphjbkeiagm','jinjaccalgkegednnccohejagnlnfdag']
all_extensions = ','.join(os.path.join(extensions_path, ext, os.listdir(os.path.join(extensions_path, ext))[0]) for ext in required_extensions)
options.add_argument(f'--load-extension={all_extensions}')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
start_time = 0.0
ub_filters = '''
dashboard.minepeakhosting.com###sidebar
dashboard.minepeakhosting.com##.flex-row.d-flex.fixed-top.p-0.navbar
dashboard.minepeakhosting.com##.footer
'''

with webdriver.Chrome(options=options) as driver:
    actions = ActionChains(driver)
    try:
        driver.get('https://dashboard.minepeakhosting.com/lv')
        try:
            WebDriverWait(driver, 120).until(EC.url_to_be('https://dashboard.minepeakhosting.com/lv'))
            print('Auto started! Press Ctrl+C to exit.')
        except TimeoutException:
            input('Timed out! Press Enter to start farm.')
            print('Script started, press Ctrl+C to exit.')
        driver.get('https://codeberg.org/Amm0ni4/bypass-all-shortlinks-debloated/raw/branch/main/Bypass_All_Shortlinks.user.js')
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL,Keys.ENTER)
        time.sleep(1)
        driver.get("chrome-extension://cjpalhdlnbpafiamejdnhcphjbkeiagm/dashboard.html#1p-filters.html")
        time.sleep(1)
        actions.send_keys(ub_filters).perform()
        actions.key_down(Keys.CONTROL).send_keys("s").key_up(Keys.CONTROL).perform()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.minimize_window()
        start_time = time.time()
        coin_count = 0
        while True:
            try:
                driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg").click()
                WebDriverWait(driver, 15,0.2).until(EC.url_to_be('https://dashboard.minepeakhosting.com/lv?success=true'))
                coin_count += 30
            except Exception as e:
                print(e)
                input('Caught an error, press Enter to continue.')
                continue
    except KeyboardInterrupt:
        run_duration = time.time() - start_time
        print('Script stopped, exiting...')
    except Exception as e:
        print(e)
        input('Crashed, press Enter to exit.')
    if start_time == 0.0:
        print('Script wasnt started.')       
    else:
        run_duration = time.time() - start_time
        print(f'Run time: {run_duration:.2f} seconds, earned {coin_count} coins.')
