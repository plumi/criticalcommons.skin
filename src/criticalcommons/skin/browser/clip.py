from plumi.content.browser.video import VideoView
from criticalcommons.content.forms import CommentaryForm
from plone.z3cform import z2
from z3c.form.interfaces import IFormLayer
from zope.security import checkPermission
from AccessControl import getSecurityManager


class ClipView(VideoView):
    """ View class for CC Clips """
    def __init__(self,context,request):
        super(ClipView, self).__init__(context,request)
        z2.switch_on(self, request_layer=IFormLayer)
        self.commentary_form = CommentaryForm(context, request)
        self.commentary_form.update()

    def commentaries(self):
        ret = []
        related = self.context.getRelatedItems()
        for item in related:
            if item.portal_type == 'Commentary':
                ret.append(item)
        return ret

    def canDownload(self):
        return getSecurityManager().checkPermission('criticalcommons.content.CanDownload', self.context)
