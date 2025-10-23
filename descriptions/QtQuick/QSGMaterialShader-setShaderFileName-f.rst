.. sip:method-description::
    :status: todo
    :pysig: 2b3abbb7c65d47580c08fde73c4fbf8e
    :realsig: (QSGMaterialShader::Stage, const QString&, int)
    :digest: d70239fba3dc13a6b6f93deb11afb6bb

Sets the *filename* for the shader for the specified *stage*.

The file is expected to contain a serialized QShader.

This overload is used when enabling :sip:ref:`~PyQt6.QtQuick.QSGMaterial.viewCount` rendering, in particular when the build system's MULTIVIEW convenience option is used.

*viewCount* should be 2, 3, or 4. The *filename* is adjusted automatically based on this.

**Warning:** Shaders, including ``.qsb`` files, are assumed to be trusted content. Application developers are advised to carefully consider the potential implications before allowing the loading of user-provided content that is not part of the application.
