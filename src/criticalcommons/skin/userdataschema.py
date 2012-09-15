from zope.interface import Interface, implements
from zope import schema

from criticalcommons.content import _
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema

def validateAccept(value):
    if not value == True:
        return False
    return True

class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema

class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    usertype = schema.Choice(
        title=u'User Status',
        values=[u'Basic User', u'Advanced User'],
        default=u'Basic User',
    )

    user_title = schema.TextLine(
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
