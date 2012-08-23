from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CriticalcommonsSkin(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import criticalcommons.skin
        xmlconfig.file('configure.zcml',
                       criticalcommons.skin,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'criticalcommons.skin:default')

CRITICALCOMMONS_SKIN_FIXTURE = CriticalcommonsSkin()
CRITICALCOMMONS_SKIN_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(CRITICALCOMMONS_SKIN_FIXTURE, ),
                       name="CriticalcommonsSkin:Integration")