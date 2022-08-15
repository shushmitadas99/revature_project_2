package com.revature.steps;

import com.revature.pages.StudentHomepage;
import com.revature.pages.TeacherHomepage;
import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import java.time.Duration;

public class TViewAllAssignments {

    public TeacherHomepage teacherHomepage;

    @Given("I am at the teacher homepage")
    public void i_am_at_the_teacher_homepage() {
        TestRunner.driver.get("http://ec2-54-164-157-51.compute-1.amazonaws.com/t_homepage.html");
        teacherHomepage = new TeacherHomepage(TestRunner.driver);
    }

    @When("I click on View All Assignments #3")
    public void i_click_on_view_all_assignments() {
        teacherHomepage.clickViewAssignments();
    }

    @Then("I will see all the submitted assignments")
    public void i_will_see_all_the_submitted_assignments() {
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
        wdw.until(ExpectedConditions.urlToBe("http://ec2-54-164-157-51.compute-1.amazonaws.com/t_view_assignments.html"));
        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://ec2-54-164-157-51.compute-1.amazonaws.com/t_view_assignments.html");
    }
}
