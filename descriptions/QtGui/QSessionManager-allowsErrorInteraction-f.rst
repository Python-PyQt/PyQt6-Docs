.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 588e7df38f2a9c57f1239fca6fe4a0de

Returns ``true`` if error interaction is permitted; otherwise returns ``false``.

This is similar to :sip:ref:`~PyQt6.QtGui.QSessionManager.allowsInteraction`, but also enables the application to tell the user about any errors that occur. Session managers may give error interaction requests higher priority, which means that it is more likely that an error interaction is permitted. However, you are still not guaranteed that the session manager will allow interaction.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSessionManager.allowsInteraction`, :sip:ref:`~PyQt6.QtGui.QSessionManager.release`, :sip:ref:`~PyQt6.QtGui.QSessionManager.cancel`.
