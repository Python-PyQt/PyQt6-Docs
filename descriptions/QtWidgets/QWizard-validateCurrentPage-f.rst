.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 1ce1acfb5a56c88b7140b7f7ee371050

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QWizard` when the user clicks Next or Finish to perform some last-minute validation. If it returns ``true``, the next page is shown (or the wizard finishes); otherwise, the current page stays up.

The default implementation calls :sip:ref:`~PyQt6.QtWidgets.QWizardPage.validatePage` on the :sip:ref:`~PyQt6.QtWidgets.QWizard.currentPage`.

When possible, it is usually better style to disable the Next or Finish button (by specifying :ref:`mandatory fields<qwizard-mandatory-fields>` or by reimplementing :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete`) than to reimplement .

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.validatePage`, :sip:ref:`~PyQt6.QtWidgets.QWizard.currentPage`.
