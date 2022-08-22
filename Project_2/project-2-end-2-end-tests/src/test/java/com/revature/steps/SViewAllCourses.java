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

public class SViewAllCourses {

    public StudentHomepage studentHomepage;

    @Given("I am at the student homepage #2")
    public void i_am_at_the_student_homepage() {
        TestRunner.driver.get("http://127.0.0.1:5500/s_homepage.html");
        studentHomepage = new StudentHomepage(TestRunner.driver);
    }

    @When("I click on View All Courses")
    public void i_click_on_view_all_courses() {
        studentHomepage.clickViewC();
    }

    @Then("I should see all the courses for the student")
    public void i_should_see_all_the_courses_for_the_student() {
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
        wdw.until(ExpectedConditions.urlToBe("http://127.0.0.1:5500/s_view_courses.html"));
        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://127.0.0.1:5500/s_view_courses.html");
    }

}
