
init:
	$(MAKE) -C frontend/todoapp init
	$(MAKE) -C backend init

dev:
	$(MAKE) -C frontend/todoapp dev

build:
	$(MAKE) -C frontend/todoapp build

run: 
	$(MAKE) -C frontend/todoapp run

clean:
	$(MAKE) -C backend clean
	$(MAKE) -C frontend/todoapp clean

test:
	yarn test