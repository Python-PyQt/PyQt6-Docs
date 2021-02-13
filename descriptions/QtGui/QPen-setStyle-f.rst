.. sip:method-description::
    :status: todo
    :pysig: a629ee3653af5528635a1ee28a0bc8df
    :realsig: (Qt::PenStyle)
    :digest: 7342b0e0df3d9339f245cbeef176a03e

Sets the pen style to the given *style*.

See the :sip:ref:`~PyQt6.QtCore.Qt.PenStyle` documentation for a list of the available styles. Since Qt 4.1 it is also possible to specify a custom dash pattern using the :sip:ref:`~PyQt6.QtGui.QPen.setDashPattern` function which implicitly converts the style of the pen to :sip:ref:`~PyQt6.QtCore.Qt.PenStyle.CustomDashLine`.

**Note:** This function resets the dash offset to zero.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPen.style`, Pen Style.
