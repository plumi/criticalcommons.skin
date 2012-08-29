from Products.CMFPlone.utils import _createObjectByType
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('CC.skin_various.txt') is None:
        return

    # Add additional setup code here
    portal = context.getSite()
    try:
        portal.invokeFactory('Folder', 'blog')
    except:
        pass
