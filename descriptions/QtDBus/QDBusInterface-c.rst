.. sip:class-description::
    :status: todo
    :brief: Proxy for interfaces on remote objects
    :digest: 1447b79d95556a479cb38dae740e4282

The :sip:ref:`~PyQt6.QtDBus.QDBusInterface` class is a proxy for interfaces on remote objects.

:sip:ref:`~PyQt6.QtDBus.QDBusInterface` is a generic accessor class that is used to place calls to remote objects, connect to signals exported by remote objects and get/set the value of remote properties. This class is useful for dynamic access to remote objects: that is, when you do not have a generated code that represents the remote interface.

Calls are usually placed by using the call() function, which constructs the message, sends it over the bus, waits for the reply and decodes the reply. Signals are connected to by using the normal QObject::connect() function. Finally, properties are accessed using the :sip:ref:`~PyQt6.QtCore.QObject.property` and :sip:ref:`~PyQt6.QtCore.QObject.setProperty` functions.

The following code snippet demonstrates how to perform a mathematical operation of ``"2 + 2"`` in a remote application called ``com.example.Calculator``, accessed via the session bus.

.. literalinclude:: ../../../snippets/qtbase-src-dbus-doc-snippets-code-src_qdbus_qdbusinterface.py
    :lines: 58-66

.. seealso:: `Qt D-Bus XML compiler (qdbusxml2cpp) <https://doc.qt.io/qt-6/qdbusxml2cpp.html>`_.
