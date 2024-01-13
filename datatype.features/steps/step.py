# -- FILE: features/environment.py (location 1, global types)
#    FILE: features/steps/step.py  (location 2, more locally used types)
# ------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ------------------------------------------------------------------------
from behave import register_type
from parse_type import TypeBuilder


# -- CHOICE2: Constrain to a list of supported items (as string).
offered_shop_items = ["apples", "beef", "potatoes", "pork"]
parse_shop_item2 = TypeBuilder.make_choice2(offered_shop_items)
register_type(ShopItem2=parse_shop_item2)


# -- FILE: features/steps/step.py
# ------------------------------------------------------------------------
# STEPS:
# ------------------------------------------------------------------------
from behave import given


@given("I buy {shop_item:ShopItem2}")
def step_impl(context, shop_item):
    # EXAMPLE: "potatoes" => (selected_index=2, selected_text="potatoes")
    selected_index, selected_text = shop_item
    assert 0 <= selected_index < len(offered_shop_items)
    shop_item_id = context.shop.shop_item_index2id(selected_index)
    context.shopping_cart.append(shop_item_id)
