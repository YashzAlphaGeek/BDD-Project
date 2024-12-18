Feature: CI/CD Pipeline Integration

  Scenario: Successful deployment in a retail application
    Given Namita configures the CI/CD pipeline with version control integration
    When the code is pushed to the repository
    Then the application should be deployed successfully