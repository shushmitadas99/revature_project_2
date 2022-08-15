package com.revature.steps;

import com.revature.pages.StudentHomepage;
import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import java.time.Duration;

public class SViewAllAssignments {

    public StudentHomepage studentHomepage;

    @Given("I am at the student homepage")
    public void i_am_at_the_student_homepage() {
        TestRunner.driver.get("http://ec2-54-164-157-51.compute-1.amazonaws.com/s_homepage.html");
        studentHomepage = new StudentHomepage(TestRunner.driver);
    }

    @When("I click on View All Assignments")
    public void i_click_on_view_all_assignments() {
        studentHomepage.clickViewAssignments();
    }

    @Then("I should see all the submitted assignments for the student")
    public void i_should_see_all_the_submitted_assignments_for_the_student() {
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
        wdw.until(ExpectedConditions.urlToBe("http://ec2-54-164-157-51.compute-1.amazonaws.com/s_view_assignments.html"));
        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://ec2-54-164-157-51.compute-1.amazonaws.com/s_view_assignments.html");
    }

}
