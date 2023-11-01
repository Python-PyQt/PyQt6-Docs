.. sip:method-description::
    :status: todo
    :pysig: f9f12bc8a24fad21a1b73d7e74072c48
    :realsig: (QPainter*, int, int, int, int, const QPalette&, bool, int, int, const QBrush*)
    :digest: e438216b147c0cfc723a4cf3e7eb85dc

Draws the shaded rectangle beginning at (\ *x*, *y*) with the given *width* and *height* using the provided *painter*.

The provide *palette* specifies the shading colors (\ :sip:ref:`~PyQt6.QtGui.QPalette.light`, :sip:ref:`~PyQt6.QtGui.QPalette.dark` and :sip:ref:`~PyQt6.QtGui.QPalette.mid` colors. The given *lineWidth* specifies the line width for each of the lines; it is not the total line width. The *midLineWidth* specifies the width of a middle line drawn in the :sip:ref:`~PyQt6.QtGui.QPalette.mid` color. The rectangle's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

The rectangle appears sunken if *sunken* is true, otherwise raised.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a shaded rectangle:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 60-61

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawShadeLine`, :sip:ref:`~PyQt6.QtWidgets.qDrawShadePanel`, :sip:ref:`~PyQt6.QtWidgets.qDrawPlainRect`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
