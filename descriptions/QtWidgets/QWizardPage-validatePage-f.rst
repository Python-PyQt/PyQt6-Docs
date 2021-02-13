.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: e0e9e050c5e10f49e5b90d96c0079224

This virtual function is called by :sip:ref:`~PyQt6.QtWidgets.QWizard.validateCurrentPage` when the user clicks Next or Finish to perform some last-minute validation. If it returns ``true``, the next page is shown (or the wizard finishes); otherwise, the current page stays up.

The default implementation returns ``true``.

When possible, it is usually better style to disable the Next or Finish button (by specifying mandatory fields or reimplementing :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete`) than to reimplement .

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.validateCurrentPage`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete`.
