.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 6746e6e03271237b85b97c0abc57119e

Closes the connection to the target to enable communication with the target from a different instance. The connection will also be closed, when the :sip:ref:`~PyQt6.QtNfc.QNearFieldTarget` is destroyed. A connection to the target device is (re)created to process a command or read/write a NDEF messages.

Returns ``true`` only if an existing connection was successfully closed; otherwise returns ``false``.
