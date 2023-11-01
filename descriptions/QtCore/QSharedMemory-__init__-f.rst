.. sip:method-description::
    :status: todo
    :pysig: 0281bb2a03f8f3624f862e1826a39fe8
    :realsig: (QObject*)
    :digest: db562c0d9ec046fbd2d2bfd7412394b8

This function overloads QSharedMemory().

Constructs a shared memory object with the given *parent*. The shared memory object's key is not set by the constructor, so the shared memory object does not have an underlying shared memory segment attached. The key must be set with :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey` before :sip:ref:`~PyQt6.QtCore.QSharedMemory.create` or :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach` can be used.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.setNativeKey`.
