.. sip:method-description::
    :status: todo
    :pysig: a77d2b369853efffedd50727698d13d9
    :realsig: (QSizePolicy::ControlTypes,QSizePolicy::ControlTypes,Qt::Orientation,QStyleOption*,QWidget*) const
    :digest: 8727411fbf787ebfa456cb6cbaa017b8

Returns the spacing that should be used between *controls1* and *controls2* in a layout. *orientation* specifies whether the controls are laid out side by side or stacked vertically. The *option* parameter can be used to pass extra information about the parent widget. The *widget* parameter is optional and can also be used if *option* is ``nullptr``.

*controls1* and *controls2* are OR-combination of zero or more control types.

This function is called by the layout system. It is used only if :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutHorizontalSpacing` or :sip:ref:`~PyQt6.QtWidgets.QStyle.PixelMetric.PM_LayoutVerticalSpacing` returns a negative value.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyle.layoutSpacing`.
