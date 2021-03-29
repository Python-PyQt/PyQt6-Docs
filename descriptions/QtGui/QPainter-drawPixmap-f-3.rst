.. sip:method-description::
    :status: todo
    :pysig: 86da322082b07e15a8a8e4280193c350
    :realsig: (const QRectF&,const QPixmap&,const QRectF&)
    :digest: c1d8ccb95627ba4f0edf5500c5a84ee0

Draws the rectangular portion *source* of the given *pixmap* into the given *target* in the paint device.

**Note:** The pixmap is scaled to fit the rectangle, if both the pixmap and rectangle size disagree.

**Note:** See :ref:`qpainter-drawing-high-resolution-versions-of-pixmaps-and-images` on how this is affected by :sip:ref:`~PyQt6.QtGui.QPixmap.devicePixelRatio`.

+-----------------------------------------------------------------------------------------------------+
| .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|     :lines: 308-313                                                                                 |
+-----------------------------------------------------------------------------------------------------+

If *pixmap* is a `QBitmap <https://doc.qt.io/qt-6/gui-changes-qt6.html#qbitmap>`_ it is drawn with the bits that are "set" using the pens color. If :sip:ref:`~PyQt6.QtGui.QPainter.backgroundMode` is :sip:ref:`~PyQt6.QtCore.Qt.BGMode.OpaqueMode`, the "unset" bits are drawn using the color of the background brush; if :sip:ref:`~PyQt6.QtGui.QPainter.backgroundMode` is :sip:ref:`~PyQt6.QtCore.Qt.BGMode.TransparentMode`, the "unset" bits are transparent. Drawing bitmaps with gradient or texture colors is not supported.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawImage`, :sip:ref:`~PyQt6.QtGui.QPixmap.devicePixelRatio`.
