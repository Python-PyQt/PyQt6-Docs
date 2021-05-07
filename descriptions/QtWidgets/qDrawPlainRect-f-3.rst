.. sip:method-description::
    :status: todo
    :pysig: 64cdf13ff248c9aea7635617b4dfdb58
    :realsig: (QPainter*,int,int,int,int,const QColor&,int,const QBrush*)
    :digest: 35bb9aa2751e7fab952a495d65a9e751

Draws the plain rectangle beginning at (\ *x*, *y*) with the given *width* and *height*, using the specified *painter*, *lineColor* and *lineWidth*. The rectangle's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a plain rectangle:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 78-79

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawShadeRect`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
