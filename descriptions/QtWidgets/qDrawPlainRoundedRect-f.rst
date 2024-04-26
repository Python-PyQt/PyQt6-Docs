.. sip:method-description::
    :status: todo
    :pysig: 321f81dae855816fa9d4729da09c30a0
    :realsig: (QPainter*, const QRect&, qreal, qreal, const QColor&, int, const QBrush*)
    :digest: 7b29bc8fcda5e9cc2ec5465ea7e3a2c7

This is an overloaded function.

Draws the plain rectangle specified by *rect* using the horizontal *rx* and vertical radius *ry*, the given *painter*, *lineColor* and *lineWidth*. The rectangle's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a plain rectangle:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 108-109

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawShadeRect`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
