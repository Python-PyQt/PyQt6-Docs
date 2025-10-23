.. sip:method-description::
    :status: todo
    :pysig: 57b724016b3a99354a16ea4fedbe701f
    :realsig: (QPainter*, const QRect&, const QPalette&, bool, int, const QBrush*)
    :digest: e6971b9ecd48641c9a9100eabadf96ee

Draws the shaded panel at the rectangle specified by *rect* using the given *painter* and the given *lineWidth*.

The given *palette* specifies the shading colors (\ :sip:ref:`~PyQt6.QtGui.QPalette.light`, :sip:ref:`~PyQt6.QtGui.QPalette.dark` and :sip:ref:`~PyQt6.QtGui.QPalette.mid` colors). The panel's interior is filled with the *fill* brush unless *fill* is ``nullptr``.

The panel appears sunken if *sunken* is true, otherwise raised.

**Warning:** This function does not look at :sip:ref:`~PyQt6.QtWidgets.QWidget.style` or :sip:ref:`~PyQt6.QtWidgets.QApplication.style`. Use the drawing functions in :sip:ref:`~PyQt6.QtWidgets.QStyle` to make widgets that follow the current GUI style.

Alternatively you can use a :sip:ref:`~PyQt6.QtWidgets.QFrame` widget and apply the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function to display a shaded panel:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_painting_qdrawutil.py
    :lines: 96-97

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.qDrawWinPanel`, :sip:ref:`~PyQt6.QtWidgets.qDrawShadeLine`, :sip:ref:`~PyQt6.QtWidgets.qDrawShadeRect`, :sip:ref:`~PyQt6.QtWidgets.QStyle`.
