.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 19ee08f278d1c0f5b21ec78e1d700cc8

Returns the native directory separator: "/" under Unix and "\\" under Windows.

You do not need to use this function to build file paths. If you always use "/", Qt will translate your paths to conform to the underlying operating system. If you want to display paths to the user using their operating system's separator use :sip:ref:`~PyQt6.QtCore.QDir.toNativeSeparators`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.listSeparator`.
