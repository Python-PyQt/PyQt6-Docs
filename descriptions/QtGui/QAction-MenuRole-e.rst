.. sip:enum-description::
    :status: todo
    :digest: 67e1f14fb5a8d570a36589bea24d5eae

This enum describes how an action should be moved into the application menu on macOS.

Setting this value only has effect on items that are in the immediate menus of the menubar, not the submenus of those menus. For example, if you have File menu in your menubar and the File menu has a submenu, setting the MenuRole for the actions in that submenu have no effect. They will never be moved.
