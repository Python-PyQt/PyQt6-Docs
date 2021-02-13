.. sip:method-description::
    :status: todo
    :pysig: 9f473aba153c000d433dda7b7e46e713
    :realsig: (QMetaType)
    :digest: 71e48d758c701b6b5f1c8d8fea992efd

Opens a new D-Bus array suitable for appending elements of meta-type *id*.

This function is used usually in ``operator<<`` streaming operators, as in the following example:

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-code-src_qdbus_qdbusargument.py
    :lines: 232-240

If the type you want to marshall is a QList or any of the Qt's `Container Classes <https://doc.qt.io/qt-6/containers.html>`_ that take one template parameter, you need not declare an ``operator<<`` function for it, since Qt D-Bus provides generic templates to do the job of marshalling the data. The same applies for STL's sequence containers, such as ``std::list``, ``std::vector``, etc.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusArgument.endArray`, :sip:ref:`~PyQt6.QtDBus.QDBusArgument.beginStructure`, :sip:ref:`~PyQt6.QtDBus.QDBusArgument.beginMap`.
