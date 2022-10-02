.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 760adde54f04a4e8a64e159ade956e52

Explicitly sets this page to be final if *finalPage* is true.

After calling setFinalPage(true), :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isFinalPage` returns ``true`` and the Finish button is visible (and enabled if :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete` returns true).

After calling setFinalPage(false), :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isFinalPage` returns ``true`` if :sip:ref:`~PyQt6.QtWidgets.QWizardPage.nextId` returns -1; otherwise, it returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isFinalPage`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOption.HaveFinishButtonOnEarlyPages`.
