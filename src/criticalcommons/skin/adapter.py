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

    def get_accept(self):
        return self.context.getProperty('accept', '')
    def set_accept(self, value):
        return self.context.setMemberProperties({'accept': value})
    accept = property(get_accept, set_accept)
