
init:
	$(MAKE) -C frontend/todoapp init
	$(MAKE) -C backend init

backend-run:
	 $(MAKE) -C backend run 

frontend-dev:
	 $(MAKE) -C frontend/todoapp dev

frontend-build:
	$(MAKE) -C frontend/todoapp build

frontend-run: 
	$(MAKE) -C frontend/todoapp run

clean:
	$(MAKE) -C backend clean
	$(MAKE) -C frontend/todoapp clean

test:
	$(MAKE) -C backend test
#	$(MAKE) -C frontend/todoapp test