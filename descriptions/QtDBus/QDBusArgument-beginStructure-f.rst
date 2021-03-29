.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 97e62d0a37e4908983dfa71572b4c5ca

Opens a new D-Bus structure suitable for appending new arguments.

This function is used usually in ``operator<<`` streaming operators, as in the following example:

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-code-src_qdbus_qdbusargument.py
    :lines: 204-210

Structures can contain other structures, so the following code is also valid:

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-code-src_qdbus_qdbusargument.py
    :lines: 215-227

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusArgument.endStructure`, :sip:ref:`~PyQt6.QtDBus.QDBusArgument.beginArray`, :sip:ref:`~PyQt6.QtDBus.QDBusArgument.beginMap`.
