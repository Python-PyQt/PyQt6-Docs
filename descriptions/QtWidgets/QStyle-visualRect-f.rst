.. sip:method-description::
    :status: todo
    :pysig: b3d28ff573768f268f9e893edfedca85
    :realsig: (Qt::LayoutDirection,const QRect&,const QRect&)
    :digest: eab4b49850050580214376a62eeee13b

Returns the given *logicalRectangle* converted to screen coordinates based on the specified *direction*. The *boundingRectangle* is used when performing the translation.

This function is provided to support right-to-left desktops, and is typically used in implementations of the :sip:ref:`~PyQt6.QtWidgets.QStyle.subControlRect` function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.layoutDirection`.
