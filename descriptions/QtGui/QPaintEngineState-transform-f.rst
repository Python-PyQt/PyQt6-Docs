.. sip:method-description::
    :status: todo
    :pysig: e27247e5b452ce98dcfc93f19679f890
    :realsig: () const
    :digest: 489d1d0cfe1db009cd4a5424033aeca2

Returns the matrix in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyTransform` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
