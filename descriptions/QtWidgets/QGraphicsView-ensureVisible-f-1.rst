.. sip:method-description::
    :status: todo
    :pysig: b27f89f0fc3e550dd72f5bd6c007a386
    :realsig: (const QGraphicsItem*,int,int)
    :digest: 217267d800176dcaba9dcc8c01048193

Scrolls the contents of the viewport so that the center of item *item* is visible, with margins specified in pixels by *xmargin* and *ymargin*. If the specified point cannot be reached, the contents are scrolled to the nearest valid position. The default value for both margins is 50 pixels.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.centerOn`.
