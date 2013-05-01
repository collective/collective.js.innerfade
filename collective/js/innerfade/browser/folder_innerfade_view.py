from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.collection import collection
from plone.app.contentlisting.catalog import CatalogContentListingObject


class FolderInnerfadeView(BrowserView):

    template = ViewPageTemplateFile('folder_innerfade_view.pt')

    def getImages(self):
        if self.context.portal_type == 'Collection':
            results =  self.context.results()
            images = []
            for item in results:
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
                if item.portal_type == 'Link' and item.getObject().Title() == imageId+'.link':
                    links.append(item.getObject())
        else:
            links = self.context.getFolderContents(contentFilter={'portal_type':'Link', 'id':imageId+'.link'})

        if links:
            result = links[0]

        return result
