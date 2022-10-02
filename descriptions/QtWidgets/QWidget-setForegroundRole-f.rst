.. sip:method-description::
    :status: todo
    :pysig: 03d0b15e47fff6689293c04492f03309
    :realsig: (QPalette::ColorRole)
    :digest: e7711d51af4a22e3570d9c2610097180

Sets the foreground role of the widget to *role*.

The foreground role defines the color from the widget's :sip:ref:`~PyQt6.QtWidgets.QWidget.palette` that is used to draw the foreground.

If *role* is :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole.NoRole`, the widget uses a foreground role that contrasts with the background role.

Note that styles are free to choose any color from the palette. You can modify the palette or set a style sheet if you don't achieve the result you want with setForegroundRole().

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.foregroundRole`, :sip:ref:`~PyQt6.QtWidgets.QWidget.backgroundRole`.
