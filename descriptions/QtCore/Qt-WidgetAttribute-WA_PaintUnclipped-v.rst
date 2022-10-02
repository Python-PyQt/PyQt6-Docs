.. sip:enum-member-description::
    :status: todo
    :value: 52
    :digest: 72b57552fbbbd04621bc82d52f712fa1

Makes all painters operating on this widget unclipped. Children of this widget or other widgets in front of it do not clip the area the painter can paint on. This flag is only supported for widgets with the WA_PaintOnScreen flag set. The preferred way to do this in a cross platform way is to create a transparent widget that lies in front of the other widgets.
