.. sip:method-description::
    :status: todo
    :pysig: 0281bb2a03f8f3624f862e1826a39fe8
    :realsig: (QObject*)
    :digest: dd4449064bb8e501e6f4129da9b079b2

Default constructor for :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode` with the given *parent*. A Node constructed in this manner can not be connected to, and thus can not expose Source objects on the network. It also will not include a :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistry`, unless set manually using :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.setRegistryUrl`.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.connectToNode`, :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.setRegistryUrl`.
