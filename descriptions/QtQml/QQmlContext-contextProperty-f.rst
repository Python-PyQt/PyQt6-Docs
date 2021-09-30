.. sip:method-description::
    :status: todo
    :pysig: 9064598f6881fe97156ec2e9c47c55cf
    :realsig: (const QString&) const
    :digest: 5a3112b81059efd43d4c5c213d3e1d36

Returns the value of the *name* property for this context as a :sip:ref:`~PyQt6.QtCore.QVariant`. If you know that the property you're looking for is a :sip:ref:`~PyQt6.QtCore.QObject` assigned using a QML id in the current context, :sip:ref:`~PyQt6.QtQml.QQmlContext.objectForName` is more convenient and faster. In contrast to :sip:ref:`~PyQt6.QtQml.QQmlContext.objectForName` and :sip:ref:`~PyQt6.QtQml.QQmlContext.nameForObject`, this method does traverse the context hierarchy and searches in parent contexts if the *name* is not found in the current one. It also considers any :sip:ref:`~PyQt6.QtQml.QQmlContext.contextObject` you may have set.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty`, :sip:ref:`~PyQt6.QtQml.QQmlContext.objectForName`, :sip:ref:`~PyQt6.QtQml.QQmlContext.nameForObject`, :sip:ref:`~PyQt6.QtQml.QQmlContext.contextObject`.
