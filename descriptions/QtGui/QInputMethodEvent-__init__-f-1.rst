.. sip:method-description::
    :status: todo
    :pysig: aefbe0aa64d3fd16e58b9fef3fdab3ac
    :realsig: (const QString&, const QList<QInputMethodEvent::Attribute>&)
    :digest: b709bfb3344d472c7e4f34dc3a15e5ac

Constructs an event of type :sip:ref:`~PyQt6.QtCore.QEvent.Type.InputMethod`. The preedit text is set to *preeditText*, the attributes to *attributes*.

The :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.commitString`, :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.replacementStart`, and :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.replacementLength` values can be set using :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.setCommitString`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.preeditString`, :sip:ref:`~PyQt6.QtGui.QInputMethodEvent.attributes`.
