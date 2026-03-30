.. sip:method-description::
    :status: todo
    :pysig: cee284c9fccd1be0f8364410e2807d7c
    :realsig: (const QString&) const
    :digest: 6f24c663d689ff9e3e84f9e4bc405f85

Searches this context and its children recursively for an object with ID *id*. If such an object is found, the object is returned. Otherwise returns ``nullptr``.

There can only be one object with the given *id* in any given context, but you can create many contexts within one document, for example with views and delegates. Each of those contexts can contain an object with the given *id*. Only the first one found is returned here. The search is conducted using breadth-first search.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlContext.findObjectsRecursively`, :sip:ref:`~PyQt6.QtQml.QQmlContext.objectForName`, :sip:ref:`~PyQt6.QtQml.QQmlContext.childContexts`.
