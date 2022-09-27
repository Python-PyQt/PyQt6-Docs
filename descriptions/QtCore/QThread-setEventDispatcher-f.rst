.. sip:method-description::
    :status: todo
    :pysig: 7d16c5138475ae03f6c721e9e98f5b85
    :realsig: (QAbstractEventDispatcher*)
    :digest: 960fb2d63e390409dad0530adf0ee15b

Sets the event dispatcher for the thread to *eventDispatcher*. This is only possible as long as there is no event dispatcher installed for the thread yet.

An event dispatcher is automatically created for the main thread when :sip:ref:`~PyQt6.QtCore.QCoreApplication` is instantiated and on :sip:ref:`~PyQt6.QtCore.QThread.start` for auxiliary threads.

This method takes ownership of the object.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.eventDispatcher`.
