.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: dde560237838902067869a353a639993

Returns the current session's identifier.

If the application has been restored from an earlier session, this identifier is the same as it was in that previous session. The session identifier is guaranteed to be unique both for different applications and for different instances of the same application.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.isSessionRestored`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.sessionKey`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.saveStateRequest`.
