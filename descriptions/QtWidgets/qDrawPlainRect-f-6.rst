.. sip:method-description::
    :status: todo
    :pysig: 6b76c9f260b9b20a87eae292f9035b4f
    :realsig: (QPainter*, const QRect&, const QColor&, int, const QBrush*)
    :digest: 37c8a94ba3e063f9146c3bf45daf806e

Draws the plain rectangle specified by *rect* using the given *painter*, *lineColor* and *lineWidth*. The rectangle's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a plain rectangle:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 108-109

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawShadeRect`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
