.. sip:method-description::
    :status: todo
    :pysig: 39cc0046c0239b415ece0a9b06038777
    :realsig: (QWizard::WizardButton,QAbstractButton*)
    :digest: 0cb7769230d44c947674a1f68b5a2f9c

Sets the button corresponding to role *which* to *button*.

To add extra buttons to the wizard (e.g., a Print button), one way is to call setButton() with :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton1` to :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton3`, and make the buttons visible using the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOption.HaveCustomButton1` to :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOption.HaveCustomButton3` options.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.button`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonText`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonLayout`, :sip:ref:`~PyQt6.QtWidgets.QWizard.options`.
