.. sip:method-description::
    :status: todo
    :pysig: 7e219fc6e58b7a39f125f48d90372d00
    :realsig: (QMetaType,QMetaType)
    :digest: ca918f70153c2a1524f697b352f52168

Returns ``true`` if QMetaType::view can create a mutable view of type *toType* on type *fromType*.

Converting between pointers of types derived from :sip:ref:`~PyQt6.QtCore.QObject` will return true for this function if a qobject_cast from the type described by *fromType* to the type described by *toType* would succeed.

You can create a mutable view of type QSequentialIterable on any container registered with Q_DECLARE_SEQUENTIAL_CONTAINER_METATYPE().

Similarly you can create a mutable view of type QAssociativeIterable on any container registered with Q_DECLARE_ASSOCIATIVE_CONTAINER_METATYPE().

.. seealso:: convert(), QSequentialIterable, Q_DECLARE_SEQUENTIAL_CONTAINER_METATYPE(), QAssociativeIterable, Q_DECLARE_ASSOCIATIVE_CONTAINER_METATYPE().
