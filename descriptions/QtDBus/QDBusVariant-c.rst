.. sip:class-description::
    :status: todo
    :brief: Enables the programmer to identify the variant type provided by the D-Bus typesystem
    :digest: 0842445550bafb67b46158a2e81f6f64

The :sip:ref:`~PyQt6.QtDBus.QDBusVariant` class enables the programmer to identify the variant type provided by the D-Bus typesystem.

A D-Bus function that takes an integer, a D-Bus variant and a string as parameters can be called with the following argument list (see :sip:ref:`~PyQt6.QtDBus.QDBusMessage.setArguments`):

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-qdbusextratypes-qdbusextratypes.py
    :lines: 63-65

When a D-Bus function returns a D-Bus variant, it can be retrieved as follows:

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-qdbusextratypes-qdbusextratypes.py
    :lines: 69-74

The `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ within a :sip:ref:`~PyQt6.QtDBus.QDBusVariant` is required to distinguish between a normal D-Bus value and a value within a D-Bus variant.

.. seealso:: `The Qt D-Bus Type System <https://doc.qt.io/qt-6/qdbustypesystem.html>`_.
