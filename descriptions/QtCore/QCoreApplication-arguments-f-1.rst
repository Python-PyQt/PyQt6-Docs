.. sip:method-description::
    :status: todo
    :pysig: d409847c33b4369753f8b837c22758e9
    :realsig: ()
    :digest: 3cb2a60d9a1c84d3bc492d8e1d3f8a19

Returns the list of command-line arguments.

Usually arguments().at(0) is the program name, arguments().at(1) is the first argument, and arguments().last() is the last argument. See the note below about Windows.

Calling this function is slow - you should store the result in a variable when parsing the command line.

**Warning:** On Unix, this list is built from the argc and argv parameters passed to the constructor in the main() function. The string-data in argv is interpreted using QString::fromLocal8Bit(); hence it is not possible to pass, for example, Japanese command line arguments on a system that runs in a Latin1 locale. Most modern Unix systems do not have this limitation, as they are Unicode-based.

On Windows, the list is built from the argc and argv parameters only if modified argv/argc parameters are passed to the constructor. In that case, encoding problems might occur.

Otherwise, the arguments() are constructed from the return value of `GetCommandLine() <https://docs.microsoft.com/en-us/windows/win32/api/processenv/nf-processenv-getcommandlinea>`_. As a result of this, the string given by arguments().at(0) might not be the program name on Windows, depending on how the application was started.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationFilePath`, :sip:ref:`~PyQt6.QtCore.QCommandLineParser`.
