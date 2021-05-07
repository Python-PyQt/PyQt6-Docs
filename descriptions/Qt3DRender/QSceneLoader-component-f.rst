.. sip:method-description::
    :status: todo
    :pysig: f3838b391c86e1a6eaaffb7d081ac14f
    :realname: Qt3DRender::QSceneLoader::component
    :realsig: (const QString&,Qt3DRender::QSceneLoader::ComponentType) const
    :digest: 580ff39f3bb211d49685f26cd82be6fc

Returns a component matching *componentType* of a loaded entity with an objectName matching the *entityName*. If the entity has multiple matching components, the first match in the component list of the entity is returned. If there is no match, a null pointer is returned.
