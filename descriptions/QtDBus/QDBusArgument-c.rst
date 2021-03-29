.. sip:class-description::
    :status: todo
    :brief: Used to marshall and demarshall D-Bus arguments
    :digest: 47d67fdefdad3d65ece8cb4e7e6df643

The `QDBusArgument <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusargument>`_ class is used to marshall and demarshall D-Bus arguments.

The class is used to send arguments over D-Bus to remote applications and to receive them back. D-Bus offers an extensible type system, based on a few primitive types and associations of them. See the `Qt D-Bus Type System <https://doc.qt.io/qt-6/qdbustypesystem.html>`_ page for more information on the type system.

`QDBusArgument <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusargument>`_ is the central class in the Qt D-Bus type system, providing functions to marshall and demarshall the primitive types. The compound types are then created by association of one or more of the primitive types in arrays, dictionaries or structures.

The following example illustrates how a structure containing an integer and a string can be constructed using the `Qt D-Bus type system <https://doc.qt.io/qt-6/qdbustypesystem.html>`_:

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-code-src_qdbus_qdbusargument.py
    :lines: 135-138

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-code-src_qdbus_qdbusargument.py
    :lines: 145-165

The type has to be registered with qDBusRegisterMetaType() before it can be used with `QDBusArgument <https://doc.qt.io/qt-6/dbus-changes-qt6.html#qdbusargument>`_. Therefore, somewhere in your program, you should add the following code:

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-code-src_qdbus_qdbusargument.py
    :lines: 181-181

Once registered, a type can be used in outgoing method calls (placed with :sip:ref:`~PyQt6.QtDBus.QDBusAbstractInterface.call`), signal emissions from registered objects or in incoming calls from remote applications.

It is important to note that the ``operator<<`` and ``operator>>`` streaming functions must always produce the same number of entries in case of structures, both in reading and in writing (marshalling and demarshalling), otherwise calls and signals may start to silently fail.

The following example illustrates this wrong usage in context of a class that may contain invalid data:

::

    //bad code
        // Wrongly marshall the MyTime data into a D-Bus argument
        QDBusArgument &operator<<(QDBusArgument &argument, const MyTime &mytime)
        {
            argument.beginStructure();
            if (mytime.isValid)
                argument << true << mytime.hour
                         << mytime.minute << mytime.second;
            else
                argument << false;
            argument.endStructure();
            return argument;
        }

In this example, both the ``operator<<`` and the ``operator>>`` functions may produce a different number of reads/writes. This can confuse the Qt D-Bus type system and should be avoided.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusAbstractInterface`, `The Qt D-Bus type system <https://doc.qt.io/qt-6/qdbustypesystem.html>`_, `Using Adaptors <https://doc.qt.io/qt-6/usingadaptors.html>`_, qdbus_cast().
