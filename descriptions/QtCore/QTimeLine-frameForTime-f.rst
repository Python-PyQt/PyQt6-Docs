.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int) const
    :digest: b231572e1f955004c39e48f72b66be7e

Returns the frame corresponding to the time *msec*. This value is calculated using a linear interpolation of the start and end frame, based on the value returned by :sip:ref:`~PyQt6.QtCore.QTimeLine.valueForTime`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTimeLine.valueForTime`, :sip:ref:`~PyQt6.QtCore.QTimeLine.setFrameRange`.
