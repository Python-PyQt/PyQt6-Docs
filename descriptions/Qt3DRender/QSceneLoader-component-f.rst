.. sip:method-description::
    :status: todo
    :pysig: f3838b391c86e1a6eaaffb7d081ac14f
    :realname: Qt3DRender::QSceneLoader::component
    :realsig: (const QString&,Qt3DRender::QSceneLoader::ComponentType) const
    :digest: 34e4349fbfcdbd32d0a202fc0e72f545

Returns a component matching *componentType* of a loaded entity with an objectName matching the *entityName*. If the entity has multiple matching components, the first match in the component list of the entity is returned. If there is no match, a null pointer is returned.
