from Acquisition import aq_inner
from zope.interface import alsoProvides
from plone.z3cform.interfaces import IWrappedForm

from z3c.form.interfaces import IFormLayer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase
from plone.z3cform import z2
from criticalcommons.content.forms import CommentaryForm

class CommentaryViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/commentaryviewlet.pt')
    label = 'Add commentary'
    def update(self):
        super(CommentaryViewlet, self).update()
        z2.switch_on(self, request_layer=IFormLayer)
        self.form = CommentaryForm(aq_inner(self.context), self.request)
        alsoProvides(self.form, IWrappedForm)
        self.form.update()
