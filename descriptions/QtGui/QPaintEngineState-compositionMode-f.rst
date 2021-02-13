.. sip:method-description::
    :status: todo
    :pysig: 00a5108bcf814b9a5ef3d14b7027ad99
    :realsig: () const
    :digest: 9ff2fb2c008bd9b754cdaa2564f427f2

Returns the composition mode in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyCompositionMode` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
