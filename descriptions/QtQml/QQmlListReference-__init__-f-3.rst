.. sip:method-description::
    :status: todo
    :pysig: 984e29ea75d61e08ebe0bf88d9934e7f
    :realsig: (const QVariant&,QQmlEngine*)
    :digest: b0171d3883e6bcf2f10d3a2ab72c212f

Constructs a :sip:ref:`~PyQt6.QtQml.QQmlListReference` from a :sip:ref:`~PyQt6.QtCore.QVariant` *variant* containing a QQmlListProperty. If *variant* does not contain a list property, an invalid :sip:ref:`~PyQt6.QtQml.QQmlListReference` is created. If the object owning the list property is destroyed after the reference is constructed, it will automatically become invalid. That is, it is safe to hold :sip:ref:`~PyQt6.QtQml.QQmlListReference` instances even after the object is deleted.

The *engine* is required to look up the element type, which may be a dynamically created QML type. If it's omitted, only pre-registered types are available. The element type is needed when inserting values into the list and when the value meta type is explicitly retrieved.
