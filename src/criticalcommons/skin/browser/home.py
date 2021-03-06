from Products.Five import BrowserView

from zope.component import queryMultiAdapter
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
from AccessControl import getSecurityManager

from random import shuffle

class HomePage(BrowserView):
    u"""This browser view is used to replace the home page
    """

    limit_featured = 5

    @property
    def featured_videos(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        filtering = dict(portal_type='PlumiVideo',
                 sort_on='effective',
                 sort_order='reverse',
                 review_state='featured')
        brains = catalog(filtering)
        shuffled_videos = list(brains)
        shuffle(shuffled_videos)
        while len(shuffled_videos) < self.limit_featured:
            shuffled_videos.append(None)
        return shuffled_videos[:self.limit_featured]

    def blog_posts(self):
        """ """
        context = self.context
        portal = getSite()
        folder = portal['blog']
        folder_path = '/'.join(folder.getPhysicalPath())
        portal_catalog = getToolByName(context, 'portal_catalog')
        results = portal_catalog(portal_type=['Document','News Item'], Subject=('Updates'), review_state=['published','featured'], path={'query': folder_path,}, sort_on="effective", sort_order='reverse')[:3]
        return self.request.get(
            'items', results)

    def featured_blog_posts(self):
        """ """
        context = self.context
        portal = getSite()
        folder = portal['blog']
        folder_path = '/'.join(folder.getPhysicalPath())
        portal_catalog = getToolByName(context, 'portal_catalog')
        results = portal_catalog(portal_type=['News Item'], Subject=('Featured Content'), review_state=['published','featured'], sort_on="effective", sort_order='reverse')[:6]
        return self.request.get(
            'items', results)

    def canUpload(self):
        return getSecurityManager().checkPermission('criticalcommons.content: Can Download', self.context)

class PublishPage(BrowserView):
    """Publish browser view
    """


