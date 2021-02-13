.. sip:signal-description::
    :status: todo
    :pysig: 9064598f6881fe97156ec2e9c47c55cf
    :realsig: (const QString&,const QVariant&)
    :digest: 2256f884198533ef6f58c7c29495698c

This signal is emitted whenever one of the values in the map is changed. *key* is the key corresponding to the *value* that was changed.

**Note:**  is **NOT** emitted when changes are made by calling :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap.insert` or :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap.clear` - it is only emitted when a value is updated from QML.
