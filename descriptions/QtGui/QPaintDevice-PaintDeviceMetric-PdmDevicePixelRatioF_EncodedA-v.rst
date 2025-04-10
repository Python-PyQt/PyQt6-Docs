.. sip:enum-member-description::
    :status: todo
    :value: 13
    :digest: 4ca9e8f7767a063e5177e82b3dd7f684

This enum item, together with the corresponding ``B`` item, are used together for the device pixel ratio of the device, as an encoded ``double`` floating point value. A :sip:ref:`~PyQt6.QtGui.QPaintDevice` subclass that supports *fractional* DPR values should implement support for these two enum items in its override of the :sip:ref:`~PyQt6.QtGui.QPaintDevice.metric` function. The return value is expected to be the result of the encodeMetricF() function.
