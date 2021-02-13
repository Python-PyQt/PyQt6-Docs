.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 64b2fa0aa7159a9b9f90aec837ba1b76

Returns the session key in the current session.

If the application has been restored from an earlier session, this key is the same as it was when the previous session ended.

The session key changes every time the session is saved. If the shutdown process is cancelled, another session key will be used when shutting down again.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.isSessionRestored`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.sessionId`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.saveStateRequest`.
