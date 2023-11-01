.. sip:method-description::
    :status: todo
    :pysig: f4e86ac5b584849db57da810d3d02979
    :realsig: (QPainter*, int, int, int, int, const QPalette&, bool, const QBrush*)
    :digest: bedd36a6430d7b3a2aaabf6ccecce0d3

Draws the Windows-style panel specified by the given point(\ *x*, *y*), *width* and *height* using the provided *painter* with a line width of 2 pixels. The button's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

The given *palette* specifies the shading colors. The panel appears sunken if *sunken* is true, otherwise raised.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a shaded panel:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 72-73

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawShadePanel`, :sip:ref:`~PyQt6.QtWidgets.qDrawWinButton`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
