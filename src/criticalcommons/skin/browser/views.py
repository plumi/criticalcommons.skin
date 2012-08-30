from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

class LectureView(BrowserView):
    """A view of a critical commons lecture"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def clips(self):
        clips = []
        for item in self.context.relatedItems:
            video = item.to_object
            clips.append(video)
        return clips

class LectureLibraryView(BrowserView):
    """A view of a library of critical commons lectures """

    lecture_limit_latest = 200

    def __init__(self, context, request):
        self.context = context
        self.request = request
        #setup a catalog object
        self.catalog = getToolByName(self.context,"portal_catalog")
        self.author = self.context.Creator()
        #print " author of lecture library %s" % self.author

    def latestlectures(self):
        """Return the latest lectures for the library"""
        filtering = dict(portal_type='Lecture',
                         sort_on='created',
                         sort_order='reverse',
                         review_state='published',
                         sort_limit=self.lecture_limit_latest)
        if self.author!='admin':
                filtering.update(Creator=self.author)
        brains = self.catalog(filtering)[:self.lecture_limit_latest]
        #return real objects
        return [ b.getObject() for b in brains ]


