.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 8d1a78e8c6a98b91ab1e998d74240ddd

Returns the session key in the current session.

If the application has been restored from an earlier session, this key is the same as it was when the previous session ended.

The session key changes with every call of commitData() or saveState().

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSessionManager.sessionId`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.sessionKey`.
