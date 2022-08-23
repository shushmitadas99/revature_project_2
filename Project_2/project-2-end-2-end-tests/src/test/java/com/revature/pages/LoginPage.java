package com.revature.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import javax.xml.ws.WebEndpoint;
import java.time.Duration;

public class LoginPage {

    private WebDriver driver;
    private WebDriverWait wdw;

    @FindBy(id="sBtn")
    private WebElement studentLoginButton;
    @FindBy(id="s-username-login-input")
    private WebElement susernameInput;
    @FindBy(id="s-password-login-input")
    private WebElement spasswordInput;
    @FindBy(id="s-login-btn")
    private WebElement sloginButton;

    @FindBy(id="tBtn")
    private WebElement teacherLoginButton;
    @FindBy(id="t-username-login-input")
    private WebElement tusernameInput;
    @FindBy(id="t-password-login-input")
    private WebElement tpasswordInput;
    @FindBy(id="t-login-btn")
    private WebElement tloginButton;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
        this.wdw = new WebDriverWait(driver, Duration.ofSeconds(10));
        PageFactory.initElements(driver, this);
    }

    public void clickStudentLoginButton () {
        studentLoginButton.click();
    }
    public void stypeUsername (String susername) {
        susernameInput.sendKeys(susername);
    }
    public void stypePassword (String spassword) {
        spasswordInput.sendKeys(spassword);
    }
    public void sclickLoginButton () {
        sloginButton.click();
    }

    public void clickTeacherLoginButton () {
        teacherLoginButton.click();
    }
    public void ttypeUsername (String username) {
        tusernameInput.sendKeys(username);
    }
    public void ttypePassword (String password) {
        tpasswordInput.sendKeys(password);
    }
    public void tclickLoginButton () {
        tloginButton.click();
    }


}
