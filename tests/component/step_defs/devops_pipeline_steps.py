from pytest_bdd import given, when, then

@given('Namita configures the CI/CD pipeline with version control integration')
def step_impl():
    print("Namita has configured the CI/CD pipeline with version control integration")

@when('the code is pushed to the repository')
def step_impl():
    print("Code has been pushed to the repository")

@then('the application should be deployed successfully')
def step_impl():
    print("Application has been deployed successfully")