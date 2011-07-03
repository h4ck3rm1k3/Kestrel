#ifndef event_queue_h
#define event_queue_h

class xmlstream;
class handler;
class stanza;

class event_queue {

 public:

    /**
     * @element-type xmlstream
     */
    xmlstream *myxmlstream;

    /**
     * @element-type handler
     */
    handler *myhandler;

    /**
     * @element-type stanza
     */
    stanza *mystanza;
};

#endif // event_queue_h
