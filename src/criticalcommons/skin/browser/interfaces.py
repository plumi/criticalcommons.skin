from plonetheme.classic.browser.interfaces import IThemeSpecific as IClassicTheme
from zope.viewlet.interfaces import IViewletManager
from zope.interface import Interface

class IThemeSpecific(IClassicTheme):
    """theme-specific layer"""

class IAddCommentary(IViewletManager):
    """ A viewlet manager to display the commentary form  """

class IMyRegistrationForm(Interface):
    """Marker interface for my custom registration form
    """

