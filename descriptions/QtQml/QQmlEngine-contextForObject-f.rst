.. sip:method-description::
    :status: todo
    :pysig: 0a03a9fae9bc5d51ecd31c92778714b3
    :realsig: (const QObject*)
    :digest: 613a77b011b2d70589cc7e1b25907c6d

Returns the :sip:ref:`~PyQt6.QtQml.QQmlContext` for the *object*, or nullptr if no context has been set.

When the :sip:ref:`~PyQt6.QtQml.QQmlEngine` instantiates a :sip:ref:`~PyQt6.QtCore.QObject`, an internal context is assigned to it automatically. Such internal contexts are read-only. You cannot set context properties on them.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.setContextForObject`, :sip:ref:`~PyQt6.QtQml.qmlContext`, :sip:ref:`~PyQt6.QtQml.qmlEngine`, :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty`.
