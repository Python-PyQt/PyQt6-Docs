.. sip:method-description::
    :status: todo
    :pysig: fbeabf8d6c3e3867a27352f8990f36c6
    :realsig: (QSGMaterialShader::Stage, const QString&)
    :digest: 90c3d30a4fe9830ac5de66ba2c49a00b

Sets the *filename* for the shader for the specified *stage*.

The file is expected to contain a serialized QShader.

**Warning:** Shaders, including ``.qsb`` files, are assumed to be trusted content. Application developers are advised to carefully consider the potential implications before allowing the loading of user-provided content that is not part of the application.
