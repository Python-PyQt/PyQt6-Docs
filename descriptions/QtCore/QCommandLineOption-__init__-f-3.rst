.. sip:method-description::
    :status: todo
    :pysig: 786595ec1db88b394674333ea8ad9e00
    :realsig: (const QString&,const QString&,const QString&,const QString&)
    :digest: 7cd1052c37e5211eab5066887e98622f

Constructs a command line option object with the given arguments.

The name of the option is set to *name*. The name can be either short or long. If the name is one character in length, it is considered a short name. Option names must not be empty, must not start with a dash or a slash character, must not contain a ``=`` and cannot be repeated.

The description is set to *description*. It is customary to add a "." at the end of the description.

In addition, the *valueName* needs to be set if the option expects a value. The default value for the option is set to *defaultValue*.

In Qt versions before 5.4, this constructor was ``explicit``. In Qt 5.4 and later, it no longer is and can be used for C++11-style uniform initialization:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineoption.py
    :lines: 65-66

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDescription`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setValueName`, :sip:ref:`~PyQt6.QtCore.QCommandLineOption.setDefaultValues`.
