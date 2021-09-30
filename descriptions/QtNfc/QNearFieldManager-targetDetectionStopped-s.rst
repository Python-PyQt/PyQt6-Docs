.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ccbfb0b3959746ed4baf2590a8973a5c

This signal is emitted whenever the target detection is stopped.

**Note:** Mostly this signal is emitted when :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.stopTargetDetection` has been called. Additionally the user is able to stop the detection on iOS within a popup shown by the system during the scan, which also leads to emitting this signal.
