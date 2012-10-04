from zope.formlib import form
from plone.app.users.browser.register import RegistrationForm
from criticalcommons.skin.browser.interfaces import IMyRegistrationForm
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.component.hooks import getSite
from zope.component import getUtility
from Products.CMFCore.utils import getToolByName
from criticalcommons.content import _

class MyRegistrationForm(RegistrationForm):
    """ Subclass the standard registration form
    """

    implements(IMyRegistrationForm)

    template = ViewPageTemplateFile('templates/register_form.pt')

    @property
    def form_fields(self):
        myfields = super(MyRegistrationForm, self).form_fields
        return myfields


    @form.action(_(u'label_register', default=u'Register'),
                 validator='validate_registration', name=u'register')
    def action_join(self, action, data):
        self.handle_join_success(data)
        if data['usertype'] == u'Advanced User':
            portal = getSite()
            mail_host = getToolByName(portal, 'MailHost')
            sender = data['email']
            mto = portal.getProperty('email_from_address')

            subject = 'User: ' + data['username'] + ' requested advanced status'
            message = 'Hi. The user ' + data['username'] + 'has requested to become an advanced user' + '\n\n'
            message += '\n\n' + 'Visit the user overview to grant the role:' + portal.absolute_url() + '/@@usergroup-userprefs' + '\n\n'
            mail_host.send(message, mto, sender, subject, charset='utf-8')
        
        # XXX Return somewhere else, depending on what
        # handle_join_success returns?
        return self.context.unrestrictedTraverse('registered')()
