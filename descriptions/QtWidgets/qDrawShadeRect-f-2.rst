.. sip:method-description::
    :status: todo
    :pysig: 28af627829cb732ec83a661532983c19
    :realsig: (QPainter*,const QRect&,const QPalette&,bool,int,int,const QBrush*)
    :digest: d527125cd4aef26132caa84fda92e675

This is an overloaded function.

Draws the shaded rectangle specified by *rect* using the given *painter*.

The provide *palette* specifies the shading colors (\ :sip:ref:`~PyQt6.QtGui.QPalette.light`, :sip:ref:`~PyQt6.QtGui.QPalette.dark` and :sip:ref:`~PyQt6.QtGui.QPalette.mid` colors. The given *lineWidth* specifies the line width for each of the lines; it is not the total line width. The *midLineWidth* specifies the width of a middle line drawn in the :sip:ref:`~PyQt6.QtGui.QPalette.mid` color. The rectangle's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

The rectangle appears sunken if *sunken* is true, otherwise raised.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a shaded rectangle:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 90-91

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawShadeLine`, :sip:ref:`~PyQt6.QtWidgets.qDrawShadePanel`, :sip:ref:`~PyQt6.QtWidgets.qDrawPlainRect`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
