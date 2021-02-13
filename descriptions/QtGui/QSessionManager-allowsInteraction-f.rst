.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 3d4e99958c25581ccb9f4ac9ef76ffd1

Asks the session manager for permission to interact with the user. Returns true if interaction is permitted; otherwise returns ``false``.

The rationale behind this mechanism is to make it possible to synchronize user interaction during a shutdown. Advanced session managers may ask all applications simultaneously to commit their data, resulting in a much faster shutdown.

When the interaction is completed we strongly recommend releasing the user interaction semaphore with a call to :sip:ref:`~PyQt6.QtGui.QSessionManager.release`. This way, other applications may get the chance to interact with the user while your application is still busy saving data. (The semaphore is implicitly released when the application exits.)

If the user decides to cancel the shutdown process during the interaction phase, you must tell the session manager that this has happened by calling :sip:ref:`~PyQt6.QtGui.QSessionManager.cancel`.

Here's an example of how an application's :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest` might be implemented:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qguiapplication.py
    :lines: 82-114

If an error occurred within the application while saving its data, you may want to try :sip:ref:`~PyQt6.QtGui.QSessionManager.allowsErrorInteraction` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.commitDataRequest`, :sip:ref:`~PyQt6.QtGui.QSessionManager.release`, :sip:ref:`~PyQt6.QtGui.QSessionManager.cancel`.
