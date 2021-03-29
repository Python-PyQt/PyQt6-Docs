.. sip:class-description::
    :status: todo
    :brief: Support for MIME-based drag and drop data transfer
    :digest: 74978fd3120b1181755af306ee743e66

The :sip:ref:`~PyQt6.QtGui.QDrag` class provides support for MIME-based drag and drop data transfer.

Drag and drop is an intuitive way for users to copy or move data around in an application, and is used in many desktop environments as a mechanism for copying data between applications. Drag and drop support in Qt is centered around the :sip:ref:`~PyQt6.QtGui.QDrag` class that handles most of the details of a drag and drop operation.

The data to be transferred by the drag and drop operation is contained in a :sip:ref:`~PyQt6.QtCore.QMimeData` object. This is specified with the :sip:ref:`~PyQt6.QtGui.QDrag.setMimeData` function in the following way:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-dragging-mainwindow.py
    :lines: 89-93

Note that :sip:ref:`~PyQt6.QtGui.QDrag.setMimeData` assigns ownership of the :sip:ref:`~PyQt6.QtCore.QMimeData` object to the :sip:ref:`~PyQt6.QtGui.QDrag` object. The :sip:ref:`~PyQt6.QtGui.QDrag` must be constructed on the heap with a parent :sip:ref:`~PyQt6.QtCore.QObject` to ensure that Qt can clean up after the drag and drop operation has been completed.

A pixmap can be used to represent the data while the drag is in progress, and will move with the cursor to the drop target. This pixmap typically shows an icon that represents the MIME type of the data being transferred, but any pixmap can be set with :sip:ref:`~PyQt6.QtGui.QDrag.setPixmap`. The cursor's hot spot can be given a position relative to the top-left corner of the pixmap with the :sip:ref:`~PyQt6.QtGui.QDrag.setHotSpot` function. The following code positions the pixmap so that the cursor's hot spot points to the center of its bottom edge:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-separations-finalwidget.py
    :lines: 119-120

**Note:** On X11, the pixmap may not be able to keep up with the mouse movements if the hot spot causes the pixmap to be displayed directly under the cursor.

The source and target widgets can be found with :sip:ref:`~PyQt6.QtGui.QDrag.source` and :sip:ref:`~PyQt6.QtGui.QDrag.target`. These functions are often used to determine whether drag and drop operations started and finished at the same widget, so that special behavior can be implemented.

:sip:ref:`~PyQt6.QtGui.QDrag` only deals with the drag and drop operation itself. It is up to the developer to decide when a drag operation begins, and how a :sip:ref:`~PyQt6.QtGui.QDrag` object should be constructed and used. For a given widget, it is often necessary to reimplement :sip:ref:`~PyQt6.QtWidgets.QWidget.mousePressEvent` to determine whether the user has pressed a mouse button, and reimplement :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseMoveEvent` to check whether a :sip:ref:`~PyQt6.QtGui.QDrag` is required.

.. seealso:: `Drag and Drop <https://doc.qt.io/qt-6/dnd.html>`_, :sip:ref:`~PyQt6.QtGui.QClipboard`, :sip:ref:`~PyQt6.QtCore.QMimeData`, `Draggable Icons Example <https://doc.qt.io/qt-6/qtwidgets-draganddrop-draggableicons-example.html>`_, `Draggable Text Example <https://doc.qt.io/qt-6/qtwidgets-draganddrop-draggabletext-example.html>`_, `Drop Site Example <https://doc.qt.io/qt-6/qtwidgets-draganddrop-dropsite-example.html>`_, `Fridge Magnets Example <https://doc.qt.io/qt-6/qtwidgets-draganddrop-fridgemagnets-example.html>`_.
