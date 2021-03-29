.. sip:method-description::
    :status: todo
    :pysig: 0a03a9fae9bc5d51ecd31c92778714b3
    :realsig: (QObject*,QQmlContext*)
    :digest: 0c5f9cae1f865e8ce6e2a03af1af622a

Sets the :sip:ref:`~PyQt6.QtQml.QQmlContext` for the *object* to *context*. If the *object* already has a context, a warning is output, but the context is not changed.

When the :sip:ref:`~PyQt6.QtQml.QQmlEngine` instantiates a :sip:ref:`~PyQt6.QtCore.QObject`, the context is set automatically.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.contextForObject`.
