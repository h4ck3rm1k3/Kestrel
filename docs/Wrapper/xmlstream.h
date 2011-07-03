#ifndef xmlstream_h
#define xmlstream_h

#include "basexmpp.h"

class threading;
class Kestrel_manager;
class handler;
class stanza;
class event_queue;

class xmlstream : public basexmpp {

 public:

    virtual void event_runner();

    virtual void run_with_except_hook();

    virtual void _threaded_event_wrapper();

    virtual void process();

    virtual void connect();


    /** 
     *  Analyze incoming XML stanzas and convert them into stanza
     *  objects if applicable and queue stream events to be processed
     *  by matching handlers.
     */
    virtual void __spawn_event();


    /** 
     *  Apply any preprocessing filters.
     */
    virtual void incoming_filter();


    /** 
     *  Convert the raw XML object into a stanza object. If no registered
     *  stanza type applies, a generic StanzaBase stanza will be used.
     *  @author _build_stanza
     */
    virtual void newOperation();

 public:

    /**
     * @element-type threading
     */
    threading *calls;

    /**
     * @element-type Kestrel_manager
     */
    Kestrel_manager *event runner calls start;

    /**
     * @element-type basexmpp
     */
    basexmpp *XMLStream;

    /**
     * @element-type handler
     */
    handler *myhandler;

    /**
     * @element-type stanza
     */
    stanza *stream;

    /**
     * @element-type event_queue
     */
    event_queue *myevent_queue;
};

#endif // xmlstream_h
