import unittest
from zope.component import getMultiAdapter
from plone.registry import Registry
from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase.ptc import PloneTestCase
from collective.js.innerfade.interfaces import IInnerfadeSettings
from collective.js.innerfade.tests.layer import InnerfadeLayer


class RegistryTest(PloneTestCase):
    layer = InnerfadeLayer

    def afterSetUp(self):
        self.loginAsPortalOwner()
        self.registry = Registry()
        self.registry.registerInterface(IInnerfadeSettings)

    def test_innerfade_controlpanel_view(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name="innerfade-settings")
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_innerfade_controlpanel_view_protected(self):
        # Test that the innerfade setting control panel view can not be accessed
        # by anonymous users
        from AccessControl import Unauthorized
        self.logout()
        self.assertRaises(Unauthorized,
                          self.portal.restrictedTraverse,
                         '@@innerfade-settings')

    def test_innerfade_in_controlpanel(self):
        # Check that there is an akismet entry in the control panel
        self.controlpanel = getToolByName(self.portal, "portal_controlpanel")
        self.failUnless('innerfade' in [a.getAction(self)['id']
                            for a in self.controlpanel.listActions()])

    def test_record_innerfade_width(self):
        # Test that the akismet_key record is in the control panel
        record_innerfade_width = self.registry.records[
            'collective.js.innerfade.interfaces.IInnerfadeSettings.innerfade_width']
        self.failUnless('innerfade_width' in IInnerfadeSettings)
        self.assertEquals(record_innerfade_width.value, 480)

    def test_record_innerfade_height(self):
        # Test that the akismet_key record is in the control panel
        record_innerfade_width = self.registry.records[
            'collective.js.innerfade.interfaces.IInnerfadeSettings.innerfade_height']
        self.failUnless('innerfade_height' in IInnerfadeSettings)
        self.assertEquals(record_innerfade_width.value, 271)

    def test_record_innerfade_animationtype(self):
        # Test that the akismet_key record is in the control panel
        record_innerfade_width = self.registry.records[
            'collective.js.innerfade.interfaces.IInnerfadeSettings.innerfade_animationtype']
        self.failUnless('innerfade_animationtype' in IInnerfadeSettings)
        self.assertEquals(record_innerfade_width.value, u"fade")

    def test_record_innerfade_speed(self):
        # Test that the akismet_key record is in the control panel
        record_innerfade_width = self.registry.records[
            'collective.js.innerfade.interfaces.IInnerfadeSettings.innerfade_speed']
        self.failUnless('innerfade_speed' in IInnerfadeSettings)
        self.assertEquals(record_innerfade_width.value, u"slow")

    def test_record_innerfade_timeout(self):
        # Test that the akismet_key record is in the control panel
        record_innerfade_width = self.registry.records[
            'collective.js.innerfade.interfaces.IInnerfadeSettings.innerfade_timeout']
        self.failUnless('innerfade_timeout' in IInnerfadeSettings)
        self.assertEquals(record_innerfade_width.value, 5000)

    def test_record_innerfade_type(self):
        # Test that the akismet_key record is in the control panel
        record_innerfade_width = self.registry.records[
            'collective.js.innerfade.interfaces.IInnerfadeSettings.innerfade_type']
        self.failUnless('innerfade_type' in IInnerfadeSettings)
        self.assertEquals(record_innerfade_width.value, u"sequence")



def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

