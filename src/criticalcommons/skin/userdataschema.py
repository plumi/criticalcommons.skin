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

    fullname = schema.TextLine(
        title=_(u'label_full_name', default=u'Full Name'),
        description=_(u'help_full_name_creation',
                      default=u"Enter full name, example John Smith."),
        required=True)

    user_title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    institution = schema.TextLine(
        title=_(u'Institution'),
        required=False,
    )

    accept = schema.Bool(
        title=_(u'label_accept', default=u'Accept terms of use'),
        description=_(u'help_accept',
                      default=u"Tick this box to indicate that you have found,"
                      " read and accepted the Terms of Service. "),
        required=True,
        constraint=validateAccept,
        )
