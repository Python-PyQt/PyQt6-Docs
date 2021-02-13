.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: (bool)
    :digest: 989dcfa464187cedc696b5e60c516078

Sets whether Qt should use the system's standard colors, fonts, etc., to *on*. By default, this is ``true``.

This function must be called before creating the :sip:ref:`~PyQt6.QtGui.QGuiApplication` object, like this:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_kernel_qguiapplication.py
    :lines: 71-77

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.desktopSettingsAware`.
