from android_utils import android_get_desired_capabilities
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

cap = android_get_desired_capabilities()

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities= cap)
driver.implicitly_wait(30)
try:
    driver.find_element(by= AppiumBy.CLASS_NAME, value='android.widget.Button').click()
    log= driver.find_element(by= AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText")
    log.send_keys("qa.ajax.app.automation@gmail.com")
    log= driver.find_element(by= AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText")
    log.send_keys("qa_automation_password")
    driver.find_element(by= AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView').click()
    driver.implicitly_wait(30)
    driver.quit()
except:
    driver.quit()
    
# driver.execute_script('mobile: performEditorAction',{'action': 'search'})

# go, search, send,next, done, previous