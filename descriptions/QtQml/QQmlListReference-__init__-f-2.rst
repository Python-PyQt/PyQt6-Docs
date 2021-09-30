.. sip:method-description::
    :status: todo
    :pysig: 5c90b06dbcf47c6c846c7f3c98da7522
    :realsig: (QObject*,const char*,QQmlEngine*)
    :digest: 17d9ea0f871863bce8029d0463c5dc7e

Constructs a :sip:ref:`~PyQt6.QtQml.QQmlListReference` for *object*'s *property*. If *property* is not a list property, an invalid :sip:ref:`~PyQt6.QtQml.QQmlListReference` is created. If *object* is destroyed after the reference is constructed, it will automatically become invalid. That is, it is safe to hold :sip:ref:`~PyQt6.QtQml.QQmlListReference` instances even after *object* is deleted.

The *engine* is required to look up the element type, which may be a dynamically created QML type. If it's omitted, only pre-registered types are available. The element type is needed when inserting values into the list and when the value meta type is explicitly retrieved.
