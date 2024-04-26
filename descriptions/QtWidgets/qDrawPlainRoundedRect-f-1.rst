.. sip:method-description::
    :status: todo
    :pysig: 367e12cfab07b4fd6fba7def5166d89d
    :realsig: (QPainter*, int, int, int, int, qreal, qreal, const QColor&, int, const QBrush*)
    :digest: a78d8ab1f2818a6e359da713f00b3177

Draws the plain rounded rectangle beginning at (\ *x*, *y*) with the given *width* and *height*, using the horizontal *rx* and vertical radius *ry*, specified *painter*, *lineColor* and *lineWidth*. The rectangle's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a plain rectangle:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 78-79

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawShadeRect`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
