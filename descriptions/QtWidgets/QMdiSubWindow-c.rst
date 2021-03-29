.. sip:class-description::
    :status: todo
    :brief: Subwindow class for QMdiArea
    :digest: c87f156962db548cd6e2d78edeffe778

The :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` class provides a subwindow class for :sip:ref:`~PyQt6.QtWidgets.QMdiArea`.

:sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` represents a top-level window in a :sip:ref:`~PyQt6.QtWidgets.QMdiArea`, and consists of a title bar with window decorations, an internal widget, and (depending on the current style) a window frame and a size grip. :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` has its own layout, which consists of the title bar and a center area for the internal widget.

.. image:: ../../../images/qmdisubwindowlayout.png

The most common way to construct a :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` is to call :sip:ref:`~PyQt6.QtWidgets.QMdiArea.addSubWindow` with the internal widget as the argument. You can also create a subwindow yourself, and set an internal widget by calling :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.setWidget`.

You use the same API when programming with subwindows as with regular top-level windows (e.g., you can call functions such as show(), hide(), showMaximized(), and setWindowTitle()).

.. _qmdisubwindow-subwindow-handling:

Subwindow Handling
------------------

:sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` also supports behavior specific to subwindows in an MDI area.

By default, each :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` is visible inside the MDI area viewport when moved around, but it is also possible to specify transparent window movement and resizing behavior, where only the outline of a subwindow is updated during these operations. The :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.setOption` function is used to enable this behavior.

The :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.isShaded` function detects whether the subwindow is currently shaded (i.e., the window is collapsed so that only the title bar is visible). To enter shaded mode, call :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.showShaded`. :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow` emits the :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.windowStateChanged` signal whenever the window state has changed (e.g., when the window becomes minimized, or is restored). It also emits :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.aboutToActivate` before it is activated.

In keyboard-interactive mode, the windows are moved and resized with the keyboard. You can enter this mode through the system menu of the window. The :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.keyboardSingleStep` and :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.keyboardPageStep` properties control the distance the widget is moved or resized for each keypress event. When shift is pressed down page step is used; otherwise single step is used.

You can also change the active window with the keyboard. By pressing the control and tab keys at the same time, the next (using the current :sip:ref:`~PyQt6.QtWidgets.QMdiArea.WindowOrder`) subwindow will be activated. By pressing control, shift, and tab, you will activate the previous window. This is equivalent to calling :sip:ref:`~PyQt6.QtWidgets.QMdiArea.activateNextSubWindow` and :sip:ref:`~PyQt6.QtWidgets.QMdiArea.activatePreviousSubWindow`. Note that these shortcuts overrides global shortcuts, but not the :sip:ref:`~PyQt6.QtWidgets.QMdiArea`\ s shortcuts.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiArea`.
