.. sip:method-description::
    :status: todo
    :pysig: 7d1e8d15141d1224c60df9fd258272eb
    :realsig: (int, int, const QVector3D&, const QVector3D&, const QString&)
    :digest: 08e1fe8f2320b20876c4955b71a1368b

Adds new subset to the geometry. Subsets allow rendering parts of the geometry with different materials. The materials are specified in the `model <https://doc.qt.io/qt-6/qml-qtquick3d-model.html#materials-prop>`_.

If the geometry has index buffer, then the *offset* and *count* are the primitive offset and count of indices in the subset. If the geometry has only vertex buffer, the offset is the vertex offset and count is the number of vertices in the subset.

The bounds *boundsMin* and *boundsMax* should enclose the subset just like geometry bounds. Also the subset can have a *name*.
