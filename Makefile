
init:
	$(MAKE) -C frontend/todoapp init
	$(MAKE) -C backend init

front-dev:
	 $(MAKE) -C frontend/todoapp dev

backend-run:
	 $(MAKE) -C backend run 

build:
	$(MAKE) -C frontend/todoapp build

run: 
	$(MAKE) -C frontend/todoapp run

clean:
	$(MAKE) -C backend clean
	$(MAKE) -C frontend/todoapp clean

test:
	yarn test