//package com.revature.steps;
//
//import com.revature.pages.StudentHomepage;
//import com.revature.pages.TeacherHomepage;
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
//public class TFilterAssignments {
//
//    public TeacherHomepage teacherHomepage;
//
//    @Given("I am at the teacher homepage #3")
//    public void i_am_at_the_teacher_homepage() {
//        TestRunner.driver.get("http://127.0.0.1:5500/t_homepage.html");
//        teacherHomepage = new TeacherHomepage(TestRunner.driver);
//    }
//
//    @When("I click on View All Assignments #4")
//    public void i_click_on_view_all_assignments() {
//        teacherHomepage.clickViewAssignments();
//    }
//
//    @When("I click on the filter dropdown and select Science #2")
//    public void i_click_on_the_filter_dropdown_and_select_Science() {
//        WebElement filter = TestRunner.driver.findElement(By.id("status-filter"));
//        Select scienceTag = new Select(filter);
//        scienceTag.selectByValue("science");
//    }
//
//    @Then("I can see only assignments for the Science course #2")
//    public void i_can_see_only_assignments_for_the_science_course() {
//        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
//        wdw.until(ExpectedConditions.urlToBe("http://127.0.0.1:5500/t_view_assignments.html"));
//        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://127.0.0.1:5500/t_view_assignments.html");
//    }
//
//}
