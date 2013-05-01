from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from AccessControl import getSecurityManager
from collective.transcode.star.interfaces import ITranscodeTool
from zope.component import getUtility

class LectureView(BrowserView):
    """A view of a critical commons lecture"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def clips(self):
        clips = []
        for item in self.context.relatedItems:
            try:
                video = item.to_object
            except:
                video = item
            clips.append(video)
        return clips

class LectureLibraryView(BrowserView):
    """A view of a library of critical commons lectures """

    lecture_limit_latest = 400

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.catalog = getToolByName(self.context,"portal_catalog")
        self.author = self.context.Creator()

    def latestlectures(self):
        """Return the latest lectures for the library"""
        filtering = dict(portal_type='Lecture',
                         sort_on='created',
                         sort_order='reverse',
                         review_state='published',
                         sort_limit=self.lecture_limit_latest)
        
        lectures = self.catalog(filtering)
        return [ l for l in lectures ]

    def canUpload(self):
        return getSecurityManager().checkPermission('criticalcommons.content: Can Download', self.context)



class ClipLibraryView(BrowserView):
    """A view of a library of critical commons Clips """

    clip_limit_latest = 20000

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.catalog = getToolByName(self.context,"portal_catalog")

    def latestclips(self):
        """Return the latest Clips for the library"""
        genre = self.request.form.get('genre', None)
        if genre and genre != 'all':
            filtering = dict(portal_type='PlumiVideo',
                         sort_on='created',
                         sort_order='reverse',
                         review_state='published',
                         getGenre=genre,
                         sort_limit=self.clip_limit_latest)
        else:
            filtering = dict(portal_type='PlumiVideo',
                         sort_on='created',
                         sort_order='reverse',
                         review_state='published',
                         sort_limit=self.clip_limit_latest)
        clips = self.catalog(filtering)
        return [ l for l in clips ]
   
    def videogenres(self):
        pv = getToolByName(self.context, 'portal_vocabularies')
        voc = pv.getVocabularyByName('video_genre')
        genresDict = []
        voc_terms = voc.getDisplayList(self.context).items()
        genresDict = [SimpleTerm(value=term[0], token=term[0], title=term[1])
                         for term in voc_terms if term[0] != 'none']
        return SimpleVocabulary(genresDict)

    def canUpload(self):
        return getSecurityManager().checkPermission('criticalcommons.content: Can Download', self.context)


class CommentaryView(BrowserView):
    """A view of a critical commons Commentary"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def clips(self):
        clips = []
        for item in self.context.relatedItems:
            video = item.to_object
            clips.append(video)
        return clips


class Playlist(BrowserView):
    """A view for the RSS feed used by Scalar project"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def profiles(self, uid):
        tt = getUtility(ITranscodeTool)
        try:
            return tt[uid][tt[uid].keys()[0]]
        except:
            return []

    def isVideo(self, obj):
        if self.isAudio(obj) or self.isImage(obj):
            return False
        else:
            return True

    def isAudio(self, obj):
        return 'audio' in obj.getContentType()

    def isImage(self, obj):
        return 'image' in obj.getContentType()
