.. sip:method-description::
    :status: todo
    :pysig: 984e29ea75d61e08ebe0bf88d9934e7f
    :realsig: (const QVariant&,QQmlEngine*)
    :digest: c1e40ebc62d6f118c0bc44294f4c86ae

Use the constructors without :sip:ref:`~PyQt6.QtQml.QQmlEngine` argument instead.

Constructs a :sip:ref:`~PyQt6.QtQml.QQmlListReference` from a :sip:ref:`~PyQt6.QtCore.QVariant` *variant* containing a QQmlListProperty. If *variant* does not contain a list property, an invalid :sip:ref:`~PyQt6.QtQml.QQmlListReference` is created. If the object owning the list property is destroyed after the reference is constructed, it will automatically become invalid. That is, it is safe to hold :sip:ref:`~PyQt6.QtQml.QQmlListReference` instances even after the object is deleted.

The *engine* is unused.
