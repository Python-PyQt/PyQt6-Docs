.. sip:method-description::
    :status: todo
    :pysig: f4d554c305231c9f48fe291dbcc8d247
    :realsig: () const
    :digest: dd56ff9df898dce2343fc0dc34bcfd9f

Returns the render hints in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyHints` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
