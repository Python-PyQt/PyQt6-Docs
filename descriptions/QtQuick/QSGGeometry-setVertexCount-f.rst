.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 1716a811a2ac6d819639652b2955fb9c

Sets the number of vertices to be rendered.

The *count* is not validated and it is the users responsibility to ensure that only values between zero and the number of allocated vertices are specified.

Vertex data is not invalidated after this call, but the caller must mark the geometry node as dirty, by calling ``node->markDirty(QSGNode::DirtyGeometry)``, to ensure that the renderer has a chance to update internal buffers.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometry.vertexCount`.
