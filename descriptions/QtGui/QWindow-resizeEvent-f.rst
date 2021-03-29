.. sip:method-description::
    :status: todo
    :pysig: c956f297e3f17e0e0de95e2e5b46c3ee
    :realsig: (QResizeEvent*)
    :digest: f7d163acb960eb8e06c065a86e3f9c53

Override this to handle resize events (\ *ev*).

The resize event is called whenever the window is resized in the windowing system, either directly through the windowing system acknowledging a :sip:ref:`~PyQt6.QtGui.QWindow.setGeometry` or :sip:ref:`~PyQt6.QtGui.QWindow.resize` request, or indirectly through the user resizing the window manually.
