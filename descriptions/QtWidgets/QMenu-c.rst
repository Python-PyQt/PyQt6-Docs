.. sip:class-description::
    :status: todo
    :brief: Menu widget for use in menu bars, context menus, and other popup menus
    :digest: 8614264b85766543a8018ec2267b45b9

The :sip:ref:`~PyQt6.QtWidgets.QMenu` class provides a menu widget for use in menu bars, context menus, and other popup menus.

.. image:: ../../../images/fusion-menu.png

A menu widget is a selection menu. It can be either a pull-down menu in a menu bar or a standalone context menu. Pull-down menus are shown by the menu bar when the user clicks on the respective item or presses the specified shortcut key. Use :sip:ref:`~PyQt6.QtWidgets.QMenuBar.addMenu` to insert a menu into a menu bar. Context menus are usually invoked by some special keyboard key or by right-clicking. They can be executed either asynchronously with :sip:ref:`~PyQt6.QtWidgets.QMenu.popup` or synchronously with :sip:ref:`~PyQt6.QtWidgets.QMenu.exec`. Menus can also be invoked in response to button presses; these are just like context menus except for how they are invoked.

.. _qmenu-actions:

Actions
-------

A menu consists of a list of action items. Actions are added with the :sip:ref:`~PyQt6.QtWidgets.QMenu.addAction`, addActions() and insertAction() functions. An action is represented vertically and rendered by :sip:ref:`~PyQt6.QtWidgets.QStyle`. In addition, actions can have a text label, an optional icon drawn on the very left side, and shortcut key sequence such as "Ctrl+X".

The existing actions held by a menu can be found with actions().

There are four kinds of action items: separators, actions that show a submenu, widgets, and actions that perform an action. Separators are inserted with :sip:ref:`~PyQt6.QtWidgets.QMenu.addSeparator`, submenus with :sip:ref:`~PyQt6.QtWidgets.QMenu.addMenu`, and all other items are considered action items.

When inserting action items you usually specify a receiver and a slot. The receiver will be notifed whenever the item is :sip:ref:`~PyQt6.QtGui.QAction.triggered`. In addition, :sip:ref:`~PyQt6.QtWidgets.QMenu` provides two signals, :sip:ref:`~PyQt6.QtWidgets.QMenu.triggered` and :sip:ref:`~PyQt6.QtWidgets.QMenu.hovered`, which signal the :sip:ref:`~PyQt6.QtGui.QAction` that was triggered from the menu.

You clear a menu with :sip:ref:`~PyQt6.QtWidgets.QMenu.clear` and remove individual action items with removeAction().

A :sip:ref:`~PyQt6.QtWidgets.QMenu` can also provide a tear-off menu. A tear-off menu is a top-level window that contains a copy of the menu. This makes it possible for the user to "tear off" frequently used menus and position them in a convenient place on the screen. If you want this functionality for a particular menu, insert a tear-off handle with :sip:ref:`~PyQt6.QtWidgets.QMenu.setTearOffEnabled`. When using tear-off menus, bear in mind that the concept isn't typically used on Microsoft Windows so some users may not be familiar with it. Consider using a :sip:ref:`~PyQt6.QtWidgets.QToolBar` instead.

Widgets can be inserted into menus with the :sip:ref:`~PyQt6.QtWidgets.QWidgetAction` class. Instances of this class are used to hold widgets, and are inserted into menus with the :sip:ref:`~PyQt6.QtWidgets.QMenu.addAction` overload that takes a :sip:ref:`~PyQt6.QtGui.QAction`. If the :sip:ref:`~PyQt6.QtWidgets.QWidgetAction` fires the :sip:ref:`~PyQt6.QtWidgets.QMenu.triggered` signal, the menu will close.

**Warning:** To make :sip:ref:`~PyQt6.QtWidgets.QMenu` visible on the screen, :sip:ref:`~PyQt6.QtWidgets.QMenu.exec` or :sip:ref:`~PyQt6.QtWidgets.QMenu.popup` should be used instead of show().

.. _qmenu-qmenu-on-macos-with-qt-build-against-cocoa:

QMenu on macOS with Qt Build Against Cocoa
------------------------------------------

:sip:ref:`~PyQt6.QtWidgets.QMenu` can be inserted only once in a menu/menubar. Subsequent insertions will have no effect or will result in a disabled menu item.

See the `Menus <https://doc.qt.io/qt-6/qtwidgets-mainwindows-menus-example.html>`_ example for an example of how to use :sip:ref:`~PyQt6.QtWidgets.QMenuBar` and :sip:ref:`~PyQt6.QtWidgets.QMenu` in your application.

**Important inherited functions:** :sip:ref:`~PyQt6.QtWidgets.QMenu.addAction`, removeAction(), :sip:ref:`~PyQt6.QtWidgets.QMenu.clear`, :sip:ref:`~PyQt6.QtWidgets.QMenu.addSeparator`, and :sip:ref:`~PyQt6.QtWidgets.QMenu.addMenu`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMenuBar`, `GUI Design Handbook: Menu, Drop-Down and Pop-Up <https://doc.qt.io/qt-6/guibooks.html#fowler>`_, `Qt Widgets - Application Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-application-example.html>`_, `Menus Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-menus-example.html>`_.
