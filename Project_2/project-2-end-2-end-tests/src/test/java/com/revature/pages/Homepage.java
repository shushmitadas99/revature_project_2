package com.revature.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Homepage {

    private WebDriver driver;

    private WebDriverWait wdw;

    @FindBy(id="sBtn")
    private WebElement studentLoginButton;

    @FindBy(id="tBtn")
    private WebElement teacherLoginButton;

    public void clickStudentLoginButton () {
        studentLoginButton.click();
    }

    public void clickTeacherLoginButton () {
        teacherLoginButton.click();
    }
}
