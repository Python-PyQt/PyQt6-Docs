.. sip:method-description::
    :status: todo
    :pysig: 1cc65e25c37483dcea2376001c654842
    :realsig: (QKeySequence::StandardKey)
    :digest: a556d047717adedf83ab11c2c5b37ced

Sets a platform dependent list of shortcuts based on the *key*. The result of calling this function will depend on the currently running platform. Note that more than one shortcut can assigned by this action. If only the primary shortcut is required, use :sip:ref:`~PyQt6.QtGui.QAction.setShortcut` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QKeySequence.keyBindings`.
