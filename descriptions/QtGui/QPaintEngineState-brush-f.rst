.. sip:method-description::
    :status: todo
    :pysig: e5e9a29a67ac7eb0925abe849396e0b8
    :realsig: () const
    :digest: e6da663620e8a6c6d16c76aa739bb201

Returns the brush in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyBrush` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
