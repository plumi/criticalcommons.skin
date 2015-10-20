from zope.formlib import form
from plone.app.users.browser.register import RegistrationForm
from criticalcommons.skin.browser.interfaces import IMyRegistrationForm
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.app.component.hooks import getSite
from zope.component import getUtility
from Products.CMFCore.utils import getToolByName
from criticalcommons.content import _
from five import grok

from zope.app.form.interfaces import WidgetInputError, InputErrors


class MyRegistrationForm(RegistrationForm):
    """ Subclass the standard registration form
    """

    implements(IMyRegistrationForm)

    template = ViewPageTemplateFile('templates/register_form.pt')

    label = _(u"Register")
    description = _(u"To add commentaries to media, please register for a BASIC USER account. These accounts are processed automatically and you can begin commenting immediately. Educators may apply for ADVANCED USER status based on their institutional afiliation. Once approved by site administrators, ADVANCED USERS may upload and download media for classroom instruction. Non-institutionally affiliated applicants for Advanced User status should should get in touch via the Contact form.")

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
            message = "%s of %s , is applying for Advanced User status in Critical Commons.\n\n Home page URL is %s, Username is %s, and email address is %s. \n\n  Visit the User Overview to respond to this request: %s" % (data['user_title'], data['institution'], data['home_page'], data['username'], data['email'], portal.absolute_url() + '/@@usergroup-userprefs' )

            mail_host.send(message, mto, sender, subject, charset='utf-8')
    
            # email user as well
            user_email = data['email']    
            subject = "Critical Commons Advanced User application"
            message = "Dear %s\n\nThank you for applying for Advanced User status in Critical Commons!\n\nWe will review your application and respond as quickly as possible -- usually between 5 minutes and 24 hours.\nIf you have any questions, please reply to this message.\n\nCritical Commons" % data['user_title']
            mail_host.send(message, user_email, mto, subject, charset='utf-8')

        # XXX Return somewhere else, depending on what
        # handle_join_success returns?
        return self.context.unrestrictedTraverse('registered')()


    def validate_registration(self, action, data):
        """
        """

        #import pdb; pdb.set_trace()
        errors = super(MyRegistrationForm, self).validate_registration(action, data)

        form_field_names = [f.field.getName() for f in self.form_fields]

        if not ('accept' in data.keys() and data.get('accept', '')):
            err_str = _(u'Please check if you agree with the terms')
            errors.append(WidgetInputError('accept', u'label_accept', err_str))
            self.widgets['accept'].error = err_str

        if not ('fullname' in data.keys() and data.get('fullname', '')):
            err_str = _(u'Please fill in the full name')
            errors.append(WidgetInputError('fullname', u'label_fullname', err_str))
            self.widgets['fullname'].error = err_str

        if data['usertype'] == u'Advanced User':
            if not ('user_title' in data.keys() and data.get('user_title', '')):
                err_str = _(u'Please fill in the title')
                errors.append(WidgetInputError('user_title', u'label_user_title', err_str))
                self.widgets['user_title'].error = err_str
            if not ('institution' in data.keys() and data.get('institution', '')):
                err_str = _(u'Please fill in the institution')
                errors.append(WidgetInputError('institution', u'label_institution', err_str))
                self.widgets['institution'].error = err_str
            if not ('description' in data.keys() and data.get('description', '')):
                err_str = _(u'Please fill in the Biography')
                errors.append(WidgetInputError('description', u'label_description', err_str))
                self.widgets['description'].error = err_str
            if not ('home_page' in data.keys() and data.get('home_page', '')):
                err_str = _(u'Please fill in the Home Page')
                errors.append(WidgetInputError('home_page', u'label_home_page', err_str))
                self.widgets['home_page'].error = err_str

        return errors

