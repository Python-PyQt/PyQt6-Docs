.. sip:method-description::
    :status: todo
    :pysig: 7e219fc6e58b7a39f125f48d90372d00
    :realsig: (QMetaType,QMetaType)
    :digest: 8a8c90f08ef0651ebc765bb7804f9e2e

Returns ``true`` if QMetaType::view can create a mutable view of type *toType* on type *fromType*.

Converting between pointers of types derived from :sip:ref:`~PyQt6.QtCore.QObject` will return true for this function if a qobject_cast from the type described by *fromType* to the type described by *toType* would succeed.

You can create a mutable view of type QMetaSequence::Iterable on any container registered with Q_DECLARE_SEQUENTIAL_CONTAINER_METATYPE().

Similarly you can create a mutable view of type QMetaAssociation::Iterable on any container registered with Q_DECLARE_ASSOCIATIVE_CONTAINER_METATYPE().

.. seealso:: convert(), QMetaSequence::Iterable, Q_DECLARE_SEQUENTIAL_CONTAINER_METATYPE(), QMetaAssociation::Iterable, Q_DECLARE_ASSOCIATIVE_CONTAINER_METATYPE().
