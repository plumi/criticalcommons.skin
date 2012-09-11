from plonetheme.classic.browser.interfaces import IThemeSpecific as IClassicTheme
from zope.viewlet.interfaces import IViewletManager
from zope.interface import Interface
from zope import schema
from criticalcommons.content import _

class IThemeSpecific(IClassicTheme):
    """theme-specific layer"""

class IAddCommentary(IViewletManager):
    """ A viewlet manager to display the commentary form  """

class IMyRegistrationForm(Interface):
    """Marker interface for my custom registration form
    """

class IAdvancedSchema(Interface):

    usertype = schema.Choice(
        title=_(u'User Status'),
        values=[_(u'Basic User'), _(u'Advanced User')],
        default=_(u'Basic User'),
    )

    title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    institution = schema.TextLine(
        title=_(u'Institution'),
        required=False,
    )

    biography = schema.Text(
        title=_(u'Biography'),
        description= _(u"A short overview of who you are and what you do. Will be displayed on the your author page, linked from the items you create."),
        required=False,
    )

    homePage = schema.TextLine(
        title=_(u'Home page'),
        description= _(u"The URL for your external home page, if you have one."),
        required=False,
    )
