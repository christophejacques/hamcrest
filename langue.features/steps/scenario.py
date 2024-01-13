from behave import given, when, then
from browser import Browser


@given(u'Le navigateur est ouvert sur le site "{site}"')
def le_navigateur_est_ouvert_sur_site(context, site):
    if hasattr(context, "navigateur"):
        return
    context.navigateur = Browser()
    context.navigateur.open(site)


# Francais.feature
# ----------------
@given("j'ouvre le navigateur")
def given_ouvrir_le_navigateur(context):
    when_ouvrir_le_navigateur(context)


@when("j'ouvre le navigateur")
def when_ouvrir_le_navigateur(context):
    context.navigateur = Browser()


@given("le navigateur est ouvert (sinon l'ouvrir)")
def le_navigateur_est_ouvert(context):
    if hasattr(context, "navigateur"):
        assert Browser.is_connected()
        return

    context.navigateur = Browser()


@when('je me rends sur la page web "{url}"')
def when_se_rendre_sur_la_page_web(context, url):
    then_se_rendre_sur_la_page_web(context, url)


@then('je me rends sur la page web "{url}"')
def then_se_rendre_sur_la_page_web(context, url):
    context.navigateur.open(url)


@then("la page web est ouverte")
def page_web_ouverte(context):
    assert context.navigateur.is_connected()


@given(u'l\'utilisateur est connecte au site "{site}"')
def given_utilisateur_connecte_site(context, site):
    when_utilisateur_connecte_site(context, site)


@when(u'l\'utilisateur est connecte au site "{site}"')
def when_utilisateur_connecte_site(context, site):
    assert hasattr(context, "navigateur")
    print(site, "<=!=>", context.navigateur.get())
    assert site == context.navigateur.get()


@then(u'l\'utilisateur est connecte au site "{site}"')
def then_utilisateur_connecte_site(context, site):
    when_utilisateur_connecte_site(context, site)


@then(u'se deconnecter')
def se_deconnecter(context):
    assert context.navigateur.is_connected()
    context.navigateur.close()


@given(u'un utilisateur admin')
def utilisateur_admin(context):
    pass


@given(u'L\'utilisateur est connecte')
def utilisateur_connecte(context):
    pass


@then(u'afficher un message')
def afficher_message(context):
    pass
