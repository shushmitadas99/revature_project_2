package com.revature.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class TeacherHomepage {
        private WebDriver driver;
        private WebDriverWait wdw;

        @FindBy(id="viewC")
        private WebElement tViewCourses;
        @FindBy(id="viewA")
        private WebElement tViewAssignments;
        @FindBy(id="gradeA")
        private WebElement gradeAssignment;
        @FindBy(id="viewP")
        private WebElement viewTProfile;

        public TeacherHomepage(WebDriver driver) {
            this.driver = driver;
            this.wdw = new WebDriverWait(driver, Duration.ofSeconds(10));
            PageFactory.initElements(driver, this);
        }

        public void clickViewC () {
            tViewCourses.click();
        }

        public void clickViewAssignments () {
            tViewAssignments.click();
        }

        public void clickGradeAssignment () {
            gradeAssignment.click();
        }

        public void clickViewSProfile () {
            viewTProfile.click();
        }
}

