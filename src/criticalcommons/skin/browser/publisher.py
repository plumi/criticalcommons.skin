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
        try:
            url = '/'.join(mtool.getHomeFolder(member.id).getPhysicalPath()) + '/clips/@@publish_video'
        except:
            url = '/acl_users/credentials_cookie_auth/require_login?came_from=http%3A//www.criticalcommons.org/publisher'
        return url

class SCPublisher(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def url(self):
        # url to redirect upon succesfull creation, for Scalar
        try:
            ref_link = self.request.QUERY_STRING
        except:
            ref_link = ''

        mtool = getToolByName(self.context, 'portal_membership')
        member = mtool.getAuthenticatedMember()
        try:
            url = '/'.join(mtool.getHomeFolder(member.id).getPhysicalPath()) + '/clips/@@publish_video_scalar?%s' % ref_link
        except:
            url = '/acl_users/credentials_cookie_auth/require_login?came_from=http%3A//www.criticalcommons.org/scpublisher?%s' % ref_link
        return url

