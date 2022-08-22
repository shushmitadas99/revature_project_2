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

import java.time.Duration;

public class LoginTeacher {

    public LoginPage loginPage;

    @Given("I am at the teacher login page")
    public void i_am_at_the_teacher_login_page() {
        TestRunner.driver.get("http://127.0.0.1:5500/index.html");
        loginPage = new LoginPage(TestRunner.driver);
        loginPage.clickTeacherLoginButton();
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
        wdw.until(ExpectedConditions.urlToBe("http://127.0.0.1:5500/t_login.html"));
    }

    @When("I type in a tusername of {string}")
    public void i_type_in_a_valid_tusername_of(String tusername) {
        loginPage.ttypeUsername(tusername);
    }

    @When("I type in a tpassword of {string}")
    public void i_type_in_a_valid_tpassword_of(String tpassword) {
        loginPage.ttypePassword(tpassword);
    }

    @When("I click the tlogin button")
    public void i_click_the_tlogin_button() {
        loginPage.tclickLoginButton();
    }

    @Then("I should be redirected to the teacher homepage")
    public void i_should_be_redirected_to_the_teacher_homepage() {
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
        wdw.until(ExpectedConditions.urlToBe("http://127.0.0.1:5500/t_homepage.html"));
        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://127.0.0.1:5500/t_homepage.html");
    }

    @Then("I should stay on the teacher login page")
    public void i_should_stay_on_the_teacher_login_page() {
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(2));
        wdw.until(ExpectedConditions.urlToBe("http://127.0.0.1:5500/t_login.html"));
        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://127.0.0.1:5500/t_login.html");
    }
}
