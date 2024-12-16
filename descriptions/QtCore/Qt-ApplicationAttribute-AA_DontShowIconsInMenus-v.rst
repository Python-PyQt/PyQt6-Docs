.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: 91f64429ae6d92f04ab89a1b1999be54

Actions with the Icon property won't be shown in any menus unless specifically set by the QAction::iconVisibleInMenu property. The default value of this attribute depends on the platform. To override the default behavior, set the attribute after :sip:ref:`~PyQt6.QtGui.QGuiApplication` has been instantiated. Menus that are currently open or menus already created in the native macOS menubar *may not* pick up a change in this attribute. Changes in the QAction::iconVisibleInMenu property will always be picked up.
