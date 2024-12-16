.. sip:signal-description::
    :status: todo
    :pysig: 57376ba4def0b83f83f076c5427a5cfb
    :realsig: (const QRemoteObjectSourceLocation&)
    :digest: 19c1fd915ed7ab40a35c2392f8a46f2d

This signal is emitted whenever a known `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ object is removed from the Registry. The signal will not be emitted if there is no Registry set (i.e., Sources over connections made via :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.connectToNode` directly). The *loc* parameter contains the information about the removed Source, including name, type and the :sip:ref:`~PyQt6.QtCore.QUrl` of the hosting Node.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.remoteObjectAdded`, :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.instances`.
