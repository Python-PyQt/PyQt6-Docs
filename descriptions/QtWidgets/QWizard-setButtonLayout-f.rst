.. sip:method-description::
    :status: todo
    :pysig: 4e7449224829786f092b0c244b4cddf5
    :realsig: (const QList<QWizard::WizardButton>&)
    :digest: 6a1b4306e3946392388acfcd54d3e771

Sets the order in which buttons are displayed to *layout*, where *layout* is a list of :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.WizardButton`\ s.

The default layout depends on the options (e.g., whether :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardOptions.HelpButtonOnRight`) that are set. You can call this function if you need more control over the buttons' layout than what `options <https://doc.qt.io/qt-6/qt-wrap-ui.html#options>`_ already provides.

You can specify horizontal stretches in the layout using :sip:ref:`~PyQt6.QtWidgets.QWizard.WizardButton.Stretch`.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qwizard.py
    :lines: 82-91

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizard.setButton`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setButtonText`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setOptions`.
