.. sip:method-description::
    :status: todo
    :pysig: dfc50d0ccac6c89d872603eabed40539
    :realsig: (int,int,const QPixmap&,int,int,int,int)
    :digest: a13cdf86cbc75eeeeddca24e63978687

Draws a pixmap at (\ *x*, *y*) by copying a part of the given *pixmap* into the paint device.

(\ *x*, *y*) specifies the top-left point in the paint device that is to be drawn onto. (\ *sx*, *sy*) specifies the top-left point in *pixmap* that is to be drawn. The default is (0, 0).

(\ *sw*, *sh*) specifies the size of the pixmap that is to be drawn. The default, (0, 0) (and negative) means all the way to the bottom-right of the pixmap.
