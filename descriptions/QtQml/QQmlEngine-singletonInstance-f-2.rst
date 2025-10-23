.. sip:method-description::
    :status: todo
    :pysig: 733588a523fee44b44a88682b99dbf24
    :realsig: (QAnyStringView, QAnyStringView)
    :digest: 75ec38a8ec1ae013d3378aa1b6e22ec7

Returns the instance of a singleton type named *typeName* from the module specified by *uri*.

This method can be used as an alternative to calling :sip:ref:`~PyQt6.QtQml.qmlTypeId` followed by the id based overload of :sip:ref:`~PyQt6.QtQml.QQmlEngine.singletonInstance`. This is convenient when one only needs to do a one time setup of a singleton; if repeated access to the singleton is required, caching its typeId will allow faster subsequent access via the type-id based overload.

The template argument *T* may be either :sip:ref:`~PyQt6.QtQml.QJSValue` or a pointer to a :sip:ref:`~PyQt6.QtCore.QObject`-derived type and depends on how the singleton was registered. If no instance of *T* has been created yet, it is created now. If *typeName* does not represent a valid singleton type, either a default constructed :sip:ref:`~PyQt6.QtQml.QJSValue` or a ``nullptr`` is returned.

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_qml_qqmlengine.py

.. seealso:: `QML_SINGLETON <https://doc.qt.io/qt-6/qtqml-documents-structure.html#singleton>`_, :sip:ref:`~PyQt6.QtQml.qmlRegisterSingletonType`, :sip:ref:`~PyQt6.QtQml.qmlTypeId`.
