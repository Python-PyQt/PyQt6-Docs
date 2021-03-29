.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: b6a9b36c03bb5d98d3a26f9e69505499

Set *hasTransparency* to true if the texture data has an active alpha channel with non-opaque values.

This is used as an optimization by the engine so that for formats that do support an alpha channel do not need to have each value checked for non-opaque values.

.. seealso:: :sip:ref:`~PyQt6.QtQuick3D.QQuick3DTextureData.hasTransparency`.
