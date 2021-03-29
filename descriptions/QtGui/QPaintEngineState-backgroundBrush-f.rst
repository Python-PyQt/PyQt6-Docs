.. sip:method-description::
    :status: todo
    :pysig: e5e9a29a67ac7eb0925abe849396e0b8
    :realsig: () const
    :digest: 1e6a53bc3195dfb5b7d8e8ac66c15c68

Returns the background brush in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyBackground` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
