.. sip:method-description::
    :status: todo
    :pysig: bc1c2a9191fcd0651d40f39ad471ca69
    :realsig: (int,int)
    :digest: 8d4296ca794752d54082cafc654c9114

Resizes the vertex and index data of this geometry object to fit *vertexCount* vertices and *indexCount* indices.

Vertex and index data will be invalidated after this call and the caller must mark the associated geometry node as dirty, by calling node->markDirty(\ :sip:ref:`~PyQt6.QtQuick.QSGNode.DirtyState.DirtyGeometry`) to ensure that the renderer has a chance to update internal buffers.
