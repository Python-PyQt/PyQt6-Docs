.. sip:class-description::
    :status: todo
    :brief: Mouse cursor with an arbitrary shape
    :digest: 17d4ef1a74fe85a94edf0b642613a667

The `QCursor <https://doc.qt.io/qt-6/gui-changes-qt6.html#qcursor>`_ class provides a mouse cursor with an arbitrary shape.

This class is mainly used to create mouse cursors that are associated with particular widgets and to get and set the position of the mouse cursor.

Qt has a number of standard cursor shapes, but you can also make custom cursor shapes based on a `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_, a mask and a hotspot.

To associate a cursor with a widget, use :sip:ref:`~PyQt6.QtWidgets.QWidget.setCursor`. To associate a cursor with all widgets (normally for a short period of time), use :sip:ref:`~PyQt6.QtGui.QGuiApplication.setOverrideCursor`.

To set a cursor shape use :sip:ref:`~PyQt6.QtGui.QCursor.setShape` or use the `QCursor <https://doc.qt.io/qt-6/gui-changes-qt6.html#qcursor>`_ constructor which takes the shape as argument, or you can use one of the predefined cursors defined in the :sip:ref:`~PyQt6.QtCore.Qt.CursorShape` enum.

If you want to create a cursor with your own bitmap, either use the `QCursor <https://doc.qt.io/qt-6/gui-changes-qt6.html#qcursor>`_ constructor which takes a bitmap and a mask or the constructor which takes a pixmap as arguments.

To set or get the position of the mouse cursor use the static methods :sip:ref:`~PyQt6.QtGui.QCursor.pos` and :sip:ref:`~PyQt6.QtGui.QCursor.setPos`.

**Note:** It is possible to create a `QCursor <https://doc.qt.io/qt-6/gui-changes-qt6.html#qcursor>`_ before :sip:ref:`~PyQt6.QtGui.QGuiApplication`, but it is not useful except as a place-holder for a real `QCursor <https://doc.qt.io/qt-6/gui-changes-qt6.html#qcursor>`_ created after :sip:ref:`~PyQt6.QtGui.QGuiApplication`. Attempting to use a `QCursor <https://doc.qt.io/qt-6/gui-changes-qt6.html#qcursor>`_ that was created before :sip:ref:`~PyQt6.QtGui.QGuiApplication` will result in a crash.

.. _qcursor-a-note-for-x11-users:

A Note for X11 Users
--------------------

On X11, Qt supports the `Xcursor <https://doc.qt.io/qt-6/http://www.xfree86.org/4.3.0/Xcursor.3.html>`_ library, which allows for full color icon themes. The table below shows the cursor name used for each :sip:ref:`~PyQt6.QtCore.Qt.CursorShape` value. If a cursor cannot be found using the name shown below, a standard X11 cursor will be used instead. Note: X11 does not provide appropriate cursors for all possible :sip:ref:`~PyQt6.QtCore.Qt.CursorShape` values. It is possible that some cursors will be taken from the Xcursor theme, while others will use an internal bitmap cursor.

+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
| Shape                        | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape` Value              | Cursor Name              | Shape                         | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape` Value            | Cursor Name              |
+==============================+============================================================+==========================+===============================+==========================================================+==========================+
| |image-cursor-arrow-png|     | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.ArrowCursor`        | ``left_ptr``             | |image-cursor-sizev-png|      | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.SizeVerCursor`    | ``size_ver``             |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
| |image-cursor-uparrow-png|   | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.UpArrowCursor`      | ``up_arrow``             | |image-cursor-sizeh-png|      | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.SizeHorCursor`    | ``size_hor``             |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
| |image-cursor-cross-png|     | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.CrossCursor`        | ``cross``                | |image-cursor-sizeb-png|      | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.SizeBDiagCursor`  | ``size_bdiag``           |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
| |image-cursor-ibeam-png|     | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.IBeamCursor`        | ``ibeam``                | |image-cursor-sizef-png|      | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.SizeFDiagCursor`  | ``size_fdiag``           |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
| |image-cursor-wait-png|      | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.WaitCursor`         | ``wait``                 | |image-cursor-sizeall-png|    | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.SizeAllCursor`    | ``size_all``             |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
| |image-cursor-busy-png|      | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.BusyCursor`         | ``left_ptr_watch``       | |image-cursor-vsplit-png|     | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.SplitVCursor`     | ``split_v``              |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
| |image-cursor-forbidden-png| | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.ForbiddenCursor`    | ``forbidden``            | |image-cursor-hsplit-png|     | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.SplitHCursor`     | ``split_h``              |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
| |image-cursor-hand-png|      | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.PointingHandCursor` | ``pointing_hand``        | |image-cursor-openhand-png|   | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.OpenHandCursor`   | ``openhand``             |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
| |image-cursor-whatsthis-png| | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.WhatsThisCursor`    | ``whats_this``           | |image-cursor-closedhand-png| | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.ClosedHandCursor` | ``closedhand``           |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
|                              | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.DragMoveCursor`     | ``dnd-move`` or ``move`` |                               | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.DragCopyCursor`   | ``dnd-copy`` or ``copy`` |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+
|                              | :sip:ref:`~PyQt6.QtCore.Qt.CursorShape.DragLinkCursor`     | ``dnd-link`` or ``link`` |                               |                                                          |                          |
+------------------------------+------------------------------------------------------------+--------------------------+-------------------------------+----------------------------------------------------------+--------------------------+

.. seealso:: `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_, `GUI Design Handbook: Cursors <https://doc.qt.io/qt-6/guibooks.html#fowler>`_.

.. |image-cursor-arrow-png| image:: ../../../images/cursor-arrow.png
.. |image-cursor-sizev-png| image:: ../../../images/cursor-sizev.png
.. |image-cursor-uparrow-png| image:: ../../../images/cursor-uparrow.png
.. |image-cursor-sizeh-png| image:: ../../../images/cursor-sizeh.png
.. |image-cursor-cross-png| image:: ../../../images/cursor-cross.png
.. |image-cursor-sizeb-png| image:: ../../../images/cursor-sizeb.png
.. |image-cursor-ibeam-png| image:: ../../../images/cursor-ibeam.png
.. |image-cursor-sizef-png| image:: ../../../images/cursor-sizef.png
.. |image-cursor-wait-png| image:: ../../../images/cursor-wait.png
.. |image-cursor-sizeall-png| image:: ../../../images/cursor-sizeall.png
.. |image-cursor-busy-png| image:: ../../../images/cursor-busy.png
.. |image-cursor-vsplit-png| image:: ../../../images/cursor-vsplit.png
.. |image-cursor-forbidden-png| image:: ../../../images/cursor-forbidden.png
.. |image-cursor-hsplit-png| image:: ../../../images/cursor-hsplit.png
.. |image-cursor-hand-png| image:: ../../../images/cursor-hand.png
.. |image-cursor-openhand-png| image:: ../../../images/cursor-openhand.png
.. |image-cursor-whatsthis-png| image:: ../../../images/cursor-whatsthis.png
.. |image-cursor-closedhand-png| image:: ../../../images/cursor-closedhand.png
