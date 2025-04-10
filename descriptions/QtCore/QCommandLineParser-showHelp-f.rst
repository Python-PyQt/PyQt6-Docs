.. sip:method-description::
    :status: todo
    :pysig: 5f237fb136a13ee36dec1b14d9f10aa2
    :realsig: (int)
    :digest: 4dd8e0ea65165d062cbd39215e0da4b3

Displays the help information, and exits the application. This is automatically triggered by the –help option, but can also be used to display the help when the user is not invoking the application correctly. The exit code is set to *exitCode*. It should be set to 0 if the user requested to see the help, and to any other value in case of an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCommandLineParser.helpText`, :sip:ref:`~PyQt6.QtCore.QCommandLineParser.showMessageAndExit`.
