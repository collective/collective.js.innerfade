from plone.theme.interfaces import IDefaultPloneLayer
from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.js.innerfade')


class IInnerfadeSettings(Interface):
    """Global innerfade settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """
    innerfade_width = schema.Int(title=_(u"Innerfade plugin width"),
                                 description=_(u"help_innerfade_width",
                                               default=u"Enter the width of your innerfade plugin here"),
                                 default=480,)
    innerfade_height = schema.Int(title=_(u"Innerfade plugin height"),
                                  description=_(u"help_innerfade_height",
                                                default=u"Enter the height of your innerfade plugin here"),
                                  default=271,)

    innerfade_animationtype = schema.Choice(title=_(u"Innerfade animation type"),
                                            description=_(u"help_innerfade_animationtype",
                                                          default=u"Choice of animation type"),
                                            values=(
                                                u"fade",
                                                u"slide",
                                            ),
                                            default=u"fade")

    innerfade_speed = schema.Choice(title=_(u"Innerfade speed"),
                                    description=_(u"help_innerfade_speed",
                                                  default=u"Choice of animation speed"),
                                    values=(
                                        u"slow",
                                        u"normal",
                                        u"fast",
                                    ),
                                    default=u"slow")

    innerfade_timeout = schema.Int(title=_(u"Innerfade timeout"),
                                   description=_(u"help_innerfade_timeout",
                                                 default=u"Enter time between fades in milliseconds"),
                                   default=5000)

    innerfade_type = schema.Choice(title=_(u"Innerfade slideshow type"),
                                   description=_(u"help_innerfade_type",
                                                 default=u"Choice between animation types"),
                                   values=(
                                       u"sequence",
                                       u"random",
                                       u"random_start",
                                   ),
                                   default=u"sequence")


class IInnerfadeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """