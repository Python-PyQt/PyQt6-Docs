.. sip:method-description::
    :status: todo
    :pysig: 5c90b06dbcf47c6c846c7f3c98da7522
    :realsig: (QObject*,const char*,QQmlEngine*)
    :digest: 1760a0084c0205bffcfe24ee13b4936b

Use the constructors without :sip:ref:`~PyQt6.QtQml.QQmlEngine` argument instead.

Constructs a :sip:ref:`~PyQt6.QtQml.QQmlListReference` for *object*'s *property*. If *property* is not a list property, an invalid :sip:ref:`~PyQt6.QtQml.QQmlListReference` is created. If *object* is destroyed after the reference is constructed, it will automatically become invalid. That is, it is safe to hold :sip:ref:`~PyQt6.QtQml.QQmlListReference` instances even after *object* is deleted.

The *engine* is unused.
