.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: 6c59704298fac2ce9bf2424853c18822

Constructs a command line option object with the names *names*.

This overload allows to set multiple names for the option, for instance ``o`` and ``output``.

The names can be either short or long. Any name in the list that is one character in length is a short name. Option names must not be empty, must not start with a dash or a slash character, must not contain a ``=`` and cannot be repeated.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDescription`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setValueName`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValues`.
