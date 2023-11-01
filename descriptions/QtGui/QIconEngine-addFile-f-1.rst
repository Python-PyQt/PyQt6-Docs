.. sip:method-description::
    :status: todo
    :pysig: 05cad792483ee8bd374f75d3b15e3680
    :realsig: (const QString&, const QSize&, QIcon::Mode, QIcon::State)
    :digest: 588ead42b8ca71f3c78b703b331ec574

Called by :sip:ref:`~PyQt6.QtGui.QIcon.addFile`. Adds a specialized pixmap from the file with the given *fileName*, *size*, *mode* and *state*. The default pixmap-based engine stores any supplied file names, and it loads the pixmaps on demand instead of using scaled pixmaps if the size of a pixmap matches the size of icon requested. Custom icon engines that implement scalable vector formats are free to ignores any extra files.
