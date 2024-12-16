.. sip:method-description::
    :status: todo
    :pysig: 1cc65e25c37483dcea2376001c654842
    :realsig: (QKeySequence::StandardKey)
    :digest: 7e08bf629bbe1a4661ad6bf9d2e28149

Sets a platform dependent list of shortcuts based on the *key*. The result of calling this function will depend on the currently running platform. Note that more than one shortcut can assigned by this action. If only the primary shortcut is required, use :sip:ref:`~PyQt6.QtGui.QAction.setShortcut` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction.shortcuts`, :sip:ref:`~PyQt6.QtGui.QKeySequence.keyBindings`.
