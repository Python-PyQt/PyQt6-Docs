.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: (QIODevice*)
    :digest: e5d5ab73ebc44d5c8113ab3e4f4a5787

In order to QRemoteObjectNode::acquire() `Replica <https://doc.qt.io/qt-6/qtremoteobjects-replica.html#replica>`_ objects over `External QIODevices <https://doc.qt.io/qt-6/qtremoteobjects-external-schemas.html#external-qiodevices>`_, Qt Remote Objects needs access to the communications channel (a :sip:ref:`~PyQt6.QtCore.QIODevice`) between the respective nodes. It is the  call that enables this, taking the *ioDevice* as input. Any acquire() call made without calling  will still work, but the Node will not be able to initialize the `Replica <https://doc.qt.io/qt-6/qtremoteobjects-replica.html#replica>`_ without being provided the connection to the Host node.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.addHostSideConnection`.
