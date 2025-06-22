# file:features/steps/step_tutorial01.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from behave.runner import Context
from hamcrest import assert_that, is_, equal_to, instance_of, not_none, none


@given('we have behave installed')
def step_impl_given(context):
    print("Behave installed")
    assert_that(context, is_(not_none()))
    assert_that(context, is_(instance_of(Context)))


@when('we implement a test')
def step_impl_when(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl_then(context):
    assert_that(context.failed, is_(False))
