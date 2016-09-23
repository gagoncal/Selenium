import org.junit.Test;

import static org.junit.Assert.assertTrue;
/**
 * Created by gabrielgoncalves on 22/09/16.
 */

public class MyFirstTest {
    @Test
    public void goToWebPage()
    {
        Webdriver driver = new FirefoxDriver();
        driver.get("http://the-internet.herokuapp.com");
        assertTrue(driver.getTitle().equals("The Internet"));
        driver.quit();
    }
}
