#ifndef handler_h
#define handler_h

class xmlstream;
class stanza;
class event_queue;


    /** @author handlers
     */
class handler {

 public:


    /** 
     *  match stanza
     */
    virtual void match();

    virtual void prerun();

    virtual void checkdelete();

    virtual void remove();

 public:

    /**
     * @element-type xmlstream
     */
    xmlstream *myxmlstream;

    /**
     * @element-type stanza
     */
    stanza *mystanza;

    /**
     * @element-type event_queue
     */
    event_queue *myevent_queue;
};

#endif // handler_h
