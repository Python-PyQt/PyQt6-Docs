.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e5041d50c4601d4590274a8a8f127218

Writes any unsaved changes to permanent storage, and reloads any settings that have been changed in the meantime by another application.

This function is called automatically from :sip:ref:`~PyQt6.QtCore.QSettings`'s destructor and by the event loop at regular intervals, so you normally don't need to call it yourself.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.status`.
