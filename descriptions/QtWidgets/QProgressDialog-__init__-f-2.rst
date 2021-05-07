.. sip:method-description::
    :status: todo
    :pysig: d33117a4cf830e8da8ce315c28395b25
    :realsig: (QWidget*,Qt::WindowFlags)
    :digest: ddcffcb4838181f6ba5d883307dea50a

Constructs a progress dialog.

Default settings:

* The label text is empty.

* The cancel button text is (translated) "Cancel".

* minimum is 0;

* maximum is 100

The *parent* argument is dialog's parent widget. The widget flags, *f*, are passed to the :sip:ref:`~PyQt6.QtWidgets.QDialog.__init__` constructor.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setLabelText`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setCancelButtonText`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setCancelButton`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setMinimum`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setMaximum`.
