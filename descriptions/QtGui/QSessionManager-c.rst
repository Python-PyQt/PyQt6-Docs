.. sip:class-description::
    :status: todo
    :brief: Access to the session manager
    :digest: 553a86ba406cae867b29b780b11dd1db

The :sip:ref:`~PyQt6.QtGui.QSessionManager` class provides access to the session manager.

A session manager in a desktop environment (in which Qt GUI applications live) keeps track of a session, which is a group of running applications, each of which has a particular state. The state of an application contains (most notably) the documents the application has open and the position and size of its windows.

The session manager is used to save the session, e.g., when the machine is shut down, and to restore a session, e.g., when the machine is started up. We recommend that you use :sip:ref:`~PyQt6.QtCore.QSettings` to save an application's settings, for example, window positions, recently used files, etc. When the application is restarted by the session manager, you can restore the settings.

:sip:ref:`~PyQt6.QtGui.QSessionManager` provides an interface between the application and the platform's session manager. In Qt, session management requests for action are handled by the two signals :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest` and :sip:ref:`~PyQt6.QtGui.QGuiApplication.saveStateRequest`. Both provide a reference to a :sip:ref:`~PyQt6.QtGui.QSessionManager` object as argument. The session manager can only be accessed in slots invoked by these signals.

No user interaction is possible *unless* the application gets explicit permission from the session manager. You ask for permission by calling :sip:ref:`~PyQt6.QtGui.QSessionManager.allowsInteraction` or, if it is really urgent, :sip:ref:`~PyQt6.QtGui.QSessionManager.allowsErrorInteraction`. Qt does not enforce this, but the session manager may.

You can try to abort the shutdown process by calling :sip:ref:`~PyQt6.QtGui.QSessionManager.cancel`.

For sophisticated session managers provided on Unix/X11, :sip:ref:`~PyQt6.QtGui.QSessionManager` offers further possibilities to fine-tune an application's session management behavior: :sip:ref:`~PyQt6.QtGui.QSessionManager.setRestartCommand`, :sip:ref:`~PyQt6.QtGui.QSessionManager.setDiscardCommand`, :sip:ref:`~PyQt6.QtGui.QSessionManager.setRestartHint`, setProperty(), :sip:ref:`~PyQt6.QtGui.QSessionManager.requestPhase2`. See the respective function descriptions for further details.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication`.
