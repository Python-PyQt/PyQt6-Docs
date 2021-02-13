.. sip:method-description::
    :status: todo
    :pysig: 3955508ccb28ae90f06877bd877a600e
    :realsig: (const QRectF&,int,int)
    :digest: aeace6e5634f436a38b8c401f6e91fd8

Scrolls the contents of the viewport so that the scene rectangle *rect* is visible, with margins specified in pixels by *xmargin* and *ymargin*. If the specified rect cannot be reached, the contents are scrolled to the nearest valid position. The default value for both margins is 50 pixels.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.centerOn`.
