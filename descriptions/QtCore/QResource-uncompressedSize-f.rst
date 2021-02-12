.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: e18525942a8cc07244501d8e6e7c8b89

Returns the size of the data in this resource. If the data was not compressed, this function returns the same as :sip:ref:`~PyQt6.QtCore.QResource.size`. If it was, then this function extracts the size of the original uncompressed data from the stored stream.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QResource.size`, :sip:ref:`~PyQt6.QtCore.QResource.uncompressedData`, :sip:ref:`~PyQt6.QtCore.QResource.isFile`.
