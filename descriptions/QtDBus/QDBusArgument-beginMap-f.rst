.. sip:method-description::
    :status: todo
    :pysig: 2a23f830f9bbda5230cc67e42450e411
    :realsig: (QMetaType,QMetaType)
    :digest: 64cf93fb850d315e9cc54266192850a7

Opens a new D-Bus map suitable for appending elements. Maps are containers that associate one entry (the key) to another (the value), such as Qt's QMap or QHash. The ids of the map's key and value meta types must be passed in *keyMetaType* and *valueMetaType* respectively.

This function is used usually in ``operator<<`` streaming operators, as in the following example:

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-code-src_qdbus_qdbusargument.py
    :lines: 244-256

You usually don't need to provide an ``operator<<`` or ``operator>>`` function for associative containers such as QHash or std::map, since Qt D-Bus provides generic templates to do the job of marshalling the data.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusArgument.endMap`, :sip:ref:`~PyQt6.QtDBus.QDBusArgument.beginStructure`, :sip:ref:`~PyQt6.QtDBus.QDBusArgument.beginArray`, :sip:ref:`~PyQt6.QtDBus.QDBusArgument.beginMapEntry`.
