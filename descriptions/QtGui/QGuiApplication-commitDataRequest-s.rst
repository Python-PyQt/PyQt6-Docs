.. sip:signal-description::
    :status: todo
    :pysig: 1acb94ce3abc6bce1ee08a2c6dbcc427
    :realsig: (QSessionManager&)
    :digest: 8df553a13f7c794d1fe1ded2c38c781d

This signal deals with session management. It is emitted when the :sip:ref:`~PyQt6.QtGui.QSessionManager` wants the application to commit all its data.

Usually this means saving all open files, after getting permission from the user. Furthermore you may want to provide a means by which the user can cancel the shutdown.

You should not exit the application within this signal. Instead, the session manager may or may not do this afterwards, depending on the context.

**Warning:** Within this signal, no user interaction is possible, *unless* you ask the *manager* for explicit permission. See :sip:ref:`~PyQt6.QtGui.QSessionManager.allowsInteraction` and :sip:ref:`~PyQt6.QtGui.QSessionManager.allowsErrorInteraction` for details and example usage.

**Note:** You should use :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.DirectConnection` when connecting to this signal.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.isSessionRestored`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.sessionId`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.saveStateRequest`.
