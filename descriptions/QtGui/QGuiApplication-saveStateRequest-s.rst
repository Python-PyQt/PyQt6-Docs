.. sip:signal-description::
    :status: todo
    :pysig: 1acb94ce3abc6bce1ee08a2c6dbcc427
    :realsig: (QSessionManager&)
    :digest: 0a0f589767219ef7977e838b9a6e8eab

This signal deals with session management. It is invoked when the :sip:ref:`~PyQt6.QtGui.QSessionManager` wants the application to preserve its state for a future session.

For example, a text editor would create a temporary file that includes the current contents of its edit buffers, the location of the cursor and other aspects of the current editing session.

You should never exit the application within this signal. Instead, the session manager may or may not do this afterwards, depending on the context. Furthermore, most session managers will very likely request a saved state immediately after the application has been started. This permits the session manager to learn about the application's restart policy.

**Warning:** Within this signal, no user interaction is possible, *unless* you ask the *manager* for explicit permission. See :sip:ref:`~PyQt6.QtGui.QSessionManager.allowsInteraction` and :sip:ref:`~PyQt6.QtGui.QSessionManager.allowsErrorInteraction` for details.

**Note:** You should use :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.DirectConnection` when connecting to this signal.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.isSessionRestored`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.sessionId`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest`.
