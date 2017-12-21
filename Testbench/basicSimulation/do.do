vlib work                                            
vmap work work

vlog *.v

vsim work.test_counter

#add wave *
add wave -radix  unsigned sim:/test_counter/*

run 500 ns