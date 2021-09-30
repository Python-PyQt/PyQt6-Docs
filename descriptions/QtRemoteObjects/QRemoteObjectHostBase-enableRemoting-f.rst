.. sip:method-description::
    :status: todo
    :pysig: 5bc1be2f0c6555400b11d52ef93226f6
    :realsig: (QObject*,const QString&)
    :digest: f8dfbe4c0f821e0bf92aece5b5cba3e3

Enables a host node to dynamically provide remote access to the :sip:ref:`~PyQt6.QtCore.QObject` *object*. Client nodes connected to the node hosting this object may obtain Replicas of this Source.

The optional *name* defines the lookup-name under which the :sip:ref:`~PyQt6.QtCore.QObject` can be acquired using QRemoteObjectNode::acquire() . If not explicitly set then the name given in the QCLASSINFO_REMOTEOBJECT_TYPE will be used. If no such macro was defined for the :sip:ref:`~PyQt6.QtCore.QObject` then the :sip:ref:`~PyQt6.QtCore.QObject.objectName` is used.

Returns ``false`` if the current node is a client node, or if the :sip:ref:`~PyQt6.QtCore.QObject` is already registered to be remoted, and ``true`` if remoting is successfully enabled for the dynamic :sip:ref:`~PyQt6.QtCore.QObject`.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.disableRemoting`.
