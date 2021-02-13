.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 89e1d1dd3e568641d9f10e3e57d0999e

Returns ``true`` if the application is currently saving the session; otherwise returns ``false``.

This is ``true`` when :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest` and :sip:ref:`~PyQt6.QtGui.QGuiApplication.saveStateRequest` are emitted, but also when the windows are closed afterwards by session management.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.sessionId`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.saveStateRequest`.
