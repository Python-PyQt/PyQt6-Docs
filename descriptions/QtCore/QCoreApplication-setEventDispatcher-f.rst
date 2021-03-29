.. sip:method-description::
    :status: todo
    :pysig: 2fb0e247466d9fe67aba78ea5e55fa4a
    :realsig: (QAbstractEventDispatcher*)
    :digest: 30c222419e1b4cb1f727739aa4ff1eaa

Sets the event dispatcher for the main thread to *eventDispatcher*. This is only possible as long as there is no event dispatcher installed yet. That is, before :sip:ref:`~PyQt6.QtCore.QCoreApplication` has been instantiated. This method takes ownership of the object.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.eventDispatcher`.
