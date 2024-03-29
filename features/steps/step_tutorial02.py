from behave import given, when, then
from hamcrest import assert_that, equal_to, is_not
from ninja_fight import NinjaFight


# file:features/steps/step_tutorial02.py
# ----------------------------------------------------------------------------
# BACKGROUND-STEPS: Needed for tutorial09
# ----------------------------------------------------------------------------
@given('the ninja encounters another opponent')
def step_the_ninja_encounters_another_opponent(context):
    """
    BACKGROUND steps are called at begin of each scenario before other steps.
    """
    # -- SETUP/TEARDOWN:
    if hasattr(context, "ninja_fight"):
        # -- VERIFY: Double-call does not occur.
        assert_that(context.ninja_fight, is_not(equal_to(None)))
    context.ninja_fight = None


# file:features/steps/step_tutorial02.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
@given('the ninja has a {achievement_level}')
def step_the_ninja_has_a(context, achievement_level):
    context.ninja_fight = NinjaFight(achievement_level)


@when('attacked by a {opponent_role}')
def step_attacked_by_a(context, opponent_role):
    context.ninja_fight.opponent = opponent_role


@when('attacked by {opponent}')
def step_attacked_by(context, opponent):
    context.ninja_fight.opponent = opponent


@then('the ninja should {reaction}')
def step_the_ninja_should(context, reaction):
    assert_that(reaction, equal_to(context.ninja_fight.decision()))


