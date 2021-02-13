.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 29f13b773e4bf0b506f7b03eedfc6395

Explicitly sets this page to be final if *finalPage* is true.

After calling (true), :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isFinalPage` returns ``true`` and the Finish button is visible (and enabled if :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete` returns true).

After calling (false), :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isFinalPage` returns ``true`` if :sip:ref:`~PyQt6.QtWidgets.QWizardPage.nextId` returns -1; otherwise, it returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isFinalPage`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveFinishButtonOnEarlyPages`.
