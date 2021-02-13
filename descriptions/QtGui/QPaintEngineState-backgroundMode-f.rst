.. sip:method-description::
    :status: todo
    :pysig: 36c849f247726a19e90226b56f53d2bd
    :realsig: () const
    :digest: 4f7f59a8504fc6fd755516bd33a26fa6

Returns the background mode in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyBackgroundMode` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
