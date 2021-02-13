.. sip:method-description::
    :status: todo
    :pysig: a5ea1d3ab96bd0315a9bec805e2f30cb
    :realsig: (const QPixmap&,QIcon::Mode,QIcon::State)
    :digest: 95a2f48210de2631ecdaa9308119e67b

Called by :sip:ref:`~PyQt6.QtGui.QIcon.addPixmap`. Adds a specialized *pixmap* for the given *mode* and *state*. The default pixmap-based engine stores any supplied pixmaps, and it uses them instead of scaled pixmaps if the size of a pixmap matches the size of icon requested. Custom icon engines that implement scalable vector formats are free to ignores any extra pixmaps.
