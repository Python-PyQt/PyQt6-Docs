.. sip:method-description::
    :status: todo
    :pysig: b53df27f41e7e1e87eded6e72ecfdeb9
    :realsig: () const
    :digest: abfadf3eb380a235ef5d08ac5b75bf0a

Returns the clip path in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyClipPath` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
