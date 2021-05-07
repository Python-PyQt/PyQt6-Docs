.. sip:method-description::
    :status: todo
    :pysig: b186c98119d2d8ea8ad4c5938de49443
    :realsig: () const
    :digest: dd56ff9df898dce2343fc0dc34bcfd9f

Returns the render hints in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlag.DirtyHints` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
