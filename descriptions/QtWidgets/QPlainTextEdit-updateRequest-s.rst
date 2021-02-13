.. sip:signal-description::
    :status: todo
    :pysig: 9ab2057112fbb591bf746afe8f851a75
    :realsig: (const QRect&,int)
    :digest: d218aa4239c3c8c5b01fd98d9be5fd6f

This signal is emitted when the text document needs an update of the specified *rect*. If the text is scrolled, *rect* will cover the entire viewport area. If the text is scrolled vertically, *dy* carries the amount of pixels the viewport was scrolled.

The purpose of the signal is to support extra widgets in plain text edit subclasses that e.g. show line numbers, breakpoints, or other extra information.
