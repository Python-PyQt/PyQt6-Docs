.. sip:method-description::
    :status: todo
    :pysig: 3d07276bfda601d69bcad0b66c9bdaad
    :realsig: (const QWidget*)
    :digest: b7062eb0d3f06db5acf1919b0e207194

Creates a proxy widget for the given *child* of the widget contained in this proxy.

You should not call this function directly; use :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.createProxyForChildWidget` instead.

This function is a fake virtual slot that you can reimplement in your subclass in order to control how new proxy widgets are created. The default implementation returns a proxy created with the :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget` constructor with this proxy widget as the parent.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.createProxyForChildWidget`.
