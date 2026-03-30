.. sip:method-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: 18ba26109bf8da76cebe80b57dc90706

Constructs a command line option object with the name *name*.

The name can be either short or long. If the name is one character in length, it is considered a short name. Option names must not be empty, must not start with a dash or a slash character, must not contain a ``=`` and cannot be repeated.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDescription`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setValueName`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValues`.
