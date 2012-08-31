from Products.Five import BrowserView

from zope.component import queryMultiAdapter
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

class Publisher(BrowserView):
    u"""This browser view is used to redirect to the publish video page
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def url(self):
        mtool = getToolByName(self.context, 'portal_membership')
        member = mtool.getAuthenticatedMember()
        url = '/'.join(mtool.getHomeFolder(member.id).getPhysicalPath()) + '/videos/@@publish_video'
        return url
