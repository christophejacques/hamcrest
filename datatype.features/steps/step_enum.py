# file:datatype.features/steps/step_enum.py
# ------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ------------------------------------------------------------------------
from behave import register_type
from parse_type import TypeBuilder

# -- ENUM: Returns True (for "yes" and "jubilee"), False (for "no")
parse_yesno = TypeBuilder.make_enum({"yes": True, "no": False, "jubilee": True})
register_type(YesNo=parse_yesno)


# file:datatype.features/steps/step_enum.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import when, then
from hamcrest import assert_that, equal_to
# ------------------------------------------------------------------------
# DOMAIN MODEL:
# ------------------------------------------------------------------------
answer_oracle = {
    "Do you love me?": True,
    "Do you hate me?": False,
    "Do you kiss me?": True,
}


@when(u'Romeo asks Julia: "{question}"')
def step_when_romeo_asks_julia(context, question):
    context.question = question


@then(u'the answer is "{answer:YesNo}"')
def step_then_the_answer_is(context, answer):
    assert_that(answer, equal_to(answer_oracle.get(context.question, None)))
