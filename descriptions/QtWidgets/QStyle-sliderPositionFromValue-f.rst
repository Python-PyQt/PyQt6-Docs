.. sip:method-description::
    :status: todo
    :pysig: d6682dcf3fb2cf7037722cb679819ca4
    :realsig: (int,int,int,int,bool)
    :digest: e104920116e6a6bcc6bf17c4f69235b3

Converts the given *logicalValue* to a pixel position. The *min* parameter maps to 0, *max* maps to *span* and other values are distributed evenly in-between.

This function can handle the entire integer range without overflow, providing that *span* is less than 4096.

By default, this function assumes that the maximum value is on the right for horizontal items and on the bottom for vertical items. Set the *upsideDown* parameter to true to reverse this behavior.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyle.sliderValueFromPosition`.
