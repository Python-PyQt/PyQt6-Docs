.. sip:method-description::
    :status: todo
    :pysig: 94202fb5c6fdbea937ba36a329c82d39
    :realsig: (const QSize&,QIcon::Mode,QIcon::State)
    :digest: 083e148b5d71bc348f2d53a9321fc88e

Returns the icon as a pixmap with the required *size*, *mode*, and *state*. The default implementation creates a new pixmap and calls :sip:ref:`~PyQt6.QtGui.QIconEngine.paint` to fill it.
