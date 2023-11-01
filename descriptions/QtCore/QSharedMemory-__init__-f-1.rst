.. sip:method-description::
    :status: todo
    :pysig: be4cf29ba73c5c1c9c66cbed303bedcd
    :realsig: (const QString&,QObject*)
    :digest: fa1b1c529f8e69a0a988b5527b86dabb

Constructs a shared memory object with the given *parent* and with the legacy key set to *key*. Because its key is set, its :sip:ref:`~PyQt6.QtCore.QSharedMemory.create` and :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach` functions can be called.

Legacy keys are deprecated. See `Native IPC Keys <https://doc.qt.io/qt-6/native-ipc-keys.html>`_ for more information.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSharedMemory.setKey`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.create`, :sip:ref:`~PyQt6.QtCore.QSharedMemory.attach`.
