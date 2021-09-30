.. sip:class-description::
    :status: todo
    :brief: Acts like a union for the most common Qt data types
    :digest: 9e828be06b4a04d3c0295e9c7f766a31

The :sip:ref:`~PyQt6.QtCore.QVariant` class acts like a union for the most common Qt data types.

Because C++ forbids unions from including types that have non-default constructors or destructors, most interesting Qt classes cannot be used in unions. Without :sip:ref:`~PyQt6.QtCore.QVariant`, this would be a problem for :sip:ref:`~PyQt6.QtCore.QObject.property` and for database work, etc.

A :sip:ref:`~PyQt6.QtCore.QVariant` object holds a single value of a single :sip:ref:`~PyQt6.QtCore.QVariant.typeId` at a time. (Some types are multi-valued, for example a string list.) You can find out what type, T, the variant holds, convert it to a different type using :sip:ref:`~PyQt6.QtCore.QVariant.convert`, get its value using one of the toT() functions (e.g., toSize()), and check whether the type can be converted to a particular type using :sip:ref:`~PyQt6.QtCore.QVariant.canConvert`.

The methods named toT() (e.g., toInt(), toString()) are const. If you ask for the stored type, they return a copy of the stored object. If you ask for a type that can be generated from the stored type, toT() copies and converts and leaves the object itself unchanged. If you ask for a type that cannot be generated from the stored type, the result depends on the type; see the function documentation for details.

Here is some example code to demonstrate the use of :sip:ref:`~PyQt6.QtCore.QVariant`:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qvariant.py
    :lines: 54-70

You can even store QList<\ :sip:ref:`~PyQt6.QtCore.QVariant`> and QMap<QString, :sip:ref:`~PyQt6.QtCore.QVariant`> values in a variant, so you can easily construct arbitrarily complex data structures of arbitrary types. This is very powerful and versatile, but may prove less memory and speed efficient than storing specific types in standard data structures.

:sip:ref:`~PyQt6.QtCore.QVariant` also supports the notion of null values. A variant is null if the variant contains no initialized value, or contains a null pointer.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qvariant.py
    :lines: 75-78

:sip:ref:`~PyQt6.QtCore.QVariant` can be extended to support other types than those mentioned in the :sip:ref:`~PyQt6.QtCore.QMetaType.Type` enum. See `Creating Custom Qt Types <https://doc.qt.io/qt-6/custom-types.html>`_ for details.

.. _qvariant-a-note-on-gui-types:

A Note on GUI Types
-------------------

Because :sip:ref:`~PyQt6.QtCore.QVariant` is part of the Qt Core module, it cannot provide conversion functions to data types defined in Qt GUI, such as :sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtGui.QImage`, and :sip:ref:`~PyQt6.QtGui.QPixmap`. In other words, there is no ``toColor()`` function. Instead, you can use the :sip:ref:`~PyQt6.QtCore.QVariant.value` or the qvariant_cast() template function. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qvariant.py
    :lines: 83-85

The inverse conversion (e.g., from :sip:ref:`~PyQt6.QtGui.QColor` to :sip:ref:`~PyQt6.QtCore.QVariant`) is automatic for all data types supported by :sip:ref:`~PyQt6.QtCore.QVariant`, including GUI-related types:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qvariant.py
    :lines: 90-91

.. _qvariant-using-canconvert-and-convert-consecutively:

Using canConvert() and convert() Consecutively
----------------------------------------------

When using :sip:ref:`~PyQt6.QtCore.QVariant.canConvert` and :sip:ref:`~PyQt6.QtCore.QVariant.convert` consecutively, it is possible for :sip:ref:`~PyQt6.QtCore.QVariant.canConvert` to return true, but :sip:ref:`~PyQt6.QtCore.QVariant.convert` to return false. This is typically because :sip:ref:`~PyQt6.QtCore.QVariant.canConvert` only reports the general ability of :sip:ref:`~PyQt6.QtCore.QVariant` to convert between types given suitable data; it is still possible to supply data which cannot actually be converted.

For example, ``canConvert(QMetaType::fromType<int>())`` would return true when called on a variant containing a string because, in principle, :sip:ref:`~PyQt6.QtCore.QVariant` is able to convert strings of numbers to integers. However, if the string contains non-numeric characters, it cannot be converted to an integer, and any attempt to convert it will fail. Hence, it is important to have both functions return true for a successful conversion.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaType`.
