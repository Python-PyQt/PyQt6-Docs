.. sip:method-description::
    :status: todo
    :pysig: 90fe1d659e4380a295fde38c457dd697
    :realsig: (QSGMaterial*)
    :digest: b36b0426172b7fdafae75311991bf734

Sets the material of this geometry node to *material*.

Geometry nodes must have a material before they can be added to the scene graph.

If the material is changed without calling setMaterial() again, the user must also mark the material as dirty using :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode.material`.
