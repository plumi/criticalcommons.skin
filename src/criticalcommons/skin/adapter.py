from plone.app.users.browser.personalpreferences import UserDataPanelAdapter

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_usertype(self):
        return self.context.getProperty('usertype', '')
    def set_usertype(self, value):
        return self.context.setMemberProperties({'usertype': value})
    usertype = property(get_usertype, set_usertype)

    def get_user_title(self):
        return self.context.getProperty('user_title', '')
    def set_user_title(self, value):
        return self.context.setMemberProperties({'user_title': value})
    user_title = property(get_user_title, set_user_title)

    def get_institution(self):
        return self.context.getProperty('institution', '')
    def set_institution(self, value):
        return self.context.setMemberProperties({'institution': value})
    institution = property(get_institution, set_institution)

    def get_biography(self):
        return self.context.getProperty('biography', '')
    def set_biography(self, value):
        return self.context.setMemberProperties({'biography': value})
    biography = property(get_biography, set_biography)

    def get_homePage(self):
        return self.context.getProperty('homePage', '')
    def set_homePage(self, value):
        return self.context.setMemberProperties({'homePage': value})
    homePage = property(get_homePage, set_homePage)
