.. sip:class-description::
    :status: todo
    :brief: Manages named types in the meta-object system
    :digest: b47ae0fa3b5df5517d7374f9f5a09efb

The `QMetaType <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qmetatype>`_ class manages named types in the meta-object system.

The class is used as a helper to marshall types in `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ and in queued signals and slots connections. It associates a type name to a type so that it can be created and destructed dynamically at run-time. Declare new types with Q_DECLARE_METATYPE() to make them available to `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ and other template-based functions. Call qRegisterMetaType() to make types available to non-template based functions, such as the queued signal and slot connections.

Any class or struct that has a public default constructor, a public copy constructor, and a public destructor can be registered.

The following code allocates and destructs an instance of ``MyClass``:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetatype.py
    :lines: 87-93

If we want the stream operators ``operator<<()`` and ``operator>>()`` to work on `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ objects that store custom types, the custom type must provide ``operator<<()`` and ``operator>>()`` operators.

.. seealso:: Q_DECLARE_METATYPE(), QVariant::setValue(), :sip:ref:`~PyQt6.QtCore.QVariant.value`, QVariant::fromValue().
