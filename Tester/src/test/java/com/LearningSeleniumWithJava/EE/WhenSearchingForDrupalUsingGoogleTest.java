package com.LearningSeleniumWithJava.EE;/*
  Created by gabrielgoncalves on 22/09/16.
 */

import Pages.GooglePage;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.io.IOException;

public class WhenSearchingForDrupalUsingGoogleTest {
    private String baseUrl;
    private WebDriver driver;
    private GooglePage.ScreenshotHelper screenshotHelper;
    private GooglePage.WaitForElement waitForElement
    private String CSSForText = "div[class='hdtb-mitem hdtb-msel hdtb-imb']"

    @Before
    public void openBrowser() {
        baseUrl = "https://www.google.pt/";
        driver = new ChromeDriver();
        driver.get(baseUrl);
        screenshotHelper = new GooglePage.ScreenshotHelper();
    }

    @After
    public void saveScreenshotAndCloseBrowser() throws IOException {
        screenshotHelper.saveScreenshot("screenshot.png");
        driver.quit();
    }

    @Test
    public void pageTitleAfterSearchShouldBeginWithDrupal() throws IOException {
        Assert.assertEquals("The page title should equal Google at the start of the test.", "Google", driver.getTitle());
        WebElement searchField = driver.findElement(By.name("q"));
        searchField.sendKeys("Drupal!");
        searchField.submit();
        waitForElement = WaitForElements.isElementLoaded(CSSForText);
        Assert.assertTrue(driver.getTitle().contains("Drupal"));

    }

}
