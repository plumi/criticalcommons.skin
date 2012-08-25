from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from zope.component import queryMultiAdapter
from Products.CMFCore.utils import getToolByName

from plumi.content.browser.interfaces import IFeaturedVideosRetriever, IPlumiVideoBrain

from random import shuffle

class FeaturedViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/featured.pt')

    limit_featured = 5

    def update(self):
        # set here the values that you need to grab from the template.
        # stupid example:
        self.designer = "mitsos"

    @property
    def featured_videos(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        filtering = dict(portal_type='PlumiVideo',
                 sort_on='effective',
                 sort_order='reverse',
                 review_state='featured',
                         limit=self.limit_featured)
        brains = catalog(filtering)[:self.limit_featured]
        shuffled_videos = list(brains)
        shuffle(shuffled_videos)
        while len(shuffled_videos) < self.limit_featured:
            shuffled_videos.append(None)
        return shuffled_videos
