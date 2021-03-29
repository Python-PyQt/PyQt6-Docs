.. sip:method-description::
    :status: todo
    :pysig: 4fb88d9ec23b1a8b7c68562fcad0cc74
    :realname: Qt3DCore::QEntity::parentEntity
    :realsig: () const
    :digest: f0da8f070d7e287866f489481e6e342a

Returns the parent :sip:ref:`~PyQt6.Qt3DCore.QEntity` instance of this entity. If the immediate parent isn't a :sip:ref:`~PyQt6.Qt3DCore.QEntity`, this function traverses up the scene hierarchy until a parent :sip:ref:`~PyQt6.Qt3DCore.QEntity` is found. If no :sip:ref:`~PyQt6.Qt3DCore.QEntity` parent can be found, returns null.
