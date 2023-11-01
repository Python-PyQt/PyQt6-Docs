.. sip:method-description::
    :status: todo
    :pysig: cb5a588efdd99ec30b570d2df5aa8b4f
    :realsig: (QWizard::WizardButton, const QString&)
    :digest: 7d65645e73fa23621fc84df2099e07f8

Sets the text on button *which* to be *text*.

By default, the text on buttons depends on the :sip:ref:`~PyQt6.QtWidgets.QWizard.wizardStyle`. For example, on macOS, the Next button is called Continue.

To add extra buttons to the wizard (e.g., a Print button), one way is to call setButtonText() with :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton1`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton2`, or :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton3` to set their text, and make the buttons visible using the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOption.HaveCustomButton1`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOption.HaveCustomButton2`, and/or :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOption.HaveCustomButton3` options.

Button texts may also be set on a per-page basis using :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setButtonText`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.buttonText`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setButton`, :sip:ref:`~PyQt6.QtWidgets.QWizard.button`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonLayout`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setOptions`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setButtonText`.
