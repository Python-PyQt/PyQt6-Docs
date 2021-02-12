.. sip:class-description::
    :status: todo
    :brief: Means for handling the command line options
    :digest: 144246e80bf8786bbac0dd65df0c3ee4

The :sip:ref:`~PyQt6.QtCore.QCommandLineParser` class provides a means for handling the command line options.

:sip:ref:`~PyQt6.QtCore.QCoreApplication` provides the command-line arguments as a simple list of strings. :sip:ref:`~PyQt6.QtCore.QCommandLineParser` provides the ability to define a set of options, parse the command-line arguments, and store which options have actually been used, as well as option values.

Any argument that isn't an option (i.e. doesn't start with a ``-``) is stored as a "positional argument".

The parser handles short names, long names, more than one name for the same option, and option values.

Options on the command line are recognized as starting with a single or double ``-`` character(s). The option ``-`` (single dash alone) is a special case, often meaning standard input, and not treated as an option. The parser will treat everything after the option ``--`` (double dash) as positional arguments.

Short options are single letters. The option ``v`` would be specified by passing ``-v`` on the command line. In the default parsing mode, short options can be written in a compact form, for instance ``-abc`` is equivalent to ``-a -b -c``. The parsing mode for can be set to :sip:ref:`~PyQt6.QtCore.QCommandLineParser.SingleDashWordOptionMode.ParseAsLongOptions`, in which case ``-abc`` will be parsed as the long option ``abc``.

Long options are more than one letter long and cannot be compacted together. The long option ``verbose`` would be passed as ``--verbose`` or ``-verbose``.

Passing values to options can be done using the assignment operator: ``-v=value`` ``--verbose=value``, or a space: ``-v value`` ``--verbose value``, i.e. the next argument is used as value (even if it starts with a ``-``).

The parser does not support optional values - if an option is set to require a value, one must be present. If such an option is placed last and has no value, the option will be treated as if it had not been specified.

The parser does not automatically support negating or disabling long options by using the format ``--disable-option`` or ``--no-option``. However, it is possible to handle this case explicitly by making an option with ``no-option`` as one of its names, and handling the option explicitly.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineparser_main.py
    :lines: 56-95

If your compiler supports the C++11 standard, the three :sip:ref:`~PyQt6.QtCore.QCommandLineParser.addOption` calls in the above example can be simplified:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineparser_main.py
    :lines: 100-111

Known limitation: the parsing of Qt options inside :sip:ref:`~PyQt6.QtCore.QCoreApplication` and subclasses happens before :sip:ref:`~PyQt6.QtCore.QCommandLineParser` exists, so it can't take it into account. This means any option value that looks like a builtin Qt option, will be treated by :sip:ref:`~PyQt6.QtCore.QCoreApplication` as a builtin Qt option. Example: ``--profile -reverse`` will lead to QGuiApplication seeing the -reverse option set, and removing it from :sip:ref:`~PyQt6.QtCore.QCoreApplication.arguments` before :sip:ref:`~PyQt6.QtCore.QCommandLineParser` defines the ``profile`` option and parses the command line.

.. _qcommandlineparser-how-to-use-qcommandlineparser-in-complex-applications:

How to Use QCommandLineParser in Complex Applications
.....................................................

In practice, additional error checking needs to be performed on the positional arguments and option values. For example, ranges of numbers should be checked.

It is then advisable to introduce a function to do the command line parsing which takes a struct or class receiving the option values returning an enumeration representing the result. The dnslookup example of the QtNetwork module illustrates this:

.. literalinclude:: ../../../snippets/qtbase-examples-network-dnslookup-dnslookup.py
    :lines: 57-66

.. literalinclude:: ../../../snippets/qtbase-examples-network-dnslookup-dnslookup.py
    :lines: 57-66

In the main function, help should be printed to the standard output if the help option was passed and the application should return the exit code 0.

If an error was detected, the error message should be printed to the standard error output and the application should return an exit code other than 0.

.. literalinclude:: ../../../snippets/qtbase-examples-network-dnslookup-dnslookup.py

A special case to consider here are GUI applications on Windows and mobile platforms. These applications may not use the standard output or error channels since the output is either discarded or not accessible.

On Windows, :sip:ref:`~PyQt6.QtCore.QCommandLineParser` uses message boxes to display usage information and errors if no console window can be obtained.

For other platforms, it is recommended to display help texts and error messages using a QMessageBox. To preserve the formatting of the help text, rich text with ``<pre>`` elements should be used:

::

    switch (parseCommandLine(parser, &query, &errorMessage)) {
    case CommandLineOk:
        break;
    case CommandLineError:
        QMessageBox::warning(0, QGuiApplication::applicationDisplayName(),
                             "<html><head/><body><h2>" + errorMessage + "</h2><pre>"
                             + parser.helpText() + "</pre></body></html>");
        return 1;
    case CommandLineVersionRequested:
        QMessageBox::information(0, QGuiApplication::applicationDisplayName(),
                                 QGuiApplication::applicationDisplayName() + ' '
                                 + QCoreApplication::applicationVersion());
        return 0;
    case CommandLineHelpRequested:
        QMessageBox::warning(0, QGuiApplication::applicationDisplayName(),
                             "<html><head/><body><pre>"
                             + parser.helpText() + "</pre></body></html>");
        return 0;
    }

However, this does not apply to the dnslookup example, because it is a console application.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineOption`, :sip:ref:`~PyQt6.QtCore.QCoreApplication`.
