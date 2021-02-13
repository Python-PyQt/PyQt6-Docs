.. sip:enum-member-description::
    :status: todo
    :value: 0x0010
    :realname: QSGMaterial::Flag::CustomCompileStep
    :digest: d74612c14f28bf8f785ff4f1e9ee8f85

Starting with Qt 5.2, the scene graph will not always call QSGMaterialShader::compile() when its shader program is compiled and linked. Set this flag to enforce that the function is called.
