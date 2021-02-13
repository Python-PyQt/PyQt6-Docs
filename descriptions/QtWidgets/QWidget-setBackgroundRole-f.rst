.. sip:method-description::
    :status: todo
    :pysig: 03d0b15e47fff6689293c04492f03309
    :realsig: (QPalette::ColorRole)
    :digest: 04995560390bfc68b46098888a49ab5f

Sets the background role of the widget to *role*.

The background role defines the brush from the widget's :sip:ref:`~PyQt6.QtWidgets.QWidget.palette` that is used to render the background.

If *role* is :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole.NoRole`, then the widget inherits its parent's background role.

Note that styles are free to choose any color from the palette. You can modify the palette or set a style sheet if you don't achieve the result you want with .

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.backgroundRole`, :sip:ref:`~PyQt6.QtWidgets.QWidget.foregroundRole`.
