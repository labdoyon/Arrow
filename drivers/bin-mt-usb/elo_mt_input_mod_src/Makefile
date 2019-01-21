obj-m := elo_mt_input_mod.o 
elo_mt_input_mod-objs := elo_mt_input.o

KDIR := /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

default:
	$(MAKE) -C $(KDIR) SUBDIRS=$(PWD) modules 

install:
	cp ./elo_mt_input_mod.ko ../elo_mt_input_mod_`uname -r`.ko

clean:
	rm -f *.o *.cmd *.mod.c .*.o* .*.ko* *~ *.ko Module.markers modules.order Module.symvers 
	rm -rf .tmp_versions/
