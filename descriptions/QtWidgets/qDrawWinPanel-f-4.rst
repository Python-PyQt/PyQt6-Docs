.. sip:method-description::
    :status: todo
    :pysig: da37cdac6d241ccc9401262bf399d7e7
    :realsig: (QPainter*, const QRect&, const QPalette&, bool, const QBrush*)
    :digest: e64801dfb9f4118bb9ac283a958f6d40

This is an overloaded function.

Draws the Windows-style panel at the rectangle specified by *rect* using the given *painter* with a line width of 2 pixels. The button's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

The given *palette* specifies the shading colors. The panel appears sunken if *sunken* is true, otherwise raised.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a shaded panel:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 102-103

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawShadePanel`, :sip:ref:`~PyQt6.QtWidgets.qDrawWinButton`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
