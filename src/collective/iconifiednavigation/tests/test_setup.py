# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.iconifiednavigation.testing import COLLECTIVE_ICONIFIEDNAVIGATION_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.iconifiednavigation is properly installed."""

    layer = COLLECTIVE_ICONIFIEDNAVIGATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.iconifiednavigation is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.iconifiednavigation'))

    def test_browserlayer(self):
        """Test that ICollectiveIconifiednavigationLayer is registered."""
        from collective.iconifiednavigation.interfaces import (
            ICollectiveIconifiednavigationLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveIconifiednavigationLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_ICONIFIEDNAVIGATION_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.iconifiednavigation'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.iconifiednavigation is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.iconifiednavigation'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveIconifiednavigationLayer is removed."""
        from collective.iconifiednavigation.interfaces import \
            ICollectiveIconifiednavigationLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveIconifiednavigationLayer,
            utils.registered_layers())
