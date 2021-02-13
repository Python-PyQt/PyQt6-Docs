.. sip:method-description::
    :status: todo
    :pysig: 55f552ea46303be11893a6cc458da50f
    :realsig: (QSessionManager::RestartHint)
    :digest: 1e1c7ddae45229149a695ad99ea25b39

Sets the application's restart hint to *hint*. On application startup, the hint is set to ``RestartIfRunning``.

**Note:** These flags are only hints, a session manager may or may not respect them.

We recommend setting the restart hint in :sip:ref:`~PyQt6.QtGui.QGuiApplication.saveStateRequest` because most session managers perform a checkpoint shortly after an application's startup.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSessionManager.restartHint`.
