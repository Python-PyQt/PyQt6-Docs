.. sip:method-description::
    :status: todo
    :pysig: 3d07276bfda601d69bcad0b66c9bdaad
    :realsig: (QWidget*)
    :digest: 804830e4cc1d7832afd02aafd229a581

Creates a proxy widget for the given *child* of the widget contained in this proxy.

This function makes it possible to acquire proxies for non top-level widgets. For instance, you can embed a dialog, and then transform only one of its widgets.

If the widget is already embedded, return the existing proxy widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget.newProxyWidget`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.addWidget`.
