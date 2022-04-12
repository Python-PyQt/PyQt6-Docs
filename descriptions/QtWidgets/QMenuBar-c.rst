.. sip:class-description::
    :status: todo
    :brief: Horizontal menu bar
    :digest: fad1e58f88f0366cb4d302ace5b590c0

The :sip:ref:`~PyQt6.QtWidgets.QMenuBar` class provides a horizontal menu bar.

A menu bar consists of a list of pull-down menu items. You add menu items with :sip:ref:`~PyQt6.QtWidgets.QMenuBar.addMenu`. For example, assuming that ``menubar`` is a pointer to a :sip:ref:`~PyQt6.QtWidgets.QMenuBar` and ``fileMenu`` is a pointer to a :sip:ref:`~PyQt6.QtWidgets.QMenu`, the following statement inserts the menu into the menu bar:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmenubar.py
    :lines: 54-54

The ampersand in the menu item's text sets Alt+F as a shortcut for this menu. (You can use "&&" to get a real ampersand in the menu bar.)

There is no need to lay out a menu bar. It automatically sets its own geometry to the top of the parent widget and changes it appropriately whenever the parent is resized.

.. _qmenubar-usage:

Usage
-----

In most main window style applications you would use the :sip:ref:`~PyQt6.QtWidgets.QMainWindow.menuBar` function provided in :sip:ref:`~PyQt6.QtWidgets.QMainWindow`, adding :sip:ref:`~PyQt6.QtWidgets.QMenu`\ s to the menu bar and adding :sip:ref:`~PyQt6.QtGui.QAction`\ s to the pop-up menus.

Example (from the `Menus <https://doc.qt.io/qt-6/qtwidgets-mainwindows-menus-example.html>`_ example):

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-mainwindows-menus-mainwindow.py
    :lines: 345-346

Menu items may be removed with removeAction().

Widgets can be added to menus by using instances of the :sip:ref:`~PyQt6.QtWidgets.QWidgetAction` class to hold them. These actions can then be inserted into menus in the usual way; see the :sip:ref:`~PyQt6.QtWidgets.QMenu` documentation for more details.

.. _qmenubar-platform-dependent-look-and-feel:

Platform Dependent Look and Feel
--------------------------------

Different platforms have different requirements for the appearance of menu bars and their behavior when the user interacts with them. For example, Windows systems are often configured so that the underlined character mnemonics that indicate keyboard shortcuts for items in the menu bar are only shown when the Alt key is pressed.

.. _qmenubar-qmenubar-as-a-global-menu-bar:

QMenuBar as a Global Menu Bar
-----------------------------

On macOS and on certain Linux desktop environments such as Ubuntu Unity, :sip:ref:`~PyQt6.QtWidgets.QMenuBar` is a wrapper for using the system-wide menu bar. If you have multiple menu bars in one dialog the outermost menu bar (normally inside a widget with widget flag :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.Window`) will be used for the system-wide menu bar.

Qt for macOS also provides a menu bar merging feature to make :sip:ref:`~PyQt6.QtWidgets.QMenuBar` conform more closely to accepted macOS menu bar layout. The merging functionality is based on string matching the title of a :sip:ref:`~PyQt6.QtWidgets.QMenu` entry. These strings are translated (using :sip:ref:`~PyQt6.QtCore.QObject.tr`) in the "\ :sip:ref:`~PyQt6.QtWidgets.QMenuBar`" context. If an entry is moved its slots will still fire as if it was in the original place. The table below outlines the strings looked for and where the entry is placed if matched:

+-------------------------------------------------+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| String matches                                  | Placement                                   | Notes                                                                                                                                                        |
+=================================================+=============================================+==============================================================================================================================================================+
| about.\*                                        | Application Menu | About <application name> | The application name is fetched from the ``Info.plist`` file (see note below). If this entry is not found no About item will appear in the Application Menu. |
+-------------------------------------------------+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| config, options, setup, settings or preferences | Application Menu | Preferences              | If this entry is not found the Settings item will be disabled                                                                                                |
+-------------------------------------------------+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| quit or exit                                    | Application Menu | Quit <application name>  | If this entry is not found a default Quit item will be created to call :sip:ref:`~PyQt6.QtCore.QCoreApplication.quit`                                        |
+-------------------------------------------------+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

You can override this behavior by using the :sip:ref:`~PyQt6.QtGui.QAction.menuRole` property.

If you want all windows in a Mac application to share one menu bar, you must create a menu bar that does not have a parent. Create a parent-less menu bar this way:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qmenubar.py
    :lines: 59-59

**Note:** Do *not* call :sip:ref:`~PyQt6.QtWidgets.QMainWindow.menuBar` to create the shared menu bar, because that menu bar will have the :sip:ref:`~PyQt6.QtWidgets.QMainWindow` as its parent. That menu bar would only be displayed for the parent :sip:ref:`~PyQt6.QtWidgets.QMainWindow`.

**Note:** The text used for the application name in the macOS menu bar is obtained from the value set in the ``Info.plist`` file in the application's bundle. See Qt for macOS - Deployment for more information.

**Note:** On Linux, if the com.canonical.AppMenu.Registrar service is available on the D-Bus session bus, then Qt will communicate with it to install the application's menus into the global menu bar, as described.

.. _qmenubar-examples:

Examples
--------

The `Menus <https://doc.qt.io/qt-6/qtwidgets-mainwindows-menus-example.html>`_ example shows how to use :sip:ref:`~PyQt6.QtWidgets.QMenuBar` and :sip:ref:`~PyQt6.QtWidgets.QMenu`. The other `main window application examples <https://doc.qt.io/qt-6/examples-mainwindow.html>`_ also provide menus using these classes.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMenu`, :sip:ref:`~PyQt6.QtGui.QShortcut`, :sip:ref:`~PyQt6.QtGui.QAction`, `Introduction to Apple Human Interface Guidelines <http://developer.apple.com/documentation/UserExperience/Conceptual/AppleHIGuidelines/XHIGIntro/XHIGIntro.html>`_, `Menus Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-menus-example.html>`_.
