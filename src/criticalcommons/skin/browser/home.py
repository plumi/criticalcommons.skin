from Products.Five import BrowserView

from zope.component import queryMultiAdapter
from Products.CMFCore.utils import getToolByName

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
                 review_state='featured',
                         limit=self.limit_featured)
        brains = catalog(filtering)[:self.limit_featured]
        shuffled_videos = list(brains)
        shuffle(shuffled_videos)
        while len(shuffled_videos) < self.limit_featured:
            shuffled_videos.append(None)
        return shuffled_videos
