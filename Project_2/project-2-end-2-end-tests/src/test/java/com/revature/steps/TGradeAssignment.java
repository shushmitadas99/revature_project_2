//package com.revature.steps;
//
//import com.revature.pages.TeacherHomepage;
//import com.revature.runner.TestRunner;
//import io.cucumber.java.en.Given;
//import io.cucumber.java.en.Then;
//import io.cucumber.java.en.When;
//import org.openqa.selenium.By;
//import org.openqa.selenium.WebElement;
//import org.openqa.selenium.support.ui.ExpectedConditions;
//import org.openqa.selenium.support.ui.WebDriverWait;
//import org.testng.Assert;
//
//import java.time.Duration;
//
//public class TGradeAssignment {
//
//    public TeacherHomepage teacherHomepage;
//
//    @Given("I am at the teacher homepage #3")
//    public void i_am_at_the_teacher_homepage() {
//        TestRunner.driver.get("http://127.0.0.1:5500/t_homepage.html");
//        teacherHomepage = new TeacherHomepage(TestRunner.driver);
//    }
//
//    @When("I click on Grade Assignment")
//    public void i_click_on_grade_assignment() {
//        teacherHomepage.clickGradeAssignment();
//    }
//    @When("I click on a B radio button")
//    public void i_click_checkbox_for_submit_assignment() throws InterruptedException {
//        WebElement radio = TestRunner.driver.findElement(By.cssSelector("input[value='A']"));
//        radio.click();
//    }
//    @Then("I should see the graded assignments")
//    public void i_have_successfully_submitted_an_assignment() throws InterruptedException {
//        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
//        wdw.until(ExpectedConditions.urlToBe("http://127.0.0.1:5500/t_homepage.html"));
//        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://127.0.0.1:5500/t_homepage.html");
//    }
//}
