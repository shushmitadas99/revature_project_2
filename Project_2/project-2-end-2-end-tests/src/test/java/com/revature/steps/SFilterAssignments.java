package com.revature.steps;

import com.revature.pages.StudentHomepage;
import com.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.time.Duration;

import static java.lang.Thread.sleep;

public class SFilterAssignments {

    public StudentHomepage studentHomepage;

    @Given("I am at the student homepage #3")
    public void i_am_at_the_student_homepage() {
        TestRunner.driver.get("http://127.0.0.1:5500/s_homepage.html");
        studentHomepage = new StudentHomepage(TestRunner.driver);
    }

    @When("I click on View All Assignments #2")
    public void i_click_on_view_all_assignments() {
        studentHomepage.clickViewAssignments();
    }

    @When("I click on the filter dropdown and select Science")
    public void i_click_on_the_filter_dropdown_and_select_Science() {
        WebElement filter = TestRunner.driver.findElement(By.id("status-filter"));
        Select scienceTag = new Select(filter);
        scienceTag.selectByValue("science");
    }

    @Then("I can see only assignments for the Science course")
    public void i_can_see_only_assignments_for_the_science_course() {
        WebDriverWait wdw = new WebDriverWait(TestRunner.driver, Duration.ofSeconds(10));
        wdw.until(ExpectedConditions.urlToBe("http://127.0.0.1:5500/s_view_assignments.html"));
        Assert.assertEquals(TestRunner.driver.getCurrentUrl(), "http://127.0.0.1:5500/s_view_assignments.html");
    }

}
