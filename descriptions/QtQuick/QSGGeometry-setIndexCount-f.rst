.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 1c1b343cd0dbc001abb8479e9996e3aa

Sets the number of indices to be processed each time the geometry object is rendered.

The *count* is not validated and it is the users responsibility to ensure that only values between zero and the number of allocated indices are specified.

Vertex and index data is not invalidated after this call, but the caller must mark the geometry node as dirty, by calling ``node->markDirty(QSGNode::DirtyGeometry)``, to ensure that the renderer has a chance to update internal buffers.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometry.indexCount`.
