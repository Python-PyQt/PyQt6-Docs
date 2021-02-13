.. sip:method-description::
    :status: todo
    :pysig: 032ae39310eed76820341f238387e9cd
    :realsig: (int,int,int,int)
    :digest: 9e73e93e804b99c220287d12227a69bd

Scrolls the contents of the scroll area so that the point (\ *x*, *y*) is visible inside the region of the viewport with margins specified in pixels by *xmargin* and *ymargin*. If the specified point cannot be reached, the contents are scrolled to the nearest valid position. The default value for both margins is 50 pixels.
