.. sip:method-description::
    :status: todo
    :pysig: 1e2f20529c2382bdf026aededc9421ed
    :realsig: (const QStringList&, const QString&, const QString&, const QString&)
    :digest: b5b37b15c032ce37d7dd16a70c89165e

Constructs a command line option object with the given arguments.

This overload allows to set multiple names for the option, for instance ``o`` and ``output``.

The names of the option are set to *names*. The names can be either short or long. Any name in the list that is one character in length is a short name. Option names must not be empty, must not start with a dash or a slash character, must not contain a ``=`` and cannot be repeated.

The description is set to *description*. It is customary to add a "." at the end of the description.

In addition, the *valueName* needs to be set if the option expects a value. The default value for the option is set to *defaultValue*.

In Qt versions before 5.4, this constructor was ``explicit``. In Qt 5.4 and later, it no longer is and can be used for C++11-style uniform initialization:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineoption.py
    :lines: 70-71

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDescription`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setValueName`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValues`.
