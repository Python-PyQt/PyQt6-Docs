.. sip:method-description::
    :status: todo
    :pysig: 4c41871cb30ce61151cf1eaa1492bd4c
    :realsig: (const QString&,QWidget*,const char*,const char*)
    :digest: 79115557627251da23601f368f3c8323

Creates a field called *name* associated with the given *property* of the given *widget*. From then on, that property becomes accessible using :sip:ref:`~PyQt6.QtWidgets.QWizardPage.field` and :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setField`.

Fields are global to the entire wizard and make it easy for any single page to access information stored by another page, without having to put all the logic in :sip:ref:`~PyQt6.QtWidgets.QWizard` or having the pages know explicitly about each other.

If *name* ends with an asterisk (``\*``), the field is a mandatory field. When a page has mandatory fields, the Next and/or Finish buttons are enabled only when all mandatory fields are filled. This requires a *changedSignal* to be specified, to tell :sip:ref:`~PyQt6.QtWidgets.QWizard` to recheck the value stored by the mandatory field.

:sip:ref:`~PyQt6.QtWidgets.QWizard` knows the most common Qt widgets. For these (or their subclasses), you don't need to specify a *property* or a *changedSignal*. The table below lists these widgets:

+---------------------------------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
| Widget                                      | Property                                                                              | Change Notification Signal                                |
+=============================================+=======================================================================================+===========================================================+
| :sip:ref:`~PyQt6.QtWidgets.QAbstractButton` | bool checked                                                                          | :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.toggled`       |
+---------------------------------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider` | int :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.value`                                 | :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.valueChanged`  |
+---------------------------------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QComboBox`       | int :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentIndex`                                | :sip:ref:`~PyQt6.QtWidgets.QComboBox.currentIndexChanged` |
+---------------------------------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit`   | :sip:ref:`~PyQt6.QtCore.QDateTime` :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.dateTime` | :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.dateTimeChanged` |
+---------------------------------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QLineEdit`       | QString :sip:ref:`~PyQt6.QtWidgets.QLineEdit.text`                                    | :sip:ref:`~PyQt6.QtWidgets.QLineEdit.textChanged`         |
+---------------------------------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QListWidget`     | int :sip:ref:`~PyQt6.QtWidgets.QListWidget.currentRow`                                | :sip:ref:`~PyQt6.QtWidgets.QListWidget.currentRowChanged` |
+---------------------------------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtWidgets.QSpinBox`        | int :sip:ref:`~PyQt6.QtWidgets.QSpinBox.value`                                        | :sip:ref:`~PyQt6.QtWidgets.QSpinBox.valueChanged`         |
+---------------------------------------------+---------------------------------------------------------------------------------------+-----------------------------------------------------------+

You can use :sip:ref:`~PyQt6.QtWidgets.QWizard.setDefaultProperty` to add entries to this table or to override existing entries.

To consider a field "filled", :sip:ref:`~PyQt6.QtWidgets.QWizard` simply checks that their current value doesn't equal their original value (the value they had before :sip:ref:`~PyQt6.QtWidgets.QWizardPage.initializePage` was called). For :sip:ref:`~PyQt6.QtWidgets.QLineEdit`, it also checks that :sip:ref:`~PyQt6.QtWidgets.QLineEdit.hasAcceptableInput` returns true, to honor any validator or mask.

:sip:ref:`~PyQt6.QtWidgets.QWizard`'s mandatory field mechanism is provided for convenience. It can be bypassed by reimplementing :sip:ref:`~PyQt6.QtWidgets.QWizardPage.isComplete`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWizardPage.field`, :sip:ref:`~PyQt6.QtWidgets.QWizardPage.setField`, :sip:ref:`~PyQt6.QtWidgets.QWizard.setDefaultProperty`.
