.. sip:method-description::
    :status: todo
    :pysig: 2abef7b16156b268e31dcd88eb0b2bff
    :realsig: (QPushButton*)
    :digest: 9528ca0f6bbc039281f87b6a80d06b25

Sets the cancel button to the push button, *cancelButton*. The progress dialog takes ownership of this button which will be deleted when necessary, so do not pass the address of an object that is on the stack, i.e. use new() to create the button. If ``nullptr`` is passed, no cancel button will be shown.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.setCancelButtonText`.
