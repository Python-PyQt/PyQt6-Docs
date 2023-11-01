.. sip:enum-member-description::
    :status: todo
    :value: 28
    :digest: 9f7f2cd7d22d2313aa9ffce9490b8ab2

Actions with the Shortcut property won't be shown in any shortcut menus unless specifically set by the QAction::shortcutVisibleInContextMenu property. This value was added in Qt 5.10, and is by default based on the value reported by :sip:ref:`~PyQt6.QtGui.QStyleHints.showShortcutsInContextMenus`. To override the default behavior, set the style hint before :sip:ref:`~PyQt6.QtCore.QCoreApplication` has been instantiated, or set this attribute after :sip:ref:`~PyQt6.QtCore.QCoreApplication` has been instantiated.
