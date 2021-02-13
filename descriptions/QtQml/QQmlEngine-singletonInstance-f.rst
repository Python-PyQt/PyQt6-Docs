.. sip:method-description::
    :status: todo
    :pysig: 1794526a133c101ed5249f3aa1e3bdff
    :realsig: (int)
    :digest: 84f890729746ba7adf91698151952171

Returns the instance of a singleton type that was registered under *qmlTypeId*.

The template argument *T* may be either :sip:ref:`~PyQt6.QtQml.QJSValue` or a pointer to a :sip:ref:`~PyQt6.QtCore.QObject`-derived type and depends on how the singleton was registered. If no instance of *T* has been created yet, it is created now. If *qmlTypeId* does not represent a valid singleton type, either a default constructed :sip:ref:`~PyQt6.QtQml.QJSValue` or a ``nullptr`` is returned.

:sip:ref:`~PyQt6.QtCore.QObject`\* example:

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_qml_qqmlengine.py
    :lines: 54-63

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_qml_qqmlengine.py
    :lines: 68-68

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_qml_qqmlengine.py
    :lines: 74-76

:sip:ref:`~PyQt6.QtQml.QJSValue` example:

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_qml_qqmlengine.py
    :lines: 82-83

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_qml_qqmlengine.py
    :lines: 89-91

It is recommended to store the QML type id, e.g. as a static member in the singleton class. The lookup via :sip:ref:`~PyQt6.QtQml.qmlTypeId` is costly.

.. seealso:: QML_SINGLETON, :sip:ref:`~PyQt6.QtQml.qmlRegisterSingletonType`, :sip:ref:`~PyQt6.QtQml.qmlTypeId`.
