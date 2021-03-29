.. sip:method-description::
    :status: todo
    :pysig: 18fbe481efdcd25ae0348ae6d98c2c6f
    :realsig: () const
    :digest: 4e1ca97d7995fa520db115add8198664

Returns the clip operation in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes either the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyClipPath` or the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyClipRegion` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
