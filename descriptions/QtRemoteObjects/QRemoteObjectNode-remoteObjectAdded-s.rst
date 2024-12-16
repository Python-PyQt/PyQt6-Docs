.. sip:signal-description::
    :status: todo
    :pysig: 57376ba4def0b83f83f076c5427a5cfb
    :realsig: (const QRemoteObjectSourceLocation&)
    :digest: ccdcf15783180d3b1f48fdc6ac69bae9

This signal is emitted whenever a new `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ object is added to the Registry. The signal will not be emitted if there is no Registry set (i.e., Sources over connections made via :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.connectToNode` directly). The *loc* parameter contains the information about the added Source, including name, type and the :sip:ref:`~PyQt6.QtCore.QUrl` of the hosting Node.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.remoteObjectRemoved`, :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectNode.instances`.
