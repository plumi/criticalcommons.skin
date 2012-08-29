from plumi.content.browser.video import VideoView

class ClipView(VideoView):
    """ View class for CC Clips """

    def commentaries(self):
        ret = []
        related = self.context.getRelatedItems()
        for item in related:
            if item.portal_type == 'Commentary':
                ret.append(item)
        return ret            
