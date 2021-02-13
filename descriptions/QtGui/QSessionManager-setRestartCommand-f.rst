.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: d095a25faccb51dd09dd0e6427300abc

If the session manager is capable of restoring sessions it will execute *command* in order to restore the application. The command defaults to

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qguiapplication.py
    :lines: 121-121

The ``-session`` option is mandatory; otherwise :sip:ref:`~PyQt6.QtGui.QGuiApplication` cannot tell whether it has been restored or what the current session identifier is. See :sip:ref:`~PyQt6.QtGui.QGuiApplication.isSessionRestored` and :sip:ref:`~PyQt6.QtGui.QGuiApplication.sessionId` for details.

If your application is very simple, it may be possible to store the entire application state in additional command line options. This is usually a very bad idea because command lines are often limited to a few hundred bytes. Instead, use :sip:ref:`~PyQt6.QtCore.QSettings`, temporary files, or a database for this purpose. By marking the data with the unique :sip:ref:`~PyQt6.QtGui.QSessionManager.sessionId`, you will be able to restore the application in a future session.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSessionManager.restartCommand`, :sip:ref:`~PyQt6.QtGui.QSessionManager.setDiscardCommand`, :sip:ref:`~PyQt6.QtGui.QSessionManager.setRestartHint`.
