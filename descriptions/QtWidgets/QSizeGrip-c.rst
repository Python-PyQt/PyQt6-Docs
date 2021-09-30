.. sip:class-description::
    :status: todo
    :brief: Resize handle for resizing top-level windows
    :digest: 9a51400f02d470e9c40ad146a0bdf02c

The :sip:ref:`~PyQt6.QtWidgets.QSizeGrip` class provides a resize handle for resizing top-level windows.

This widget works like the standard Windows resize handle. In the X11 version this resize handle generally works differently from the one provided by the system if the X11 window manager does not support necessary modern post-ICCCM specifications.

Put this widget anywhere in a widget tree and the user can use it to resize the top-level window or any widget with the :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.SubWindow` flag set. Generally, this should be in the lower right-hand corner.

Note that :sip:ref:`~PyQt6.QtWidgets.QStatusBar` already uses this widget, so if you have a status bar (e.g., you are using :sip:ref:`~PyQt6.QtWidgets.QMainWindow`), then you don't need to use this widget explicitly. The same goes for :sip:ref:`~PyQt6.QtWidgets.QDialog`, for which you can just call :sip:ref:`~PyQt6.QtWidgets.QDialog.setSizeGripEnabled`.

On some platforms the size grip automatically hides itself when the window is shown full screen or maximised.

**Note:** On macOS, size grips are no longer part of the human interface guideline, and won't show unless used in a :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow`. Set another style on size grips that you want to be visible in main windows.

+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| |image-fusion-statusbar-sizegrip-png| | A size grip widget at the bottom-right corner of a main window, shown in the `Fusion widget style <https://doc.qt.io/qt-6/gallery.html>`_. |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

The :sip:ref:`~PyQt6.QtWidgets.QSizeGrip` class inherits :sip:ref:`~PyQt6.QtWidgets.QWidget` and reimplements the :sip:ref:`~PyQt6.QtWidgets.QWidget.mousePressEvent` and :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseMoveEvent` functions to feature the resize functionality, and the :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEvent` function to render the size grip widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStatusBar`, :sip:ref:`~PyQt6.QtWidgets.QWidget.windowState`.

.. |image-fusion-statusbar-sizegrip-png| image:: ../../../images/fusion-statusbar-sizegrip.png
