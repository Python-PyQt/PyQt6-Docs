.. sip:method-description::
    :status: todo
    :pysig: a6ff8e8f447009dbee17bad3a730ef1a
    :realsig: (QWindow::AncestorMode) const
    :digest: 37ea8fb813796b925815851bcc5321fe

Returns the parent window, if any.

If *mode* is :sip:ref:`~PyQt6.QtGui.QWindow.AncestorMode.IncludeTransients`, then the transient parent is returned if there is no parent.

A window without a parent is known as a top level window.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.setParent`.
