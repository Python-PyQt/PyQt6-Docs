.. sip:class-description::
    :status: todo
    :brief: A dynamically instantiated Replica
    :digest: 6f269f2dae868ae048001b79c48bb0b3

A dynamically instantiated `Replica <https://doc.qt.io/qt-6/qtremoteobjects-replica.html#replica>`_.

There are generated replicas (replicas having the header files produced by the `Replica Compiler <https://doc.qt.io/qt-6/qtremoteobjects-repc.html>`_), and dynamic replicas, that are generated on-the-fly. This is the class for the dynamic type of replica.

When the connection to the `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ object is made, the initialization step passes the current property values (see `Replica Initialization <https://doc.qt.io/qt-6/qtremoteobjects-replica.html#replica-initialization>`_). In a DynamicReplica, the property/signal/slot details are also sent, allowing the replica object to be created on-the-fly. This can be convenient in QML or scripting, but has two primary disadvantages. First, the object is in effect "empty" until it is successfully initialized by the `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_. Second, in C++, calls must be made using :sip:ref:`~PyQt6.QtCore.QMetaObject.invokeMethod`, as the moc generated lookup will not be available.

This class does not have a public constructor. It can only be instantiated by using the dynamic QRemoteObjectNode::acquire method.
