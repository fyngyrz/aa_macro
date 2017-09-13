// plugin_demo.c
// -------------
// tab stops every 4 spaces

#include <math.h>
#include <string.h>
#include "developer.h"

void pengine(struct plug *p,long start,long finish,struct pkg *(*service)(struct req *p))	// sets 64K remap
{
long i,v,b;

	b = (p->f[0] - 100.0f) * 655.35f;	// b is now [-65535...65535]
	for (i = start; i < finish; i++)	// we set this range to [0...65536]
	{
		v = i + b;					// temp brightness adjust;
		if (v < 0) v = 0;			// now limit remap range...
		if (v > 65535) v = 65535;	// ...to acceptable bounds
		p->lr[i] = v;				// install in remap channel
	}
}

void dengine(struct plug *p,long start,long finish,struct pkg *(*service)(struct req *p))	// generates output
{
long i;

	for (i = start; i < finish; i++) // 1-dimensional pixel processing
	{
		p->sr[i] = p->lr[p->mr[i]];	// remap pixel brightness
		p->sg[i] = p->lr[p->mg[i]];	// ...using 64k table in layer
		p->sb[i] = p->lr[p->mb[i]];	// ...
	}
}

void setup(struct plugin *p)	// NOTE: most struct elements are preset to 0,
{								// if that is the setting you need, it's there.
#include "ak_pu_date.txt"				// this inserts the current date in the plugin

	p->layer_pri	= 9500;				// layer priority (posit in fx stack - see developer.h)
	strcpy(p->panel.n,"Brightness");	// name appearing on panel
	p->pthread[0]	= 1;				// plugin desires pengine() threading
	p->prange_methods[0]= 2;			// custom range for pengine()
	p->pfinish[0]	= 65536;			// end+1 range for pengine() to process
	p->dthread[0]	= 1;				// plugin desires dengine() threading
	p->promotable	= 1;				// BUT user can add alpha, paint
	p->req_lr		= 65536;			// we'd like 1 layer of this size in lr
	p->slider_req	= 1;				// we'd like 1 slider (#0)
	strcpy(p->sliders[0].n,"Intensity");// legend for slider
	p->forder[0]	= 20;				// position on line zero
	p->svalues[0]	= 100.0f;			// initial value
	p->zvalues[0]	= 200.0f;			// initial hi value (user settable)
	p->ticks[0] = 21;					// Ten ticks per hundred
}										// (low values default to 0.0f)

void init(struct plug *pl,struct pkg *(*service)(struct req *p)) // called before pengine() and dengine()
{
struct req r;
struct pkg *p;
char *msg = "demo plugin init";
	// the following just demonstrates using the service function
	r.svc = REQ_STATUS;		// request status line message service
	r.p1 = msg;				// set up request with proper parameter
	p = service(&r);		// send msg to status line, get package back
}

void cleanup(struct plug *pl,struct pkg *(*service)(struct req *p))	// called after all pengine() and dengine threads complete
{
struct req r;
struct pkg *p;
char *msg = "demo plugin cleanup";
	// the following just demonstrates using the service function
	r.svc = REQ_STATUS;		// request status line message service
	r.p1 = msg;				// set up request with proper parameter
	p = service(&r);		// send msg to status line, get package back
}
