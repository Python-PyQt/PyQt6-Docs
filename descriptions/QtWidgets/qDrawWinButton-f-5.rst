.. sip:method-description::
    :status: todo
    :pysig: f4e86ac5b584849db57da810d3d02979
    :realsig: (QPainter*, int, int, int, int, const QPalette&, bool, const QBrush*)
    :digest: 13d9f8e02f56aeaa1f812d41b29ef683

Draws the Windows-style button specified by the given point (\ *x*, *y*}, *width* and *height* using the provided *painter* with a line width of 2 pixels. The button's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

The given *palette* specifies the shading colors (\ :sip:ref:`~PyQt6.QtGui.QPalette.light`, :sip:ref:`~PyQt6.QtGui.QPalette.dark` and :sip:ref:`~PyQt6.QtGui.QPalette.mid` colors).

The button appears sunken if *sunken* is true, otherwise raised.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`-> Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawWinPanel`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
