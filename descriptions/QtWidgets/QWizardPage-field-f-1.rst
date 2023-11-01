.. sip:method-description::
    :status: todo
    :pysig: 83c921ee2b414a3ed36e51e962a49a8e
    :realsig: (const QString&) const
    :digest: 07bd206c3c7fcf00ae9f60096f943dd1

Returns the value of the field called *name*.

This function can be used to access fields on any page of the wizard. It is equivalent to calling :sip:ref:`~PyQt6.QtWidgets.QWizardPage.wizard`->\ :sip:ref:`~PyQt6.QtWidgets.QWizard.field`).

Example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-licensewizard-licensewizard.py

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.field`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setField`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.registerField`.
