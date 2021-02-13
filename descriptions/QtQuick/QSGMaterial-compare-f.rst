.. sip:method-description::
    :status: todo
    :pysig: df06a0027f57d0110066c470b02305ea
    :realsig: (const QSGMaterial*) const
    :digest: 467a76b1760b2e60f0c523108f2b8e32

Compares this material to *other* and returns 0 if they are equal; -1 if this material should sort before *other* and 1 if *other* should sort before.

The scene graph can reorder geometry nodes to minimize state changes. The compare function is called during the sorting process so that the materials can be sorted to minimize state changes in each call to QSGMaterialShader::updateState().

The this pointer and *other* is guaranteed to have the same :sip:ref:`~PyQt6.QtQuick.QSGMaterial.type`.
