.. sip:method-description::
    :status: todo
    :pysig: 36c849f247726a19e90226b56f53d2bd
    :realsig: (Qt::BGMode)
    :digest: b0fd165c8579517a2967833ee54a57bd

Sets the background mode of the painter to the given *mode*

:sip:ref:`~PyQt6.QtCore.Qt.BGMode.TransparentMode` (the default) draws stippled lines and text without setting the background pixels. :sip:ref:`~PyQt6.QtCore.Qt.BGMode.OpaqueMode` fills these space with the current background color.

Note that in order to draw a bitmap or pixmap transparently, you must use :sip:ref:`~PyQt6.QtGui.QPixmap.setMask`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.backgroundMode`, :sip:ref:`~PyQt6.QtGui.QPainter.setBackground`, Settings.
