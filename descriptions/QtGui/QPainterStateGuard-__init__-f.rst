.. sip:method-description::
    :status: todo
    :pysig: 46e6ff17a2a6e4a785b51753b77c25fd
    :realsig: (QPainter*, QPainterStateGuard::InitialState)
    :digest: ef4f881a80d8ebe9bf226edcac9393f1

Constructs a :sip:ref:`~PyQt6.QtGui.QPainterStateGuard` and calls :sip:ref:`~PyQt6.QtGui.QPainterStateGuard.save` on *painter* if *state* is ``InitialState::Save`` (which is the default). When :sip:ref:`~PyQt6.QtGui.QPainterStateGuard` is destroyed, :sip:ref:`~PyQt6.QtGui.QPainterStateGuard.restore` is called as often as :sip:ref:`~PyQt6.QtGui.QPainterStateGuard.save` was called to restore the :sip:ref:`~PyQt6.QtGui.QPainter`'s state.
