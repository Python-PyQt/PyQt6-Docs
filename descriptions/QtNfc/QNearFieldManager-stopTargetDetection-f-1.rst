.. sip:method-description::
    :status: todo
    :pysig: 1fdf6c96c8ab97591704173ec3966956
    :realsig: (const QString&)
    :digest: 38606d4bf18b3ae769ee6298014effec

Stops detecting targets. The :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.targetDetected` signal will no longer be emitted until another call to :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.startTargetDetection` is made. Targets detected before are still valid.

**Note:** On iOS, detected targets become invalid after this call (e.g. an attempt to write or read NDEF messages will result in an error).

If an *errorMessage* is provided, this is a hint to the system that the goal, the application had, was not reached. The *errorMessage* and a matching error icon are shown to the user. Calling this function with an empty *errorMessage*, implies a successful operation end; otherwise an *errorMessage* should be passed to this function.

**Note:** Currently, *errorMessage* only has an effect on iOS because a popup is shown by the system during the scan where the *errorMessage* is visible. Other platforms will ignore this parameter.

.. seealso:: :sip:ref:`~PyQt6.QtNfc.QNearFieldManager.setUserInformation`.
