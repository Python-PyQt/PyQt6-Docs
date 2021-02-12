.. sip:class-description::
    :status: todo
    :brief: Information about the Qt library
    :digest: bff7cdd6a5c4c9ac77bcb94476aeac0b

The :sip:ref:`~PyQt6.QtCore.QLibraryInfo` class provides information about the Qt library.

Many pieces of information are established when Qt is configured and built. This class provides an abstraction for accessing that information. By using the static functions of this class, an application can obtain information about the instance of the Qt library which the application is using at run-time.

You can also use a ``qt.conf`` file to override the hard-coded paths that are compiled into the Qt library. For more information, see the Using qt.conf documentation.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSysInfo`.
