.. sip:method-description::
    :status: todo
    :pysig: feb5eb0b809686bfed4e30cbacd7fa8e
    :realsig: ()
    :digest: 50b747d02e61cbef4236d50d17c3dceb

On any platform other than Windows, this function returns a new UUID with variant :sip:ref:`~PyQt6.QtCore.QUuid.Variant.DCE` and version :sip:ref:`~PyQt6.QtCore.QUuid.Version.Random`. On Windows, a GUID is generated using the Windows API and will be of the type that the API decides to create.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUuid.variant`, :sip:ref:`~PyQt6.QtCore.QUuid.version`.
