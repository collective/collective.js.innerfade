from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from collective.js.innerfade.interfaces import IInnerfadeSettings



class FolderInnerfadeView(BrowserView):

    template = ViewPageTemplateFile('folder_innerfade_view.pt')

    @property
    def innerfade_registry(self):
        registry = getUtility(IRegistry)
        return registry.forInterface(IInnerfadeSettings)

    def getImages(self):
        if self.context.portal_type == 'Collection':
            images = []
            for item in self.context.results():
                if item.portal_type == 'Image':
                    images.append(item.getObject())
            return images
        else:
            return self.context.listFolderContents(contentFilter={'portal_type':'Image'})

    def getLink(self, imageId):

        result = ''
        if self.context.portal_type == 'Collection':
            results = self.context.results()
            links = []
            for item in results:
                if item.portal_type == 'Link' and item.id == imageId+'.link':
                    links.append(item)
        else:
            links = self.context.getFolderContents(contentFilter={'portal_type':'Link', 'id':imageId+'.link'})

        if links:
            result = links[0]
        return result

    def getWidth(self):
        return self.innerfade_registry.innerfade_width

    def getHeight(self):
        return self.innerfade_registry.innerfade_height

    def getAnimationtype(self):
        return self.innerfade_registry.innerfade_animationtype

    def getSpeed(self):
        return self.innerfade_registry.innerfade_speed

    def getTimeout(self):
        return self.innerfade_registry.innerfade_timeout

    def getInnerfadeType(self):
        return self.innerfade_registry.innerfade_type
