.. sip:method-description::
    :status: todo
    :pysig: 9064598f6881fe97156ec2e9c47c55cf
    :realsig: (const QString&) const
    :digest: 07bd206c3c7fcf00ae9f60096f943dd1

Returns the value of the field called *name*.

This function can be used to access fields on any page of the wizard. It is equivalent to calling :sip:ref:`~PyQt6.QtWidgets.QWizardPage.wizard`->\ :sip:ref:`~PyQt6.QtWidgets.QWizard.field`).

Example:

.. literalinclude:: ../../../snippets/qtbase-examples-widgets-dialogs-classwizard-classwizard.py
    :lines: 414-420

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.field`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setField`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.registerField`.
