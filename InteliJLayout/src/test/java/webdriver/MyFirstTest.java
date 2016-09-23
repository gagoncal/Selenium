package webdriver;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

/**
 * Created by gabrielgoncalves on 21/09/16.
 */
public class MyFirstTest {

    @Test
    public void startWebDriver{

        WebDriver driver = new FirefoxDriver();
        driver.navigate().to('http://seleniumsimplified.com/');
        Assert.assertTrue("title should start with selenium simplified",
                driver.getTitle().startsWith("Selenium simplified"));
        driver.close();
        driver.quit();
    }



}
