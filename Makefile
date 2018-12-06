CC=g++
CFLAGS=-std=c++11 -static -O3 -lm
CFLAGS2=-std=gnu++0x -static -O3 -lm
SOURCES:=$(wildcard *.cpp)
OUTS:=${SOURCES:%.cpp=%.out}

.PHONY: all clean test

all: $(OUTS)

%.out: %.cpp
	$(CC) $< $(CFLAGS) -o $@ $(DEFINES)

test: $(prog).out
	python -m test $(prog)

clean:
	@$(RM) *.out
