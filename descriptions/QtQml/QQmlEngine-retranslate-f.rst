.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 0b071d83969bef4d193733cf43378685

Refreshes all binding expressions that use strings marked for translation.

Call this function after you have installed a new translator with :sip:ref:`~PyQt6.QtCore.QCoreApplication.installTranslator`, to ensure that your user-interface shows up-to-date translations.

**Note:** Due to a limitation in the implementation, this function refreshes all the engine's bindings, not only those that use strings marked for translation. This may be optimized in a future release.
