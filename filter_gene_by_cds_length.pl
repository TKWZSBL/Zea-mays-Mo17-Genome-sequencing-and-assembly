#!/usr/env/perl
# perl script.pl inputMatrix threshold > outputMatrix
#edit by wangzijian 2021.06.09
use strict;
use warnings;

open NEW, "$ARGV[0]" or die;
while(<NEW>){
    chomp;
    my @array = split /\s+/;
    for(my $i=1;$i<@array;$i++){
        if($array[$i] >= $ARGV[1]){
            print "$array[0]\n";
            last;
        }
    }
}
close NEW;

