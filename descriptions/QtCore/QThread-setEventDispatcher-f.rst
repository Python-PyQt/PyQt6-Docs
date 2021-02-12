.. sip:method-description::
    :status: todo
    :pysig: 7d16c5138475ae03f6c721e9e98f5b85
    :realsig: (QAbstractEventDispatcher*)
    :digest: 96f92d444addcb00449ad4d54867bd05

Sets the event dispatcher for the thread to *eventDispatcher*. This is only possible as long as there is no event dispatcher installed for the thread yet. That is, before the thread has been started with :sip:ref:`~PyQt6.QtCore.QThread.start` or, in case of the main thread, before :sip:ref:`~PyQt6.QtCore.QCoreApplication` has been instantiated. This method takes ownership of the object.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.eventDispatcher`.
