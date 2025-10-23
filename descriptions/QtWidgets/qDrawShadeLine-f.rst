.. sip:method-description::
    :status: todo
    :pysig: 31e5fee707a272e34d2a04093c77a51f
    :realsig: (QPainter*,const QPoint&,const QPoint&,const QPalette&,bool,int,int)
    :digest: 8d82823f81bf02148932ac4d1c8e7d67

Draws a horizontal or vertical shaded line between *p1* and *p2* using the given *painter*. Note that nothing is drawn if the line between the points would be neither horizontal nor vertical.

The provided *palette* specifies the shading colors (\ :sip:ref:`~PyQt6.QtGui.QPalette.light`, :sip:ref:`~PyQt6.QtGui.QPalette.dark` and :sip:ref:`~PyQt6.QtGui.QPalette.mid` colors). The given *lineWidth* specifies the line width for each of the lines; it is not the total line width. The given *midLineWidth* specifies the width of a middle line drawn in the :sip:ref:`~PyQt6.QtGui.QPalette.mid` color.

The line appears sunken if *sunken* is true, otherwise raised.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a shaded line:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 84-85

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawShadeRect`, :sip:ref:`~PyQt6.QtWidgets.qDrawShadePanel`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
