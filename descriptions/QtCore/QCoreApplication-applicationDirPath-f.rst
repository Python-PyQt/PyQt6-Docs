.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: adcda079e9e9f5f2f7d162faf30b438a

Returns the directory that contains the application executable.

For example, if you have installed Qt in the ``C:\Qt`` directory, and you run the ``regexp`` example, this function will return "C:/Qt/examples/tools/regexp".

On macOS and iOS this will point to the directory actually containing the executable, which may be inside an application bundle (if the application is bundled).

**Warning:** On Linux, this function will try to get the path from the ``/proc`` file system. If that fails, it assumes that ``argv[0]`` contains the absolute file name of the executable. The function also assumes that the current directory has not been changed by the application.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationFilePath`.
