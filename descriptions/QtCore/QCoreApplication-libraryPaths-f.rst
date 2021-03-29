.. sip:method-description::
    :status: todo
    :pysig: 2959872364c7b497ae5baab9d50a0314
    :realsig: ()
    :digest: 0f8503f4d6a72229910b46af4eebee4f

Returns a list of paths that the application will search when dynamically loading libraries.

The return value of this function may change when a :sip:ref:`~PyQt6.QtCore.QCoreApplication` is created. It is not recommended to call it before creating a :sip:ref:`~PyQt6.QtCore.QCoreApplication`. The directory of the application executable (\ **not** the working directory) is part of the list if it is known. In order to make it known a :sip:ref:`~PyQt6.QtCore.QCoreApplication` has to be constructed as it will use ``argv[0]`` to find it.

Qt provides default library paths, but they can also be set using a qt.conf file. Paths specified in this file will override default values. Note that if the qt.conf file is in the directory of the application executable, it may not be found until a :sip:ref:`~PyQt6.QtCore.QCoreApplication` is created. If it is not found when calling this function, the default library paths will be used.

The list will include the installation directory for plugins if it exists (the default installation directory for plugins is ``INSTALL/plugins``, where ``INSTALL`` is the directory where Qt was installed). The colon separated entries of the ``QT_PLUGIN_PATH`` environment variable are always added. The plugin installation directory (and its existence) may change when the directory of the application executable becomes known.

If you want to iterate over the list, you can use the `foreach <https://doc.qt.io/qt-6/containers.html#foreach>`_ pseudo-keyword:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qcoreapplication.py
    :lines: 66-67

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.setLibraryPaths`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.addLibraryPath`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.removeLibraryPath`, :sip:ref:`~PyQt6.QtCore.QLibrary`.
