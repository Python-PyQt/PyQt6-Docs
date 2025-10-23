.. sip:method-description::
    :status: todo
    :pysig: bc1c2a9191fcd0651d40f39ad471ca69
    :realsig: (int,int)
    :digest: 94edef714a06518601eb77448aea4811

Resizes the vertex and index data of this geometry object to fit *vertexCount* vertices and *indexCount* indices and sets the number of vertices and indices accordingly.

Use :sip:ref:`~PyQt6.QtQuick.QSGGeometry.setVertexCount` or :sip:ref:`~PyQt6.QtQuick.QSGGeometry.setIndexCount` to change the number of vertices or indices without calling allocate() again.

Vertex and index data will be invalidated after this call and the caller must mark the associated geometry node as dirty, by calling ``node->markDirty(QSGNode::DirtyGeometry)``, to ensure that the renderer has a chance to update internal buffers.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometry.setVertexCount`, :sip:ref:`~PyQt6.QtQuick.QSGGeometry.setIndexCount`.
