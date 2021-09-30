.. sip:class-description::
    :status: todo
    :brief: A (Host/Registry) node on a Qt Remote Objects network
    :digest: 1b043a771b055a7b3b3bb2b4022496a4

A (Host/Registry) node on a Qt Remote Objects network.

The :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistryHost` class provides an entry point to a `QtRemoteObjects <https://doc.qt.io/qt-6/qml-qtremoteobjects-qtremoteobjects.html>`_ network. A network can be as simple as two Nodes, or an arbitrarily complex set of processes and devices.

A :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistryHost` has the same capability that a :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` has (which includes everything a :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode` supports), and in addition is the owner of the Registry. Any :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` node that connects to this Node will have all of their Source objects made available by the Registry.

Nodes only support connection to one `registry <https://doc.qt.io/qt-6/qtremoteobjects-registry.html#registry>`_, calling :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.setRegistryUrl` when a Registry is already set is considered an error. For something like a secure and insecure network (where different Registries would be applicable), the recommendation is to create separate Nodes to connect to each, in effect creating two independent Qt Remote Objects networks.

Nodes may connect to each other directly using connectToNode, or they can use the :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry` to simplify connections.

The :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry` is a special Replica available to every Node that connects to the Registry Url. It knows how to connect to every QRemoteObjectSource object on the network.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode`, :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost`.
