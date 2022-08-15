package com.revature.steps;

import com.revature.pages.LoginPage;
import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.time.Duration;

public class LoginStudent {
    public LoginPage loginPage;

    @Given("I am at the student login page")
    public void i_am_at_the_student_login_page() {
        TestRunner.driver.get("http://ec2-54-164-157-51.compute-1.amazonaws.com/");
        loginPage = new LoginPage(TestRunner.driver);
        loginPage.clickStudentLoginButton();
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
        wdw.until(ExpectedConditions.urlToBe("http://ec2-54-164-157-51.compute-1.amazonaws.com/s_login.html"));
    }

    @When("I type in a susername of {string}")
    public void i_type_in_a_valid_username_of(String susername) {
        loginPage.stypeUsername(susername);
    }

    @When("I type in a spassword of {string}")
    public void i_type_in_a_valid_password_of(String spassword) {
        loginPage.stypePassword(spassword);
    }

    @When("I click the slogin button")
    public void i_click_the_login_button() {
        loginPage.sclickLoginButton();
    }

    @Then("I should be redirected to the student homepage")
    public void i_should_be_redirected_to_the_student_homepage() {
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
        wdw.until(ExpectedConditions.urlToBe("http://ec2-54-164-157-51.compute-1.amazonaws.com/s_homepage.html"));
        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://127.0.0.1:5500/s_homepage.html");
    }

    @Then("I should stay on the student login page")
    public void i_should_stay_on_the_student_login_page() {
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(2));
        wdw.until(ExpectedConditions.urlToBe("http://ec2-54-164-157-51.compute-1.amazonaws.com/s_login.html"));
        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://ec2-54-164-157-51.compute-1.amazonaws.com/s_login.html");
    }

}
