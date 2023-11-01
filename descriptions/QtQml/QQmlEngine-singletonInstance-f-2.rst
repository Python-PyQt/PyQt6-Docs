.. sip:method-description::
    :status: todo
    :pysig: 733588a523fee44b44a88682b99dbf24
    :realsig: (QAnyStringView, QAnyStringView)
    :digest: b42351c4541cba7e03a1a175d7353538

This is an overloaded function.

Returns the instance of a singleton type named *typeName* from the module specified by *uri*.

This method can be used as an alternative to calling :sip:ref:`~PyQt6.QtQml.qmlTypeId` followed by the id based overload of :sip:ref:`~PyQt6.QtQml.QQmlEngine.singletonInstance`. This is convenient when one only needs to do a one time setup of a singleton; if repeated access to the singleton is required, caching its typeId will allow faster subsequent access via the type-id based overload.

The template argument *T* may be either :sip:ref:`~PyQt6.QtQml.QJSValue` or a pointer to a :sip:ref:`~PyQt6.QtCore.QObject`-derived type and depends on how the singleton was registered. If no instance of *T* has been created yet, it is created now. If *typeName* does not represent a valid singleton type, either a default constructed :sip:ref:`~PyQt6.QtQml.QJSValue` or a ``nullptr`` is returned.

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_qml_qqmlengine.py

.. seealso:: QML_SINGLETON, :sip:ref:`~PyQt6.QtQml.qmlRegisterSingletonType`, :sip:ref:`~PyQt6.QtQml.qmlTypeId`.
