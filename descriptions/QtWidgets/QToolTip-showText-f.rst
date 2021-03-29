.. sip:method-description::
    :status: todo
    :pysig: dde5d0b1c753971e9cbba75c51c6ba43
    :realsig: (const QPoint&,const QString&,QWidget*,const QRect&,int)
    :digest: 3524585c20258865b5d3c2c02af94716

Shows *text* as a tool tip, with the global position *pos* as the point of interest. The tool tip will be shown with a platform specific offset from this point of interest.

If you specify a non-empty rect the tip will be hidden as soon as you move your cursor out of this area.

The *rect* is in the coordinates of the widget you specify with *w*. If the *rect* is not empty you must specify a widget. Otherwise this argument can be ``nullptr`` but it is used to determine the appropriate screen on multi-head systems.

The *msecDisplayTime* parameter specifies for how long the tool tip will be displayed, in milliseconds. With the default value of -1, the time is based on the length of the text.

If *text* is empty the tool tip is hidden. If the text is the same as the currently shown tooltip, the tip will *not* move. You can force moving by first hiding the tip with an empty text, and then showing the new tip at the new position.
