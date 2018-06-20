# encoding: utf-8

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.app.layout.viewlets.common import GlobalSectionsViewlet


class IconifiedNavigationViewlet(GlobalSectionsViewlet):
    index = ViewPageTemplateFile('iconifiednavigation-sections.pt')

    def relative_path(self, url):
        portal_url = api.portal.get_navigation_root(self.context).absolute_url()
        relative_path = url.replace(portal_url, '')
        if not relative_path:
            return ''
        if relative_path.startswith('/'):
            relative_path = relative_path[1:]
        return relative_path

    def get_image(self, url):
        icon_path = self.relative_path(url)
        if not icon_path:
            return None

        obj = api.portal.get_navigation_root(self.context).unrestrictedTraverse(icon_path)
        if obj.navigation_icon:
            return url + '/@@images/navigation_icon'
        return None
