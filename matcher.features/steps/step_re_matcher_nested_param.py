# file:step_matcher.features/steps/step_re_matcher_nested_param.py
# -----------------------------------------------------------------------------
# STEPS: With "re" matcher
# -----------------------------------------------------------------------------
from behave import use_step_matcher, when
use_step_matcher("re")


# -- NESTED GROUP:
@when(u'I try to match nested "(?P<foo>foo(?P<bar>bar)?)"')
def step_when_I_try_to_match_nested_foobar(context, foo, bar):
    context.foo = foo
    context.bar = bar


# -- SIMPLE GROUP: anything else
@when(u'I try to match nested "(?P<anything>.*)"')
def step_when_I_try_to_match_anything_else(context, anything):
    context.anything = anything
