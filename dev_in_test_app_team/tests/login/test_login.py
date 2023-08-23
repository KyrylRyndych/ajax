def test_user_login(user_login_fixture):
    user_login_fixture.driver.reset()
    login = "qa.ajax.app.automation@gmail.com"
    password = "qa_automation_password"
    element = user_login_fixture.find_element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView")
    user_login_fixture.click_element(element)
    login_field = user_login_fixture.find_element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText")
    password_field = user_login_fixture.find_element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText")
    user_login_fixture.send_keys(obj= login_field, keys=login)
    user_login_fixture.send_keys(obj= password_field, keys=password)
    element = user_login_fixture.find_element('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView')
    user_login_fixture.click_element(element)
    user_login_fixture.driver.implicitly_wait(10)

    element = user_login_fixture.find_element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[1]")
    assert element != False , 'Тест 1 провален'


    
    
def test_user_login_wrong(user_login_fixture):
    user_login_fixture.driver.reset()
    user_login_fixture.driver.implicitly_wait(10)
    login = "qa.ajax.app.automation@gmail.com"
    password = "qa.ajax.app.automation@gmail.com"
    element = user_login_fixture.find_element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.TextView")
    user_login_fixture.click_element(element)
    login_field = user_login_fixture.find_element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText")
    password_field = user_login_fixture.find_element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText")
    user_login_fixture.send_keys(obj= login_field, keys=login)
    user_login_fixture.send_keys(obj= password_field, keys=password)
    try:
        element = user_login_fixture.find_element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[1]")
    except:
        element = True
    assert element != False, 'Тест 2 провален'
    print("Тест успешно пройден")

    
    
