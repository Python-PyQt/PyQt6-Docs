.. sip:class-description::
    :status: todo
    :brief: A (Host) Node on a Qt Remote Objects network
    :digest: 0d7dd4c0c36b4ace9a9127d106594a7b

A (Host) Node on a Qt Remote Objects network.

The :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` class provides an entry point to a `QtRemoteObjects <https://doc.qt.io/qt-6/qml-qtremoteobjects-qtremoteobjects.html>`_ network. A network can be as simple as two nodes, or an arbitrarily complex set of processes and devices.

QRemoteObjectHosts have the same capabilities as QRemoteObjectNodes, but they can also be connected to and can share source objects on the network.

Nodes may connect to each other directly using connectToNode, or they can use the :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry` to simplify connections.

The :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry` is a special replica available to every node that connects to the registry Url. It knows how to connect to every QRemoteObjectSource object on the network.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode`, :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistryHost`.
