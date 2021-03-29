.. sip:class-description::
    :status: todo
    :brief: Stack of tabbed widgets
    :digest: 07b0ae5827fe998acac8c2959e1e1fe4

The :sip:ref:`~PyQt6.QtWidgets.QTabWidget` class provides a stack of tabbed widgets.

.. image:: ../../../images/windows-tabwidget.png

A tab widget provides a tab bar (see :sip:ref:`~PyQt6.QtWidgets.QTabBar`) and a "page area" that is used to display pages related to each tab. By default, the tab bar is shown above the page area, but different configurations are available (see :sip:ref:`~PyQt6.QtWidgets.QTabWidget.TabPosition.TabPosition`). Each tab is associated with a different widget (called a page). Only the current page is shown in the page area; all the other pages are hidden. The user can show a different page by clicking on its tab or by pressing its Alt+\ *letter* shortcut if it has one.

The normal way to use :sip:ref:`~PyQt6.QtWidgets.QTabWidget` is to do the following:

#. Create a :sip:ref:`~PyQt6.QtWidgets.QTabWidget`.

#. Create a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ for each of the pages in the tab dialog, but do not specify parent widgets for them.

#. Insert child widgets into the page widget, using layouts to position them as normal.

#. Call :sip:ref:`~PyQt6.QtWidgets.QTabWidget.addTab` or :sip:ref:`~PyQt6.QtWidgets.QTabWidget.insertTab` to put the page widgets into the tab widget, giving each tab a suitable label with an optional keyboard shortcut.

The position of the tabs is defined by :sip:ref:`~PyQt6.QtWidgets.QTabWidget.tabPosition`, their shape by :sip:ref:`~PyQt6.QtWidgets.QTabWidget.tabShape`.

The signal :sip:ref:`~PyQt6.QtWidgets.QTabWidget.currentChanged` is emitted when the user selects a page.

The current page index is available as :sip:ref:`~PyQt6.QtWidgets.QTabWidget.currentIndex`, the current page widget with :sip:ref:`~PyQt6.QtWidgets.QTabWidget.currentWidget`. You can retrieve a pointer to a page widget with a given index using :sip:ref:`~PyQt6.QtWidgets.QTabWidget.widget`, and can find the index position of a widget with :sip:ref:`~PyQt6.QtWidgets.QTabWidget.indexOf`. Use :sip:ref:`~PyQt6.QtWidgets.QTabWidget.setCurrentWidget` or :sip:ref:`~PyQt6.QtWidgets.QTabWidget.setCurrentIndex` to show a particular page.

You can change a tab's text and icon using :sip:ref:`~PyQt6.QtWidgets.QTabWidget.setTabText` or :sip:ref:`~PyQt6.QtWidgets.QTabWidget.setTabIcon`. A tab and its associated page can be removed with :sip:ref:`~PyQt6.QtWidgets.QTabWidget.removeTab`.

Each tab is either enabled or disabled at any given time (see :sip:ref:`~PyQt6.QtWidgets.QTabWidget.setTabEnabled`). If a tab is enabled, the tab text is drawn normally and the user can select that tab. If it is disabled, the tab is drawn in a different way and the user cannot select that tab. Note that even if a tab is disabled, the page can still be visible, for example if all of the tabs happen to be disabled.

Tab widgets can be a very good way to split up a complex dialog. An alternative is to use a :sip:ref:`~PyQt6.QtWidgets.QStackedWidget` for which you provide some means of navigating between pages, for example, a :sip:ref:`~PyQt6.QtWidgets.QToolBar` or a :sip:ref:`~PyQt6.QtWidgets.QListWidget`.

Most of the functionality in :sip:ref:`~PyQt6.QtWidgets.QTabWidget` is provided by a :sip:ref:`~PyQt6.QtWidgets.QTabBar` (at the top, providing the tabs) and a :sip:ref:`~PyQt6.QtWidgets.QStackedWidget` (most of the area, organizing the individual pages).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTabBar`, :sip:ref:`~PyQt6.QtWidgets.QStackedWidget`, :sip:ref:`~PyQt6.QtWidgets.QToolBox`, `Tab Dialog Example <https://doc.qt.io/qt-6/qtwidgets-dialogs-tabdialog-example.html>`_.
