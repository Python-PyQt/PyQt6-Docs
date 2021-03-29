.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realname: Qt3DInput::QAxisAccumulator::velocity
    :realsig: () const
    :digest: 0be929266b786c020227a7af83d60208

Returns the velocity. If the :sip:ref:`~PyQt6.Qt3DInput.QAxisAccumulator.sourceAxisType` is set to Velocity this is simply the value of the source axis multiplied by the scale. If the :sip:ref:`~PyQt6.Qt3DInput.QAxisAccumulator.sourceAxisType` is set to Acceleration, the velocity is integrated using the source axis' value as an acceleration.
