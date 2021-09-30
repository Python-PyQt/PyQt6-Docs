.. sip:enum-member-description::
    :status: todo
    :value: 28
    :digest: 30b39bac058fb4d99503831a93e7c2f4

Actions with the Shortcut property won't be shown in any shortcut menus unless specifically set by the QAction::shortcutVisibleInContextMenu property. This value was added in Qt 5.10, and defaults to the preference reported by the implementation of QPlatformIntegration::styleHint. To override the platform integration, set this attribute after :sip:ref:`~PyQt6.QtCore.QCoreApplication` has been instantiated.
