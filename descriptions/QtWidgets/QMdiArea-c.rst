.. sip:class-description::
    :status: todo
    :brief: Area in which MDI windows are displayed
    :digest: 0f3bc2a569871a63f7ec4ad4423c6f68

The :sip:ref:`~PyQt6.QtWidgets.QMdiArea` widget provides an area in which MDI windows are displayed.

:sip:ref:`~PyQt6.QtWidgets.QMdiArea` functions, essentially, like a window manager for MDI windows. For instance, it draws the windows it manages on itself and arranges them in a cascading or tile pattern. :sip:ref:`~PyQt6.QtWidgets.QMdiArea` is commonly used as the center widget in a :sip:ref:`~PyQt6.QtWidgets.QMainWindow` to create MDI applications, but can also be placed in any layout. The following code adds an area to a main window:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-mdiarea-mdiareasnippets.py
    :lines: 59-60

Unlike the window managers for top-level windows, all window flags (Qt::WindowFlags) are supported by :sip:ref:`~PyQt6.QtWidgets.QMdiArea` as long as the flags are supported by the current widget style. If a specific flag is not supported by the style (e.g., the :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.WindowShadeButtonHint`), you can still shade the window with showShaded().

Subwindows in :sip:ref:`~PyQt6.QtWidgets.QMdiArea` are instances of :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow`. They are added to an MDI area with :sip:ref:`~PyQt6.QtWidgets.QMdiArea.addSubWindow`. It is common to pass a `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_, which is set as the internal widget, to this function, but it is also possible to pass a :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` directly. The class inherits `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_, and you can use the same API as with a normal top-level window when programming. :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` also has behavior that is specific to MDI windows. See the :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` class description for more details.

A subwindow becomes active when it gets the keyboard focus, or when setFocus() is called. The user activates a window by moving focus in the usual ways. The MDI area emits the :sip:ref:`~PyQt6.QtWidgets.QMdiArea.subWindowActivated` signal when the active window changes, and the :sip:ref:`~PyQt6.QtWidgets.QMdiArea.activeSubWindow` function returns the active subwindow.

The convenience function :sip:ref:`~PyQt6.QtWidgets.QMdiArea.subWindowList` returns a list of all subwindows. This information could be used in a popup menu containing a list of windows, for example.

The subwindows are sorted by the current :sip:ref:`~PyQt6.QtWidgets.QMdiArea.WindowOrder`. This is used for the :sip:ref:`~PyQt6.QtWidgets.QMdiArea.subWindowList` and for :sip:ref:`~PyQt6.QtWidgets.QMdiArea.activateNextSubWindow` and :sip:ref:`~PyQt6.QtWidgets.QMdiArea.activatePreviousSubWindow`. Also, it is used when cascading or tiling the windows with :sip:ref:`~PyQt6.QtWidgets.QMdiArea.cascadeSubWindows` and :sip:ref:`~PyQt6.QtWidgets.QMdiArea.tileSubWindows`.

:sip:ref:`~PyQt6.QtWidgets.QMdiArea` provides two built-in layout strategies for subwindows: :sip:ref:`~PyQt6.QtWidgets.QMdiArea.cascadeSubWindows` and :sip:ref:`~PyQt6.QtWidgets.QMdiArea.tileSubWindows`. Both are slots and are easily connected to menu entries.

+-------------------------+----------------------+
| |image-mdi-cascade-png| | |image-mdi-tile-png| |
+-------------------------+----------------------+

**Note:** The default scroll bar property for :sip:ref:`~PyQt6.QtWidgets.QMdiArea` is :sip:ref:`~PyQt6.QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow`.

.. |image-mdi-cascade-png| image:: ../../../images/mdi-cascade.png
.. |image-mdi-tile-png| image:: ../../../images/mdi-tile.png
