.. sip:method-description::
    :status: todo
    :pysig: a4acbcb945511e7a64a8c0a9ed8a6f79
    :realsig: (const QString&, const QVariant&)
    :digest: ec81e625b1562e8179f2c5c4320553d2

Returns the new value to be stored for the key *key*. This function is provided to intercept updates to a property from QML, where the value provided from QML is *input*.

Override this function to manipulate the property value as it is updated. Note that this function is only invoked when the value is updated from QML.
