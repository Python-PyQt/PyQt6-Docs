.. sip:method-description::
    :status: todo
    :pysig: 7a792ec7fc75acdd989096b04406cda5
    :realsig: (const QString&) const
    :digest: 6c9234c0c5f6102a4900f39308633d77

Returns the object for a given *name* in this context. Returns nullptr if *name* is not available in the context or if the value associated with *name* is not a :sip:ref:`~PyQt6.QtCore.QObject`. Objects are named by :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty`, or as properties of a context object, or by ids in the case of QML created contexts. In contrast to :sip:ref:`~PyQt6.QtQml.QQmlContext.contextProperty`, this method does not traverse the context hierarchy. If the name is not found in the current context, nullptr is returned.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlContext.contextProperty`, :sip:ref:`~PyQt6.QtQml.QQmlContext.nameForObject`.
