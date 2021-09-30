.. sip:module-description::
    :status:    done
    :brief:     Classes for sharing the API of a QObject between processes or systems

The :sip:ref:`~PyQt6.QtRemoteObjects` module contains classes that implement an
inter-process communication mechanism for sharing the API of a
:sip:ref:`~PyQt6.QtCore.QObject` (i.e. its properties, signals and slots)
between different processes.  Those processes may be running on different
systems.

A slot called on a copy of an object (called a *replica*) is forwarded to the
true object (called a *source*) for handling.  Updates to the source (either
property changes or emitted signals) are forwarded to every replica.

A replica is a light-weight proxy for the source object, but one that supports
the same connections and behavior of :sip:ref:`~PyQt6.QtCore.QObject`\s, which
makes it as easy to use as any other locally implemented
:sip:ref:`~PyQt6.QtCore.QObject`.  Everything needed for the replica to look
like the source object is handled behind the scenes.

In Qt the API of the :sip:ref:`~PyQt6.QtCore.QObject` can be defined either
statically or dynamically.  A static definition is specified in a ``.rep`` file
which is then converted to C++ code using the :program:`repc` utility.  The
C++ code is then compiled and linked with the rest of the application.  PyQt6
does not support static definitions.

A dynamic definition uses a conventionally written
:sip:ref:`~PyQt6.QtCore.QObject`.  It is then introspected to determine the API
to share.  The replicator does not need to know the original definition that is
part of the source.  In other words, a Python client application does not need
to import the module of the Python server application that contains the
definition of the :sip:ref:`~PyQt6.QtCore.QObject`.

A Python client can interact with a C++ server (whether the server uses a
static or dynamic definition).  A Python server can interact with a C++ client.
However if the C++ client has been written using a static definition then the
Python server must ensure that the :sip:ref:`~PyQt6.QtCore.QMetaObject` of the
:sip:ref:`~PyQt6.QtCore.QObject` matches that defined in the ``.rep`` file.
For the most part this means having the properties, signals and slots appearing
in the same order.
