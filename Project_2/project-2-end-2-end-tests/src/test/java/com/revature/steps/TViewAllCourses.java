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

public class TViewAllCourses {

    public TeacherHomepage teacherHomepage;

    @Given("I am at the teacher homepage #2")
    public void i_am_at_the_teacher_homepage() {
        TestRunner.driver.get("http://127.0.0.1:5500/t_homepage.html");
        teacherHomepage = new TeacherHomepage(TestRunner.driver);
    }

    @When("I click on View All Courses #2")
    public void i_click_on_view_all_courses() {
        teacherHomepage.clickViewC();
    }

    @Then("I will see all the courses I am currently teaching")
    public void i_will_see_all_the_courses_I_am_currently_teaching() {
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
        wdw.until(ExpectedConditions.urlToBe("http://127.0.0.1:5500/t_view_courses.html"));
        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://127.0.0.1:5500/t_view_courses.html");
    }
}
