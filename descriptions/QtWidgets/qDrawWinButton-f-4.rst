.. sip:method-description::
    :status: todo
    :pysig: da37cdac6d241ccc9401262bf399d7e7
    :realsig: (QPainter*, const QRect&, const QPalette&, bool, const QBrush*)
    :digest: 488261f68c63f71b0f2e67262eda9aeb

This is an overloaded function.

Draws the Windows-style button at the rectangle specified by *rect* using the given *painter* with a line width of 2 pixels. The button's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

The given *palette* specifies the shading colors (\ :sip:ref:`~PyQt6.QtGui.QPalette.light`, :sip:ref:`~PyQt6.QtGui.QPalette.dark` and :sip:ref:`~PyQt6.QtGui.QPalette.mid` colors).

The button appears sunken if *sunken* is true, otherwise raised.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`-> Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawWinPanel`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
