from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# ==========================================================
# YOUR STREAMLIT URL
# ==========================================================
STREAMLIT_URL = "https://periop-command.streamlit.app/"

# ==========================================================
# DRIVER
# ==========================================================
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


def app_loaded():
    """
    Returns True if the app appears to be loaded.
    """
    source = driver.page_source.lower()

    if "streamlit" in source:
        return True

    if "this app has gone to sleep" in source:
        return False

    if "yes, get this app back up" in source:
        return False

    return True


try:

    print(f"Opening {STREAMLIT_URL}")

    driver.get(STREAMLIT_URL)

    wait = WebDriverWait(driver, 90)

    # -----------------------------------------------------
    # Try to click wake button
    # -----------------------------------------------------

    try:

        button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(.,'Yes, get this app back up')]"
                )
            )
        )

        print("Wake button found.")

        button.click()

        print("Clicked wake button.")

    except TimeoutException:

        print("Wake button not found.")
        print("App may already be awake or still starting.")

    # -----------------------------------------------------
    # Wait for app
    # -----------------------------------------------------

    MAX_WAIT = 180

    start = time.time()

    while time.time() - start < MAX_WAIT:

        time.sleep(10)

        driver.refresh()

        print("Checking app...")

        if app_loaded():

            print("App is awake ✅")

            break

    else:

        raise Exception("App failed to wake within 3 minutes.")

    print("Success!")

except Exception as e:

    print(f"ERROR: {e}")

    raise

finally:

    driver.quit()

    print("Driver closed.")
