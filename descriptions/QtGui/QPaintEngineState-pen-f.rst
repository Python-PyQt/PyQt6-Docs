.. sip:method-description::
    :status: todo
    :pysig: 404eeefe058485406f13ef5f77667770
    :realsig: () const
    :digest: 1f66a4428b63c0cd4e69ae34828b4551

Returns the pen in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyPen` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
