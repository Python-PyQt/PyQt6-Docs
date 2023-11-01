.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: c081b06eff01fb9e37dcbe9e90083ac1

Moves to and selects the item best matching the string *search*. If no item is found nothing happens.

In the default implementation, the search is reset if *search* is empty, or the time interval since the last search has exceeded :sip:ref:`~PyQt6.QtWidgets.QApplication.keyboardInputInterval`.
