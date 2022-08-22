//package com.revature.steps;//package com.revature.steps;
////
////import com.revature.pages.StudentHomepage;
//import com.revature.pages.StudentHomepage;
//import com.revature.runner.TestRunner;
//import io.cucumber.java.en.Given;
//import io.cucumber.java.en.Then;
//import io.cucumber.java.en.When;
//import org.openqa.selenium.By;
//import org.openqa.selenium.WebElement;
//import org.openqa.selenium.support.ui.ExpectedConditions;
//import org.openqa.selenium.support.ui.Select;
//import org.openqa.selenium.support.ui.WebDriverWait;
//import org.testng.Assert;
//
//import java.time.Duration;
//
//public class  SSubmitAssignment {
//
//    public StudentHomepage studentHomepage;
//
//    @Given("I am at the student homepage #4")
//    public void i_am_at_the_student_homepage() throws InterruptedException {
//        TestRunner.driver.get("http://127.0.0.1:5500/s_homepage.html");
//        studentHomepage = new StudentHomepage(TestRunner.driver);
//        Thread.sleep(2000);
//    }
//
//    @When("I click on Submit Assignment")
//    public void i_click_on_submit_assignment() throws InterruptedException {
//        studentHomepage.clickSubmitAssignment();
//        Thread.sleep(2000);
//    }
//    @When("I click the checkbox for submit assignment")
//    public void i_click_checkbox_for_submit_assignment() throws InterruptedException {
//        WebElement checkbox = TestRunner.driver.findElement(By.id("1"));
//        checkbox.click();
//        Thread.sleep(2000);
//    }
//    @Then("I have successfully submitted an assignment")
//    public void i_have_successfully_submitted_an_assignment() throws InterruptedException {
//        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
//        wdw.until(ExpectedConditions.urlToBe("http://127.0.0.1:5500/s_submit_assignment.html"));
//        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://127.0.0.1:5500/s_submit_assignment.html");
//        Thread.sleep(2000);
//    }
//
//}
