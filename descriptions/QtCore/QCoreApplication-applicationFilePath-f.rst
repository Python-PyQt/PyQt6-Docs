.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 664355780d64c63212656455782aba92

Returns the file path of the application executable.

For example, if you have installed Qt in the ``/usr/local/qt`` directory, and you run the ``regexp`` example, this function will return "/usr/local/qt/examples/tools/regexp/regexp".

**Warning:** On Linux, this function will try to get the path from the ``/proc`` file system. If that fails, it assumes that ``argv[0]`` contains the absolute file name of the executable. The function also assumes that the current directory has not been changed by the application.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationDirPath`.
