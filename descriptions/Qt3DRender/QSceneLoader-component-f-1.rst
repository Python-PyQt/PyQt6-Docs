.. sip:method-description::
    :status: todo
    :pysig: 368a48b41c277eb66b1971aa430b9846
    :realname: Qt3DRender::QSceneLoader::component
    :realsig: (const QString&, Qt3DRender::QSceneLoader::ComponentType) const
    :digest: 580ff39f3bb211d49685f26cd82be6fc

Returns a component matching *componentType* of a loaded entity with an objectName matching the *entityName*. If the entity has multiple matching components, the first match in the component list of the entity is returned. If there is no match, a null pointer is returned.
