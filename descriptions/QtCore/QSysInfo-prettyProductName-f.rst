.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 3b532345a82fccf121c3f93719883be3

Returns a prettier form of :sip:ref:`~PyQt6.QtCore.QSysInfo.productType` and :sip:ref:`~PyQt6.QtCore.QSysInfo.productVersion`, containing other tokens like the operating system type, codenames and other information. The result of this function is suitable for displaying to the user, but not for long-term storage, as the string may change with updates to Qt.

If :sip:ref:`~PyQt6.QtCore.QSysInfo.productType` is "unknown", this function will instead use the :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelType` and :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelVersion` functions.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelType`, :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelVersion`, :sip:ref:`~PyQt6.QtCore.QSysInfo.productType`, :sip:ref:`~PyQt6.QtCore.QSysInfo.productVersion`.
