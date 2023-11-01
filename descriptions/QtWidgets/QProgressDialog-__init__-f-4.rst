.. sip:method-description::
    :status: todo
    :pysig: 01510f1544ef74a9e359b5a9590a98ed
    :realsig: (const QString&, const QString&, int, int, QWidget*, Qt::WindowFlags)
    :digest: f669dc643dd2eee5b8c233409a2c933b

Constructs a progress dialog.

The *labelText* is the text used to remind the user what is progressing.

The *cancelButtonText* is the text to display on the cancel button. If QString() is passed then no cancel button is shown.

The *minimum* and *maximum* is the number of steps in the operation for which this progress dialog shows progress. For example, if the operation is to examine 50 files, this value minimum value would be 0, and the maximum would be 50. Before examining the first file, call :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setValue`\ (0). As each file is processed call :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setValue`\ (1), :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setValue`\ (2), etc., finally calling :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setValue`\ (50) after examining the last file.

The *parent* argument is the dialog's parent widget. The parent, *parent*, and widget flags, *f*, are passed to the :sip:ref:`~PyQt6.QtWidgets.QDialog.__init__` constructor.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setLabelText`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setLabel`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setCancelButtonText`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setCancelButton`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setMinimum`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setMaximum`.
