.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 57e85fc4cd9630add5af5fd67579f527

Scrolls the widget including its children *dx* pixels to the right and *dy* downward. Both *dx* and *dy* may be negative.

After scrolling, the widgets will receive paint events for the areas that need to be repainted. For widgets that Qt knows to be opaque, this is only the newly exposed parts. For example, if an opaque widget is scrolled 8 pixels to the left, only an 8-pixel wide stripe at the right edge needs updating.

Since widgets propagate the contents of their parents by default, you need to set the :sip:ref:`~PyQt6.QtWidgets.QWidget.autoFillBackground` property, or use :sip:ref:`~PyQt6.QtWidgets.QWidget.setAttribute` to set the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_OpaquePaintEvent` attribute, to make a widget opaque.

For widgets that use contents propagation, a scroll will cause an update of the entire scroll area.

.. seealso:: :ref:`qwidget-transparency-and-double-buffering`.
