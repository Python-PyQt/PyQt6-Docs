.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: b7a2346263cf54b5e6fb93cb2afe1e04

Returns the constraint value that is specific for the type of the length. If the length is :sip:ref:`~PyQt6.QtGui.QTextLength.Type.PercentageLength` then the raw value is in percent, in the range of 0 to 100. If the length is :sip:ref:`~PyQt6.QtGui.QTextLength.Type.FixedLength` then that fixed amount is returned. For variable lengths, zero is returned.
