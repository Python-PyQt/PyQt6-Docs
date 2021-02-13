.. sip:method-description::
    :status: todo
    :pysig: 3f80ed0280f8333e4ac074efaa246b8a
    :realsig: (QSGGeometry*)
    :digest: b30106311af3c64f310e04c180998290

Sets the geometry of this node to *geometry*.

If the node has the flag :sip:ref:`~PyQt6.QtQuick.QSGNode.Flags.OwnsGeometry` set, it will also delete the geometry object it is pointing to. This flag is not set by default.

If the geometry is changed without calling  again, the user must also mark the geometry as dirty using :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGBasicGeometryNode.geometry`, markDirty().
