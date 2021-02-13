.. sip:method-description::
    :status: todo
    :pysig: 59d522e2b645f1f78264c495a0d39146
    :realsig: () const
    :digest: 36bcab9e716c657373abb5283d8baf3f

Returns the font in the current paint engine state.

This variable should only be used when the :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state` returns a combination which includes the :sip:ref:`~PyQt6.QtGui.QPaintEngine.DirtyFlags.DirtyFont` flag.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPaintEngineState.state`, :sip:ref:`~PyQt6.QtGui.QPaintEngine.updateState`.
