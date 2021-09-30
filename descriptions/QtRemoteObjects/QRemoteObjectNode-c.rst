.. sip:class-description::
    :status: todo
    :brief: A node on a Qt Remote Objects network
    :digest: 1824e0cd3558e5b2e9b0bbf031e20288

A node on a Qt Remote Objects network.

The :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode` class provides an entry point to a `QtRemoteObjects <https://doc.qt.io/qt-6/qml-qtremoteobjects-qtremoteobjects.html>`_ network. A network can be as simple as two nodes, or an arbitrarily complex set of processes and devices.

A :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode` does not have a url that other nodes can connect to, and thus is able to acquire replicas only. It is not able to share source objects (only :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` and :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistryHost` Nodes can share).

Nodes may connect to each other directly using :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.connectToNode`, or they can use the :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry` to simplify connections.

The :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry` is a special replica available to every node that connects to the Registry Url. It knows how to connect to every QRemoteObjectSource object on the network.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost`, :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistryHost`.
