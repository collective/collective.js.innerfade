from plone.app.registry.browser import controlpanel

from collective.js.innerfade.interfaces import IInnerfadeSettings, _


class InnerfadeSettingsForm(controlpanel.RegistryEditForm):

    schema = IInnerfadeSettings
    label = _(u"Innerfade settings")
    description = _(u"""""")

    def updateFields(self):
        super(InnerfadeSettingsForm, self).updateFields()

    def updateWidgets(self):
        super(InnerfadeSettingsForm, self).updateWidgets()


class InnerfadeSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = InnerfadeSettingsForm