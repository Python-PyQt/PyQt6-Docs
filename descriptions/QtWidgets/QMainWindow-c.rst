.. sip:class-description::
    :status: todo
    :brief: Main application window
    :digest: 63e0657fe9a64a1509aa10305c1e1a47

The :sip:ref:`~PyQt6.QtWidgets.QMainWindow` class provides a main application window.

.. _qmainwindow-qt-main-window-framework:

Qt Main Window Framework
------------------------

A main window provides a framework for building an application's user interface. Qt has :sip:ref:`~PyQt6.QtWidgets.QMainWindow` and its `related classes <https://doc.qt.io/qt-6/widget-classes.html#main-window-and-related-classes>`_ for main window management. :sip:ref:`~PyQt6.QtWidgets.QMainWindow` has its own layout to which you can add :sip:ref:`~PyQt6.QtWidgets.QToolBar`\ s, :sip:ref:`~PyQt6.QtWidgets.QDockWidget`\ s, a :sip:ref:`~PyQt6.QtWidgets.QMenuBar`, and a :sip:ref:`~PyQt6.QtWidgets.QStatusBar`. The layout has a center area that can be occupied by any kind of widget. You can see an image of the layout below.

.. image:: ../../../images/mainwindowlayout.png

**Note:** Creating a main window without a central widget is not supported. You must have a central widget even if it is just a placeholder.

.. _qmainwindow-creating-main-window-components:

Creating Main Window Components
-------------------------------

A central widget will typically be a standard Qt widget such as a :sip:ref:`~PyQt6.QtWidgets.QTextEdit` or a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`. Custom widgets can also be used for advanced applications. You set the central widget with ``setCentralWidget()``.

Main windows have either a single (SDI) or multiple (MDI) document interface. You create MDI applications in Qt by using a :sip:ref:`~PyQt6.QtWidgets.QMdiArea` as the central widget.

We will now examine each of the other widgets that can be added to a main window. We give examples on how to create and add them.

.. _qmainwindow-creating-menus:

Creating Menus
..............

Qt implements menus in :sip:ref:`~PyQt6.QtWidgets.QMenu` and :sip:ref:`~PyQt6.QtWidgets.QMainWindow` keeps them in a :sip:ref:`~PyQt6.QtWidgets.QMenuBar`. :sip:ref:`~PyQt6.QtGui.QAction`\ s are added to the menus, which display them as menu items.

You can add new menus to the main window's menu bar by calling ``menuBar()``, which returns the :sip:ref:`~PyQt6.QtWidgets.QMenuBar` for the window, and then add a menu with :sip:ref:`~PyQt6.QtWidgets.QMenuBar.addMenu`.

:sip:ref:`~PyQt6.QtWidgets.QMainWindow` comes with a default menu bar, but you can also set one yourself with ``setMenuBar()``. If you wish to implement a custom menu bar (i.e., not use the :sip:ref:`~PyQt6.QtWidgets.QMenuBar` widget), you can set it with ``setMenuWidget()``.

An example of how to create menus follows:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_widgets_widgets_qmainwindow.py
    :lines: 43-48

The ``createPopupMenu()`` function creates popup menus when the main window receives context menu events. The default implementation generates a menu with the checkable actions from the dock widgets and toolbars. You can reimplement ``createPopupMenu()`` for a custom menu.

.. _qmainwindow-creating-toolbars:

Creating Toolbars
.................

Toolbars are implemented in the :sip:ref:`~PyQt6.QtWidgets.QToolBar` class. You add a toolbar to a main window with ``addToolBar()``.

You control the initial position of toolbars by assigning them to a specific :sip:ref:`~PyQt6.QtCore.Qt.ToolBarAreas`. You can split an area by inserting a toolbar break - think of this as a line break in text editing - with ``addToolBarBreak()`` or ``insertToolBarBreak()``. You can also restrict placement by the user with :sip:ref:`~PyQt6.QtWidgets.QToolBar.setAllowedAreas` and :sip:ref:`~PyQt6.QtWidgets.QToolBar.setMovable`.

The size of toolbar icons can be retrieved with ``iconSize()``. The sizes are platform dependent; you can set a fixed size with ``setIconSize()``. You can alter the appearance of all tool buttons in the toolbars with ``setToolButtonStyle()``.

An example of toolbar creation follows:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_widgets_widgets_qmainwindow.py
    :lines: 52-55

.. _qmainwindow-creating-dock-widgets:

Creating Dock Widgets
.....................

Dock widgets are implemented in the :sip:ref:`~PyQt6.QtWidgets.QDockWidget` class. A dock widget is a window that can be docked into the main window. You add dock widgets to a main window with ``addDockWidget()``.

There are four dock widget areas as given by the :sip:ref:`~PyQt6.QtCore.Qt.DockWidgetAreas` enum: left, right, top, and bottom. You can specify which dock widget area that should occupy the corners where the areas overlap with ``setCorner()``. By default each area can only contain one row (vertical or horizontal) of dock widgets, but if you enable nesting with ``setDockNestingEnabled()``, dock widgets can be added in either direction.

Two dock widgets may also be stacked on top of each other. A :sip:ref:`~PyQt6.QtWidgets.QTabBar` is then used to select which of the widgets should be displayed.

We give an example of how to create and add dock widgets to a main window:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-mainwindowsnippet.py
    :lines: 98-102

.. _qmainwindow-the-status-bar:

The Status Bar
..............

You can set a status bar with ``setStatusBar()``, but one is created the first time ``statusBar()`` (which returns the main window's status bar) is called. See :sip:ref:`~PyQt6.QtWidgets.QStatusBar` for information on how to use it.

.. _qmainwindow-storing-state:

Storing State
-------------

:sip:ref:`~PyQt6.QtWidgets.QMainWindow` can store the state of its layout with ``saveState()``; it can later be retrieved with ``restoreState()``. It is the position and size (relative to the size of the main window) of the toolbars and dock widgets that are stored.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMenuBar`, :sip:ref:`~PyQt6.QtWidgets.QToolBar`, :sip:ref:`~PyQt6.QtWidgets.QStatusBar`, :sip:ref:`~PyQt6.QtWidgets.QDockWidget`, `Qt Widgets - Application Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-application-example.html>`_, `Dock Widgets Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-dockwidgets-example.html>`_, `MDI Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-mdi-example.html>`_, `SDI Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-sdi-example.html>`_, `Menus Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-menus-example.html>`_.
