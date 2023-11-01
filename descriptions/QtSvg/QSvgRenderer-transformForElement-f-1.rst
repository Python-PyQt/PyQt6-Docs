.. sip:method-description::
    :status: todo
    :pysig: da64b91a271aff5e81fad991446df3a7
    :realsig: (const QString&) const
    :digest: 827c7637976c05ae99051eabed33a20c

Returns the transformation matrix for the element with the given *id*. The matrix is a product of the transformation of the element's parents. The transformation of the element itself is not included.

To find the bounding rectangle of the element in logical coordinates, you can apply the matrix on the rectangle returned from :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.boundsOnElement`.

.. seealso:: :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.boundsOnElement`.
