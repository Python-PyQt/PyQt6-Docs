.. sip:method-description::
    :status: todo
    :pysig: fc73313c79072cfe284468612e19acb7
    :realsig: (int,int,const QPolygon&,int)
    :digest: 1b96dc891a13ed21d4674b25dc98c5d2

Copies *nPoints* points from the given *fromIndex* ( 0 by default) in *fromPolygon* into this polygon, starting at the specified *index*. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-polygon-polygon.py
    :lines: 110-119
