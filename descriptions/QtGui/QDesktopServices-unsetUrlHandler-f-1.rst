.. sip:method-description::
    :status: todo
    :pysig: c5283bf81cad04335531dd6931c2734d
    :realsig: (const QString&)
    :digest: f6f72a5ad0094429106825d783feb3d9

Removes a previously set URL handler for the specified *scheme*.

Call this function before the handler object that was registered for *scheme* is destroyed, to prevent concurrent :sip:ref:`~PyQt6.QtGui.QDesktopServices.openUrl` calls from continuing to call the destroyed handler object.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDesktopServices.setUrlHandler`.
