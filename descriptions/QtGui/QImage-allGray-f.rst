.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 0235056e4363ec19b6994dba46fe52c3

Returns ``true`` if all the colors in the image are shades of gray (i.e. their red, green and blue components are equal); otherwise false.

Note that this function is slow for images without color table.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.isGrayscale`.
