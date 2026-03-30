.. sip:method-description::
    :status: todo
    :pysig: cade5435c9c717945f3df11a91bc47ab
    :realsig: (int,int,int,int,const QPixmap&,int,int)
    :digest: c060ce35efa039de775ca9a41588d7c3

Draws a tiled *pixmap* in the specified rectangle.

(\ *x*, *y*) specifies the top-left point in the paint device that is to be drawn onto; with the given *width* and *height*.

(\ *sx*, *sy*) specifies the origin inside the specified rectangle where the pixmap will be drawn. The origin position is specified in the device independent pixels relative to (\ *x*, *y*). This defaults to (0, 0).
