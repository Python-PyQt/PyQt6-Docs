.. sip:class-description::
    :status: todo
    :brief: Manages named types in the meta-object system
    :digest: 66e5745e61940bbeb59dd52cdef509d1

The :sip:ref:`~PyQt6.QtCore.QMetaType` class manages named types in the meta-object system.

The class is used as a helper to marshall types in :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QVariant` and in queued signals and slots connections. It associates a type name to a type so that it can be created and destructed dynamically at run-time.

Type names can be registered with :sip:ref:`~PyQt6.QtCore.QMetaType` by using either qRegisterMetaType() or registerType(). Registration is not required for most operations; it's only required for operations that attempt to resolve a type name in string form back to a :sip:ref:`~PyQt6.QtCore.QMetaType` object or the type's ID. Those include some old-style signal-slot connections using QObject::connect(), reading user-types from :sip:ref:`~PyQt6.QtCore.QDataStream` to :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QVariant`, or binding to other languages and IPC mechanisms, like QML, D-Bus, JavaScript, etc.

The following code allocates and destructs an instance of ``MyClass`` by its name, which requires that ``MyClass`` have been previously registered:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetatype.py
    :lines: 87-93

If we want the stream operators ``operator<<()`` and ``operator>>()`` to work on :sip:ref:`~PyQt6.QtCore.QMetaType.Type.QVariant` objects that store custom types, the custom type must provide ``operator<<()`` and ``operator>>()`` operators.

.. seealso:: Q_DECLARE_METATYPE(), QVariant::setValue(), :sip:ref:`~PyQt6.QtCore.QVariant.value`, QVariant::fromValue().
