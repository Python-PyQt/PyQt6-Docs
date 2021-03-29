.. sip:method-description::
    :status: todo
    :pysig: 7b302619a1f8d21d9efa913403e8d56b
    :realsig: () const
    :digest: a18254ff2e4dfe4e52ecf71462b848fd

Returns the clip region in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyClipRegion` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
