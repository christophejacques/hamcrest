# -- FILE: features/environment.py
from behave import use_step_matcher

# -- SELECT DEFAULT STEP MATCHER: Use "re" matcher as default.
# use_step_matcher("parse")
# use_step_matcher("cfparse")
use_step_matcher("re")
