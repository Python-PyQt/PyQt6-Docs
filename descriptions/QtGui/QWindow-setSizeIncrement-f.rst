.. sip:method-description::
    :status: todo
    :pysig: 364191bc772363d61cf96ad3eac70cf9
    :realsig: (const QSize&)
    :digest: 9b9fc522eca2352039efdf0a3f40042f

Sets the size increment (\ *size*) of the window.

When the user resizes the window, the size will move in steps of :sip:ref:`~PyQt6.QtGui.QWindow.sizeIncrement`.\ :sip:ref:`~PyQt6.QtGui.QWindow.width` pixels horizontally and :sip:ref:`~PyQt6.QtGui.QWindow.sizeIncrement`.\ :sip:ref:`~PyQt6.QtGui.QWindow.height` pixels vertically, with :sip:ref:`~PyQt6.QtGui.QWindow.baseSize` as the basis.

By default, this property contains a size with zero width and height.

The windowing system might not support size increments.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.sizeIncrement`, :sip:ref:`~PyQt6.QtGui.QWindow.setBaseSize`, :sip:ref:`~PyQt6.QtGui.QWindow.setMinimumSize`, :sip:ref:`~PyQt6.QtGui.QWindow.setMaximumSize`.
