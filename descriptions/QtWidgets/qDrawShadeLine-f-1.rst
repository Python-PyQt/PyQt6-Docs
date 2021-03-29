.. sip:method-description::
    :status: todo
    :pysig: c60a0e3dc70db1c5f069a1aaf527afe5
    :realsig: (QPainter*,int,int,int,int,const QPalette&,bool,int,int)
    :digest: e14759059cef64126a49ceff1ead2ef2

Draws a horizontal (\ *y1* == *y2*) or vertical (\ *x1* == *x2*) shaded line using the given *painter*. Note that nothing is drawn if *y1* != *y2* and *x1* != *x2* (i.e. the line is neither horizontal nor vertical).

The provided *palette* specifies the shading colors (\ :sip:ref:`~PyQt6.QtGui.QPalette.light`, :sip:ref:`~PyQt6.QtGui.QPalette.dark` and :sip:ref:`~PyQt6.QtGui.QPalette.mid` colors). The given *lineWidth* specifies the line width for each of the lines; it is not the total line width. The given *midLineWidth* specifies the width of a middle line drawn in the :sip:ref:`~PyQt6.QtGui.QPalette.mid` color.

The line appears sunken if *sunken* is true, otherwise raised.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a shaded line:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 54-55

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawShadeRect`, :sip:ref:`~PyQt6.QtWidgets.qDrawShadePanel`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
