.. sip:enum-member-description::
    :status: todo
    :value: 4
    :digest: d8dfb7489c0940683146a7267f4980ed

Indicates that the widget paints all its pixels when it receives a paint event. Thus, it is not required for operations like updating, resizing, scrolling and focus changes to erase the widget before generating paint events. The use of  provides a small optimization by helping to reduce flicker on systems that do not support double buffering and avoiding computational cycles necessary to erase the background prior to painting. **Note**: Unlike ,  makes an effort to avoid transparent window backgrounds. This flag is set or cleared by the widget's author.
