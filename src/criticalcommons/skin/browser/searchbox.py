from plone.app.layout.viewlets.common import SearchBoxViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
class CCSearchBoxViewlet(SearchBoxViewlet):
    render = ViewPageTemplateFile("templates/searchbox.pt")

