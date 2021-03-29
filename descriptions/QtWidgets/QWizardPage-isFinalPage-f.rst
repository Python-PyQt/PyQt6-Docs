.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 5da5acef1937b6cb22a95c90a5a1e385

This function is called by :sip:ref:`~PyQt6.QtWidgets.QWizard` to determine whether the Finish button should be shown for this page or not.

By default, it returns ``true`` if there is no next page (i.e., :sip:ref:`~PyQt6.QtWidgets.QWizardPage.nextId` returns -1); otherwise, it returns ``false``.

By explicitly calling :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setFinalPage`\ (true), you can let the user perform an "early finish".

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveFinishButtonOnEarlyPages`.
