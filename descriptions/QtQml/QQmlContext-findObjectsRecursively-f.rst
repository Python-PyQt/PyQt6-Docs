.. sip:method-description::
    :status: todo
    :pysig: 786df5e6b0048ac7f50139451cedadda
    :realsig: (const QString&) const
    :digest: a6305f94551b4a2199a144c1049a88d7

Searches this context and its children recursively for objects with ID *id*. Returns a list of these objects.

There can only be one object with the given *id* in any given context, but you can create many contexts within one document, for example with views and delegates. Each of those contexts can contain an object with the given *id*.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlContext.findObjectRecursively`, :sip:ref:`~PyQt6.QtQml.QQmlContext.objectForName`, :sip:ref:`~PyQt6.QtQml.QQmlContext.childContexts`.
