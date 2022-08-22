package com.revature.runner;

import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.time.Duration;

@CucumberOptions(glue="com.revature.steps", features={"src/test/resources/login_student.feature",
        "src/test/resources/login_teacher.feature",
        "src/test/resources/student_all_assignments.feature",
        "src/test/resources/student_all_courses.feature",
        "src/test/resources/student_filter_assignments.feature",
        "src/test/resources/teacher_all_assignments.feature",
        "src/test/resources/teacher_all_courses.feature"})
public class TestRunner extends AbstractTestNGCucumberTests {

    public static WebDriver driver;

    @BeforeMethod
    public void setup() {
        WebDriverManager.chromedriver().setup();

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");

        driver = new ChromeDriver(options);
    }

    @AfterMethod
    public void quit() {
        driver.quit();
    }

}
