# file:features/steps/step_tutorial01.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we have behave installed')
def step_impl_given(context):
    print("Behave installed")


@when('we implement a test')
def step_impl_when(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl_then(context):
    assert context.failed is False
