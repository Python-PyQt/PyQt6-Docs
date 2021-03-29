.. sip:method-description::
    :status: todo
    :pysig: 72df7f1445486f5d07187f44ac1ffef5
    :realsig: (const QPoint&)
    :digest: 1c7ab661d18d20f0819c1f18e5c66e1b

Returns the screen at *point*, or ``nullptr`` if outside of any screen.

The *point* is in relation to the virtualGeometry() of each set of virtual siblings. If the point maps to more than one set of virtual siblings the first match is returned. If you wish to search only the virtual desktop siblings of a known screen (for example siblings of the screen of your application window ``QWidget::windowHandle()->screen()``), use :sip:ref:`~PyQt6.QtGui.QScreen.virtualSiblingAt`.
