.. sip:class-description::
    :status: todo
    :brief: Abstraction for user commands that can be added to different user interface components
    :digest: 258ba92842be3c546f4d8e8f76c8b600

The :sip:ref:`~PyQt6.QtGui.QAction` class provides an abstraction for user commands that can be added to different user interface components.

In applications many common commands can be invoked via menus, toolbar buttons, and keyboard shortcuts. Since the user expects each command to be performed in the same way, regardless of the user interface used, it is useful to represent each command as an *action*.

Actions can be added to user interface elements such as menus and toolbars, and will automatically keep the UI in sync. For example, in a word processor, if the user presses a Bold toolbar button, the Bold menu item will automatically be checked.

A :sip:ref:`~PyQt6.QtGui.QAction` may contain an icon, descriptive text, icon text, a keyboard shortcut, status text, "What's This?" text, and a tooltip. All properties can be set independently with :sip:ref:`~PyQt6.QtGui.QAction.setIcon`, :sip:ref:`~PyQt6.QtGui.QAction.setText`, :sip:ref:`~PyQt6.QtGui.QAction.setIconText`, :sip:ref:`~PyQt6.QtGui.QAction.setShortcut`, :sip:ref:`~PyQt6.QtGui.QAction.setStatusTip`, :sip:ref:`~PyQt6.QtGui.QAction.setWhatsThis`, and :sip:ref:`~PyQt6.QtGui.QAction.setToolTip`. Icon and text, as the two most important properties, can also be set in the constructor. It's possible to set an individual font with :sip:ref:`~PyQt6.QtGui.QAction.setFont`, which e.g. menus respect when displaying the action as a menu item.

We recommend that actions are created as children of the window they are used in. In most cases actions will be children of the application's main window.

.. _qaction-qaction-in-widget-applications:

QAction in widget applications
------------------------------

Once a :sip:ref:`~PyQt6.QtGui.QAction` has been created, it should be added to the relevant menu and toolbar, then connected to the slot which will perform the action. For example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-mainwindows-application-mainwindow.py
    :lines: 180-186

Actions are added to widgets using :sip:ref:`~PyQt6.QtWidgets.QWidget.addAction` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.addAction`. Note that an action must be added to a widget before it can be used. This is also true when the shortcut should be global (i.e., :sip:ref:`~PyQt6.QtCore.Qt.ShortcutContext.ApplicationShortcut` as :sip:ref:`~PyQt6.QtCore.Qt.ShortcutContext`).

Actions can be created as independent objects. But they may also be created during the construction of menus. The :sip:ref:`~PyQt6.QtWidgets.QMenu` class contains convenience functions for creating actions suitable for use as menu items.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMenu`, :sip:ref:`~PyQt6.QtWidgets.QToolBar`, `Qt Widgets - Application Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-application-example.html>`_.
