#ifndef JID_h
#define JID_h

class stanza;

class JID {

 public:

    /**
     * @element-type stanza
     */
    stanza *from;

    /**
     * @element-type stanza
     */
    stanza *to;
};

#endif // JID_h
