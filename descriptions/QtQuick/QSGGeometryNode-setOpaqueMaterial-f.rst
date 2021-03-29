.. sip:method-description::
    :status: todo
    :pysig: 90fe1d659e4380a295fde38c457dd697
    :realsig: (QSGMaterial*)
    :digest: cfdc0a7b4949d3313396768b9cb6e22c

Sets the opaque material of this geometry to *material*.

The opaque material will be preferred by the renderer over the default material, as returned by the :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode.material` function, if it is not null and the geometry item has an inherited opacity of 1.

The opaqueness refers to scene graph opacity, the material is still allowed to set :sip:ref:`~PyQt6.QtQuick.QSGMaterial.Flags.Blending` to true and draw transparent pixels.

If the material is changed without calling  again, the user must also mark the opaque material as dirty using :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometryNode.opaqueMaterial`.
