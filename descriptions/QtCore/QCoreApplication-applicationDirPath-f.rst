.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 99706b98b0791c2634e7e9ec7b12d130

Returns the directory that contains the application executable.

For example, if you have installed Qt in the ``C:\Qt`` directory, and you run the ``regexp`` example, this function will return "C:/Qt/examples/tools/regexp".

On macOS and iOS this will point to the directory actually containing the executable, which may be inside an application bundle (if the application is bundled).

On Android this will point to the directory actually containing the executable, which may be inside the application APK (if it was built with uncompressed libraries support).

**Warning:** On Linux, this function will try to get the path from the ``/proc`` file system. If that fails, it assumes that ``argv[0]`` contains the absolute file name of the executable. The function also assumes that the current directory has not been changed by the application.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationFilePath`.
