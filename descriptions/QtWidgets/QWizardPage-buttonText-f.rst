.. sip:method-description::
    :status: todo
    :pysig: 1fd70167f44759a0d34da3f16721690f
    :realsig: (QWizard::WizardButton) const
    :digest: c76376a33d4a7c124260eff67ba5e535

Returns the text on button *which* on this page.

If a text has ben set using :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setButtonText`, this text is returned. Otherwise, if a text has been set using :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonText`, this text is returned.

By default, the text on buttons depends on the :sip:ref:`~PyQt6.QtWidgets.QWizard.wizardStyle`. For example, on macOS, the Next button is called Continue.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setButtonText`, :sip:ref:`~PyQt6.QtWidgets.QWizard.buttonText`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonText`.
