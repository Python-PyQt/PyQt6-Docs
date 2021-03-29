.. sip:method-description::
    :status: todo
    :pysig: 4f8f93e499a4090f930ac51556f2b328
    :realsig: () const
    :digest: 94b2f56e7b7a39fe2de55f97815b54c6

Returns a pointer to the current subwindow, or ``nullptr`` if there is no current subwindow.

This function will return the same as :sip:ref:`~PyQt6.QtWidgets.QMdiArea.activeSubWindow` if the :sip:ref:`~PyQt6.QtWidgets.QApplication` containing :sip:ref:`~PyQt6.QtWidgets.QMdiArea` is active.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiArea.activeSubWindow`, :sip:ref:`~PyQt6.QtWidgets.QApplication.activeWindow`.
