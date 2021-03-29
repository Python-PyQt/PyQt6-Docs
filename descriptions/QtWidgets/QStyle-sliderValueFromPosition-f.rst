.. sip:method-description::
    :status: todo
    :pysig: d6682dcf3fb2cf7037722cb679819ca4
    :realsig: (int,int,int,int,bool)
    :digest: 842a1deef8c4515554c03e88736438e1

Converts the given pixel *position* to a logical value. 0 maps to the *min* parameter, *span* maps to *max* and other values are distributed evenly in-between.

This function can handle the entire integer range without overflow.

By default, this function assumes that the maximum value is on the right for horizontal items and on the bottom for vertical items. Set the *upsideDown* parameter to true to reverse this behavior.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyle.sliderPositionFromValue`.
