.. sip:method-description::
    :status: todo
    :pysig: fc73313c79072cfe284468612e19acb7
    :realsig: (int,int,const QPolygon&,int)
    :digest: 94247e82d49c93d522dde43012f8f7f0

This is an overloaded function.

Copies *nPoints* points from the given *fromIndex* ( 0 by default) in *fromPolygon* into this polygon, starting at the specified *index*. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-polygon-polygon.py
    :lines: 110-119
