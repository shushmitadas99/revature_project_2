package com.revature.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class StudentHomepage {

    private WebDriver driver;
    private WebDriverWait wdw;

    @FindBy(id="viewC")
    private WebElement sViewCourses;
    @FindBy(id="viewA")
    private WebElement sViewAssignments;
    @FindBy(id="submitA")
    private WebElement sSubmitAssignment;
    @FindBy(id="viewP")
    private WebElement sViewSProfile;

    public StudentHomepage(WebDriver driver) {
        this.driver = driver;
        this.wdw = new WebDriverWait(driver, Duration.ofSeconds(10));
        PageFactory.initElements(driver, this);
    }

    public void clickViewC () {
        sViewCourses.click();
    }

    public void clickViewAssignments () {
        sViewAssignments.click();
    }

    public void clickSubmitAssignment () {
        sSubmitAssignment.click();
    }

    public void clickViewSProfile () {
        sViewSProfile.click();
    }
}
