.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: f833f97863df275526cfdc8905caf5f9

Actions with the Icon property won't be shown in any menus unless specifically set by the QAction::iconVisibleInMenu property. Menus that are currently open or menus already created in the native macOS menubar *may not* pick up a change in this attribute. Changes in the QAction::iconVisibleInMenu property will always be picked up.
