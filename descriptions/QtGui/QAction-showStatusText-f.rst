.. sip:method-description::
    :status: todo
    :pysig: 830ce7af20f130367ad8a355a1b764ee
    :realsig: (QObject*)
    :digest: 4f2af7079a39e3667a1b5923c51f3039

Updates the relevant status bar for the UI represented by *object* by sending a :sip:ref:`~PyQt6.QtGui.QStatusTipEvent`. Returns ``true`` if an event was sent, otherwise returns ``false``.

If a null widget is specified, the event is sent to the action's parent.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction.statusTip`.
