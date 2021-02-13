.. sip:method-description::
    :status: todo
    :pysig: 1fd70167f44759a0d34da3f16721690f
    :realsig: (QWizard::WizardButton,const QString&)
    :digest: 190d1bfecb3e9983dafe7caa4c702d02

Sets the text on button *which* to be *text*.

By default, the text on buttons depends on the :sip:ref:`~PyQt6.QtWidgets.QWizard.wizardStyle`. For example, on macOS, the Next button is called Continue.

To add extra buttons to the wizard (e.g., a Print button), one way is to call  with :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton1`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton2`, or :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.CustomButton3` to set their text, and make the buttons visible using the :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton1`, :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton2`, and/or :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HaveCustomButton3` options.

Button texts may also be set on a per-page basis using :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setButtonText`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.buttonText`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setButton`, :sip:ref:`~PyQt6.QtWidgets.QWizard.button`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonLayout`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setOptions`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setButtonText`.
