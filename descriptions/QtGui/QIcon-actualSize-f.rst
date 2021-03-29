.. sip:method-description::
    :status: todo
    :pysig: 5609f2728da4b41ed5cd2c2a1050dd4c
    :realsig: (const QSize&,QIcon::Mode,QIcon::State) const
    :digest: 902375f93a2a8176e2f87c2f669d68d5

Returns the actual size of the icon for the requested *size*, *mode*, and *state*. The result might be smaller than requested, but never larger. The returned size is in device-independent pixels (This is relevant for high-dpi pixmaps.)

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.pixmap`, :sip:ref:`~PyQt6.QtGui.QIcon.paint`.
