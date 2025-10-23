.. sip:method-description::
    :status: todo
    :pysig: 763eb7e9f3d45684b1d53751a3f28009
    :realsig: (int,int,const QImage&,int,int,int,int,Qt::ImageConversionFlags)
    :digest: be1cf27ce3e2e2e100f8a2c1a998a6d1

Draws an image at (\ *x*, *y*) by copying a part of *image* into the paint device.

(\ *x*, *y*) specifies the top-left point in the paint device that is to be drawn onto. (\ *sx*, *sy*) specifies the top-left point in *image* that is to be drawn. The default is (0, 0).

(\ *sw*, *sh*) specifies the size of the image that is to be drawn. The default, (0, 0) (and negative) means all the way to the bottom-right of the image.
