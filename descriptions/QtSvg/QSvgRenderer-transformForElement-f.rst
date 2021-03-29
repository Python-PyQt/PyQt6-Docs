.. sip:method-description::
    :status: todo
    :pysig: 4d87a83bb4e3720149b16a24d18592a4
    :realsig: (const QString&) const
    :digest: 827c7637976c05ae99051eabed33a20c

Returns the transformation matrix for the element with the given *id*. The matrix is a product of the transformation of the element's parents. The transformation of the element itself is not included.

To find the bounding rectangle of the element in logical coordinates, you can apply the matrix on the rectangle returned from :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.boundsOnElement`.

.. seealso:: :sip:ref:`~PyQt6.QtSvg.QSvgRenderer.boundsOnElement`.
